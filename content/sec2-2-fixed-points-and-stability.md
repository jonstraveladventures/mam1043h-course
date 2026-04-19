---
title: "2.2 Fixed Points and their Stability"
weight: 22
math: true
---
## Section 2.2: Fixed Points and Stability in General

Even though our last example was very specific, we've developed a great deal of the “technology” that we're going to need for this section already.

I can give you any differential equation of the form:

$$
\dot{x}=f\left(x\right)
$$

You can work out whether it has fixed points or not, and whether or not they are stable. We will deal with one more type of fixed point shortly.

If you’re not given $f\left(x\right)$ in terms of a functional form and just give you the graph. It turns out that from this you can already tell a huge amount.

Let's say I give you this graph:

![Figure 1](/images/part2b/output_001.png)

You can immediately work out from this that there are two fixed points (In the region given $\left[-3,2\right]$).

![Figure 2](/images/part2b/output_002.png)

We can even decide their stabilities!

- Let's say we start just to the left of the left-hand fixed point, at say $x=-2$. Well, we can see that the value of $\dot{x}$ is positive here, which says that $x$ is increasing, which says that we will be moving to the right.

- If you start just to the right of that fixed point, $\dot{x}$ is negative, so you will be moving to the left.

- This is a stable fixed point.

Using the same reasoning, you can show that the right hand fixed point is unstable.

We can now put on arrows, and mark the fixed points correctly:

![Figure 3](/images/part2b/output_003.png)

This picture is called a **phase portrait** and gives us a lot of qualitative features about the solutions to a first order differential equation.

If we start to the left of the right dot, we are going to flow over towards the left dot, but never reach it **remember**!

The direction of the arrow is given by the sign of $\dot{x}$ and the magnitude its magnitude (At the point)

The arrows are called a **flow diagram**.

You might just be given the flow diagram, which would be like:

![Figure 4](/images/part2b/output_004.png)

and be asked to figure out what equation might give rise to it (note that there are an infinite number of possibilities).

**The Summary You Were Waiting For**

Given a differential equation:

$$
\dot{x}=f\left(x\right)
$$

- The fixed points, labeled $x^{*},$ are given by $f\left(x^{*}\right)=0$.

- The particle will be moving to the right whenever $f\left(x\right)>0$ and moving to the left whenever $f\left(x\right)<0$.

- A fixed point is stable if $f\left(x\right)$ goes from positive to negative through zero as you increase $x$

- A fixed point is unstable if $f\left(x\right)$ goes from negative to positive through zero as you increase $x$

Fixed points are also know as equilibrium solutions, steady-state solutions or just constant solutions.

As $x \left(t\right)=x^{*}$ will be a solution for all time. The tricky thing about these is that, if you don't start at a steady state solution, you will never get to one. Can you see why? (Look here if not)

Plotting Trajectories

If we wanted to plot the trajectories, the first thing we would do would be to note the fixed points:

![Figure 5](/images/part2b/output_005.png)

Here I’ve drawn the stable fixed point in black and the unstable one as a dashed line.

The next thing to notice is that at around $x=0.6$ the velocity is a maximum, which implies that our function $x \left(t\right)$ will be steepest as it passes through $x=0.6$. We can also see that below our stable fixed point, the velocity only increases slowly, so the gradient of $x \left(t\right)$ won’t be increasing that quickly as we go to lower and lower values of $x$.

The sketch of some flows might look like this:

![Figure 6](/images/part2b/output_006.png)

You can see that if you start above around $x=1.5$ (actually at $\frac{\pi{}}{2}$) you shoot up very quickly, and can’t see the trajectory for more than a few moments.