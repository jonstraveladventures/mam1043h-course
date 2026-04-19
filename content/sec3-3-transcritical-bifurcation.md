---
title: "3.3 Transcritical Bifurcations"
weight: 32
math: true
---
## Section 3.3: Transcritical Bifurcations

Transcritical Bifurcations

That's a bit of a mouthful, but we'll see that this isn't any more complicated than previous examples. One example where this occurs is in population dynamics.

Imagine that you have a species in some environment. Clearly there will always be a fixed point at zero population, whatever the dynamics of the system. However, whether or not this is a stable or unstable fixed point can vary. Sometimes if you have a very small population it will die out, and in other situations, if you have a very small population it can grow exponentially. Remember we spoke about the **logistic equation** for population growth which is:

$$
\dot{P}=k P\left(1-\frac{P}{M}\right)
$$

We're going to look at a slightly simpler equation which is:

$$
\dot{x}=r x-x^{ 2}
$$

(Notice that this is equivalent to the logistic equation with $k=M=r$ and $x=P$)

Actually, we should pause for a moment and discuss the examples we ’ve been looking at. These “prototypical examples”, like “$\dot{ x}=r x-x^{ 2}$ ”, and “ $\dot{x}=x^{ 2}+r$ ” are called **normal forms**. You can think of them as the most basic example that exhibits a particular type of bifurcation. Actually there is a lot more to them than that, but that’s the best way to think of them for now. You will see in the exercises for part 3 why they are important.

So, where are the fixed points of this system? The normal form in this case is “ $\dot{x}=r x-x^{ 2}$ ”, which can also be written as $\dot{x}=x \left(r -x^{ }\right)$, so clearly $x=0$ is always going to be a fixed point. But there will be another at $x=r$. Let’s plot the situations with $r<0, r=0, r>0$ separately.

![Figure 1](/images/part3b/output_001.png)

We see that as we increase the value of $r$ the fixed point at $x=0$ moves from being stable, to half-stable to unstable. and the other fixed point goes from being unstable, to merging into the central fixed point, to being stable. We can plot these fixed points on the following bifurcation diagram. Dashed lines again correspond to unstable fixed points, and solid lines are stable fixed points.

![Figure 2](/images/part3b/output_002.png)

The sweeping fixed point swings from one direction, coalesces with the other, and they exchange stability's. Where the dashed lines are again unstable fixed points and the solid lines are stable. You can see, as you increase $r$ the fixed point at zero going from stable to unstable. As the stable and unstable fixed points come together we get a semi-stable fixed point.

Of course, in the example of a population, you can never have a negative population, so the unstable fixed point at negative $x$ (or $P$) would never show up physically, but a stable fixed point at zero can shift to an unstable fixed point at zero and a stable fixed point if the carrying capacity changes sign.

Note that it’s not always the case that this change happens at $x=0$. It can happen at any point.

Going back to the example of population dynamics, the carrying capacity can be thought of as the parameter which varies. If you have a positive carrying capacity, then $P=0$ is an unstable fixed point, but if it’s negative it becomes a stable fixed point.

In this case, if you naively plotted the bifurcation diagram it would look like:

![Figure 3](/images/part3b/output_003.png)

but clearly a negative population doesn’t make any sense, so the physically interesting part of this diagram looks like:

![Figure 4](/images/part3b/output_004.png)

This tells us that a population would die out when $M<0$ if it is governed by the logistic equation.

Let’s look at another example of a system which includes a transcritical bifurcation:

$$
\dot{x}=r \text{ ln }\left(x\right)+x-1
$$

It’s clear here that $x=1$, is always a fixed point of the system, but for $r<0$ there is also another fixed point. Let’s look at this system as we change $r$. In the following picture, you see that as $r$ changes, for the phase portrait on the left and the bifurcation diagram on the right.

![Figure 5](/images/part3b/output_005.png)

We see here that we have what appears to be a transcritical bifurcation occurring close to $x=1$ and at $r_{c}=-1$. The question then is can we expand around this point (in $x$) and put the differential equation into normal form? Well, the answer is yes! If we perform a change of variables, but let’s take this step by step.

Our equation is:

$$
\dot{x}=r \text{ ln }\left(x\right)+x-1
$$

and we want to expand this about $x=1$ , so let's perform a change of variables, from $x$ to $u$, such that $u=x-1$ , which will give us:

$$
\dot{u}=r \text{ ln }\left(u+1\right)+u
$$

Now we can expand for small $u$ (Taylor Expansion!):

$$
\dot{u}=r \left(u-\frac{u^{2}}{2}+O\left(u^{3}\right)\right)+u
$$

We can, close to $u=0$, ignore higher order terms (note that if we ignore the $u^{2} \text{ term }$ then we would get no bifurcation):

$$
\dot{u}=\left(r+1\right) u-r\frac{u^{2}}{2}
$$

Let's also define a new parameter $R=r+1$ such that:

$$
\dot{u}=R u-\left(R-1\right)\frac{u^{2}}{2}
$$

Now it's looking quite a bit like the normal form, but the factor in front of the quadratic term is not what we want, so let's rescale $u$ and define $X=\frac{u}{a}$ with some unknown $a$ to be fixed in a moment:

$$
a \dot{X}=a R X-a^{2}\left(R-1\right)\frac{X^{ 2}}{2}
$$

Dividing through by $a$:

$$
\dot{X}=R X-a \left(R-1\right)\frac{X^{ 2}}{2}
$$

Now we want to **choose** $a$ such that we are left with a factor $-1$ in front of the $X^{ 2} \text{ term }:$

$$
a \left(R-1\right)\frac{1}{2}=1, \text{ so } a=\frac{2}{R-1}
$$

And we are left with:

$$
\dot{X}=R X-X^{2}
$$

Which is precisely the normal form for a transcritical bifurcation. What this really means is that we’ve zoomed into a slice close to $x=1$ in the above bifurcation diagram, like so:

![Figure 6](/images/part3b/output_006.png)

and locally it is precisely the same as the normal form of a transcritical bifurcation (with a scaling and shift in $x$ and $r$).

There’s another way that we can think about finding the bifurcation diagram if you don’t want to plot the graph of $f\left(x\right)=r \text{ ln }\left(x\right)+x-1$, and find its zeros (and I don’t blame you...).

If we want to know when this function is zero, we can simply calculate when the graphs of $y=r \text{ ln }\left(x\right) \text{ and } y=1-x$ intercept. The point is that then the $r \text{ is just } $a scaling factor. Plotting this for a range of values of $r \text{ we see }:$

![Figure 7](/images/part3b/output_007.png)

We see how the intersection points of the two graphs move. To work out which one is stable and which unstable, we just have to ask whether $r \text{ ln }\left(x\right) \text{ or } 1-x$ is larger just to the left of the intersection point (and just to the right). If $r \text{ ln }\left(x\right) \text{ is larger }, \text{ then } r \text{ ln }\left(x\right)+x-1$ is going to be positive, so $\dot{x}$ will be positive, so we will move towards the fixed point, and vice versa to the right, so this will correspond to a stable fixed point. Including this information on the above animation we have the stable fixed point in red, and the unstable in blue.

![Figure 8](/images/part3b/output_008.png)

**Important Note**: Don’t let this example intimidate you! I know it looks complicated, and you might think it’s crazy how different it looks from start to finish, but really take time to step through it. Once you’ve do the exercise at the end, check it with the lecturer and see where you can improve. This kind of manipulation becomes incredibly important as you move forward and acing it now will set you on the right path!

This is the important point about a normal form. ALL **saddle node bifurcations**, close to the point where the bifurcation happens can be turned into the form:

$$
\dot{x}=r+x^{ 2}
$$

by a change of variables, and ALL **transcritical bifurcations** can be put into the form:

$$
\dot{x}=r x-x^{ 2}
$$

by an appropriate change of variables.

Give it a go yourself. Draw the bifurcation diagram for the equation:

$$
\dot{x}=-{\left(x-2\right)}^{2}+r \left(x-2\right)
$$

and put this equation into normal form via a change of variables.