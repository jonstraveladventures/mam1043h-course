---
title: "2.8 Exercises for Part 2"
weight: 29
math: true
---
## Section 2 exercises: Flows on the line

- For the following differential equations, calculate the fixed points and their stability, plot the phase portrait and sketch some characteristic trajectories. 

For instance, if you were given the equation $\dot{x}$ = $x^{2}-1$, you would find that this has fixed points at $x$=±1, and a phase portrait given by:

Where the stability of each point is shown. Some characteristic trajectories would look like:

Note that you want to get the characteristic trajectories general behaviour right, but you don ’t need to get them exact.

    - $\dot{x}$ = 3 $x$ + 2

    - $\dot{v}$ = $9.8-\frac{0.5}{100}v^{2}$ This equation models the velocity $v$ of a skydiver of mass 100kg and air resistance given by 0.5 kg m $s^{-1}$

    - $\dot{x}$ = $1+x^{2}$

    - $\dot{x}$ = cos $x$

    - $\dot{x}$ = $1-x^{4}$

    - $\dot{x}$ = 1-2 cos x

    - $\dot{x}$ $= -x \text{ ln } x$ This is an example of the [Gompertz differential equation](https://www.youtube.com/watch?v=K6jUVW-xrh8) which can be used to model tumour growth. There is a lovely exercise on the Gompertz equation [here](https://math.libretexts.org/Bookshelves/Calculus/Exercises_(Calculus)/Exercises%3A_Calculus_(OpenStax)/08.E%3A_Differential_Equations_(Exercises))\.

    - $\dot{N}$ $= N\left(1-\frac{N}{2}\right)\left(N-1\right)$ This differential equation models the [Allee Effect](https://www.youtube.com/watch?v=zJpW3c7p__g).

- Classify the fixed points of the following systems using a linear stability analysis. 

For instance, if you were given $\dot{x}$ = $x\left(1-x\right)$, you would see that there are two critical points given by $x^{*}=0$ and $x^{*}=1$. 

Expanding about the second critical point and so setting $x$(t)=1+η(t) for small η gives the equation $\dot{\eta{}}$ = (1+$\eta{}\right)\left(-\eta{}\right)=-\eta{}-{\eta{}}^{2}$, which, for small η is just $\dot{\eta{}}$ =-η. This has solution $\eta{}={\eta{}}_{0}e^{-t}$. This says that you will exponentially speed **towards** the point η=0 over time, so it is stable.

For the critical point at $x^{*}=0, \text{ we could } $define $x$(t)=0+η(t), but in fact this is just a change of name from $x \text{ to } \eta{}$ which doesn’t change anything, so we can simply ask about the behaviour of the equation for small $x. For x \text{ close to } 0, x-x^{2} $is well approximated by simply $x$, so we can write that for small $x$, $\dot{x}$ $=x$. This has solution $x=x_{0}e^{t}$. This says that you will exponentially speed **away from** the point $x$=0 over time, so it is unstable.

Note that we have been able here to find the exact behaviour close to the fixed points. If you just want to know whether or not they are stable, if you set $f\left(x\right)=x\left(1-x\right)$ then for $x^{*}=0, f'\left(x^{*}\right)>0$, therefore this is unstable and for $x^{*}=1, f'\left(x^{*}\right)<0$, therefore this is stable. It is only in the cases where $f'\left(x^{*}\right)=0$ that you have to be more careful in figuring out what sort of stability you have. I would like you to find the actual behaviour close to the fixed point however.

    - $\dot{x}$ = $x\left(1 - x\right)\left(3-x\right)$

    - $\dot{x}$ = $x^{2}\left(4-x\right)$

    - $\dot{x}$ = $1-e^{-x^{2}}$. Here you will need to know that for small $y$, $e^{-y^{2}}=1-y^{2}+O\left(y^{4}\right)$

    - $\dot{x}$ $= -x \text{ ln } x$

- Use Euler’s method to to plot trajectories for the following differential equations:

    - $\dot{x}=1-2x\left(1-x\right)$ starting at $x_{0}=0$ with step sizes of Δt=0.2 up to t=2. 

What happens if you use step sizes of Δt=1, starting at $x_{0}=0 \text{ and }$ $x_{0}=-1$. What goes wrong in the above equation using Euler’s method?

    - $\dot{x}=\text{ sin } x$ starting at $x_{0}=0.1$ with step sizes of Δt=1 up to t=8

    - $\dot{x}=-x$ starting at $x_{0}=1, \text{ with }$ step sizes of Δt=0.2 up to t=2

    - $\dot{x}$ $= -x \text{ ln } x$ starting at $x_{0}=1.2$ with step sizes of Δt=0.5 up to t=4

- Match the following direction fields to the differential equations: 

- a) $\dot{x}=x^{2}-t^{2}$
- b) $\dot{x}=x-t$
- c) $\dot{x}=t \text{ sin }\left(x\right)$
- d) $\dot{x}=x t $

![Figure 1](/images/part2exercises/output_001.png)

- If you look through all of the phase portraits and study the fixed points, you will find that (unless there is a discontinuity in $\dot{x}$(x)) you never have one stable fixed point next to another one, or one unstable fixed point next to another. Can you explain why this is the case?

- Go through all of the above differential equations, and write down the potential which corresponds to them, then plot that. For some of these you won’t be able to perform the integral analytically. In that case you can simply approximate a potential whose negative first derivative with respect to x gives you the f(x) in $\dot{x}=f\left(x\right).$ Notice the relationship between zeroes of $\dot{x}$ and valleys and hills of the potential.

For instance, if you had $\dot{x}=x\left(1-x\right)\left(3-x\right) $, then a $V\left(x\right)$ which satisfies $-V'\left(x\right)=x\left(1-x\right)\left(3-x\right)$ would be $V\left(x\right)=-\frac{3 x^{2}}{2}+\frac{4 x^{3}}{3}-\frac{x^{4}}{4}$. Plotting the phase portrait and the potential on the same figure gives:

![Figure 2](/images/part2exercises/output_002.png)