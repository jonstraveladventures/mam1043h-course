---
title: "3.7a Imperfect Bifurcations and Catastrophes"
weight: 36
math: true
---
## Section 3.6: Imperfect Bifurcations and Catastrophes

Things are about to get multi-dimensional. Hold on to your hats!

So far, we have looked at differential equations with a single parameter that can be tuned (generally labeled $r$ in all of our examples). Life isn't always so simple, and it turns out that having multiple parameters can give rise to some beautiful dynamics.

Remember the example of the supercritical pitchfork bifurcation? (Don’t be scared to revisit the notes if you ’re not sure)

$$
\dot{x}=r x-x^{ 3}
$$

We can describe this using a potential of the form:

$$
V\left(x\right)=x^{ 4}-r x^{ 2}
$$

As $r$ changes, we go from one stable fixed point to two stable fixed points plus one unstable fixed point:

![Figure 1](/images/part3f/output_001.png)

Imagine a ball (in some honey) rolling down the sides of this to imagine the fixed points. Remember, fixed points are the local minima and maxima of $V\left(x\right)$, whereas they are the zeroes of $\dot{x}$.

One thing to notice here is that there is a perfect symmetry to all of these potentials, which corresponds to changing $x\longrightarrow{}-x$. There is a symmetry of reflecting around the vertical axis. Notice that if you take the original differential equation, then changing $x\longrightarrow{}-x$ leaves the equation exactly the same, which tells you that this is a symmetry. (You may recall an even function from MAM1000W)

We can add in a term which will break that symmetry. That term is a constant term:

$$
\dot{x}=h+r x-x^{ 3}
$$

Now, if we change $x\longrightarrow{}-x$, the equation becomes:

$$
-\dot{x}= h-r x+x^{3}
$$

or in other words:

$$
\dot{x}=-h+r x-x^{3}
$$

which is not the same equation.

The potential for this new system is given by:

$$
V\left(x\right)=\frac{x^{ 4}}{4}-r \frac{x^{ 2}}{2}-hx
$$

which, for, let’s say $h=0.2$, will look like:

![Figure 2](/images/part3f/output_002.png)

As you can see, our lovely reflection symmetry is gone, and indeed the positions of the fixed points will also change.

Our next step is to understand about the fixed points in the two dimensional parameter space of $\left(r, h$)

Let’s pick a value of $h$ and do our bifurcation analysis. We already know what this looks like for $h=0$. This is your good old-fashioned pitchfork bifurcation:

![Figure 3](/images/part3f/output_003.png)

Let’s look however at $h=1$. Then our equation is:

$$
\dot{x}=1+r x-x^{ 3}
$$

How do we find the fixed points of this? Well, it’s the solutions to:

$$
1+r x-x^{ 3}=0
$$

Which isn’t that easy to solve. However, we can find the qualitative features by instead looking at when

$$
r x=x^{ 3}-1
$$

which is equivalent to asking when:

$$
y=r x    \text{ and }    y=x^{ 3}-1 , Intersect.
$$

Let's have a look at these on the same graph for different values of $r$:

![Figure 4](/images/part3f/output_004.png)

What do we see here? Well, it seems that for $r=-2$, for instance, there is a single solution to

$$
1-2 x-x^{3}=0
$$

At a positive value of $x$. As $r $increases there is only one solution until we reach around $r=2$, at which point two new solutions appear (at negative values of $x$). We can actually figure out what kind of fixed points these correspond to.

Let’s look at that last plot, with $r=3$. Let’s focus on the crossing of the lines to the far left:

![Figure 5](/images/part3f/output_005.png)

Just to the left of where they cross, we see that the line $y=r x$ is higher than the line y = $x^{ 3}-1$, so:

$$
r x>x^{ 3}-1
$$

or in other words:

$$
1+r x-x^{  3}>0
$$

Which means that in this region:

$$
\dot{x}>0
$$

Which means that $x$ is increasing... so you will move to the right, which is towards this fixed point.

You can do a similar analysis just to the right of this fixed point and you ’ll find that:

$$
\dot{x}<0
$$

So this is a stable fixed point. Conversely for the second intersection point you can show that this is an unstable fixed point.

And you can show that the third fixed point, which is really the one that’s been there all along is also a stable fixed point.

In fact we can plot these on the bifurcation diagram and what we actually get is:

![Figure 6](/images/part3f/output_006.png)

A saddle-node bifurcation appears! Can we see what happens overall as we change $ h$?

![Figure 7](/images/part3f/output_007.png)

**Insight:** I know this might seem a bit crazy initially and there appear to be few patterns between what you’re doing, but take some time to break down how you identify the fixed points and their stability ’s as done on this page and the previous ones. Once you solidify your understanding of this section it will become clearer how to introduce this “extra variable” and deal with different forms instead of your standard bifurcation types!

OK, that's probably enough for now. Let's take a breather and carry on on another page...