Spun up a blog: [[calculus/e_expondist_cmpd]]
# Geometric converges to exponential
[From this mathexchange question](https://math.stackexchange.com/questions/93098/how-to-prove-that-geometric-distributions-converge-to-an-exponential-distributio)

![[Expon_lt_geomtr]]
keywords: prob, exponential, limit, euler, e, e^x
![[geomtr_limit0.png#invert|300]]

![[geomtr_limit.png#invert|300]]

#exponential #prob #math #prob/geometric 
## Limits and where e comes from
```python
x=0.00001
(1+x)**(1/x)
> 2.718268237192297

(1-x)**(1/x)
> 0.3678776017682466

1/np.e
> 0.36787944117144233
```
Imagine I lend you 1\$. After a year, you have to return 2\$ to me. I decide to be clever and collect the interest more regularly from you so as to get more money. Instead of collecting just once at the end of the year, I collect $x$ times during the year, equally spaced. As $x$ becomes larger and larger, how much money will I end up collecting from you?

This is probably how inflation eats up your money.

- [ ] [Question on this](https://math.stackexchange.com/questions/4657268/why-does-compound-interest-lead-to-a-function-that-is-the-derivative-of-itself): why is compound interest same as function that is its own derivative?
![[origin_e.png#invert|300]]
Blog: [[calculus/e_expondist_cmpd]]

And now, converting Binomial to Poisson with the same methodology.
![[BinomToPoisson.png#invert|400]]


# Fred to bus vs bus to bus
In the book, "Introduction-to-probability by Joseph K Blitzstein and Jessica Hwang", exercise 42 (b) reads as follows: 

> Fred then visits Blunderville, where the times between buses are also 10 minutes on average, and independent. Yet to his dismay, he finds that on average he has to wait more than 1 hour for the next bus when he arrives at the bus stop! How is it possible that the average Fred-to-bus time is greater than the average bus-to-bus time even though Fred arrives at some time between two bus arrivals? Explain this intuitively, and construct a specific discrete distribution for the times between buses showing that this is possible

In the simulations below, when $c$ (or $k$, the shape parameter of the Weibull distribution) is <1, the time to arrival is on average greater than 10. Otherwise, it is less than 10. For $k=1$, we get an exponential where the waiting time is equal to $10$.
```python
import numpy as np
from scipy.stats import weibull_min

def wait_time(c=.295):
	time = 0
	arrival = 11543.674
	mu = weibull_min.mean(c)
	while time < arrival:
		time += 10/mu*weibull_min.rvs(c)
	return time - arrival

def avg_arrival(c=.295, n=1000):
	print("Mean: " + str(weibull_min.stats(c, moments='m')))
	sum_t = 0
	for _ in range(n):
		sum_t += wait_time(c)
	return sum_t/n
```

> keywords: poisson, probability, prob, exponential, interarrival, inter-arrival, exercise, point process, pt_process, ptproc, weibull, hazard rate, tutoring

## Theory from renewal processes
[Question on Math-exchange](https://math.stackexchange.com/questions/4652258/an-intuitive-discrete-inter-arrival-distribution-where-average-time-to-next-arr)

### Interesting answer
It follows from the key renewal theorem that the limiting mean of the forward recurrence time $Y$ is
$$
\mathbb E[Y] =\frac{\mathbb E[X^2]}{2\mathbb E[X]},
$$
where $X$ has the interrenewal distribution. Writing this as
$$
\frac{\mathbb E[X^2]}{2\mathbb E[X]} = \frac{\mathbb E[X]^2 + \operatorname{Var}(X)}{2\mathbb E[X]} = \frac{\mathbb E[X]}{2} + \frac{\operatorname{Var}(X)}{2\mathbb E[X]} > \frac{\mathbb E[X]}{2},
$$
we see that the average time until the next renewal is greater than the average interrenewal interval (assuming that the interrenewal time is not deterministic). So for example, you may check that $\mathbb P(X=1)=1/2=\mathbb P(X=2)$ satisfies this inequality.
### Comments
The particular discrete distribution referenced in the answer above doesn't really satisfy the inequality. It is more than half the bus to bus time but not more than the bus to bus time. 

## Probability distribution of the residual time 


Related to the inspection paradox: 
https://www.bbk.ac.uk/ms/brooms/teaching/SMF/SMFL5.pdf
#prob/renewal #prob 
keywords: renewal, prob, probability, stochastic, 

Quoting:
> The inspection paradox, that the component in use at a given time t tends to have a longer lifetime than a component chosen at random.

Component in use lifetime is Fred to bus time and component at random life is bus to bus time.

[Blog on inspection paradox](https://towardsdatascience.com/the-inspection-paradox-is-everywhere-2ef1c2e9d709)


[https://www.amazon.com/i-Story-Number-ebook/dp/B003VIWZ8I/ref=sr_1_1?crid=3RWWTHC6O1ZFR&keywords=the+number+e&qid=1678567210&sprefix=the+number+e%2Caps%2C90&sr=8-1](https://www.amazon.com/i-Story-Number-ebook/dp/B003VIWZ8I/ref=sr_1_1?crid=3RWWTHC6O1ZFR&keywords=the+number+e&qid=1678567210&sprefix=the+number+e%2Caps%2C90&sr=8-1)


# Appendix
"Gone are the days of hacking your model in R and importing it to a faster language like C++".
Hamiltonian monte carlo.


[https://math.stackexchange.com/questions/4666216/question-about-exponential-average-wait-time-paradox/4666224#4666224](https://math.stackexchange.com/questions/4666216/question-about-exponential-average-wait-time-paradox/4666224#4666224)