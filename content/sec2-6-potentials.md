---
title: "2.6 Potentials"
weight: 26
math: true
---
## Section 2.6: Potentials

Potentials

We can also describe flows on the line using the language of potentials.

Imagine that you’re sat on the top of a hill, and start to roll down. As you roll down, you pick up speed, which is kinetic energy increasing. That has to be coming from somewhere (conservation of energy), and indeed it is coming from potential energy that you had at the top of the hill.

You can write down the potential that you would have for all points on the hill, and call this V($x$). In fact, the shape of the hill itself can give you the potential energy at each point:

![Figure 1](/images/part2f/output_001.png)

This is a bit of a cartoon representation, but imagine that you are living in a one dimensional world, and your potential energy was given by this function, depending on your position, $x$.

We have to make a big caveat here. This picture only works when we imagine that while you are sliding down the hill, you are moving through honey! This is because if we don’t damp our system, then we have to take into account $\ddot{x}$ terms as well as $\dot{x}$. If you were on a frictionless hill you could roll backwards and forwards over the valley floor - and we know that in a flow on a line, we can ’t have such oscillations.

So, it turns out that we can use the idea of a potential to describe our systems of the form:

$$
\dot{x}=f\left(x\right)
$$

What is the important feature of the potential? Well, it’s not the value of the potential itself at any one point, but how quickly it ’s changing, i.e. $V'\left(x\right)$. We can write our system as:

$$
\dot{x}=-\frac{d V}{d x}
$$

Because V is a function of $x$ and $x$ is a function of t, so we can think about the potential felt by our particle at any one moment, and thus V(t). By the chain rule (see by rearranging):

$$
\frac{d V}{d t}=\frac{d V}{d x} \dot{x}
$$

But by equation 0.1:

$$
\frac{d V}{d t}=-\frac{d V}{d x} \frac{d V}{d x}=-{\left(\frac{d V}{d x}\right)}^{2}
$$

which is clearly less than or equal to zero. This tells us that in this overdamped system, the potential of our particle always decreases. We always want to move to points of lower V.

Note that this is different to non-damped systems, where the V can oscillate when you are rolling up and down the sides of a valley. It ’s just that when your valley is covered in honey, you will keep rolling to the bottom.

Now, given a first order differential equation, you can figure out what the form of the damped potential.

Looking at the equation:

$$
\dot{x}=2x-x^{3}
$$

We can ask what potential would correspond to this? i.e. we need to find a V($$) for which:

$$
-V'\left(x\right)=2x-x^{3}
$$

To find that you need to whip out your anti-derivatives and you can show that:

$$
V\left(x\right)=-x^{2}+\frac{x^{4}}{4}+C
$$

As we said before, the actual height of the potential doesn’t matter for the dynamics, only the gradient does (since Force = $- V'\left(x\right)$, and this is all Newton cares for), so we can set C ⟶ 0. Looking at this function gives us:

We see that there are two minima of this function, at $x=\pm{}\sqrt{2}$, so these would be the points that we could come to rest in, i.e. the **fixed points** of the system. These are then stable fixed points. There is a local maximum at $x=0$ which is an unstable fixed point.

Once again, use a ball on a hill analogue to help. The ball at the top of the hill is **unstable**, while the one at the bottom is **stable**.

Of course you could have done this same analysis using the same methods in the phase space as we did before, but this gives you another picture of what is going on. In the first case, fixed points are roots, whereas in the potential picture, fixed points are local maxima and minima.