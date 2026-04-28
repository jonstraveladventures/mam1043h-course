---
title: "1.5 Spectrum of Systems of Differential Equations"
weight: 16
math: true
---
## Section 1.5: The Spectrum of Systems of Differential Equations

The Spectrum of Systems of Differential Equations

There are many different families of dynamical systems, from the simplest, to the most complex. We’ve said that a dynamical system can be written in the form:

$$
x_{1}'\left(t\right)=f_{1}\left(x_{1}\left(t\right),x_{2}\left(t\right),...,x_{n}\left(t\right)\right)
$$

$$
x_{2}'\left(t\right)=f_{2}\left(x_{1}\left(t\right),x_{2}\left(t\right),...,x_{n}\left(t\right)\right)
$$

$$
....
$$

$$
x_{n}'\left(t\right)=f_{n}\left(x_{1}\left(t\right),x_{2}\left(t\right),...,x_{n}\left(t\right)\right)
$$

Clearly if there is just one variable $x_{1}$that’s about as simple as you can get. It turns out that there are systems where there are not just a lot of different $x_{i}$ but an infinite number. One treats these not as discrete systems, but so called continuous systems.

There's a very important area of physics called quantum field theory, where one can describe the world using an infinite number of interacting $x_{i}'s$. We will NOT deal with this in this course!

Another classification is given by the types of functions $f_{i}$. The two options are linear functions, and non-linear functions. For a system of linear differential equations, the functions on the right are all simply linear functions of the $x_{i}$.

For instance:

$$
x_{1}'\left(t\right)=5+x_{1}\left(t\right)+4x_{2}\left(t\right)
$$

$$
x_{2}'\left(t\right)=-x_{1}\left(t\right)-x_{2}\left(t\right)
$$

The terms on the right are either of zeroth order in the $x_{i}$ or first order. There are no terms with for instance ${x_{1}}^{2}$ or $\left(x_{1}. x_{2}\right)$ or $\text{ sin }\left(x\right)$ or the like. If there are constant terms (as in the 5, in equation 0.4 above), then these are known as inhomogeneous. If every term is precisely of first order in the $x_{i}$ then it is a homogenous equation.

It turns out that [systems of linear first order differential equations](https://en.wikipedia.org/wiki/Linear_dynamical_system) are always possible to solve. The most complex behaviour however tends to happen when we have non-linear differential equations - ie. where the $f_{i}$ are anything but linear.

That being said, we are going to be able to take non-linear systems and discover certain properties of them by approximating them in clever ways as linear systems.

I've produced a table here which is highly inspired by that in the book by Strogatz, but with some of my own thoughts thrown in too. You don ’t need to know this table specifically, but notice how the cases show up in your respective courses (not only this one).

N is the number of differential equations in the system.