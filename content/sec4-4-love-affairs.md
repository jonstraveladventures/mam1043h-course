---
title: "4.4 Application — Love Affairs"
weight: 64
math: true
---
## Section 4.4: Love affairs

Love Affairs

So, this is the last section of the notes, I know, it’s difficult for me too, but it’s only for now! If you carry on next year with applied maths you may find me teaching you Second Year Non-Linear Dynamics, in which case I will be carrying on with the notes then... but for now, let's look at love affairs.

This example is adapted from Strogatz, and is based on [a paper of his from 1988](http://ai.stanford.edu/~rajatr/articles/SS_love_dEq.pdf).

This is a tale of two penguins who can be found in Simon’s Town, just down the coast from here. Thando and Marsha are two penguins, and their relationship is... complicated. We will be modeling their love for one another. $T\left(t\right) \text{ measures }$ Thando’s love for Marsha and $M\left(t\right) $measures Marsha’s love for Thando. These variables can be positive (loving) or negative (hating). A nearby mathematically minded penguin named Erd[ODoubleDot]s has come up with a model for the couple’s dynamics. Erd [ODoubleDot]s the penguin claims that an appropriate model for what she has seen is:

$$
\dot{T}\left(t\right)=a M\left(t\right)
$$

$$
\dot{M}\left(t\right)=-b T\left(t\right)
$$

where $a$ and $b$ are positive real numbers.

This says that Thando's love goes up when Marsha's love is positive, and goes down when Marsha's love is negative (let's call it what it is...hate). Unfortunately Marsha's love goes down when Thando's love is positive and vice versa. This is a tricky stage of their relationship because as soon as Thando sees that Marsha is keen, Marsha loses interest and then so does Thando, and then Marsha gets into the now disinterested Thando, and so it goes on without end. Here we have a **cycle**. If $a=b=1, \text{ we have }:$

![Figure 1](/images/part4d/output_001.png)

A really toxic relationship and not advised!

Now how about if we had $\dot{T}\left(t\right)=a T\left(t\right)+b M\left(t\right)$. If both parameters are greater than zero, then Thando is an eager beaver! Thando gets punch drunk on their own love and also on Marsha ’s love! If $a<0 \text{ and } b>0$ then we have a cautious lover. When their own love goes up, Thando gets nervous and this cools off their love for Marsha, but Marsha’s love is like rocket fuel for Thando and causes T(t) to go up.

What if we have two equally cautious lovers?

$$
\dot{T}\left(t\right)=a T\left(t\right)+b M\left(t\right)
$$

$$
\dot{M}\left(t\right)=b T\left(t\right)+a M\left(t\right)
$$

so $a<0 \text{ and } b>0$. There are a couple of possibilities here. Remember that we have our eigenvalues as:

$$
{\lambda{}}_{1,2}=\frac{\tau{}\pm{}\sqrt{{\tau{}}^{2}-4\Delta{}}}{2}
$$

Now $\tau{}=2a \text{ and } \Delta{}=a^{2}-b^{2},\text{ so }:$

$$
{\lambda{}}_{1,2}=a\pm{}b
$$

Remember that a is less than zero, so we have a couple of possibilities. If $a^{2}<b^{2} \text{ then } a+b>0 \text{ and } a-b<0$. This tells us that we will have one positive eigenvalue and one negative eigenvalue. You should recognise this from the previous pages. This leads to the saddle point situation:

![Figure 2](/images/part4d/output_002.png)

Depending on where we start, we are either going to have a love fest, or an all out war, neither of which looks great for penguin society.

How about if both $a+b $and $ a-b< 0$. Well, then we end up with a stable node at (0,0) which means that independent of how much they start loving or hating each other, there will be complete indifference in the end.

![Figure 3](/images/part4d/output_003.png)

We have looked at only a very small part of the parameter space for the tale of this pair of lovers. Can you see if there are any parameters which will lead to a good outcome?

And this brings us to an end for MAM1043H! I’ll preemptively thank all of you for being great students and hope you enjoyed this course!!

Good luck for the final exam, everything you need you have in these notes and exercises, but trust your understanding, you've got this :)