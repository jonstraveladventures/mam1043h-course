---
title: "2.8 Exercises for Part 2"
weight: 29
math: true
---
## Section 2 exercises: Flows on the line

### 1. Fixed points, stability and phase portraits

For the following differential equations, calculate the fixed points and their stability, plot the phase portrait and sketch some characteristic trajectories.

For instance, if you were given the equation $\dot{x} = x^{2}-1$, you would find that this has fixed points at $x=\pm 1$, and a phase portrait given by:

Where the stability of each point is shown. Some characteristic trajectories would look like:

Note that you want to get the characteristic trajectories' general behaviour right, but you don't need to get them exact.

- (a) $\dot{x} = 3x + 2$
- (b) $\dot{v} = 9.8 - \frac{0.5}{100}v^{2}$. This equation models the velocity $v$ of a skydiver of mass 100 kg and air resistance given by $0.5\,\text{kg}\,\text{m}\,\text{s}^{-1}$.
- (c) $\dot{x} = 1 + x^{2}$
- (d) $\dot{x} = \cos x$
- (e) $\dot{x} = 1 - x^{4}$
- (f) $\dot{x} = 1 - 2\cos x$
- (g) $\dot{x} = -x\ln x$. This is an example of the [Gompertz differential equation](https://www.youtube.com/watch?v=K6jUVW-xrh8) which can be used to model tumour growth. There is a lovely exercise on the Gompertz equation [here](https://math.libretexts.org/Bookshelves/Calculus/Exercises_(Calculus)/Exercises%3A_Calculus_(OpenStax)/08.E%3A_Differential_Equations_(Exercises)).
- (h) $\dot{N} = N\left(1 - \frac{N}{2}\right)\left(N - 1\right)$. This differential equation models the [Allee Effect](https://www.youtube.com/watch?v=zJpW3c7p__g).

### 2. Linear stability analysis

Classify the fixed points of the following systems using a linear stability analysis.

For instance, if you were given $\dot{x} = x\left(1-x\right)$, you would see that there are two critical points given by $x^{*}=0$ and $x^{*}=1$.

Expanding about the second critical point and setting $x(t) = 1 + \eta(t)$ for small $\eta$ gives the equation $\dot\eta = (1+\eta)(-\eta) = -\eta - \eta^{2}$, which, for small $\eta$, is just $\dot\eta = -\eta$. This has solution $\eta = \eta_{0} e^{-t}$. This says that you will exponentially speed **towards** the point $\eta=0$ over time, so it is stable.

For the critical point at $x^{*}=0$, we could define $x(t) = 0 + \eta(t)$, but in fact this is just a change of name from $x$ to $\eta$ which doesn't change anything, so we can simply ask about the behaviour of the equation for small $x$. For $x$ close to $0$, $x-x^{2}$ is well approximated by simply $x$, so we can write that for small $x$, $\dot{x} = x$. This has solution $x = x_{0} e^{t}$. This says that you will exponentially speed **away from** the point $x=0$ over time, so it is unstable.

Note that we have been able here to find the exact behaviour close to the fixed points. If you just want to know whether or not they are stable, if you set $f(x)=x(1-x)$ then for $x^{*}=0$, $f'(x^{*})>0$, therefore this is unstable and for $x^{*}=1$, $f'(x^{*})<0$, therefore this is stable. It is only in the cases where $f'(x^{*})=0$ that you have to be more careful in figuring out what sort of stability you have. I would like you to find the actual behaviour close to the fixed point however.

- (a) $\dot{x} = x\left(1 - x\right)\left(3 - x\right)$
- (b) $\dot{x} = x^{2}\left(4 - x\right)$
- (c) $\dot{x} = 1 - e^{-x^{2}}$. Here you will need to know that for small $y$, $e^{-y^{2}} = 1 - y^{2} + O\left(y^{4}\right)$.
- (d) $\dot{x} = -x \ln x$

### 3. Euler's method

Use Euler's method to plot trajectories for the following differential equations:

- (a) $\dot{x} = 1 - 2x\left(1 - x\right)$ starting at $x_{0}=0$ with step sizes of $\Delta t = 0.2$ up to $t = 2$.

What happens if you use step sizes of $\Delta t = 1$, starting at $x_{0}=0$ and $x_{0}=-1$? What goes wrong in the above equation using Euler's method?

- (b) $\dot{x} = \sin x$ starting at $x_{0}=0.1$ with step sizes of $\Delta t = 1$ up to $t = 8$.
- (c) $\dot{x} = -x$ starting at $x_{0}=1$, with step sizes of $\Delta t = 0.2$ up to $t = 2$.
- (d) $\dot{x} = -x \ln x$ starting at $x_{0}=1.2$ with step sizes of $\Delta t = 0.5$ up to $t = 4$.

### 4. Match direction fields to differential equations

Match the following direction fields to the differential equations:

- (a) $\dot{x} = x^{2} - t^{2}$
- (b) $\dot{x} = x - t$
- (c) $\dot{x} = t \sin\left(x\right)$
- (d) $\dot{x} = xt$

![Figure 1](/images/part2exercises/output_001.png)

### 5. Adjacent fixed points

If you look through all of the phase portraits and study the fixed points, you will find that (unless there is a discontinuity in $\dot{x}(x)$) you never have one stable fixed point next to another one, or one unstable fixed point next to another. Can you explain why this is the case?

### 6. Potentials

Go through all of the above differential equations, and write down the potential which corresponds to them, then plot that. For some of these you won't be able to perform the integral analytically. In that case you can simply approximate a potential whose negative first derivative with respect to $x$ gives you the $f(x)$ in $\dot{x}=f(x)$. Notice the relationship between zeroes of $\dot{x}$ and valleys and hills of the potential.

For instance, if you had $\dot{x} = x\left(1-x\right)\left(3-x\right)$, then a $V(x)$ which satisfies $-V'(x) = x(1-x)(3-x)$ would be $V(x) = -\frac{3 x^{2}}{2} + \frac{4 x^{3}}{3} - \frac{x^{4}}{4}$. Plotting the phase portrait and the potential on the same figure gives:

![Figure 2](/images/part2exercises/output_002.png)
