---
title: "3.8 Exercise 4b"
weight: 43
math: true
---
## Exercises 3.4.a

For: \dot{x}=r x-\text{ ln }\left(1+x\right)EquationCellChangeTimes-> c3470641be9c

- i) Sketch the different vector field types that appear when you vary $r$.

We’re going to do this a little differently from how we ’ve done the others. To draw the vector field, you need to be able to draw whether $\dot{x}$ is greater than or less than zero, which is the same as asking, in this case, whether $r x \text{ is greater } \text{ than or } \text{ less than } \text{ ln }\left(1+x\right)$. Let’s plot each of these for different values of $r \text{ and then } \text{ draw arrows } \text{ on the } \text{ diagrams }:$

![Figure 1](/images/part3exercises4b/output_001.png)

Nothing very interesting happens until $r\geq{}1.$ To draw on the arrows, you just need to see whether $r x \text{ or ln }\left(1+x\right) $is bigger. If $r x \text{ is larger }, \text{ then } \dot{x}$ is positive, and draw an arrow to the right. If it’s negative, draw an arrow to the left.

![Figure 2](/images/part3exercises4b/output_002.png)

Now taking the arrows and fixed points alone and plotting them as a vector field:

![Figure 3](/images/part3exercises4b/output_003.png)

Now for the bifurcation diagram we need to flip the axes, and we would get something that looks like:

![Figure 4](/images/part3exercises4b/output_004.png)

This is clearly a transcritical bifurcation. Where is it happening though? It seemed in the diagram to be around r=1. However, we can be precise about it. It occurs at the point where the two lines $\text{ ln }\left(1+x\right) \text{ and } r x$ are tangent to one another, ie. where their gradients are the same. We also know that it occurs at the x value of x=0 as there is always an intersection at this point, so we can equate the gradients, and then set x=0:

OK, so that confirms our guess that the critical point is at $\left(r,x\right)=\left(1,0\right)$. Can we turn the original equation into the Normal Form for a transcritical bifurcation by expanding about x=0? Let’s expand the right hand side of the equation about $x=0:$

And so the equation close to the critical value of x can be written as

$$
\dot{x}=\left(r-1\right)x+\frac{x^{2}}{2}
$$

We want the $x^{2} \text{ term on } \text{ it }$s own so let's multiply through by $2 \text{ and we } \text{ get }:$

$$
2\dot{x}=2\left(r-1\right)x+x^{2}
$$

Now we want the prefactor of the $x$ term to be just the control parameter, so let's call,

$$
R=2\left(r-1\right)
$$

which means that$:$.

$$
2\dot{x}=R X+X^{2}
$$

Now the left hand side is really

$$
2\frac{\text{ dX }}{\text{ dt }}
$$

so let's define

$$
T=\frac{t}{2}
$$

$\text{ so } $

$$
2\frac{\text{ dX }}{\text{ dt }}=2\frac{\text{ dT }}{\text{ dt }}\frac{\text{ dX }}{\text{ dT }}=\frac{2}{2}\frac{\text{ dX }}{\text{ dT }}
$$

and finally we have

$$
\frac{\text{ dX }}{\text{ dT }}=R X+X^{2}
$$

$$
\frac{d\chi{}}{\text{ dT }}=\rho{} \chi{}-{\chi{}}^{2}
$$

which is precisely the normal form of a transcritical bifurcation.