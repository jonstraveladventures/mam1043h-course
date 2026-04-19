---
title: "3.8 Exercise 4e"
weight: 46
math: true
---
## Exercises 3.4.e

For: \dot{x}=r \text{ ln }\left(x\right)+x-1EquationCellChangeTimes-> c3470641be9c

- i) Sketch the different vector field types that appear when you vary $r$.

We’re going to do this a little differently from how we ’ve done the others. To draw the vector field, you need to be able to draw whether $\dot{x}$ is greater than or less than zero, which is the same as asking, in this case, whether $r \text{ ln }\left(x\right) \text{ is greater } \text{ than or } \text{ less than } 1-x$. Let’s first ask this question for positive $r.$ This is actually the same as comparing $\text{ ln }\left(x\right) \text{ and } \frac{1-x}{r}.$ So let’s plot this for different values of positive r and draw arrows on the diagrams:

![Figure 1](/images/part3exercises4e/output_001.png)

We see that for $x<0$ we always have that $\frac{1-x}{r}>\text{ ln }\left(x\right)$ and so $\dot{x}<0$, and conversely for $x>0$, so we have an unstable fixed point:

![Figure 2](/images/part3exercises4e/output_002.png)

For r=0, we get something different, because we can’t do the dividing by r trick, so we just have to plug in r=0 into the original equation and we get $\dot{x}=x-1$ which has a very simple phase portrait:

![Figure 3](/images/part3exercises4e/output_003.png)

How about for $r<0$? We have to be a little bit more careful here. We can again compare $\text{ ln }\left(x\right) \text{ and } \frac{1-x}{r}, \text{ but now } \text{ if this } \text{ value is } <0$ then that tells us that $\frac{
\dot{x}}{r}<0$, which tells us that $\dot{x}>0$ (because r is negative). Let’s plot the graphs and see what we find:

![Figure 4](/images/part3exercises4e/output_004.png)

Now we have something interesting going on. Most of the time there are two points of intersection, apart from around $r=-1$ where it seems that there’s one. We’ll come to that in a moment. Let’s figure out about the arrows first. When $\text{ ln }\left(x\right)<\frac{1-x}{r}$, this means that $\text{ ln }\left(x\right)+\frac{x-1}{r}<0$, which means that $r \text{ ln }\left(x\right)+x-1>0$, so $\dot{x}>0$, so for instance in the top left plot, the region between 0 and 1 satisfies this inequality so we will have an arrow going to the right. Let ’s fill this in on all diagrams:

![Figure 5](/images/part3exercises4e/output_005.png)

Now taking the arrows and fixed points alone and plotting them as a vector field:

![Figure 6](/images/part3exercises4e/output_006.png)

Now for the bifurcation diagram we need to flip the axes, and we would get something that looks like:

![Figure 7](/images/part3exercises4e/output_007.png)

This is clearly a transcritical bifurcation. Where is it happening though? It seemed in the diagram to be around r=-1. However, we can be precise about it. It occurs at the point where the two lines $\text{ ln }\left(x\right) \text{ and } \frac{1-x}{r}$ are tangent to one another, ie. where their gradients are the same. We also know that it occurs at the x value of x=1 as there is always an intersection at this point, so we can equate the gradients, and then set x=1:

OK, so that confirms our guess that the critical point is at $\left(r,x\right)=\left(-1,1\right)$. Can we turn the original equation into the Normal Form for a transcritical bifurcation by expanding about x=1? Well, first of all let $X=x-1$. Then the equation for $X$ is $\dot{X}=r \text{ ln }\left(X+1\right)+X$. Expanding around $x=1$ is the same now as expanding around $X=0. We \text{ can expand } \text{ the right } \text{ hand side } \text{ as }:$

And so the equation close to the critical value of x can be written as

$$
\dot{X}=\left(1+r\right)X-\frac{r X^{2}}{2}
$$

We want the $X^{2} \text{ term on } \text{ it }$s own so let's divide through by $\frac{r}{2} \text{ and we } \text{ get }:$

$$
\frac{2}{r}\dot{X}=\frac{2\left(1+r\right)}{r}X-X^{2}
$$

Now we want the prefactor of the $X$ term to be just the control parameter, so let's call,

$$
R=\frac{2\left(1+r\right)}{r}
$$

which means that $r=\frac{2}{R-2} \text{ and we } \text{ have now }:$.

$$
\left(R-2\right)\dot{X}=R X-X^{2}
$$

Now the left hand side is really

$$
\left(R-2\right)\frac{\text{ dX }}{\text{ dt }}
$$

so let's define

$$
T=\frac{t}{R-2}
$$

so

$$
\left(R-2\right)\frac{\text{ dX }}{\text{ dt }}=\left(R-2\right)\frac{\text{ dT }}{\text{ dt }}\frac{\text{ dX }}{\text{ dT }}=\frac{\left(R-2\right)}{R-2}\frac{\text{ dX }}{\text{ dT }}
$$

and finally we have

$$
\frac{\text{ dX }}{\text{ dT }}=R X-X^{2}
$$

which is precisely the normal form of a transcritical bifurcation.