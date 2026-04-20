---
title: "3.8 Exercise 1a"
weight: 39
math: true
---
## Exercises 3.1.a

$For: \dot{x}=2+r x +x^{2}$

- i) Sketch the different vector field types that appear when you vary $r$. We’re actually going to do this first the hard way, then the easier way.

Looking at the phase portrait for different values of $r$ we get the following.

![Figure 1](/images/part3exercises1a/output_001.png)

Now taking the arrows and fixed points alone and plotting them as a vector field:

![Figure 2](/images/part3exercises1a/output_002.png)

We get the bifurcation diagram by rotating this whole plot above:

![Figure 3](/images/part3exercises1a/output_003.png)

We can actually find these fixed points and thus the bifurcation diagram more simply. We need to solve $\dot{x}=2+r x +x^{2}=0. $This is just a quadratic in $x.$ So the fixed points occur at:

We can plot these fixed points and this gives us

![Figure 4](/images/part3exercises1a/output_004.png)

We actually already have whether the fixed points are stable or unstable from the vector field plot above, so let’s put these on:

![Figure 5](/images/part3exercises1a/output_005.png)

The critical points are when the term inside the square root vanishes (when we go from no fixed points, to one, to two):

Two critical points, at $r = \pm{}2\sqrt{2}$, and these occur at: $x=\frac{1}{2}\left(-r\right)=\mp{}\sqrt{2}$:

![Figure 6](/images/part3exercises1a/output_006.png)

We can actually rewrite the equation very simply to get it into Normal form. Let’s first of all complete the square:

$ \dot{x}=2+r x +x^{2}\longrightarrow{}{\left(x+\frac{r}{2}\right)}^{2}-\frac{r^{2}}{4}+2$

Now redefine $X=x+\frac{r}{2}$:

$ \dot{X}=X^{2}-\frac{r^{2}}{4}+2$

Now and now define: $R=\frac{-r^{2}}{4}+2$ :

$ \dot{X}=R+X^{2}$

Which is the normal form for a saddle-node bifurcation.