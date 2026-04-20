---
title: "2.3 Linear Stability Analysis"
weight: 23
math: true
---
## Section 2.3: Linear Stability Analysis

Linear Stability Analysis

If you haven't come across Taylor Polynomials before, look at this post I wrote for my first year pure maths class. Look at the posts before and after at the same link for more about them.

OK, we’ve got some first order autonomous differential equation:

$$
\dot{x}=f\left(x\right)
$$

fixed point $x$ = $x^{*}$

Is there a way that we can tell whether it's stable or unstable?

In fact we've already done that by inspection of the phase portrait. But we can do this in a more formal way. It turns out that we can ask about small fluctuations close to the fixed point.

Let's say that we want to look at some $x$(t) just a little away from $x^{*}$. We could write this as:

$$
x\left(t\right)=x^{*}+\eta{}\left(t\right)
$$

where η(t) (the Greek letter eta, pronounced eat-a) is very small.

We take derivatives of both sides of the above equation and because $x^{*}$ is a constant we have that (Try writing it out if you’re confused):

$$
\dot{x}\left(t\right)=\dot{\eta{}}\left(t\right)
$$

Now what can we say of $f$(x)? Well, let’s sub in $x=x^{*}+\eta{}$, where we have temporarily removed that functional dependence on t, but we know that it’s there.

What can we say about:

$$
f\left(x^{*}+\eta{}\right)
$$

Well, we have said that η is small, so presumably we can say that as long as f is continuous

$$
f\left(x^{*}+\eta{}\right)\approx{}f\left(x^{*}\right)
$$

We say that this is a zeroth order approximation. This is just a constant, and we know that in reality $f\left(x^{*}+\eta{}\right)$ isn’t a constant because η depends on time, so what would the next approximation be? Well, for a small shift in η, how much will f shift? Well, it’s going to be related to the gradient of $f$, along with how much we are moving in η, so we write:

$$
f\left(x^{*}+\eta{}\right)=f\left(x^{*}\right)+\eta{} f'\left(x^{*}\right)+O\left({\eta{}}^{2}\right)
$$

The $O\left({\eta{}}^{2}\right) $is read as “terms of order ${\eta{}}^{2}$” and is small compared to the second term so long as η is small. Essentially this means that these are terms that we are going to ignore. We have approximated the function at this point by a linear function in η (we threw away higher order terms).

Let's say that we are looking at a point which is $\eta{}=0.1$ away from a fixed point (in some units). Then ${\eta{}}^{2}=0.01$, which is smaller than η, and as long as the derivative is not very small there compared to the second derivative (see later), we can ignore the ${\eta{}}^{2} \text{ terms }$.

Let’s understand this for a general function $f$ about some point visually, let’s call it $c$. The equivalent expression to the above would be:

$$
f\left(c+a\right)=f\left(c\right)+a f'\left(c\right)+O\left(a^{2}\right)
$$

![Figure 1](/images/part2c/output_001.png)

We see that the value of the function at $c+a$ is very well approximated by the value of the function at $c$, plus $a$ times the gradient of the function at $c$. Provided $a$ isn’t very large, this is a good approximation.

This helps explain this:

$$
f\left(x^{*}+\eta{}\right)=f\left(x^{*}\right)+\eta{} f'\left(x^{*}\right)+O\left({\eta{}}^{2}\right)
$$

The point is that the first two terms don’t capture it perfectly, but the next term will be of size ${\eta{}}^{2}$, which for small $\eta{}$ is even smaller than $\eta{}$ itself, so we can ignore it to first approximation.

How on earth does this help us? Well, remember that $x^{*} \text{ is }$ a fixed point, which means that at that point $x^{*}'\left(t\right)=0$ and so $f\left(x^{*}\right)=0$, so we can write:

$$
f\left(x^{*}+\eta{}\right)=\eta{} f'\left(x^{*}\right)+O\left({\eta{}}^{2}\right)
$$

Carefully approximated to:

$$
f\left(x^{*}+\eta{}\right)=\eta{} f'\left(x^{*}\right)
$$

Keep in the back of your minds when this approximation is valid, it's only true close to the fixed points (Remember the terms we throw away **must** be smaller - this isn’t always true).

And our differential equation then becomes (remembering that $\dot{x}\left(t\right)=\dot{\eta{}}\left(t\right)$):

$$
\dot{\eta{}}\left(t\right)=\eta{}\left(t\right) f'\left(x^{*}\right)
$$

Make sure you understand and can show this!

Remember $f'\left(x^{*}\right)$ is just a constant. It turns out that this is a differential equation that we can solve. It ’s actually the same differential equation as that for population growth and radioactive decay, and has **solution**:

$$
\eta{}={\eta{}}_{0}e^{f'\left(x^{*}\right)t}
$$

Where ${\eta{}}_{0}$ is the value of η at $t=0$. So, it tells us if you start off with a small perturbation (η) away from $x^{*}$:

- if $f'\left(x^{*}\right) $> 0, perturbation will **grow exponentially** - i.e. move further and further **away** from $x=x^{*}$

- if $f'\left(x^{*}\right) $< 0, perturbation will **decay to zero exponentially** - i.e. you will move closer and **closer** to $x$ = $x^{*}$

If starting close to a fixed point, you move away from it, then that is an unstable fixed point. If towards it, then that is a stable fixed point.

We have now proved what we said previously. We said back then that:

Given a differential equation:

$\dot{x}=f\left(x\right)$

- The fixed points, labeled $x^{*},$ are given by $f\left(x^{*}\right)=0$. 
- The particle will be moving to the right whenever $f\left(x\right)>0$ and moving to the left whenever $f\left(x\right)<0$. 
- A fixed point is stable if $f\left(x\right)$ goes from positive to negative through zero as you increase $x$
- A fixed point is unstable if $f\left(x\right)$ goes from negative to positive through zero as you increase $x$

Now, in the new language:

- If $f'\left(x^{*}\right)>0$ then $x^{*}$ is an unstable fixed point.

- If $f'\left(x^{*}\right)<0$ then $x^{*}$ is a stable fixed point.

Not only does the sign of the derivative tell us about whether a fixed point is stable or not, but how large it is tells us **how stable or unstable**. If the derivative is, for instance, large and positive then not only is it an unstable fixed point, but because of the exponential solution, we will very quickly move away from the point. The timescale over which the perturbation size grows to $e$ times its original size is given by $\frac{1}{|f'\left(x^{*}\right)|}$. The same analysis holds for the stable fixed point.

(**Note that** $f'\left(x^{*}\right)$ is in units of inverse time $\left(\frac{\text{ df }\left(x^{*}\right)}{dt}\right)$, therefore $\frac{1}{|f'\left(x^{*}\right)|}$ being a timescale makes sense)

We intuitively knew this already. If we have a function which has a very small slope as it passes through the fixed point (let’s say with a negative gradient) then we would very, very slowly move towards it. If the slope was very large, then we will be moving towards it faster.

But hang on, I hear you say! What about if $f'\left(x^{*}\right)=0$? Well, it turns out that in that case we have to look at $f''\left(x^{*}\right)$ to tell if it's stable, or unstable. When might that be the case? Well, how about this differential equation?

$$
\dot{x}\left(t\right)={x\left(t\right)}^{2}
$$

Then it’s clear that $x^{*}=0$ is a fixed point, but what kind is it? The derivative of the function $\left(f\left(x\right)=x^{2}\right)$ is zero at $x=0$, so we can’t use that rule.

Let's look at the phase portrait:

![Figure 2](/images/part2c/output_002.png)

Hmmm... well, if we start from the left (i.e. negative x), the value of $\dot{x}$ is positive, so we will move to the right. If we start from the right then $\dot{x}$ is also positive, so we will also move to the right. Does that mean that if we start at negative $x$ we will end up moving all the way over to positive $x$? Well, **no**, if we start from, say $x=-1$, you will start moving to the right, but as you get closer to $x=0$ you will slow down, never actually get to the fixed point (as we’ve said before).

What we see though is that if you start off just to the left of the fixed point you will move towards it (stable fixed point), but if you start just to the right of it you will move away from it (unstable fixed point).

So which is it? Well, it's called a **half stable fixed point**. The arrows and the fixed point symbol would be drawn like this:

![Figure 3](/images/part2c/output_003.png)

Which shows that it’s stable from the left and unstable from the right.

If the parabola was the other way, we would have:

![Figure 4](/images/part2c/output_004.png)

is stable from the right and unstable from the left.

The other cases where we might have $f'\left(x^{*}\right)=0$ would be the following:

Make sure that you can understand the arrows, and the stability:

![Figure 5](/images/part2c/output_005.png)

![Figure 6](/images/part2c/output_006.png)

There is one final, trivial case the case where:

$$
\dot{x}\left(t\right)=0
$$

i.e. $f$ is identically zero. In that case, all points are fixed points. You’re never going anywhere, and we could denote this as:

![Figure 7](/images/part2c/output_007.png)

Note that it’s fixed at all $x$.

OK, so that gives us the full classification of fixed points and their stability for dynamical systems on the line. We are almost done with this section.

Next we will look at existence and uniqueness, a subtle, but **important** little topic.