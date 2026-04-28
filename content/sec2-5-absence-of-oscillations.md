---
title: "2.5 Absence of Oscillations"
weight: 25
math: true
---
## Section 2.5: Absence of Oscillations

Absence of Oscillations

There are plenty of very simple dynamical systems which oscillate over time. We saw the pendulum earlier, but there are many others. Note however that the pendulum is a second order differential equation (Or two first order order differential equations [recall](https://www.wolframcloud.com/obj/jon.shock/MAM1043part1f)).

We can ask whether it’s possible to find a single first order differential equation which has oscillating solutions, again, of the form:

$$
\dot{x}=f\left(x\right)
$$

Surely, if we pick $f$ wisely we should be able to find them?

What does it mean for a solution to oscillate?

Well, it has to go through some point, and then at a later time pass back through that point the other way. However, the direction of movement of $x$ on the line is uniquely determined by $f$($x$). Either it's positive, or negative, or zero. But you can't at one moment travel to the right through a point x and then at another point travel to the left through it. There are systems where this happens, like the pendulum, but in one dimension, there aren't any.

In one dimension there are no periodic solutions. In two dimensions, we can certainly return to a starting point even if at every point in the two dimensions, our direction of travel is fixed, so in two and higher dimensions we can have periodic solutions. In fact in three dimensions we get into even more interesting territory with chaotic solutions, but that is for another time.

The fact that there are no oscillating solutions says that given any initial point, your motion is going to be monotonic. You’re either going to increase in $x$, or decrease in $x$ (or stay where you are), but you will **never change direction**.

It should again be noted that it’s easy to think of dynamical systems that live on a line and oscillate, but their equation of motion will include second derivatives, at least. They become first order equations but in at least two variables, and are no longer on the line.

It's clear that a mass on a spring should be able to oscillate, but if there is a lot of friction in the system (which will be a force proportional to the velocity), then the friction will counter the acceleration from the spring, and it will not oscillate. Such a system is called **over-damped**, and tells you that in certain limits (like high friction), oscillating systems can become non-oscillating systems and can be described by a particle on a line.

The equation for a mass on a spring, with friction is:

$$
m \ddot{x}+b \dot{x}=-k x
$$

where $m$ is the mass of the spring, $b$ is related to the friction and $k$ is related to the force from the spring. In the region where the frictional term is strong:

$$
m \ddot{x}\ll  b \dot{x}
$$

the acceleration term can be neglected, and the equation becomes:

$$
\dot{x}=-\frac{k}{b}x
$$

and the solution to this is just exponential decay towards $x=0$.

If we study the equation fixing $m=k=1$ we can see what happens as we change $b$:

![Figure 1](/images/part2e/output_001.png)

Here $b=0$ is the darker blue oscillating solution and as we increase $b$ towards $b$ = 3 for the orange curve, we see the oscillations giving way to monotonic decay towards $x=0$.