title: Verbs Instead of Nouns
published: !!timestamp '2014-04-08 11:00:00'
active_page: blog
tags:
    - javascript
    - programming
    - books

Jorge Luis Borges introduces us to a strange world in _Tlön, Uqbar, Oris Tertius_:

> "For them, the world is not a concurrence of objects in space, but a heterogeneous series of independent acts. It is serial and temporal, but not spatial. There are no nouns in the hypothetical _Ursprache_ of Tlön...For example, there is no word corresponding to the noun _moon_, but there is a verb _to moon_ or _to moondle_. _The moon rose over the sea_ would be written..."_upward beyond the constant flow there was moondling_" (23)

See if you can catch the parallels this software engineer's description of a bit of Javascript: 

> If the functions defined by mixins are intended solely for the use of other object why bother creating mixins as regular objects at all? Put another way, a mixin should be a process not an object. The logical conclusion is to make our mixins into functions into which consumer objects inject themselves by delegation, thus cutting out the middle guy (the extend function) entirely.

> ...

> This approach feels right. Mixins as verbs instead of nouns; lightweight one stop function shops -- [Angus Croll](http://javascriptweblog.wordpress.com/2011/05/31/a-fresh-look-at-javascript-mixins/)

Uncanny, right? The idea of modeling as "verbs instead of nouns" comes up again and again. There's an interesting connection to the idea of Duck Typing, [from Wikipedia](http://en.wikipedia.org/wiki/Duck_typing):

> The name of the concept refers to the duck test, attributed to James Whitcomb Riley (see history below), which may be phrased as follows:

> When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck.[1]

> In duck typing, a programmer is only concerned with ensuring that objects _behave as demanded_ of them in a given context, rather than ensuring that they are of a specific type.

Here, we define something as a "duck" if it happens to _do_ the things that a duck does. It doesn't matter what the thing really _is_. This just happens to be found in American Pragmatism, as well:

> Pragmatists...do not believe that there is a way things really are. So they want to replace the appearance/reality distinction by [the distinction] between descriptions of the world and of ourselves, which are less useful, and those, which are more useful. –Rorty
 
All of this is sort of a dreamy, emphasizing the movement of things rather than their (seemingly) solid existence. I think this thought was at the root of my fascination with the idea of [pigment vs. structural colors](http://smallredtile.com/posts/20131029-bird/) because it revealed that color isn't necessarily a static thing; rather, it's the result of the movement of photons, scattered in a particular way, which constantly bombard my eyeballs. In other words, color is not necessarily a specific thing, but, instead, a movement through time, an action over time.

The other side to note as a computer programmer is the practical side. You are almost never concerned with what something actually _is_, just with imitating or modeling it well enough. A computer simulation of a wind turbine is not actually a wind turbine. That's ok, the computer program is interesting because it happens to describe the behavior of a wind turbine well enough for the design engineers. 