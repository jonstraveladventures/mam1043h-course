---
title: "1.2a History of Dynamics — Beginnings"
weight: 12
math: true
---
## Section 1.2(a): The History of Dynamics - The Beginnings of Dynamics

To have dynamics, we need to describe rates of change. We mostly do this using derivatives... and therefore calculus. But we don’t actually need calculus to study dynamical systems. Instead of differential equations, one can use difference equations. See this short important post [here](https://www.wolframcloud.com/obj/jon.shock/differenceequations).

Ideas of calculus were already around in Egypt, India and China, but it was formalised in the 17th century by Newton (and Leibniz).

It was at this point that Newton allowed us to start writing down differential equations to describe the world. One of the first things that he wanted to understand was gravity.

The world already had a set of laws, thanks to [Kepler](https://en.wikipedia.org/wiki/Johannes_Kepler), about planetary motion. Those laws were thanks to the observations of [Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe) - the astronomer with the metal nose (he lost the original in a sword fight). Tycho’s sister, [Sophia Brahe](https://en.wikipedia.org/wiki/Sophia_Brahe) was instrumental to making these observations.

**The first law**: A planet’s orbit around the sun is an ellipse. The sun ’s centre is at one focus of the ellipse.

![Animated ellipse: Kepler's first law](/images/part1b/anim_001.gif)

**The second law**: If you draw a line between the planet and the sun, the area swept out by the line is the same in any given time period.

![Animated area sweep: Kepler's second law](/images/part1b/anim_002.gif)

**The third law**: The square of the period of a single orbit of a planet is proportional to the cube of the semi-major axis.

![Figure 3](/images/part1b/output_003.png)

[This](https://commons.wikimedia.org/wiki/File:Solar_system_orbital_period_vs_semimajor_axis.svg) diagram below shows how well the third law holds in the solar system:

So, Brahe had studied the movements of the planets and noted down their positions over time with huge detail. Also note that Chinese astronomy was way ahead of its time, with [Shen Kuo](https://en.wikipedia.org/wiki/Shen_Kuo) (\:6c88\:62ec) having made detailed observations of planetary motion in the 11th century. Kepler had made some [empirical](https://dictionary.cambridge.org/dictionary/english/empirical) observations of these positions and come up with his [three laws](https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion), but nobody knew why these laws held. 

So, Newton came along with his fancy-pants calculus and wrote down the differential equation thanks to his law of gravitation and laws of motion. By solving them, he proved Kepler’s laws to be true (well, at least in the limit that the sun is much much heavier than the planets). You can find a nice review of this [here](https://www.mtholyoke.edu/courses/mdyar/ast223/orbits/orb_lect.html). Quoting from this page:

*Kepler’s Laws are wonderful as a description of the motions of the plan**ets. However, they provide no explanation of why the planets move in this way. Moreover, Kepler’s Third Law only works for planets around the Sun and does not ap**ply to the Moon’s orbit around the Earth or the moons of Jupiter. Isaac Newton (1642-1727) provided a more general explanation of the motions of the planets through the development of Newton ’s Laws of Motion and Newton’s Universal Law of Gravitation.*

The name of this problem is the so-called [two-body problem of celestial mechanics](https://en.wikipedia.org/wiki/Two-body_problem). In simple terms it is the problem of two massive objects (stars, planets, etc.) moving around each other through gravitational interactions. 

In fact, whenever you have two objects moving about each other, both of them move (the heavier one by less than the lighter one). In this demonstration from [here](https://demonstrations.wolfram.com/TheCelestialTwoBodyProblem/) you can explore what happens when you change various parameters in the orbits of two objects around each other. The following is just a picture.

I said that Newton “solved” the two-body problem. What do we mean by **solved**?

We can write down a set of equations that encodes the dynamics of this system. That is half the battle. They will take the form of differential equations. Once you have the equations, you need to find solutions to the equations. A solution will correspond to a function, or functions of time (the position of the planet and star as a function of time) which satisfy the equation/equations.

Generally when we say that someone “solved” a dynamical system, we mean that they found all of the solutions.

How about if you have two planets going around a star? This is the so-called three-body problem, **it cannot be solved**.

This means that you cannot write all solutions down in a finite number of ‘normal’ mathematical functions. You can find some very special solutions...but a general solution is not possible...provably!

This is an example of a very special solution.

![Three-body problem: figure-8 special solution](/images/part1b/anim_003.gif)

*If any of you like reading science fiction, then* *[The Three Body Problem](https://en.wikipedia.org/wiki/The_Three-Body_Problem_(novel))* *(\:4e09\:9898\:ff09is a wonderful book by Liu Cixin.*

**So what do we have so far?**

Well, it seems that writing down differential equations can be important to understanding how things change with time.

- Sometimes we can solve these differential equations.

- Sometimes we can't solve these differential equations.

This course will be about **trying to be as lazy as possible (but no lazier)**: getting answers without having to solve the differential equations (though sometimes we will).