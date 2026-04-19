---
title: "3.8 Exercise 4d"
weight: 45
math: true
---
## Exercises 3.4.e

For: \dot{x}=x \left(r-e^{x}\right)EquationCellChangeTimes-> c3470641be9c

- i) Sketch the different vector field types that appear when you vary $r$.

Well, let’s start a little differently here and think about where the fixed points are. Here the differential equation is given, on the right by a product of terms. $For \dot{x}$ to be zero, one or other (or both) of them have to be zero, so there are going to be, in general, two fixed points, given by:

$$
x=0 \text{ and } r=e^{x} \Longrightarrow{} x=\text{ ln }\left(r\right)
$$

In fact there’s going to be a situation where ’s there’s only one fixed point, and that will be when $r=1. $In terms of the vector fields, we need to ask when $\dot{x}$ will be positive, negative or zero. It will be positive when both factors are either positive or both are negative, it will be negative when they have different signs, and it will be zero when one of them is zero. Let ’s take an example. Let’s ask what the vector field looks like when $r=2.$ Clearly then for $x\in{} \left(-\infty{},\text{ ln }\left(2\right)\right)$, $\left(r-e^{x}\right) \text{ is going } \text{ to be } \text{ positive }$, and for $x\in{}\left(\text{ ln }\left(2\right),\infty{}\right)$ it’s going to be negative. Thus $x\left(r-e^{x}\right)<0$ when $x\in{}\left(-\infty{},0\right)\cup{}\left(\text{ ln }\left(2\right),\infty{}\right)$ and $x\left(r-e^{x}\right)>0 \text{ when } $$x\in{}\left(0,\text{ ln }\left(2\right)\right).$ As a vector field (flow on the line) this looks like:

![Figure 1](/images/part3exercises4d/output_001.png)

Of course we were just looking at $r=2 \text{ here }$ but we can do the same thing for any value of $r>1$ and we will get the same thing, just with our 2's replaced by the value of $r.$ We have to be a bit more careful with the region for $0<r<1$, as in this the value of $x \text{ where } r-e^{x}$ changes sign, x is negative rather than positive.

For $r=1$, there’s only a single fixed point, which, unsurprisingly, is semi-stable. $ \dot{x}<0$ everywhere except at $x=0 \text{ where it } \text{ is zero }.$

For $r\leq{}0, \left(r-e^{x}\right)$ is always negative, and so $x\left(r-e^{x}\right)>0$ when $x$∈(-∞,0) and $x\left(r-e^{x}\right)<0$ when $x$∈(0,∞). Let's use all of this to draw our vector fields. Let's plot a load of them together:

![Figure 2](/images/part3exercises4d/output_002.png)

Now we can draw the bifurcation diagram by turning this on its side, or alternatively just plotting the lines that we found at the very top of this page:

$$
x=0 \text{ and } x=\text{ ln }\left(r\right)
$$

![Figure 3](/images/part3exercises4d/output_003.png)

Looks like a transcritical bifurcation to me. Let’s look at it for $x$ close to the critical value $x=0$:

$$
\dot{x}=x \left(r-e^{x}\right) =x\left(r-\left(1+x+...\right)\right)\approx{}r x-x-x^{2}=x \left(r-1\right)-x^{2}
$$

Now all we have to do is to write

$$
R=r-1
$$

and we have

$$
\dot{x}=R x-x^{2}
$$

and we’re done.