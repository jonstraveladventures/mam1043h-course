---
title: "4.1 Introduction to Linear Systems in Two Dimensions"
weight: 61
math: true
---
## Section 4.1: Linear Systems in Two Dimensions

Linear Systems in 2D

So far we have been confined to the line, and first order systems only. We have found a richness of behaviour, from fixed points, to bifurcations to catastrophes. But one of the big issues was that you could only ever move in one direction... and that seems like quite a constraint!

In a first order system, having position means your velocity is fixed. In many systems that one thinks of, you can choose both as initial conditions! For instance, a pendulum, you can start at any point with any velocity. This is where a first order equation falls short.

In this section we are going to make a leap into the plane (Into the world of two dimensional systems). We have to be a bit careful because a two dimensional system can mean a number of things:

1. A system in two ‘spatial’ dimensions, say $x$ and $y,$ each of which depends on time and is governed by only first derivatives.

1. A system in one dimension whose dynamics is governed by a second derivative.

1. A non-autonomous system in one dimension whose dynamics is governed by a first derivative.

All would lead to two first order differential equations (Make sure that you can see this, otherwise ask!)

The other constraint that we will have is that while we were previously looking at systems which could be non-linear, we are only going to deal with linear systems here. This means that all of the equations will be of the form:

$$
\\\dot{y}=c x+d y
$$

Where a, b, c and d are constant parameters. We can also write this as a matrix equation of the form:

$$
\dot{x}=A x
$$

Where now

$$
x=\left(\begin{matrix} x \\ y \end{matrix}\right) ,  A=\left(\begin{matrix} a & b \\ c & d \end{matrix}\right)
$$

This tells us that the matrix $A$ encodes all of the interesting information about our system. Every single linear first order system in the plane is encoded by a different choice of the parameters in $A$.

The fact that the system is linear (there are no $x^{ 2}$ or$ \text{ sin }\left(x\right)$ or ${\dot{y}}^{ 42} $or$\sqrt{\frac{x}{y}}$terms, for instance) makes life a lot easier:

If you have found yourself two different solutions to such a system, then you can always add them together and that will give you a new solution. I have written about this extensively [in the context of second order systems](http://www.mathemafrica.org/?p=11488), but the logic is exactly the same here.

Let’s look at a simple example of such a system. It’s not going to look like it at first, but let ’s see. Remember way back in [section 1.5](/sec1-4-phase-space/) we looked at the pendulum example. The equation for the pendulum was:

$$
\ddot{x}+\frac{g}{l}\text{ sin }\left(x\right)=0
$$

Well, this sure as anything ain’t linear, and it seems to be second order, and it seems to be in one variable... However, we can ask what happens if the pendulum only swings a bit. In that case $x$ is always small $\text{ sin }\left(x\right) \text{ is } $well approximated by:

$$
\text{ sin }\left(x\right)\approx{}x
$$

![Figure 1](/images/part4a/output_001.png)

So we can write the equation in the limit of small oscillations as:

$$
\ddot{x}=-\frac{g}{l}x
$$

Now if we play our trick of letting $\dot{x}=y$, then $\ddot{x} = \dot{y}$, then we can write:

$$
\\\dot{y}=-\frac{g}{l}x
$$

Which can be written as:

$$
\left(\begin{matrix} \dot{x} \\ \dot{y} \end{matrix}\right) =\left(\begin{matrix} 0 & 1 \\ \frac{-g}{l} & 0 \end{matrix}\right) \left(\begin{matrix} x \\ y \end{matrix}\right)
$$

ta-da! The pendulum in the limit of small oscillations is a first order linear system in two dimensions. Whodathunkit!

A system of this form, which stems from an equation given by

$$
\ddot{x}=-{\omega{}}^{2}x
$$

is at the heart of a great deal of physics. ω here is the frequency of oscillations. This system is called the **simple harmonic oscillator**. In the pendulum example above, ${\omega{}}^{2}=g/l$.

Remember that in one dimension, the phase portrait was a series of arrows on the line. Well, now we can draw the phase portrait as a series of lines on the plane. The phase space is given by the $\left(x,y\right) $plane, which we should remember is really equivalent to (but not quite the same as) the $\left(x,\dot{x}\right) \text{ plane }$. This means that each point in the plane corresponds to a position of our ‘particle’ (or pendulum, or what have you), and its velocity. We’ve actually seen all of this back in [section 1.5](/sec1-4-phase-space/) Go have a read through it again to make sure that you understand.

Let’s just see how to put the arrows in the plane again using our pendulum example (for small oscillations). Here is the phase plane:

![Figure 2](/images/part4a/output_002.png)

Note here that we’ve gone out to ±1 on the $x$-axis. We should be careful because at $x=1, \text{ sin }\left(x\right)$ is no longer that close to $x$ and so for anything which is that far out, we shouldn’t trust the solution completely.

Now let’s ask what the arrow should look like at the point... (3,1), for example. Let’s also set $l=g=1$, so our equations are:

$$
\\\dot{y}=-x
$$

So, when $x=\frac{1}{2}$ and $y=\frac{1}{4}$, this says that the point in our phase space will be changing its $x$ value at a rate of $\frac{1}{4}$, and its $y$ value by a rate of $\frac{-1}{2}$. So it’s moving faster in the vertical, down direction than it is in the horizontal right direction, and we can draw in an arrow accordingly:

![Figure 3](/images/part4a/output_003.png)

The arrow is actually for illustrative purposes only, so as long as the direction is right, and the relative magnitude is right, we’re ok. So let’s scale the arrow length by $\frac{1}{4}$

![Figure 4](/images/part4a/output_004.png)

What this really means is that when we are at position $\frac{1}{2}$ and going at velocity $\frac{1}{4}$ then our position will be increasing, but our velocity will be decreasing.

Now see what happens as you move the point of interest around in the plane:

![Figure 5](/images/part4a/output_005.png)

Now let’s plot lots of these arrows together in the plane to see the ‘flow’ of this system:

![Figure 6](/images/part4a/output_006.png)

We seem to be going in circles... some sort of periodic behaviour is what you would expect for a pendulum.

What would happen to a particle of it was placed at some point in this phase plane? Well, it seems that it would go in circles, and that’s actually exactly what would happen. Let’s pick a point $x=0.5, y=0$ as our initial conditions. It will go in a circle of radius 0.5.

Note that up until now we’ve looked at the behaviour without solving the equations at all. In fact, in this case, it ’s pretty easy to solve these equations. The general solution is:

$$
\\y=c_{2}\text{ cos } t-c_{1}\text{ sin } t
$$

Where $c_{1} \text{ and } c_{2}$ are constants. The solution which starts at $x=0.5, y=0$ is the above solution with $c_{1}=0.5, c_{2}=0$, so the solution is:

$$
\\y=-0.5\text{ sin } t
$$

We can plot this in the plane:

![Figure 7](/images/part4a/output_007.png)

Such a circle is known as a **Closed Orbit** which is a general type of solution which comes back to itself in phase space. Such an orbit will always correspond to an oscillatory solution.

Plotting the actual trajectory of this corresponds to plotting $x\left(t\right)$, which is just:

![Figure 8](/images/part4a/output_008.png)

We have to be careful here. We started off with a second order system, so the above graph tells you everything about the trajectory. We could have a system which is a first order system where you are moving around on a two dimensional plane, and then this wouldn’t give you everything you need to know. Note that if we plotted $y\left(t\right) $we would have:

![Figure 9](/images/part4a/output_009.png)

But this can be obtained just from taking the derivative of the graph of $x\left(t\right)$.

We spoke a lot in the last sections about fixed points. Can you see whether there are any fixed points in this case?

The above example of the pendulum was a specific instance of the equation

$$
\dot{x}=A x
$$

with

$$
A=\left(\begin{matrix} 0 & 1 \\ -g/l & 0 \end{matrix}\right) , \text{ and setting } g/l=1
$$

Let’s look at another series of cases of the matrix $A$. We can ask what the phase portraits look like for linear equations with

$$
A=\left(\begin{matrix} a & 0 \\ 0 & -1 \end{matrix}\right)
$$

for different values of $a$.

Note, this is not something you should necessarily be able to see immediately by looking at the equation, but you should be able to plot the arrows. Make sure that you agree with the directions that the arrows are pointing for these five different cases.

For each case, see if you can see where the fixed points are and see if you can tell whether they are stable, unstable or half-stable.

Now see if you can plot some trajectories in the $\left(x,t\right) $plane for each of the above phase portraits.

In fact, we can look again at the equations that we are talking about here. They are:

$$
\left(\begin{matrix} \dot{x} \\ \dot{y} \end{matrix}\right) =\left(\begin{matrix} a & 0 \\ 0 & -1 \end{matrix}\right) \left(\begin{matrix} x \\ y \end{matrix}\right)
$$

or in other words

$$
\dot{x}=a x
$$

$$
\dot{y}=-y
$$

$x$ and $y$ are ‘decoupled’ here. They don’t depend on each other (other than the fact that secretly, $\dot{x}=y$).

So we can solve this very easily and it gives us:

$$
x=x_{o} e^{a t}
$$

$$
y=y_{o} e^{-t}
$$

where $x_{o}$ is the initial position, and $y_{o} $is the initial velocity.

We can actually find what the curves look like in phase space by solving the first of these equations for $t$

$$
t=\frac{1}{a}\text{ ln }\left(\frac{x}{x_{o}}\right)
$$

and plugging it into the second:

$$
y=y_{o} e^{-t}=y_{o} e^{-\left(\frac{1}{a}\text{ ln }\left(\frac{x}{x_{o}}\right)\right)}=y_{o} e^{\left(\text{ ln }\left({\left(\frac{x}{x_{o}}\right)}^{-\frac{1}{a}}\right)\right)}={y_{o}\left(\frac{x}{x_{o}}\right)}^{-\frac{1}{a}}
$$

So let’s say $a=-2$ and we have our initial condition $x_{o}=0.5, y_{o}=0.75$, we would have:

$$
y=0.75{\left(\frac{x}{0.5}\right)}^{\frac{1}{2}}
$$

Let’s plot this on top of the phase portrait above for the $a=-2 $case:

![Figure 10](/images/part4a/output_010.png)

The particle moves quickly in to the centre, then slows down and will never actually arrive at the origin.

As a trajectory, this looks like (with $x\left(t\right)$ in blue and $y\left(t\right)$ in red):

![Figure 11](/images/part4a/output_011.png)

We can do the same thing for other values of initial conditions and values of $a$:

![Figure 12](/images/part4a/output_012.png)

Now try and plot the trajectories for some of these different initial conditions and values of $a$.

You will explore the fixed point structure of this system in the [Exercises for part 4](/sec4-5-exercises/).
## Animated versions

![Animation](/images/part4a/anim_001.gif)

![Animation](/images/part4a/anim_002.gif)

