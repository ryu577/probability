Goal: $$P(X=x) = \frac{e^{-\lambda t}(\lambda t)^x} {x!} \tag{1}$$


Start: This is obviously just the Binomial distribution 
$${n \choose k}p^k(1-p)^{n-k}$$


Step 1: In a Binomial, n is the number of trials. That can be written as total time taken divided by the distance between trials. We use the brackets to signify it has to be an integer (can't have 5.7 trials, it would be 5) 

$$n =\left[\frac t d\right]$$

Step 2: Here we just rewrite the Binomial with n replaced by the t/d mentioned above $${{[\frac t d]} \choose k}p^k(1-p)^{[\frac t d]-k} $$
Step 3: This step always confuses me, future self, so listen carefully. The number $e$ is compound interest taken to the limit. In order for that to happen and the answer not be infinity or zero, both $d$ (distance between trials) and $p$ (probability of success) have to go to 0. Think Steph Curry 3 point shots, if $d$ goes to zero and $p$ stays at 50%, the guy will make infinite 3 pointers. Conversely if p goes to 0 and d doesn't go to zero, the guy will never ever make a shot. Now in order for d and p to go to zero together, they have to both intersect the origin at the same time (y intercept of zero). One way to do that is a simple line with no intercept term. Classic y = mx + b but in this case y = d, m = p/lambda, and b = 0. There are other ways for the y intercept to  be 0 like y = x^2 but it would just lead to a trivial answer. (question for rohit, why? don't both go to zero still if it was d = (p/lambda)^2)  $${d = \frac p \lambda},   p=\lambda d$$ 
Step 4: Algebraic manipulation of step 3 leads to this newly written form without any P's in the equation $${{[\frac {\lambda t} {\lambda d}]} \choose k}\lambda d^k(1-\lambda d)^{[\frac {\lambda t} {\lambda d}]-k} $$

Step 5: This substitution is to make the equation take the form of compound interest in the limit -> (1+tiny number)^giant number $$ F = {\frac 1 {\lambda d}}$$
Step 6: We replace $\lambda d$ with $f$ in the part of the equation that we need to become the $e$ component of the poisson pmf.  $${{[\frac {\lambda t} {\lambda d}]} \choose k}\lambda d^k(1-\frac 1 f)^{[f{\lambda t}]-k} $$
Step 7: - ONLY $e$ term, we use properties of exponents to expand out the  righthand term above, remembering to break the f * lambda * t into the integer and decimal components
$$\lim_{f \to 0}((1-\frac 1 f)^{f{\lambda t}}*(1-\frac 1 f)^{\{{f{\lambda t}}\}}*(1-\frac 1 f)^k) $$
Step 8 - > First term in step 7 becomes the e term below that we were looking for. The other terms have to equal 1 because 1 to any power is 1. $$e^{-\lambda t}$$

Step 9: Now we just need to figure out what to do with the binomial combinations term and the lambda * d to the kth power term. We're close but not there yet. $${{[\frac {\lambda t} {\lambda d}]} \choose k}\lambda d^k e^{-\lambda t}$$
Step 10: First let's expand out the binomial term into its factorial components, while also canceling out the lambdas and breaking the term in square brackets into it's integer and decimal components. $${\frac{\frac {t} {d}-{\{\frac {t} {d}}\}!} {k!({\frac {t} {d}-{\{\frac {t} {d}}\}}-k!)}}\lambda d^k e^{-\lambda t}$$
Step 11: We can cancel out the factorial term on the denominator because it's already baked into the numerator, and we just adjust the numerator to go until k-1 $${\frac{(\frac {t} {d}-{\{\frac {t} {d}}\})+k-1!} {k!}}\lambda d^k e^{-\lambda t}$$
Step 12: Now we can take d to 0 and the k-1 terms effectively go away because the t/d terms become huge, so we can that t/d expression raised ot the kth power instead of a factorial, which is useful because exponents can be manipulated much more easily than factorials.  $$\lim_{d\to 0} {\frac {1} {k!}} * (\frac {t} {d}-{\{\frac {t} {d}}\})+k-1! * \lambda d^k e^{-\lambda t} $$
Step 13: This is the result of what I described in prevoius step $${\frac {1} {k!}} * (\frac {t} {d}-{\{\frac {t} {d}}\})^k *  \lambda d^k e^{-\lambda t}

$$


Step 14: Here we need to essentially find a way to get the remaining terms in the Poisson pmf. One thing to try is another substitution. If we look at the original PMF, it's clear that we need t/d term which is being multiplied by lambda * d ^k term to all be equal to lambda * t ^ k, and we would be done. $$ z =\lim_{d\to inf} (\frac {t} {d}-{\{\frac {t} {d}}\})^k$$
Step 15: This is just the equation rewritten after doing what's described in previous step. $$ \lim_{d\to inf} {\frac {1} {k!}} *z \lambda d^k e^{-\lambda t}$$

Step 16: Now is the cool part. Since we know the two have to be equivalent, we can do some algebraic manipulation and write lambda * d ^k in terms of lambda * t ^k and z. $$z \lambda d^k = \lambda t^k,\lambda d^k = {\frac {\lambda t^k} {z} }  $$
Step 17: Turns out that's exactly what we need because the z's cancel out and we're left with the poisson PMF. $$P(X=x) = \left(e^{-\lambda t}\lambda t^x /x!\right) \tag{1}$$
#prob #math 