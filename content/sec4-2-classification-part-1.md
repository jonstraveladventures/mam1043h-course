---
title: "4.2 Classification of Linear Systems — Part 1"
weight: 62
math: true
---
## Section 4.2a: Classification of Linear Systems (Part 1)

Classification of Linear Systems

We said in the previous section that in general, a first order, autonomous linear system in two dimensions could be written:

$$
\dot{x}=A x
$$

Where

$$
x=\left(\begin{matrix} x \\ y \end{matrix}\right) ,  A=\left(\begin{matrix} a & b \\ c & d \end{matrix}\right)
$$

We also showed the behaviour for a subset of these systems, in particular where:

$$
A=\left(\begin{matrix} a & 0 \\ 0 & -1 \end{matrix}\right)
$$

In this section we will look at the more general case and ask about how we can classify the different types of behaviour.

To solve the system in general, we will make use of the fact that the systems are linear, which means that if we find any two solutions, they can be added together in any linear combination and they will still be a solution. Because this is a first order equation in two variables, we need to find precisely two linearly independent solutions and we are done.
 
Let us make a guess solution (which we call an ansatz). Let's see if we can find solutions of the form:

$$
x=e^{\lambda{} t}v
$$

where $v$ is some vector and λ is some number, both to be determined. If this is to be a solution, then it must satisfy the differential equation. Let’s plug it in:

$$
LHS:= \dot{x}=\lambda{}e^{\lambda{} t}v,     RHS:=A x={Ae}^{\lambda{} t}v
$$

which we write as:

$$
{\lambda{}e}^{\lambda{} t}v=A e^{\lambda{} t}v
$$

The scalar $e^{\lambda{} t}$ can pass through the matrix, and we get

$$
{\lambda{}e}^{\lambda{} t}v=e^{\lambda{} t}A v
$$

We can multiply both sides by $e^{-\lambda{} t}$ and this gives:

$$
\lambda{} v=A v
$$

or, more normally written:

$$
A v=\lambda{} v
$$

This is a so-called eigenvalue equation. Remember that $A $is given, and we want to find λ (the eigenvalue) and $v$ (the eigenvector). There will generally be 2 of these. 

What does this mean? Remember $A $is a matrix, and $v$ is a vector. So, we want to find a vector, which, when we multiply it by a matrix, gives back the same vector, but scaled by some scalar. Let's take a really concrete example. 

What if you were given:

$$
A=\left(\begin{matrix} 1 & 3 \\ 1 & -1 \end{matrix}\right)
$$

Can you find a vector which, when you multiply it by this matrix, returns the same vector, only scaled? Let’s make a random guess. Does

$$
v=\left(\begin{matrix} 2 \\ 3 \end{matrix}\right)
$$

work? Let’s check:

$$
A v=\left(\begin{matrix} 1 & 3 \\ 1 & -1 \end{matrix}\right)\left(\begin{matrix} 2 \\ 3 \end{matrix}\right) =\left(\begin{matrix} 1 2+3 3 \\ 1 2-1 3 \end{matrix}\right) =\left(\begin{matrix} 10 \\ -1 \end{matrix}\right)
$$

Is $\left(\begin{matrix} 10 \\ -1 \end{matrix}\right) $equal to $\left(\begin{matrix} 2 \\ 3 \end{matrix}\right) $multiplied by some scalar? Nope... there is no λ such that

$$
\left(\begin{matrix} 10 \\ -1 \end{matrix}\right) =\lambda{} \left(\begin{matrix} 2 \\ 3 \end{matrix}\right)
$$

$$
v=\left(\begin{matrix} -1 \\ 1 \end{matrix}\right)
$$

Because:

$$
A v=\left(\begin{matrix} 1 & 3 \\ 1 & -1 \end{matrix}\right)\left(\begin{matrix} -1 \\ 1 \end{matrix}\right) =\left(\begin{matrix} 1 \left(-1\right)+3 1 \\ 1  \left(-1\right)-1  1 \end{matrix}\right) =\left(\begin{matrix} 2 \\ -2 \end{matrix}\right)
$$

and we can certainly find a λ such that:

$$
\left(\begin{matrix} 2 \\ -2 \end{matrix}\right) =\lambda{} \left(\begin{matrix} 1 \\ -1 \end{matrix}\right)
$$

The answer is λ (the eigenvalue) = 2. There’s another vector which is

$$
v=\left(\begin{matrix} 3 \\ 1 \end{matrix}\right)
$$

which is also an eigenvector, with eigenvalue λ = 2.

What’s really going on here? Well, the matrix can be thought of as a transformation of vectors in the plane. It can rotate, scale and skew the vectors. We are asking which are the vectors which are only scaled by the transformation. There will generally be two orthogonal vectors. 

Note that actually once we’ve found an eigenvector $v$, any scalar multiple of $v$ will also be an eigenvector, but of course it won’t be linearly independent.

OK, so now we actually want to see how to find these eigenvectors rather than just check that one you’ve been handed is really an eigenvector. The method is relatively straightforward.

To find the eigenvalues, λ, of a matrix $A$=$\left(\begin{matrix} a & b \\ c & d \end{matrix}\right)$, we need to solve the equation:

$$
\text{ det }\left(A-\lambda{} I\right)=0
$$

where $I$ is the 2x2 identity matrix $\left(\begin{matrix} 1 & 0 \\ 0 & 1 \end{matrix}\right)$. This can be written as:

$$
\text{ det }\left(\begin{matrix} a-\lambda{} & b \\ c & d-\lambda{} \end{matrix}\right)=0
$$

which is just:

$$
{\lambda{}}^{2}-\tau{} \lambda{}+\Delta{}=0
$$

where:

$$
\\\Delta{}=\text{ det }\left(A\right)=a d-b c
$$

Which means that in general we have two eigenvalues ${\lambda{}}_{1}$ and ${\lambda{}}_{2}$ given by:

$$
{\lambda{}}_{1}=\frac{\tau{}+\sqrt{{\tau{}}^{2}-4\Delta{}}}{2}   \text{ and }  {\lambda{}}_{2}=\frac{\tau{}-\sqrt{{\tau{}}^{2}-4\Delta{}}}{2}
$$

Once you have an eigenvalue you can calculate the eigenvectors by solving:

$$
\left(\begin{matrix} a-{\lambda{}}_{1} & b \\ c & d-{\lambda{}}_{1} \end{matrix}\right)\left(\begin{matrix} v_{1,1} \\ v_{1,2} \end{matrix}\right) =\left(\begin{matrix} 0 \\ 0 \end{matrix}\right)   \text{ and }  \left(\begin{matrix} a-{\lambda{}}_{2} & b \\ c & d-{\lambda{}}_{2} \end{matrix}\right)\left(\begin{matrix} v_{2,1} \\ v_{2,2} \end{matrix}\right) =\left(\begin{matrix} 0 \\ 0 \end{matrix}\right)
$$

This all looks pretty complicated, but in practice it’s really not.

Now, having found your ${\lambda{}}_{1}, {\lambda{}}_{2} \text{ and } v_{1}, v_{2}$, we can write our general solution to the differential equation as:

$$
x\left(t\right)=c_{1}e^{{\lambda{}}_{1}t}v_{1}+c_{2}e^{{\lambda{}}_{2}t}v_{2}
$$

where $c_{1}$and $c_{2}$ are free constants, which are fixed by the two initial conditions.

Let’s look at an example of all of this. What if you were given the differential equations:

$$
\dot{x}=x+y
$$

$$
\dot{y}=4x-2y
$$

with initial conditions $\left(x\left(0\right),y\left(0\right)\right)=\left(2,-3\right)$? Well, first let’s put it in the form of a matrix equation:

$$
\dot{x}=\left(\begin{matrix} 1 & 1 \\ 4 & -2 \end{matrix}\right) x
$$

Now with our ansatz $x = e^{\lambda{} t}v$, we end up with the eigenvalue equation:

$$
\left(\begin{matrix} 1 & 1 \\ 4 & -2 \end{matrix}\right) v=\lambda{} v
$$

The eigenvalues are given by

$$
{\lambda{}}_{1}=\frac{\tau{}+\sqrt{{\tau{}}^{2}-4\Delta{}}}{2}   \text{ and }  {\lambda{}}_{2}=\frac{\tau{}-\sqrt{{\tau{}}^{2}-4\Delta{}}}{2}
$$

where now τ=1-2=-1 and $\Delta{}=\left(1\left(-2\right)-1\left(4\right)\right)=-6, \text{ so }:$

$$
{\lambda{}}_{1}=2   \text{ and }  {\lambda{}}_{2}=-3
$$

Now we have to solve:

$$
\left(\begin{matrix} 1-2 & 1 \\ 4 & -2-2 \end{matrix}\right)\left(\begin{matrix} v_{1,1} \\ v_{1,2} \end{matrix}\right) =\left(\begin{matrix} 0 \\ 0 \end{matrix}\right)   \text{ and }  \left(\begin{matrix} 1+3 & 1 \\ 4 & -2+3 \end{matrix}\right)\left(\begin{matrix} v_{2,1} \\ v_{2,2} \end{matrix}\right) =\left(\begin{matrix} 0 \\ 0 \end{matrix}\right)
$$

which gives:

$$
v_{1}=\left(\begin{matrix} v_{1,1} \\ v_{1,2} \end{matrix}\right) =\left(\begin{matrix} 1 \\ 1 \end{matrix}\right)   \text{ and }  v_{2}=\left(\begin{matrix} v_{2,1} \\ v_{2,2} \end{matrix}\right) =\left(\begin{matrix} 1 \\ -4 \end{matrix}\right)
$$

So finally we have the general solution:

$$
x\left(t\right)=c_{1}e^{2t }\left(\begin{matrix} 1 \\ 1 \end{matrix}\right)  +c_{2}e^{-3t}\left(\begin{matrix} 1 \\ -4 \end{matrix}\right)
$$

Now we have to fix $c_{1}$ and $c_{2}$ by the initial conditions:

$$
x\left(0\right)=\left(\begin{matrix} 2 \\ -3 \end{matrix}\right) =c_{1}\left(\begin{matrix} 1 \\ 1 \end{matrix}\right)  +c_{2}\left(\begin{matrix} 1 \\ -4 \end{matrix}\right)
$$

which means that $c_{1}=1$ and $c_{2}=1$, so the solution is:

$$
x\left(t\right)=e^{2t }\left(\begin{matrix} 1 \\ 1 \end{matrix}\right)  +e^{-3t}\left(\begin{matrix} 1 \\ -4 \end{matrix}\right)
$$

or in other words

$$
x\left(t\right)=e^{2t}+e^{-3t}, y\left(t\right)=e^{2t}-4e^{-3t}
$$

How would we draw the phase portrait for this system?

Well, what have we discovered? We know that this system has two eigenvalues, one given by$\left(\begin{matrix} 1 \\ 1 \end{matrix}\right) $which has eigenvalue 2, and one give by $\left(\begin{matrix} 1 \\ -4 \end{matrix}\right)$ which has eigenvalue -3. Any multiple of these eigenvectors will behave the same way. The one with eigenvalue 2 will grow exponentially, and the one with eigenvalue -3 will fall off exponentially. We can thus draw vectors going from the fixed point at $\left(x,y\right)=\left(0,0\right)$ (which will always be a fixed point) as follows:

![Figure 1](/images/part4b/output_001.png)

Here we have drawn the arrows of the length of the eigenvalues. This says that the incoming arrows are length 3 and the outgoing arrows are length 2. You can picture this as saying that you decay along the decaying eigenvectors faster than you grow out of the growing ones.

OK, so what happens in between? Well, we can get a qualitative picture by imagining that here you have a flow of water which, if you get close to the arrows going in, you will be moving into the centre, and if you get close to the arrows moving out, you will be moving out, and the force of the arrows flowing in is faster than that flowing out.

Let’s look at this quantitatively:

Remember that our general solution to this differential equation was:

$$
x\left(t\right)=c_{1}e^{2t }\left(\begin{matrix} 1 \\ 1 \end{matrix}\right)  +c_{2}e^{-3t}\left(\begin{matrix} 1 \\ -4 \end{matrix}\right)
$$

Let’s say that at $t=0$ we start at the point $\left(\begin{matrix} -0.5 \\ 3 \end{matrix}\right)$. This really means that $x\left(0\right)=-0.5$ and $y\left(0\right)=3$. Let’s plug this in and see what we get for $c_{1} \text{ and } c_{2}$:

$$
\left(\begin{matrix} -0.5 \\ 3 \end{matrix}\right)=c_{1}\left(\begin{matrix} 1 \\ 1 \end{matrix}\right)  +c_{2}\left(\begin{matrix} 1 \\ -4 \end{matrix}\right)
$$

You can write this as: $-0.5=c_{1}+c_{2}$, $3=c_{1}-4c_{2}$ and solve this to get: $c_{1}=0.2$, $c_{2}=-0.7$, so the solution will be:

$$
x\left(t\right)=0.2e^{2t }\left(\begin{matrix} 1 \\ 1 \end{matrix}\right)  -0.7e^{-3t}\left(\begin{matrix} 1 \\ -4 \end{matrix}\right)
$$

Let’s look at this for times from $t=0$ to $t=1$ in steps of 0.1. This will be a list of the points in ${x,y}$ that we visit.

We can plot these on the diagram (starting point in red):

![Figure 2](/images/part4b/output_002.png)

Let’s plot them for a finer set of points (let’s put in 100, and then join the line):

![Figure 3](/images/part4b/output_003.png)

![Figure 4](/images/part4b/output_004.png)

and some more:

![Figure 5](/images/part4b/output_005.png)

An animation starting with these points will look like:

![Figure 6](/images/part4b/output_006.png)

It took us quite a long time to get here, but let’s put it all together and see how we could solve this much quicker. The original DE was:

$$
\dot{x}=x+y
$$

$$
\dot{y}=4x-2y
$$

We start by putting this into a matrix equation:

$$
\dot{x}=\left(\begin{matrix} 1 & 1 \\ 4 & -2 \end{matrix}\right) x
$$

And our job will be to find eigenvalues and eigenvectors of this matrix which comes down to solving:

$$
\left(\begin{matrix} 1 & 1 \\ 4 & -2 \end{matrix}\right) v=\lambda{} v
$$

We can find the eigenvalues and eigenvectors and they are given by:

$$
{\lambda{}}_{1}=2   \text{ and }  {\lambda{}}_{2}=-3
$$

$$
v_{1}=\left(\begin{matrix} v_{1,1} \\ v_{1,2} \end{matrix}\right) =\left(\begin{matrix} 1 \\ 1 \end{matrix}\right)   \text{ and }  v_{2}=\left(\begin{matrix} v_{2,1} \\ v_{2,2} \end{matrix}\right) =\left(\begin{matrix} 1 \\ -4 \end{matrix}\right)
$$

and so our solution is given by:

$$
x\left(t\right)=c_{1}e^{2t }\left(\begin{matrix} 1 \\ 1 \end{matrix}\right)  +c_{2}e^{-3t}\left(\begin{matrix} 1 \\ -4 \end{matrix}\right)
$$

where $c_{1}$and $c_{2}$ are found from the initial conditions that you want to set the system up in.

We will always have two eigenvalues, however these eigenvalues can be real or complex. If they are real, then they can be positive or negative (or zero), and if they are complex, they can have different signs for the real and imaginary parts. Each of these is going to give us a different kind of behaviour.

In the case we’ve just looked at, we have one positive and one negative eigenvalue. This says that we will have one eigenvector coming in to the fixed point, and one going out. What if we had two negative eigenvalues? Well, in that case both of the eigenvectors coming in, so it might give us something like:

![Figure 7](/images/part4b/output_007.png)

Everything is piling all into the centre.

One thing which is very important to note here is that when we get close to the centre, everything is flowing in along the $\left(\begin{matrix} 1 \\ 1 \end{matrix}\right) $direction. This is the direction of the smallest absolute eigenvalue (smallest |λ|). This is a general rule, that to work out the flow close to the fixed point, we need to find the eigenvector corresponding to the smallest |λ| and this is where everything will be coming in from. The same is true when we have two positive eigenvalues - ie. everything is flowing out in the direction of smallest |λ|.

And unsurprisingly, if the eigenvalues are both positive, everything is going to explode out from the centre: Exactly the same as the above but you can imagine it all going the other way.

Let’s stop there for now and in the next lesson we will look at what happens when we have complex eigenvalues.
## Animated versions

![Animation 1](/images/part4b/anim_001.gif)

