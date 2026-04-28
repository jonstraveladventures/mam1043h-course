---
title: "3.8 Exercise 1b"
weight: 40
math: true
---
## Exercise 1b

$For: \dot{x}=r-\text{ cosh }\left(x\right)$

- i) Sketch the different vector field types that appear when you vary $r$. We’re actually going to do this first the hard way, then the easier way.

Looking at the phase portrait for different values of $r$ we get the following.

![Figure 1](/images/part3exercises1b/output_001.png)

Now taking the arrows and fixed points alone and plotting them as a vector field:

![Figure 2](/images/part3exercises1b/output_002.png)

We get the bifurcation diagram by rotating this whole plot above:

![Figure 3](/images/part3exercises1b/output_003.png)

We can actually find these fixed points and thus the bifurcation diagram more simply. We need to solve $\dot{x}=r-\text{ cosh }\left(x\right)=0. $So the fixed points occur at:

We can plot these fixed points and this gives us

![Figure 4](/images/part3exercises1b/output_004.png)

We actually already have whether the fixed points are stable or unstable from the vector field plot above, so let’s put these on:

![Figure 5](/images/part3exercises1b/output_005.png)

The critical point is when the two solutions are the same (when we go from no fixed points, to one, to two):

Critical point at $r = 1$, and this occurs at: $x=0$:

![Figure 6](/images/part3exercises1b/output_006.png)

To get the equation about the critical point into normal form we can simply expand the right hand side of the equation about $x=0.$

Defining $R=2\left(r-1$), multiplying everything by 2 and redefining $t=2T$, we get: $\frac{\text{ dx }}{\text{ dT }}=R-x^{2}$. Which is one of the two normal forms for a saddle-node bifurcation.