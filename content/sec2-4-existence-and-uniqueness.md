---
title: "2.4 Existence and Uniqueness of Solutions"
weight: 24
math: true
---
## Section 2.4: Existence and Uniqueness

Existence and Uniqueness

One thing that we have kind of assumed is that if you are given a differential equation of the form:

$$
\dot{x}=f\left(x\right)
$$

then given an initial starting point, say $x\left(0\right)=x_{0}$ there is a unique solution forward. That is to say that your present perfectly determines your future on the line. This is not always the case and we are going to look at a particular example of this!

Let’s look at the differential equation:

$$
\dot{x}=x^{\frac{1}{3}}
$$

It turns out that the solution for this can be written as:

$$
x={\left(\frac{2}{3}t+c\right)}^{\frac{3}{2}}
$$

where c is a constant of integration. One solution is therefore with $c=0$:

$$
x={\left(\frac{2}{3}t\right)}^{\frac{3}{2}}
$$

All seems fine so far, so if you start of at $x=0$ at time $t=0$ it seems that you will increase your value of $x$.

There’s a problem though - there is another solution which we haven’t captured here, and it’s a trivial solution. Check that:

$$
x=0
$$

Is also a solution to the differential equation. But this also has $x=0$ at time $t=0$. So if you start off at $x=0$ at time $t=0$, how do you know whether you’re going to take the path of $x={\left(\frac{2}{3}t\right)}^{\frac{3}{2}}$or you will stick at $x=0$ forever?

What is going on here? It turns out that the source of the problem can be seen in the type of fixed point we have. We draw the phase diagram as usual:

![Figure 1](/images/part2d/output_001.png)

and we notice that the gradient at $x$ = 0 is actually infinite! It’s not just quite an unstable fixed point - it ’s infinitely unstable (that isn’t really a technical term...). It actually turns out that there are an infinite number of different possible behaviours starting at $x=0$.

We can make a more general statement:

Given a differential equation and initial condition

$$
\dot{x}=f\left(x\right), x\left(0\right)=x_{0}\epsilon{} \mathbb{R}
$$

then if $f\left(x\right)$ and $f'\left(x\right)$ are continuous on an open interval in ℝ then there exists a unique solution on some interval (-τ,τ) about $t=0$. It says nothing about how long the solution will remain for, so after some time, something funky may happen, but if $f$ is sufficiently smooth, then there will be a unique solution which will last for some time.

Doesn’t it seem strange that a solution may only exist for a finite time? Well, let’s look at another system which looks pretty well behaved.

$$
\dot{x}=1+x^{2}, x\left(0\right)=0
$$

Well, the first thing that we might notice about this is that there are no fixed points... that’s fine. The function is continuous and smooth for all $x$ so apparently there will exist a unique solution at least for some time. It turns out that there is a solution to this differential equation which is given by:

$$
{\text{ tan }}^{-1}x=t+c
$$

where $c$ is an integration constant and in fact with our initial condition, $c=0$, so we have:

$$
{\text{ tan }}^{-1}x=t
$$

So:

$$
x=\text{ tan } t
$$

What happens if we look at this function:

![Figure 2](/images/part2d/output_002.png)

If we start at $x=0$, then as t increases we start increasing...but we blow up to infinity at $t=\frac{\pi{}}{2}$, so the solution can’t continue after that. The solution only exists between $\left(\frac{-\pi{}}{ 2},\frac{\pi{}}{2}\right)$.

In general we won’t delve any further, but it ’s important to know that even if a solution exists and is unique, it doesn’t always last forever.

C'est la vie