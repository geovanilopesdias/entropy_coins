# Entropy Coins
**Abstract**: A tiny script in Python that "flips" a certain number of coins a certain numbers of times, outputting how many times they're fall on all equal.

## Background
It was my first personal code, i.e., a personal problem I challenge myself to solve by coding.

As a physics teacher, I've been propose to my high school students, for some time now, the well known coin-flipping analogy to learn associated entropy concepts, mainly macrostate and microstate. 

According to such analogy, the flipping of x number of different coins y number of times stands as a binary framework to the y possibilities a portion of x particles (atoms, ions or molecules) of a substance may have. As a binary framework, the analogy is simpler to realize and apply the aforementioned concepts if compared to the use of degrees of freedom concept, standing as a good introduction of such concepts. An even different approach is used in [this video](https://www.youtube.com/watch?v=vX_WLrcgikc) of Eugene Khutoryansky, but the idea is the same.

With only three coins, every year I show to students a table with all the draw possibiities and analyze with them how unlikely the specific condition that all the coins fall on with the same result (all head on or otherwise) is. However, as one may only flip a few number of coins a few number of times without getting bored or else, it is virtual impossible to realize how unlikely is a great number of coins fall on with the same result. Then I realized a program would do it easily. With a simple click, students can easily see for themselves how this result has a very low probability indeed. 

## A beginner study
Certainly an experienced developer, specially on Python, may think the code has a bad performance, or low readability or has some unpythonic expressions. However, I choose to let this code untouched even I learn any improvement for the code, so I or anyone can analyze it and discuss it.

## Updates
At August 8th, I've upload a newer version, using methods, list comprehension and the build-in sum(iterable). I do so, because I invert the approach: instead of appending all flips of a single coin into an array, I append a set of flips of all coins into one array. So, I build an analysis to sum all the random result as 0 or 1 (and not "$$" and "50" anymore): if the sum has the same value of the array length, or it equals zero, than on the coins fell on all equally.
Due to list comprehension and the build-in use, I could save respectively 8 and 18 lines of code, but didn't test the speed yet.
