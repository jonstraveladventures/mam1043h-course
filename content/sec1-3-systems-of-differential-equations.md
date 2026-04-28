---
title: "1.3 Systems of Differential Equations"
weight: 14
math: true
---
## Section 1.3: Systems Of Differential Equations

Systems of Differential Equations

In this course we will look at simple, yet powerful tools for understanding dynamical systems.

We begin with looking in detail at the language of mathematics that we will be using. I’ve already outlined that we will be using differential equations, but these come in a variety of forms.

In this course we will almost entirely be using **First Order Systems of Differential Equations**. An example of this might be:

$$
X'\left(t\right)=X\left(t\right)-Y\left(t\right)
$$

$$
Y'\left(t\right)=X\left(t\right)
$$

This says that I have two variables, X and Y, which can both change with time. The rate of change of X a given time is given by the difference between the values of X and Y at that time. The rate of change of Y is given by the value of X at that time. Below you can see the solution to these equations plotted as a function of t. As you change the initial values (ie. at time t=0) of X and Y, the solutions change.

(You don't need to be able to solve these equations)

![Animated solutions: X(t) and Y(t) as initial values vary](/images/part1d/anim_002.gif)

What are we seeing here? Well, we have these two functions, X and Y, which are changing in time, and they are related through a system of first order differential equations. Changing the values of the functions at an initial time alter the future behaviour of them.

Let's see an example of this. If you start off with $X\left(0\right)=1.5 $and $Y\left(0\right)=0.5.$ From the differential equations this immediately sets:

$$
X'\left(0\right)=1.5-0.5=1
$$

$$
Y'\left(0\right)=1.5
$$

And that is the initial ‘trajectory’ of your functions. So $Y$ is increasing faster than X, so Y will be approaching X...

Which means that $X'\left(t\right)=X\left(t\right)-Y\left(t\right) $will be getting smaller...etc.

So as we change the initial conditions we will see different future trajectories.

Ok, so that is one example of a first order system of two differential equations.

We can be a bit more general - We can write down a system of n first-order differential equations:

$$
x_{1}'\left(t\right)=f_{1}\left(x_{1}\left(t\right),x_{2}\left(t\right),...,x_{n}\left(t\right)\right)
$$

$$
x_{2}'\left(t\right)=f_{2 }\left(x_{1}\left(t\right),x_{2}\left(t\right),...,x_{n}\left(t\right)\right)
$$

$$
....
$$

$$
x_{n}'\left(t\right)=f_{n}\left(x_{1}\left(t\right),x_{2}\left(t\right),...,x_{n}\left(t\right)\right)
$$

Where we have *n* variables $x_{1} \text{ to } x_{n}$ and their derivatives are given by *n* functions $f_{1} \text{ to } f_{n} \text{ which are } \text{ functions of } \text{ the variables }$. These are called first order because we have only first derivatives.

These variables could be many things. For instance if we were talking about a particle moving around in three dimensions then they might correspond to the coordinates so we would have that $x_{1}$, $x_{2}$, and $x_{3} $are the traditional x, y and z coordinates respectively. Here is a particle moving about in three dimensions with the $x_{i}'s$ changing in time.

![Particle moving in three dimensions](/images/part1d/anim_001.gif)

**The differential equation says**: however the thing is moving, the rate of change of the $x_{i}'s$ has some fixed relationship with the value of the $x_{i}'s $themselves.

If we had second derivatives, these would be second order differential equations. Here is an example of a single, second order differential equation:

$$
x''\left(t\right)+x'\left(t\right)+3\text{ sin }\left(x\left(t\right)\right)=0
$$

Now comes some magic.

It turns out we can take a second order differential equation and turn it into two first order differential equations!

Let’s actually take this one above. The first thing that we will always do, is to define some new variable (say y) as the derivative of your first variable. So we are simply going to define:

$$
y\left(t\right)=x'\left(t\right)
$$

You agree that I can do that right? We just need that definition function as part of out system.

Well, that means that the second derivative of x is the first derivative of y:

$$
y'\left(t\right)=x''\left(t\right)
$$

Now our job will be to eliminate all second derivatives using that last expression:

$$
\text{ this } \to  x''\left(t\right)+x'\left(t\right)+3\text{ sin }\left(x\left(t\right)\right)=0
$$

$$
\text{ becomes } \to  y'\left(t\right)+x'\left(t\right)+3\text{ sin }\left(x\left(t\right)\right)=0
$$

So now we could write:

$$
\text{ becomes } \to y'\left(t\right)=-\left(x'\left(t\right)+3\text{ sin }\left(x\left(t\right)\right)\right)
$$

$$
\text{ because of } \text{ this } \to  x'\left(t\right)=y\left(t\right)
$$

We would really like to have expressions as we had in our general case for the system of equations.

So we can also get rid of the $x'\left(t\right)$ on the right hand side and just replace it with y(t). So now we have:

$$
y'\left(t\right)=-\left(y\left(t\right)+3\text{ sin }\left(x\left(t\right)\right)\right)
$$

$$
x'\left(t\right)=y\left(t\right)
$$

We have just converted our second order equation into two first order equations which fulfil the pattern that we defined above here.

Hang on a minute. **Why** are we doing this?

Well, it turns out to be really convenient to work with systems of first order equations in general.