

Need to show the following:

$$
e^{i\theta} = cos(\theta) + isin(\theta)
$$
1. Expand out left hand side with Taylor Series

$$
e^{i\theta} = 1 + ix - \frac{x^2}{2} - i\frac{x^3}{3}....
$$
2. Expand out cos(theta)

$$
\begin{align}
cos(0) = 1 \\
c0  = 1 \\
d\theta/dx = -sin(\theta) \\
sin(0)= 0 \\
c1  = 0 \\
d^2\theta^2\ = -cos(\theta) \\
-cos(0) = -1 \\
c2  = -1/2! \\
d^3\theta^3\ = sin(\theta) \\
sin(0)=0 \\ 
d^4\theta^4\ = cos(\theta) \\
cos(0) = 1
\end{align}
$$

3. Expand out isin(theta)

$$
\begin{align}
i\sin(0) = 0 \\
c0 = 0 \\
d\theta/dx = icos(\theta) \\
icos(0) = i \\
c1 = i \\
d^2\theta^2 = -i\sin(\theta) \\
-i\sin(\theta) = 0 \\
c2 = 0 \\
d^3\theta^3 = -i\cos(\theta) \\
-i\cos(\theta) = -i \\
c3 = -i/3!
\end{align}
$$
4. Combine the two
$$
\begin{align}
e^{i\theta} = cos(\theta) + isin(\theta)\\
1 + ix - \frac{\theta^2}{2} - i\frac{\theta^3}{3}.... = (1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!}) + (i\theta - \frac{i\theta^3}{3!} + \frac{i\theta^5}{5!})  \\
e^{i\theta}= cos(\theta) + isin(\theta)

\end{align}
$$

1. 