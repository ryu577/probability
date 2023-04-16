from graphing.special_graphs.neural_trigraph.marginal_matching.\
    marginal_matching1 import get_schedule, get_schedule_rand
from graphing.special_graphs.neural_trigraph.marginal_matching.scoring\
    import score
from graphing.special_graphs.neural_trigraph.path_set import\
    add_one_path, remove_one_path
from graphing.special_graphs.neural_trigraph.toy_graphs import ToyGraph1
from graphing.graph import remove_zeros
import numpy as np
import copy


class Evolutor(object):
    def __init__(self, probs_l=None, probs_c=None, probs_r=None,
                 edges1=None, edges2=None, num_nodes=280,
                 start_dict=None):
        if probs_l is None:
            self.probs_left = ToyGraph1.probs_left.copy()
            self.probs_center = ToyGraph1.probs_center.copy()
            self.probs_right = ToyGraph1.probs_right.copy()
            self.edges1 = ToyGraph1.edges1
            self.edges2 = ToyGraph1.edges2
        else:
            self.probs_left = probs_l
            self.probs_center = probs_c
            self.probs_right = probs_r
            self.edges1 = edges1.astype(int)
            self.edges2 = edges2.astype(int)
        self.num_nodes = num_nodes
        self.dest = max(self.edges2[::, 1]) + 1
        self.tmp_probs_left = self.probs_left.copy()
        self.tmp_probs_center = self.probs_center.copy()
        self.tmp_probs_right = self.probs_right.copy()
        self.update_best_probs()
        if start_dict is None:
            self.best_dict = get_schedule(self.probs_left, self.probs_right,
                                      self.edges1, 
                                      self.edges2, num_nodes)
        else:
            self.best_dict = start_dict
        self.best_dict = remove_zeros(self.best_dict)
        self.min_score = score(self.best_dict, self.probs_left,
                               self.probs_center, self.probs_right)
        self.curr_dict = copy.deepcopy(self.best_dict)
        self.candidate_dict = copy.deepcopy(self.best_dict)
        self.curr_score = self.min_score
        self.candidate_score = self.min_score
        self.probs_arr = [self.tmp_probs_left,
                          self.tmp_probs_center,
                          self.tmp_probs_right]
        self.pert_ix = 0

    def evolve(self, n_iter=100):
        b_ix = 0
        for ix in range(n_iter):
            res = get_schedule(self.tmp_probs_left,
                               self.tmp_probs_right,
                               self.edges1, self.edges2)
            candidate_score = score(res, self.probs_left,
                                    self.probs_center,
                                    self.probs_right)
            print("Score: " + str(candidate_score))
            if candidate_score < self.min_score:
                self.min_score = candidate_score
                self.best_dict = res
                self.update_best_probs()
                b_ix = ix
            self.perturb_probs()
            # Sometimes, a reset should occur.
            if (candidate_score - self.min_score)/self.min_score > 0.3\
                    and (ix - b_ix) > 10:
                self.reset_to_best_probs()

    def anneal(self, n_iter=1000, presv_cov=False):
        prob_swtch = 1.0
        anneal_rate = 0.99
        b_ix = 0
        score_diff_threshold = 2.0 
        best_score_iters_threshold = 225
        for ix in range(n_iter):
            print("Current score: " + str(self.curr_score) +\
                  " best score: " + str(self.min_score))
            prob_swtch *= anneal_rate
            self.replace_one_path(presv_cov)
            if self.candidate_score <= self.min_score:
                self.best_dict = copy.deepcopy(self.candidate_dict)
                self.min_score = self.candidate_score
                self.curr_dict = copy.deepcopy(self.candidate_dict)
                self.curr_score = self.candidate_score
                b_ix = ix
            elif prob_swtch > np.random.uniform():
                self.curr_dict = copy.deepcopy(self.candidate_dict) 
                self.curr_score = self.candidate_score
            if (self.candidate_score - self.min_score) > score_diff_threshold * self.min_score\
                    and (ix-b_ix)>best_score_iters_threshold:
                self.reset_to_best() 

    def perturb_probs(self):
        probs = self.probs_arr[self.pert_ix % 3]
        self.pert_ix += 1
        ix = np.random.choice(list(probs.keys()))
        perturb = np.random.normal(0, .03)
        probs[ix] = max(0, probs[ix]+perturb)
        self.tmp_probs_left = self.probs_arr[0]
        self.tmp_probs_center = self.probs_arr[1]
        self.tmp_probs_right = self.probs_arr[2]

    def update_best_probs(self):
        self.probs_left_bst = self.tmp_probs_left.copy()
        self.probs_center_bst = self.tmp_probs_center.copy()
        self.probs_right_bst = self.tmp_probs_right.copy()

    def reset_to_best_probs(self):
        self.tmp_probs_left = self.probs_left_bst.copy()
        self.tmp_probs_center = self.probs_center_bst.copy()
        self.tmp_probs_right = self.probs_right_bst.copy()

    def replace_one_path(self, presv_cov=False):
        self.candidate_dict = remove_one_path(self.curr_dict, self.dest,
                                              presv_cov)
        self.candidate_dict = add_one_path(self.candidate_dict,
                                           self.edges1,
                                           self.edges2)
        self.candidate_score = score(self.candidate_dict,
                                     self.probs_left,
                                     self.probs_center,
                                     self.probs_right)

    def reset_to_best(self):
        self.curr_dict = copy.deepcopy(self.best_dict)
        self.curr_score = self.min_score


def remove_one_path1(res, dest):
    complete = False
    ix = 0
    while not complete:
        ix += 1
        if ix == 100:
            print(res)
            raise Exception("Infinite loop!")
        res1 = copy.deepcopy(res)
        # First, remove one path.
        strt_key = np.random.choice(list(res1[0].keys()))
        res1[0][strt_key] -= 1
        if res1[0][strt_key] < 0:
            continue
        scnd_key = np.random.choice(list(res1[strt_key].keys()))
        res1[strt_key][scnd_key] -= 1
        if res1[strt_key][scnd_key] < 0:
            continue
        thrd_key = np.random.choice(list(res1[scnd_key].keys()))
        res1[scnd_key][thrd_key] -= 1
        try:
            res1[thrd_key][dest] -= 1
        except:
            print(thrd_key)
            print(dest)
            raise Exception("Hanging key?")
        if (res1[scnd_key][thrd_key] < 0) or (res1[thrd_key][dest] < 0):
            continue
        complete = True
    return remove_zeros(res1)


def add_one_path1(res, edges1, edges2):
    res1 = copy.deepcopy(res)
    dest = max(edges2[::, 1]) + 1
    strt_ix = np.random.choice(edges1[::, 0])
    if strt_ix in res1[0]:
        res1[0][strt_ix] += 1
    else:
        res1[0][strt_ix] = 1
    mid_ix = np.random.choice(edges1[edges1[::, 0] == strt_ix][::, 1])
    if strt_ix in res1 and mid_ix in res1[strt_ix]:
        res1[strt_ix][mid_ix] += 1
    elif strt_ix in res1:
        res1[strt_ix][mid_ix] = 1
    else:
        res1[strt_ix] = {}
        res1[strt_ix][mid_ix] = 1
    end_ix = np.random.choice(edges2[edges2[::, 0] == mid_ix][::, 1])
    if mid_ix in res1 and end_ix in res1[mid_ix]:
        res1[mid_ix][end_ix] += 1
    elif mid_ix in res1:
        res1[mid_ix][end_ix] = 1
    else:
        res1[mid_ix] = {}
        res1[mid_ix][end_ix] = 1

    if end_ix in res1:
        try:
            res1[end_ix][dest] += 1
        except:
            print(str(res1[end_ix]))
            print(dest)
            raise Exception("Weird graph!")
    else:
        res1[end_ix] = {}
        res1[end_ix][dest] = 1
    return res1

