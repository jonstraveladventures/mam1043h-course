---
title: "2.8 Answers to Exercises for Part 2"
weight: 30
math: true
---
## Section 2 - solutions to exercises

Question 1)

1.1)

![Figure 1](/images/part2answers/output_001.png)

1.2)

![Figure 2](/images/part2answers/output_002.png)

1.3)

![Figure 3](/images/part2answers/output_003.png)

Note that the solutions only exist for a finite time before blowing up to ∞.

1.4)

![Figure 4](/images/part2answers/output_004.png)

1.5)

![Figure 5](/images/part2answers/output_005.png)

Note that if you start below $x=-1 \text{ you will } \text{ go to } -\infty{}$ in finite time.

1.6)

![Figure 6](/images/part2answers/output_006.png)

1.7) Note that there are oscillations that get smaller and smaller for larger and larger $x$.

![Figure 7](/images/part2answers/output_007.png)

For larger negative x solutions, they will very very quickly go towards their nearest stable fixed points. For larger positive solutions, it takes a very long time because for $e^{-x}\text{ sin } x$, for large $x$, $e^{-x}$is very small, so $\dot{x}$ is always small, so it takes a long time to get anywhere...

1.8)

![Figure 8](/images/part2answers/output_008.png)

There is no fixed point at 0 because the function is not defined at x=0.

1.9)

![Figure 9](/images/part2answers/output_009.png)

Question 2)

2.1)

$$
\dot{x}=x\left(1-x\right)\left(3-x\right)
$$

Here there are three fixed points at $x^{*}=0,1$ and 3. Starting with the fixed point at 0, there is no point in going from $x \text{ to } \eta{}$ when $x^{*}=0$. Here we can just expand the right hand side:

$$
\dot{x}=3 x-4 x^{2}+x^{3}
$$

We can simply take the linear term, and for small $x$ ignore the higher order terms...remember that we are asking about what happens when x is small. So the linear approximation is:

$$
\dot{x}=3 x
$$

This has solution:

$$
x=x_{0}e^{3t}
$$

This fixed point is unstable because as t increases, we will move further from it.

Now looking at the fixed point at $x=1, \text{ now } $we can let $x=1+\eta{}:$

$$
\dot{\eta{}}=\left(1+\eta{}\right)\left(1-\left(1+\eta{}\right)\right)\left(3-\left(1+\eta{}\right)\right)=-2 \eta{}-{\eta{}}^{2}+{\eta{}}^{3}
$$

Now we are asking about small $\eta{}$ and so just as before we can ignore the higher order terms. The linear approximation is:

$$
\dot{\eta{}}=-2 \eta{}
$$

Which has solution

$$
\eta{}={\eta{}}_{0}e^{-2t}
$$

So:

$$
x=1+{\eta{}}_{0}e^{-2t}
$$

This is an attracting fixed point.

Finally for the last fixed point you would do the same as the second one, and you should find that:

$$
x=3+{\eta{}}_{0}e^{6t}
$$

so again we have a repulsive/unstable fixed point.

2.2)

$$
\dot{x}=x^{2}\left(4-x\right)
$$

We have to be a bit more careful here. There is a fixed point at $x=0$, and a fixed point at $x=4$. However, there is no linear term close to $x=0.$ We can still expand the expression and get:

$$
\dot{x}=4x^{2}-x^{3}
$$

And so for small $x$ the cubic term is less important than the quadratic term and we can approximate:

$$
\dot{x}=4x^{2}
$$

Which we can write as:

$$
\frac{d x}{d t}=4x^{2}
$$

Taking everything in x to theleft and $t$ to the right, and integrating we have:

$$
\int{}\frac{1}{4x^{2}}\mathrm{d}x=\int{}1\mathrm{d}t
$$

which gives:

$$
-\frac{1}{4 x}=t+c
$$

which can be rearranged to give:

$$
x=\frac{1}{-4\left(t+c\right)}
$$

letting $x\left(0\right)=x_{0}, \text{ we have }:$

$$
x_{0}=\frac{1}{-4\left(0+c\right)} \text{ which implies } \text{ that } c=-\frac{1}{4x_{0}}
$$

which means that:

$$
x=\frac{x_{0}}{\left(1-4t x_{0}\right)}
$$

which, for positive $x_{0}, $as $t$ increasing, moves away from $x=0$, and for negative $x_{0},$ as t increases, moves towards $x=0$ - ie. this is a semi-stable fixed point.

For the second fixed point, at $x=4, $we can let $x=4+\eta{}$ which gives:

$$
\dot{\eta{}}={\left(4+\eta{}\right)}^{2}\left(4-\left(4+\eta{}\right)\right)=-16 \eta{}-8 {\eta{}}^{2}-{\eta{}}^{3}
$$

Linearising, we have:

$$
\dot{\eta{}}=-16 \eta{}
$$

which has solution

$$
\eta{}={\eta{}}_{0}e^{-16 t}
$$

and so:

$$
x=4+{\eta{}}_{0}e^{-16 t}
$$

which is a stable fixed point.

2.3)

$$
\dot{x}=1-e^{-x^{2}}
$$

This has a fixed point at $x^{*}=0$.

You can perform a Taylor expansion on the right hand side for small $x$ and get:

$$
\dot{x}=1-\left(1+\left(-x^{2}\right)+\frac{{\left(-x^{2}\right)}^{2}}{2}+{O\left[x\right]}^{6}\right)
$$

Which for small x is approximated by:

$$
\dot{x}=x^{2}
$$

which, similar to the first fixed point in 2.2 has solution:

$$
x=\frac{x_{0}}{1-t x_{0}}
$$

2.4)

$$
\dot{x}=-x \text{ ln } x
$$

This only has a fixed point at $x=1.$ First we let $x=1+\eta{}$:

$$
\dot{\eta{}}=-\left(1+\eta{}\right) \text{ ln } \left(1+\eta{}\right)
$$

Expanding for small η gives:

$$
\dot{\eta{}}=-\left(\eta{}+\frac{{\eta{}}^{2}}{2}-\frac{{\eta{}}^{3}}{6}+{O\left[\eta{}\right]}^{4}Editable\to False\right]Editable\to False\right]\right)
$$

Linearising, gives:

$$
\dot{\eta{}}=-\eta{}
$$

Which has solution

$$
\eta{}={\eta{}}_{0}e^{-t}
$$

and therefore

$$
x=1+{\eta{}}_{0}e^{-t}
$$

3.1a)

$$
\dot{x}=1-2x\left(1-x\right)
$$

Starting at $x_{0}=0, \text{ with stepsize }$ 0.2. The gradient at $x=0 \text{ is }$:

$$
\dot{x_{0}}=1-2 0\left(1-0\right)=1
$$

Going 0.2 forward at gradient 1 will take us from 0 to 0+1x0.2=0.2. Now we are at $x_{1}=0.2$

$$
\dot{x_{1}}=1-2 0.2\left(1-0.2\right)=0.68
$$

Going 0.2 forward at gradient 0.68 will take us from 0.2 to 0.2+0.68x0.2=0.336. Now we are at $x_{2}=0.336$

Continuing like this we can write a For loop (you don’t need to understand the code, but you should be able to do this by hand for a few iterations, as above).

![Figure 10](/images/part2answers/output_010.png)

- b) Now try with Δt=1 with initial conditions $x_{0}=0 \text{ and } -1$:

![Figure 11](/images/part2answers/output_011.png)

It looks like the trajectories cross, which we know can’t happen for a flow on the line.

3.2)

$$
\dot{x}=\text{ sin }\left(x\right), \text{ with } x_{0}=0.1, \Delta{}t=1 \text{ up to } t=8:
$$

![Figure 12](/images/part2answers/output_012.png)

3.3)

$$
\dot{x}=-x, \text{ with } x_{0}=1, \Delta{}t=0.2 \text{ up to } t=2:
$$

![Figure 13](/images/part2answers/output_013.png)

3.4)

$$
\dot{x}=-x \text{ ln }\left(x\right) \text{ with } x_{0}=1.2, \Delta{}t=0.5 \text{ up to } t=4:
$$

![Figure 14](/images/part2answers/output_014.png)

4. a) is the bottom left

4. b) is the top left

4. c) is the top right

4. d) is the bottom right

5) For a stable fixed point, the function, f(x), must pass from positive to negative through the fixed point. This means that to the left the function must be positive, and to the right it must be negative. If you had two stable fixed points next to each other then somehow the function would have to go from being negative to the right of the first, to positive to the left of the second. That is only possible if the function passes through the horizontal axis (in which case you have an unstable fixed point in between them) or if there is a discontinuity in the function.

6) For each case we just have to integrate the negative of f(x). I will illustrate it for a selection of them. Let me know if there are any that you are unsure about.

Red is the original equation, blue is the potential. Zeros of the original function correspond to turning points of the potential.