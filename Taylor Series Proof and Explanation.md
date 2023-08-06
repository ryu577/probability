

Explanation:

1. Taylor Series enables us to approximate functions at a particular point with polynomials
2. In order to approximate a function at a point, we need to understand certain characteristics about how the function behaves at that particular point (slope, concavity, etc) If we can understand these characteristics, and then create a polynomial with the same characteristics around that same point, then we have created a polynomial approximation for the original function at that point
3. We use derivatives to find tangent lines, concavity, etc. So the general idea of Taylor Series is to differentiate the original function and plug the point we're approximating around into the resulting derivative, then take advantage of the power rule for derivatives of polynomials to make the ith derivative of the polynomial equal to the output of the ith derivative of the original function evaluated at the particular point. 


Proof:
$$ 
f(x) = a_0 + a_1(x-a)^1 + a_2(x-a)^2 + ...a_i(x-a)^i+...a_n(x-a)^n
$$

$$
f(0) = 0
$$
$$
f^2(x) = a_1 + 2a_2(x-a) ... na_n(x-a)^{n-1}
$$
$$
f^i(x) = i!*a_i ... na_n(x-a)^{n-1}
$$

All terms except the ith term are either gone or still have an X in them. As long as we plug in a for x, the only term left in the general case is i! * ai. This leads to the natural conclusion that:

$$
f^i(x)/i! = a_i
$$

Which is how we use the Taylor series to obtain the coefficients of a polynomial that best approximate a function around a point