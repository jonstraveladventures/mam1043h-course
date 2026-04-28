---
title: "2.7b Back to Basics — Phase Spaces and Phase Portraits"
weight: 28
math: true
---
## Section 2.7b: Back to Basics

Back to Basics

I think that at this stage it’s useful, with some new context, to go back to basics and to cover the ideas of phase space and phase portraits again. In class, I’ve found that students find themselves feeling a bit confused by some ideas so it’s good to make sure that we are all on the same page now.

Phase Space

The phase space of a dynamical system is the space of all possible states that it can take. For instance, if you have a pendulum governed by the differential equation:

$$
\ddot{\theta{} }\left(t\right)=- \frac{g}{l}\text{ sin }\left( \theta{} \left(t\right) \right)
$$

You can ask what the possible states of the system are.

Well, you can have the pendulum be at a particular angle at some time, $t$. This doesn’t give us all the information about the system. It will not tell you about how fast it was going, so you need to specify that. You don’t need to give the angular acceleration as that is given to you by the differential equation provided you have the angle. So you only need two pieces of information to tell you exactly the state that the system is in at any one moment: θ and $\dot{\theta{}}$.

Given these, you can calculate any other derivatives you want. There is nothing more to know about the system. So, we can plot the space of all possible solutions, and it is given by:

![Figure 1](/images/part2h/output_001.png)

This is a pretty boring plot, as it stands, but if you pick any spot in this two dimensional phase space corresponds to some configuration of the pendulum. Furthermore, given any one point, the differential equation will tell you where it is at any future moments in time. So you can plot trajectories in the phase space, and these look like:

![Figure 2](/images/part2h/output_002.png)

There are different kinds of solutions plotted in the above: pendulum swings that just go back and forth (the closed loops) and swings which go over the top and keep swinging around.

So, the phase space itself is just the space of all possible states of the system, and within that, if you solve the differential equation you can calculate trajectories within the phase space. Note that a trajectory in phase space will correspond to a particular trajectory in the solution space. So for instance the largest yellow loop in the plot above would correspond to the following trajectory of θ:

![Figure 3](/images/part2h/output_003.png)

A single, autonomous second order differential equation will give you a two dimensional phase space. The differential equation can also be rewritten as two first order autonomous differential equations:

$$
\dot{\theta{}}\left(t\right)=v\left(t\right)
$$

Where $v\left(t\right)$ is the angular velocity. This says that given the angle, and the velocity, the rate of change of the angle and velocity can be calculated directly.

There is another way that we might end up with a two dimensional phase space, and that’s when the dynamical system is made up, from the start, of two systems which interact. For instance, a so-called predator-prey model (also called a Lotka-Volterra model). If you have a population of rabbits and foxes interacting (i.e. each reproducing, but the foxes eating the rabbits), this can be described by the following differential equations:

$$
\dot{R}\left(t\right)=\alpha R\left(t\right)-\beta R\left(t\right) F\left(t\right)
$$

$$
\dot{F}\left(t\right)=\delta R\left(t\right) F\left(t\right)-\gamma F\left(t\right)
$$

where the parameters α, β, γ, δ are factors related to the environment and they will generally be fixed for a given system. $R\left(t\right) $is the rabbit population and $F\left(t\right) \text{ is the } \text{ fox population }$. The phase space again in this case is two-dimensional, made up now of the number of rabbits and the number of foxes:

![Figure 4](/images/part2h/output_004.png)

Pick any point in this space and it’s a particular population of rabbits and foxes. Use the differential equations and you can find out how this then evolves in time. For instance, if we set α, β, γ, δ all to be 1 for simplicity’s sake, and set $R\left(0\right)=2 \text{ and } F\left(0\right)=1$ (let’s say that these are in units of a thousand individuals), we get the following closed curve in phase space:

![Figure 5](/images/part2h/output_005.png)

In the space of trajectories of rabbits and foxes separately, this looks like:

![Figure 6](/images/part2h/output_006.png)

Phase portraits

Phase portraits give us more information than simply plotting the phase space. They generally give us the behaviour of all possible solutions. We have only been plotting phase portraits of one dimensional systems, not two dimensional systems as above.

For a one dimensional system like:

$$
\dot{x}\left(t\right)={x\left(t\right)}^{2}
$$

The phase space is one dimensional - i.e. it’s just the value of $x$. If I give you $x$, then everything else is determined by the equation. However, for a phase portrait we are plotting the differential equation itself:

![Figure 7](/images/part2h/output_007.png)

The phase space is just the $x$-axis, but by plotting the differential equation like this, we can determine (qualitatively) the behaviour of the system including fixed points and the direction of flows along the line.

It is possible to plot a phase portrait for a second order equation and it will include a two dimensional surface in a three dimensional space, but we are not going to do that in this course.