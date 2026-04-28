---
title: "3.8 Exercises for Part 3"
weight: 38
math: true
---
## Section 3 exercises: Bifurcations

Many of these questions come from or are inspired by the questions in [Strogatz - Nonlinear dynamics and Chaos.](http://www.stevenstrogatz.com/books/nonlinear-dynamics-and-chaos-with-applications-to-physics-biology-chemistry-and-engineering)

- Questions on saddle-node bifurcations:

- i) Sketch the different vector field types that appear when you vary $r$ in the following differential equations. 
ii) Show that there is a saddle-node bifurcation (though there may more fixed points than just the two), and find the critical point of the bifurcation 
iii) and plot the bifurcation diagram. 

For instance, if you were given the equation $\dot{x}=x^{2}+r$, you would write:

- i) ii) There is a critical point at $r=r_{c} $where the stable and unstable fixed points come together after which there is no fixed point. This is the definition of a saddle-node bifurcation. 

iii) The bifurcation diagram looks like:

    - $\dot{x}=2+r x +x^{2}$ ([Solution](https://www.wolframcloud.com/obj/jon.shock/MAM1043part3exercises1a) including questions 2 and 3)

    - $\dot{ x}=r-\text{ cosh }\left(x\right) $([Solution](https://www.wolframcloud.com/obj/jon.shock/MAM1043part3exercises1b) including questions 2 and 3)

    - $\dot{ x}=r+x-\text{ ln }\left(1+x\right) $([Solution](https://www.wolframcloud.com/obj/jon.shock/MAM1043part3exercises1c) including questions 2 and 3)

    - $\dot{x}=r+\frac{x}{2}-\frac{x}{1+x}$ ([Solution](https://www.wolframcloud.com/obj/jon.shock/MAM1043part3exercises1d) including questions 2 and 3)

- For the example of the equation $\dot{x}=x^{2}+r$, plot the potential for different values of $r$ and see what the behaviour looks like there in that picture.

- We mentioned **Normal Forms** in the notes. The point is that close to the bifurcation point, ALL saddle-node bifurcations look like $\dot{x}=r+x^{2}$ or $\dot{x}=r-x^{2}.$ 

For instance, for the equation $\dot{x}=r-x-e^{-x}, $there is a critical point at $r$=1 at $x=0$. We can expand the right hand side close to $x=0 \text{ and }$ it gives us: $\dot{x}=r-x-\left(1-x+\frac{x^{2}}{2!}-...\right)=\left(r-1\right)-\frac{x^{2}}{2}+....$ Up to a scaling in $x$ and a shift in $r$, this is the same as $\dot{x}=r-x^{2}.$ 

Go through the above equations from exercise 1 and show that when you expand around the bifurcation point, they all take on the same normal form. If you need to expand a function, you can use Wolfram Alpha, for instance, for $\text{ cosh }\left(x\right):$

which you can then plug into the right hand side of $\dot{ x}=r-\text{ cosh }\left(x\right) $ and see what happens for x close to 0.

- Now do the same thing as questions **1** and **2** for the following transcritical bifurcations:

    - $\dot{x}=r x+x^{2}$ (This is the canonical example of a transcritical bifurcation (with $+x^{2}$ instead of $-x^{2}$). Follow the logic in the notes for the original example).

    - $\dot{ x}=r x-\text{ ln }\left(1+x\right)$ ([Solution](https://www.wolframcloud.com/obj/jon.shock/MAM1043part3exercises4b))

    - $\dot{ x}=x-r x \left(1-x\right)$ ([Solution](https://www.wolframcloud.com/obj/jon.shock/MAM1043part3exercises4c))

    - $\dot{x}=x\left(r-e^{x}\right)$ ([Solution](https://www.wolframcloud.com/obj/jon.shock/MAM1043part3exercises4d))

    - $\dot{x}=r \text{ ln } x+x-1$ ([Solution](https://www.wolframcloud.com/obj/jon.shock/MAM1043part3exercises4e))

- Now do the same thing as questions **1** and **2** for the following pitchfork bifurcations. This time also classify them as subcritical or supercritical.

    - $\dot{x}=r x+4x^{3}$ (This is the canonical example of a pitchfork bifurcation but with an extra factor of 4. The method is the same as in the notes for pitchfork bifurcations, just with a scaling. Make sure that you can follow this).

    - $\dot{ x}=r x-\text{ sinh }\left(x\right)$ ([Solution](https://www.wolframcloud.com/obj/jon.shock/MAM1043part3exercises5b))

    - $\dot{ x}=r x-4x^{3}$

    - $\dot{x}=x+\frac{r x}{1+x^{2}}$

- For these flows on the line, find the value of r for which a bifurcation occurs, classify the bifurcation type, and draw the bifurcation diagram

    - $\dot{x}=r-3x^{2}$

    - $\dot{ x}=r x-\frac{x}{1+x}$

    - $\dot{ x}=5-r e^{-x^{2}}$

    - $\dot{x}=r x-\frac{x}{1+x^{2}}$

    - $\dot{ x}=x+\text{ tanh }\left(r x\right)$

    - $\dot{ x}=r x+\frac{x^{3}}{1+x^{2}}$

- Can you find a differential equation which, at a critical value of $r$ goes from no fixed points to four fixed points?

- Plot the bifurcation diagram for $\dot{ x}=h +r x-x^{2}$ for $h<0, h=0 \text{ and } h>0 \text{ separately }$.

Sketch the regions in the (r,h) plane that correspond to qualitatively different vector fields and identify the bifurcations that occur on the boundaries of those regions.

- Imagine that you are in a crowded room and you are all asked to vote on a given topic by either keeping your hands down or putting them up. You don ’t care very much about the topic, but you do care that your vote is similar to your neighbour’s vote.

Let’s say that if you vote yes, then you (labelled by person $i$) are assigned a value $S_{i}=+1$ and if you vote no, you are assigned a value $S_{i}=-1$.

We can ask how much of a majority the yes votes have over the no’s, or vice versa by:

$m=|\frac{1}{N}\underset{i=1}{\overset{N}{\sum{}}}S_{i}|$

where here you are summing over each of the people in the room (there are $N$) of them.

If you are all full of coffee you might be a bit jumpy and won’t look carefully at your neighbour, so your vote won’t depend on them, and everyone ’s vote will be essentially random. If this is the case then there will be about the same number of yes votes as no votes, and you will find that $m$[TildeTilde]0.

However, if the coffee is wearing off, and you start to look around, there will be some critical moment where people start to see what is happening around them and you will start to be influenced by your neighbour’s vote. At this moment, a phase transition occurs, and you go from having $m$[TildeTilde]0 to m > 0.

Perhaps one person had their hand up, and the people around them saw this and put their hands up as well, and this spread. Then you would have $m>0$ and the majority of people would have their hands up. Or, you might have had one person with their hand down, the people around them noticed, and so on, and so $m>0$ but now the majority of people have their hand down. 

There is a symmetry between these two different states. Both of them are stable configurations. It’s hard to move from everyone with their hands up to everyone with their hands down, or vice versa because everyone likes to do what their neighbours are doing, unless they are too hyped up on coffee.

You can change this situation by persuading people that maybe voting yes is a good idea. Although the neighbours will still have an effect, people will generally like to have their hands up anyway. The strength of the persuasion is given by a parameter $h.$ If $h$ is positive, then people are more persuaded to have their hands up, and if $h$ is negative then people are more persuaded to have their hands down. Caffeine in the system might mean that people don’t list to reason however.

It turns out that there is an equation which governs the relationship between $h, m, T \left(\text{ how much } \text{ coffee people } \text{ have had }\right), J>0$ (how much you are influenced by your neighbours) and $n$ (how many neighbours you have). The equation says that m can be found by solving:

$ h=T {\text{ tanh }}^{-1}m-J n m$

What on Earth?!! I hear you say...well, it turns out I’ve played a terrible trick on you!! I wasn ’t really talking about voting, but spins in a magnet, and I ’ve just sneakily taught you some physics. Haha!! In this model (the Ising model - pronounced (Eas(as in East)ing), T is the temperature of the magnet which makes the individual atoms which each have a magnetic spin want to point randomly up or down. $S_{i} \text{ is }$ the value of each spin. $J$ is how strongly each spin likes to couple to the spins around it. h is the value of an external magnetic field, n is the number of neighbours that each spin has and m is the magnetisation of the material. When m=0, the material is said to be paramegnetic, but if you turn down the temperature enough, then the spins align, m>0 and you have a ferromagnetic, which has two stable states, one with most spins up, and one with most spins down (the temperature will still make some of them point in random directions). If you turn on an external field, h, then this symmetry will be broken, and h will push most of the spins up (if h>0) or most of the spins down (if h<0).

The funny equation above with the inverse tanh function is what is called the Mean Field Approximation equilibrium solution to the Ising model.

OK, so now a question for you! 

For the special case where h=0, can you find the critical temperature at which you go from a paramagnet to a ferromagnet? 

If h is not 0, can you use a graphical method to find the approximate solution $m^{*}\text{ to the } \text{ above equation }?$

Note that you are not expected to know where the above equation came from - it actually comes from some absolutely beautiful statistical mechanics. I hope that one day you will get to study it!