---
title: "3.8 Exercise 5b"
weight: 47
math: true
---
## Exercises 3.4.e

$For: \dot{x}=r x-\text{ sinh }\left(x\right)$

- i) Sketch the different vector field types that appear when you vary $r$.

So, for this example we can’t solve the equation$ 0=r x-\text{ sinh }\left(x\right)$ analytically. This is what’s known as a transcendental equation, so we have to be a little smarter. You can look up the graph of $y=\text{ sinh }\left(x\right) $and you will get:

![Figure 1](/images/part3exercises5b/output_001.png)

From this immediately it should give you hints of why we might expect a pitchfork bifurcation. This looks quite a bit like the graph of $y=x^{3}. $It’s not quite the same, but it has some qualitative features. OK, so to work out the vector fields, we have to plot $y=r x$ for different values of r and see whether $r x>\text{ sinh }\left(x\right)$ in which case$ \dot{x}>0$, or vice versa. Clearly for all negative values of r, there will be a single point of intersection (at $x=0\right)$ and $r x>\text{ sinh }\left(x\right)$ for $x<0$ and $r x<\text{ sinh }\left(x\right)$ for $x>0$. For instance:

![Figure 2](/images/part3exercises5b/output_002.png)

Things don’t start getting interesting until the gradient of $y=r x$ is as large as the gradient of $y=\text{ sinh }\left(x\right) \left(\text{ at } x=0\right)$, which happens when:

$$
\frac{d \left(r x\right)}{d x}=\frac{d \left(\text{ sinh }\left(x\right)\right)}{d x}\Longrightarrow{}r=\text{ cosh }\left(x\right)|_{x=0}=1
$$

At this point we will have:

![Figure 3](/images/part3exercises5b/output_003.png)

So it’s still stable at $r=1.$ When $r>1$ however, we get something else happening. Let’s look at $r=2:$

![Figure 4](/images/part3exercises5b/output_004.png)

As the value of $r$ increases, the stable fixed points are going to move away from $x=0$ but they are going to move away slower and slower. Plotting the vector fields together we have:

![Figure 5](/images/part3exercises5b/output_005.png)

To plot the bifurcation diagram, we just flip the r and x axes:

![Figure 6](/images/part3exercises5b/output_006.png)

This is then a supercritical pitchfork bifurcation with a bifurcation point at $\left(r_{c},x_{c}\right)=\left(1,0\right)$.

Let’s make sure that we can put this into the appropriate Normal Form. One thing which will help us is to know that:

$$
\text{ sinh }\left(x\right)=\frac{e^{x}-e^{-x}}{2}
$$

and therefore its Maclaurin expansion is given by:

$$
\text{ sinh }\left(x\right)=\frac{\left(1+x+\frac{x^{2}}{2}+\frac{x^{3}}{3!}...\right)-\left(1-x+\frac{x^{2}}{2}-\frac{x^{3}}{3!}\right)}{2}=\frac{2x+\frac{2x^{3}}{3!}}{2}+...=x+\frac{x^{3}}{3!}+...
$$

So we can write the equation of motion close to $x=0$ as being approximated by:

$$
\dot{x}=r x-x-\frac{x^{3}}{3!}=x\left(r-1\right)-\frac{x^{3}}{3!}
$$

Multiplying through by 3!, letting $T=3!t \text{ and } R=r-1$ we have:

$$
\frac{d x}{d T}=R x-x^{3}
$$

Which is the Normal Form of a supercritical pitchfork bifurcation.