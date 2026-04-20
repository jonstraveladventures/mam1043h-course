---
title: "1.1 Overview of the Course"
weight: 11
math: true
---
## Section 1.1: Course Introduction

If you find any mistakes, or have comments on the notes, please message me at jon.shock@gmail.com.

The textbook that I will be following is: Nonlinear Dynamics and Chaos, by Steven Strogatz.

You do not need to get it. I will aim for this all to be self-contained. However, it is a beautifully written book, and almost certainly

the best introduction to the subject.

Steven Strogatz actually has some of the material that we will be covering on Youtube (Note that we will only really cover the first two his lectures):here.

He has in the past tweeted to this link which has some Python code for some of the examples in the book.

Here are some more links to online courses which you may want to browse.

- Complexity Explorer course on intro to dynamical systems and chaos
- Complexity Explorer course on introduction-to-differential-equations

Please note, that I will often put in links to Wikipedia articles. One has to be careful about how accurate Wikipedia pages are, and in general if you are writing a scientific research paper, Wikipedia articles are not good to reference. However, for an educational set of notes like this, where I think that it will add useful content, I will be doing so. Wikipedia articles should be read with a critical hat on, and if you want to dig further, look at the references in the articles themselves.

**What is this course about?**

1. Understanding what a dynamical system is
    through examples and definitions
1. Knowing how to write down the mathematics of a dynamical system
    through examples and problems
1. Knowing how to understand the interactions of dynamical systems through quantitative and qualitative means
    through many different techniques

I am writing these notes using the Wolfram Mathematica programming language. It means that I can very easily include nice plots and animations which should add to the content. You do not need to know how to use this.

The Course Content:

Section 1: Introduction (Strogatz chapter 1)

- 1.1 Overview of the course (what you're reading now)
- 1.2 a) The history of dynamics - The beginnings of dynamics
- 1.2 b) The history of dynamics - Poincare and chaos

Aside: Difference equations

- 1.3 Systems of differential equations
- 1.4 Phase space
- 1.5 The spectrum of systems of differential equations

- 1.6 Exercises for part 1

Section 2: Flows on the line (Strogatz chapter 2)

- 2.1 Fixed points and trajectories
- 2.2 Fixed Points and their stability
- 2.3 Linear stability analysis
- 2.4 Existence and uniqueness of solutions
- 2.5 Absence of oscillations
- 2.6 Potentials
- 2.7 a) Solving equations on the computer

- 2.7 b) Back to basics: A summary of phase spaces and phase portraits
- 2.8 Exercises for part 2


Section 3: Bifurcations (Strogatz chapter 3)

- 3.1 and 3.2 Introduction and saddle-node bifurcations
- 3.3 Transcritical bifurcations
- 3.4 Pitchfork bifurcations
- 3.5 Combinations of bifurcations
- 3.6 Chaos and the logistic map
- 3.7 a) Imperfect bifurcations and catastrophes

- 3.7 b) Imperfect bifurcations and catastrophes part 2
- 3.8 Exercises for part 3


Section 4: Linear systems in two dimensions (Strogatz chapter 5)

- 4.1 Introduction to linear systems in two dimensions
- 4.2 Classification of linear systems and their origin part 1

- 4.3 Classification of linear systems and their origin part 2
- 4.4 Application: Love affairs

- 4.5 Exercises for part 4

## Chapter 1: Introduction

The scientific method often goes something like this:

1. Find some phenomenon that you want to understand.
2. See if you can translate that phenomenon into the language of mathematics.
 3. Study the mathematics to see if you can make predictions.
4. Test those predictions in the real world.
5. If the predictions turn out to be true, make some more until you break your model.
6. When the predictions turn out not to be true, change your model until it matches the world.

This way you are slowly but surely moving towards a more and more accurate picture of the world. There are a number of disclaimers to all of this. One is that you don't want to keep making your model of the world more and more complicated (see the epicyclic model of the solar system). You want it to be as simple as possible while capturing everything that you observe - ie. as simple as possible, but no simpler. You may ask why we want to break your model. Well, this is due to the statement at the beginning of this chapter from George Box. If we want to find out where our model is wrong, the best way to do this is to find out where it breaks.

 So, what is the type of mathematics that you might want to use to describe physical reality? Well, in the first semester you saw a number of different methods that can be used:

- Write down the likely probability of something happening.
    - Write down an equation using dimensional analysis.
   - Write down a differential equation which you think may describe your system.

You will have seen differential equations in MAM1044H and a little in this course already. Essentially, the definition couldn't be simpler. 
They are equations...with derivatives in them. Here are a few examples:

1. Exponential growth:

$$
\frac{d P\left(t\right)}{\text{ dt }}=k P\left(t\right)
$$

This equation is related to population growth and says that the rate of change of a population $P$ with time is proportional to the population that you have at that time (the more people you have, the faster you can produce more people). $k$****is a constant known as the growth rate. I’ve written a long blog post about this here.

1. The logistic equation:

$$
\frac{d  P\left(t\right)}{\text{ dt }}=k P\left(t\right)\left(1-\frac{P\left(t\right)}{M}\right)
$$

This is another equation related to the growth rate of a population, but it is a little more sophisticated and realistic. It’s called the Logistic equation. Now $M$ is known as the carrying capacity and is related to the maximum size of population that the environment can sustain.

1. The pendulum:

$$
\frac{d^{2} \theta{}\left(t\right)}{{\text{ dt }}^{2}}=- \frac{g}{l}\text{ sin }\left(\theta{}\left(t\right)\right)
$$

This equation describes the swinging of a pendulum and relates the acceleration of the angle to the angle itself. $g$****is the strength of gravity and $l^{ } $is the length of the pendulum arm. This says that (at least for angles less than horizontal) the rate of change of the angular velocity is related to how far from the lowest position the pendulum is. Here is a little animation that comes from solving this equation. You do not need to know how this code works.

![Pendulum animation](/images/part1a/anim_001.gif)

All of these differential equations are in terms of time, but a differential equation doesn't have to be. However, in this course, we will be talking about time...and we'll see why. The key is in the word **dynamics****.**

If you’re given a differential equation describing some complicated system, like populations of rabbits and wolves, or planets moving around each other, or neurons firing in the brain, we very often can figure out some behavioural traits without solving the equation. This 2nd half of MAM1043H is about solving these so-called dynamical systems. Systems of interacting elements (things) which are described by differential equations. We will see lots along the way, but the types of things that we might be interested in are:

- A planet moving around a star
    - A population of rhinos interacting with a population of poachers
- The propagation of light from a lightbulb through the air
- The price of oil 
- The flow of water through a river 
- The weather
- The evolution of life on Earth
- The expansion of the universe
- The swinging of a pendulum
- The firing of a single neuron in your brain
- The firing of all of the neurons in your brain
    - The growth of the internet
- The flow of heat through a piece of metal
- The spread of fire through a forest
    - The running of a computer program
- The increase in the number of bacteria in a sample
- and so many more!

As you can see, these already come from so many disciplines: physics, biology, economics, computer science, meteorology, sociology, neuroscience...

What do all of these things have in common?

- They are all about how something changes in time.

- They are all about the interaction, either with itself, or in some environment. Let’s look at that list again:

- A planet moving around a star: The position of the planet is changing with time, the planet is interacting with the star.
- A population of rhinos interacting with a population of poachers: The number of rhinos and poachers are changing over time. The rhinos and poachers are interacting with each other, but the rhinos also depend on the amount of food around, and many other factors. The number of poachers depends on economic factors, family dynamics, police enforcement.
- The propagation of light from a lightbulb through the air: Light is an excitation of the electromagnetic field. The position of photons changes with time. 
- The price of oil: The price changes over time. It is dependent on the supply and demand.
    - The flow of water through a river: We can treat the individual water molecules, or we can talk about the velocity of water at any one point and see how that changes over time.

Now try and complete the list below on your own, as much as you can. There are many ways to answer this, and most of them are very complicated systems. It's more a matter of getting you to think about it than getting a fixed answer.

- The weather
- The evolution of life on Earth
- The expansion of the universe
    - The swinging of a pendulum
- The firing of a single neuron in your brain
- The firing of all of the neurons in your brain
- The growth of the internet
- The flow of heat through a piece of metal
- The spread of fire through a forest
- The running of a computer program
    - The increase in the number of bacteria in a sample
    - and so many more!

Now try and write down some dynamical systems of your own... ie. interacting things which change in time.

You may ask the question “What is a system which is not dynamical”. Well, the definition of system, is one from Wikipedia (though many dictionary definitions are similar):

**“****A system is a group of interacting or interrelated elements that act according to a set of rules to form a unified whole****”**

So, a set of equations which are connected, like:

$$
x=4y-3
$$

Would be a system of equations, because the variables $x$ and $y$ which would here correspond to the **elements** of the system, interact via a set of rules. The unified whole is just the set **{**x , y**}** which isn’t very interesting here. Most of the physical systems (collection of interacting elements) that you can think of will already be dynamical, because most things around us which interact **do******change with time.