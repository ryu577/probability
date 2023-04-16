# Vector spaces
Objects where addition is defined and multiplication by a scalar is defined. This means the objects should be closed under these operations.

There are many ways to express an object in a vector space. One of them is with vectors. Vectors require an arbitrary "basis". 

# Linear map
From [Linear map](https://en.wikipedia.org/wiki/Linear_map)

Let <math>V</math> and <math>W</math> be vector spaces over the same [Field](https://en.wikipedia.org/wiki/Field_(mathematics)) $K$. 

A function $f: V \to W$ is said to be a ''linear map'' if for any two vectors $\mathbf{u}, \mathbf{v} \in V$ and any scalar $c \in K$ the following two conditions are satisfied:

* [[Additive map|Additivity]] / operation of addition 
$$f(\mathbf{u} + \mathbf{v}) = f(\mathbf{u}) + f(\mathbf{v})$$
* [[Homogeneous function|Homogeneity]] of degree 1 / operation of scalar multiplication 
$$f(c \mathbf{u}) = c f(\mathbf{u})$$

Thus, a linear map is said to be ''operation preserving''. In other words, it does not matter whether the linear map is applied before (the right hand sides of the above examples) or after (the left hand sides of the examples) the operations of addition and scalar multiplication.

By [the associativity of the addition operation](https://en.wikipedia.org/wiki/Addition#Associativity "Addition"), for any vectors $$ \mathbf{u}_1, \ldots, \mathbf{u}_n \in V$$ and scalars $$c_1, \ldots, c_n \in K,$$ the following equality holds:
$$f(c_1 u_1 + c_2 u_2 + \dots c_n u_n) = c_1 f(u_1)+c_2f(u_2)+\dots +c_n f(u_n)$$

Thus a linear map is one which preserves [linear combinations](https://en.wikipedia.org/wiki/Linear_combination "Linear combination").

Given a basis, a linear map can be expressed as a matrix.

# Full rank
Full row rank means all row vectors are linearly independent. Full column rank means all column vectors are linearly independent. For a square matrix, the two become equivalent. So, the vectors span the whole space. Such a square matrix will also be invertible. See [mathexch post](https://math.stackexchange.com/questions/332908/looking-for-an-intuitive-explanation-why-the-row-rank-is-equal-to-the-column-ran) and also [this geometric answer](https://math.stackexchange.com/a/636198/155881) for why row rank and column rank of a square matrix have to be the same.

# Diagonalization
A matrix is diagonalizable if it can be expressed as:

$$A = P D P^{-1}$$
> Note: This transformation is called "Eigen decomposition"

We care about this property since (for one) it becomes easy to raise the matrix to powers.

$$A^n = (P D P^{-1}) (P D P^{-1}) (P D P^{-1}) = P D^n P^{-1}$$
> A matrix that isn't diagonalizable is defective. This can happen when the algebraic multiplicity is greater than the geometric multiplicity.
> Related concept: [Jordan normal form](https://en.wikipedia.org/wiki/Jordan_normal_form).


## Diagonalizable vs invertible
Taken from [mathexchange](https://math.stackexchange.com/questions/2107610/is-there-any-connection-between-a-matrix-being-invertible-and-being-diagonalizab)

One does not imply the other.

This matrix is invertible and not diagonalizable:

$\begin{pmatrix} 1 & 1 \\ 0 & 1\\ \end{pmatrix}$

This matrix is diagonalizable (in fact it is already a diagonal matrix) but not invertible: 

$\begin{pmatrix} 0 & 0 \\ 0 & 0 \\ \end{pmatrix}$

# Singular value decomposition
Taken from [Wikipedia SVD article](https://en.wikipedia.org/wiki/Singular_value_decomposition)

For any real matrix $A$, we can express it as:
$$A = U \Sigma V^T$$
See [mathexchange post](https://math.stackexchange.com/questions/320220/intuitively-what-is-the-difference-between-eigendecomposition-and-singular-valu) for difference between eigen decomposition and SVD.

- The vectors in the eigendecomposition matrix $P$ are not necessarily orthogonal, so the change of basis isn't a simple rotation. On the other hand, the vectors in the matrices $U$ and $V$ in the SVD are orthonormal, so they do represent rotations (and possibly flips).
 - In the SVD, the nondiagonal matrices $U$ and $V$ are not necessairily the inverse of one another. They are usually not related to each other at all. In the eigendecomposition the nondiagonal matrices $P$ and $P^{-1}$ are inverses of each other.
 - In the SVD the entries in the diagonal matrix $\Sigma$ are all real and nonnegative. In the eigendecomposition, the entries of $D$ can be any complex number - negative, positive, imaginary, whatever.
 - The SVD always exists for any sort of rectangular or square matrix, whereas the eigendecomposition can only exists for square matrices, and even among square matrices sometimes it doesn't exist.

# Symmetric matrices are diagonalizable
Taken from [mathexchange post](https://math.stackexchange.com/a/833622/155881).

A real symmetric operator $\mathcal{A}$ has real eigenvalues (thus real eigenvectors) and that eigenvectors corresponding to different eigenvalues are orthogonal.
> Question: is a linear operator the same as linear map?

## Real eigen values
For any real matrix $A$ and any vectors $\mathbf{x}$ and $\mathbf{y}$, we have
$$\langle A\mathbf{x},\mathbf{y}\rangle = \langle\mathbf{x},A^T\mathbf{y}\rangle.$$
Now assume that $A$ is symmetric, and $\mathbf{x}$ and $\mathbf{y}$ are eigenvectors of $A$ corresponding to distinct eigenvalues $\lambda$ and $\mu$. Then
$$\lambda\langle\mathbf{x},\mathbf{y}\rangle = \langle\lambda\mathbf{x},\mathbf{y}\rangle = \langle A\mathbf{x},\mathbf{y}\rangle = \langle\mathbf{x},A^T\mathbf{y}\rangle = \langle\mathbf{x},A\mathbf{y}\rangle = \langle\mathbf{x},\mu\mathbf{y}\rangle = \mu\langle\mathbf{x},\mathbf{y}\rangle.$$
Therefore, $(\lambda-\mu)\langle\mathbf{x},\mathbf{y}\rangle = 0$. Since $\lambda-\mu\neq 0$, then $\langle\mathbf{x},\mathbf{y}\rangle = 0$, i.e., $\mathbf{x}\perp\mathbf{y}$.

Now find an orthonormal basis for each eigenspace; since the eigenspaces are mutually orthogonal, these vectors together give an orthonormal subset of $\mathbb{R}^n$. Finally, since symmetric matrices are diagonalizable, this set will be a basis (just count dimensions).

This proves that a real symmetric operator $\mathcal{A}$ has real eigenvalues (thus real eigenvectors) and that eigenvectors corresponding to different eigenvalues are orthogonal.

## Jordan blocks
One question still stands: how do we know that there are no generalized eigenvectors of rank more than 1, that is, all Jordan blocks are one-dimensional?

We prove by induction in the number of eigenvectors, namely it turns out that finding an eigenvector (and at least one exists for any matrix) of a symmetric matrix always allows us to generate another eigenvector. So we will run out of dimensions before we run out of eigenvectors, making the matrix diagonalizable.

Suppose $\lambda_1$ is an eigenvalue of $A$ and there exists at least one eigenvector $\boldsymbol{v}_1$ such that $A\boldsymbol{v}_1=\lambda_1 \boldsymbol{v}_1$. Choose an orthonormal basis $\boldsymbol{e}_i$ so that $\boldsymbol{e}_1=\boldsymbol{v}_1$. The change of basis is represented by an orthogonal matrix $V$. In this new basis the matrix associated with $\mathcal{A}$ is $$A_1=V^TAV.$$
It is easy to check that $\left(A_1\right)_{11}=\lambda_1$ and all the rest of the numbers $\left(A_1\right)_{1i}$ and $\left(A_1\right)_{i1}$ are zero. In other words, $A_1$ looks like this:
$$\left(
\begin{array}{c|ccc}
\lambda_1 &  \\
\hline &  & \\
  & & B_1 & \\
 & &
\end{array}   
\right)$$
Thus the operator $\mathcal{A}$ breaks down into a direct sum of two operators: $\lambda_1$ in the subspace $\mathcal{L}\left(\boldsymbol{v}_1\right)$ ($\mathcal{L}$ stands for linear span) and a symmetric operator $\mathcal{A}_1=\mathcal{A}\mid_{\mathcal{L}\left(\boldsymbol{v}_1\right)^{\bot}}$ whose associated $(n-1)\times (n-1)$ matrix is $B_1=\left(A_1\right)_{i > 1,j > 1}$. $B_1$ is symmetric thus it has an eigenvector $\boldsymbol{v}_2$ which has to be orthogonal to $\boldsymbol{v}_1$ and the same procedure applies: change the basis again so that $\boldsymbol{e}_1=\boldsymbol{v}_1$ and $\boldsymbol{e}_2=\boldsymbol{v}_2$ and consider $\mathcal{A}_2=\mathcal{A}\mid_{\mathcal{L}\left(\boldsymbol{v}_1,\boldsymbol{v}_2\right)^{\bot}}$, etc. After $n$ steps we will get a diagonal matrix $A_n$.

![[linalg_symmetr_diagonal.png]]

This proof suggests an algorithm for diagonalizing a symmetric matrix. Implement that algorithm in Python.
