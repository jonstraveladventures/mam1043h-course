---
title: "3.4 Pitchfork Bifurcations"
weight: 33
math: true
---
## Section 3.4: Pitchfork Bifurcations

Pitchfork Bifurcations

Next we’re looking at **pitchfork bifurcations**, the name will make sense I promise! In this case we go from one fixed point to three. Before looking at the phase diagrams and bifurcation diagram below, see if you can imagine a function, which when you alter a parameter goes from one zero to three.

There are two different types of pitchfork bifurcations, one is a **supercritical pitchfork bifurcation**, and this occurs in equations of the form:

$$
\dot{x}=r x-x^{ 3}
$$

This is similar to the saddle-node bifurcation normal form, but with an extra factor of $x$. Meaning we can write: $\dot{x}=x \left(r-x^{ 2}\right)$, so it's going to have the same fixed point behaviour as the saddle note, with an extra fixed point at $x=0$. We can see from this that that we will always have a fixed point at $x=0$, but as in the last example, it's not always going to be the same kind of fixed point.

Let’s again draw in our phase portraits for $r<0, r=0$ and $r>0$.

![Figure 1](/images/part3c/output_001.png)

It looks like from $r<0$ to$ r=0$ nothing changes, but let’s do a stability analysis. Let’s first of all look at $r<0$ at small $x$. Basically ask the question about what is happening close to $x=0$. For small $x$, $ x^{ 3}$<< $x$ so we can approximate the equation by:

$$
\dot{x}=r x
$$

ie. we can ignore the $x^{ 3}$ term. The solution to this differential equation is just an exponential decay:

$$
x=x_{o}e^{r t}
$$

remembering of course that $r$ is negative. So for $r<0$, if you start a little away from $x=0$ then you will exponentially decay towards $x=0$.

How about if $r$ actually equals zero? Well, then the equation is

$$
\dot{x}=-x^{ 3}
$$

and this has solution:

$$
x=\frac{x_{o}}{\sqrt{2 t {x_{o}}^{2}+1}}
$$

Which decays much more slowly than the exponential decay. In fact, for late times (large $t$), this goes like:

$$
x=\frac{\pm{}1}{\sqrt{2 t }}
$$

Make sure you can see this.

Let's plot what happens if you start in both cases at $x=0.1$ , and let's look at a small value of $r$ and compare it with $r=0$, so we can see that a very small change has a big impact. Let's go for $r=0.01$:

![Figure 2](/images/part3c/output_002.png)

We see that with just a very small change in $r$, the behaviour changes from exponential decay of $x$ over time, to a much shallower form of decay. This slow decay is called **Critical Slowing Down**.

So what do we know? Well, for negative $r$ we have one fixed point which is stable, and indeed exponentially slow to decay. At $r=0$, we have a fixed point, but you will only ever decay to it very slowly, and then for $r>0$, *kablam*! You have three fixed points, two of which are stable, and one unstable (replaces the old stable one). For positive $r$, the critical points will be at the positive solutions to:

$$
r x-x^{ 3}=0
$$

$$
x=\pm{}\sqrt{r}\text{ and } x=0
$$

The **bifurcation plot** looks like:

![Figure 3](/images/part3c/output_003.png)

All of a sudden you can, hopefully, see why it’s called a pitchfork bifurcation!

**Question**: Remember when we spoke about potentials, a few pages back, and found a $V\left(x\right)$ such that we could write:

$$
\dot{x}=-V'\left(x\right)
$$

Calculate what $V\left(x\right)$ would be for the differential equation at the top of the page, and then plot it for different values of r. What do you notice? Imagine that this was the landscape of a hill... what do the critical points look like?

Now give it a go yourself: Draw the bifurcation diagram for the equation:

$$
\dot{x}=r \left(x+2\right)-3{\left(x+2\right)}^{3}
$$

So we said that there are two types of pitchfork diagrams. We've just looked at supercritical ones, now we’re going to look at **Subcritical Pitchfork Bifurcations**. These look very similar but have some important differences. They are of the form:

$$
\dot{x}=r x+x^{ 3}
$$

It’s just a change in sign of the $x^{ 3}$ term. So, let’s run through the same procedure. First we ’ll explore what happens for different values of $r$:

![Figure 4](/images/part3c/output_004.png)

It looks pretty similar, but now the single fixed point is unstable.

You can do the same analysis close to $x=0$ (Do it for practice, you'll need to know how to!)

You will find that for $r>0$ the solutions are exponentially unstable, whereas for $r=0$, it's unstable, but you will decay away very slowly (like the $\sqrt{t}$). Now the bifurcation plot looks like:

![Figure 5](/images/part3c/output_005.png)

Actually, there’s something else that we can look at in this case. Here, for $r>0$, the cubic term and linear term are both contributing to an increasing $\dot{x}$. The further we go in $x$ the faster we will move. One can ask what a trajectory looks like for this case. For the case $r=1$, and $x\left(0\right)=x_{o}$ (positive), one can show that the solution is:

$$
x=\frac{e^{t} }{\sqrt{\frac{1}{{x_{o}}^{2}}+\left(1-e^{2 t}\right)}}
$$

What happens when we plot this, for, say $x_{o}=0.1$?

![Figure 6](/images/part3c/output_006.png)

You can show that this goes off to infinity when:

$$
\frac{1}{{x_{o}}^{2}}+\left(1-e^{2 t}\right)=0
$$

This is when:

$$
t=\text{ ln }\left(\frac{\sqrt{1+{x_{o}}^{2}}}{x_{o}}\right)
$$

So this is really really unstable, and that instability is actually pushed by the cubic term.