---
title: "3.8 Exercise 4c"
weight: 44
math: true
---
## Exercises 3.4.c

For: \dot{x}=x-r x \left(1-x\right)EquationCellChangeTimes-> c3470641be9c

- i) Sketch the different vector field types that appear when you vary $r$.

We can actually get some intuition here before drawing any graphs. To find the fixed points, just solve

$$
x-r x \left(1-x\right)=0
$$

for $x$ which gives:

$$
x=0 \text{ and } x=\frac{r-1}{r}
$$

So before we even plot a phase portrait we can get the bifurcation diagram. We need to be able to figure out along the fixed point lines what is going to be stable and what unstable. Let’s look at the $x=0$ fixed point first and do a linear stability analysis. Close to $x=0, \text{ the equation } $is approximated by:

$$
\dot{x}=x \left(1-r\right)
$$

(as the $1-x$ is approximated by just 1 close to $x=0\right).$ We know that this has solutions:

$$
x=x_{0}e^{\left(1-r\right)t}
$$

and therefore if $\left(1-r\right)>0\Longrightarrow{}r<1$ this is an unstable solution if $r>1$ then it’s stable.

For completeness, let’s expand the equation also about the other fixed point: $x=\frac{r-1}{r}. $Let $x=\frac{r-1}{r}+\eta{}: $

$$
\dot{\eta{}}=\left(\frac{r-1}{r}+\eta{}\right)-r \left(\frac{r-1}{r}+\eta{}\right) \left(1-\left(\frac{r-1}{r}+\eta{}\right)\right)
$$

which, after some algebra actually gives the much simpler looking:

$$
\dot{\eta{}}=\eta{}\left(r-1\right)+r {\eta{}}^{2}
$$

which, for small η gives

$$
\dot{\eta{}}=\eta{}\left(r-1\right)
$$

and we have exactly the opposite situation than we had for the first fixed point. ie. $r<1 \text{ is stable }$ and $r>1$ is unstable. Let’s plot these two solutions

![Figure 1](/images/part3exercises4c/output_001.png)

OK, so we should also be drawing the phase portrait for this. We can do this the old fashioned way by just plotting the graph of the differential equation for different values of r:

Which, while there’s a fixed point which is doing some funky things around $r=0$, just has a single bifurcation at $r=1$.

![Figure 2](/images/part3exercises4c/output_002.png)

Which ties in with our bifurcation plot. Now we just need to make sure that we can convert it into the Normal Form for a transcritical bifurcation. The equation is:

$$
\dot{x}=x-r x \left(1-x\right)
$$

Expanding in x this is just:

$$
\dot{x}=\left(1-r\right)x+r x^{2}
$$

Dividing through by -r gives:

$$
-\frac{1}{r} \dot{x}=\frac{\left(r-1\right)}{r}x-x^{2}
$$

Now let

$$
R=\frac{r-1}{r}\Longrightarrow{} r=\frac{1}{1-R}
$$

which gives us

$$
\left(R-1\right) \dot{x}=R x-x^{2}
$$

Now the left hand side is really

$$
\left(R-1\right) \frac{d x}{d t}
$$

and so defining $T=\frac{1}{\left(R-1\right)}t \longrightarrow{} \left(R-1\right)\frac{d x}{d t}=\left(R-1\right)\frac{d x}{d T}\frac{d T}{d t}=\frac{\left(R-1\right)}{\left(R-1\right)} \frac{d x}{d T}$ this gives us finally:

$$
\frac{d x}{d T}=R x-x^{2}
$$

Which is the normal form of a transcritical bifurcation.