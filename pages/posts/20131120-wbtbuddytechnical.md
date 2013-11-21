title: Implementing Interactive Engineering Calculations with Backbone Javascript
published: !!timestamp '2013-11-20 11:00:00'
active_page: blog
tags:
  - javascript
  - engineering

I wrote lots of engineering reports as an undergrad in Mechanical Engineering, and I've always dreamed there was something more we could do more to present calculations to be understand, learned, and shared. Here is the result of a recent experiment to simplify a nasty Excel spreadsheet into an interactive calculation.

The [WBT Buddy](http://smallredtile.com/stove/wbt-buddy/) is a single-page app that performs an energy efficiency calculation with the steps explicitly laid out. It also visualizes your result against some baseline quantities. 

Everything happens in the browser. While the capability to do so has been around for a decade, it's never been easier to develop this sort of functionality thanks to a constellation of front-end tools: Backbone Javascript, CSS3, and Bootstrap.

The integration of these tools is quite painless. I built a sort of framework on top of them for the notion of a "user interface for engineering calculations". This is a big area, and this effort is certainly not the final say in how this should be done. Each problem will have its own contours, and you should choose your abstractions to fit into them.

With that in mind, here are some of the tools I chose and how they were deployed:

Binding to Bootstrap events
----

The fuel type selection box is a Bootstrap `.nav-pills` list. Each link item is given `data-toggle="pill"`. When the link is clicked a `shown.bs.tab` event is triggered. You can bind that event with one line of Backbone code:

![navpills](/static/images/20131120navpills.png)

<pre class="prettyprint">
events: {
  'shown.bs.tab .fuel-type-choice' : 'updateOnClick'
}
</pre>

CSS bar-graph
----

While I love the d3 visualization library, I was not looking forward to laying out an entire visualization for a single bar graph. Fortunately, I managed to pull this off with just CSS.

To render the bar corresponding to 15% here:

![bargraph](/static/images/20131120-bar.png)

This is all that's required:

<pre class="prettyprint">
&lt;li class="yours"&gt;
  15%
  &lt;span class="bar" style="width:12%"&gt;&lt;/span&gt;
&lt;/li&gt;
</pre>

Back when I was introduced to web programming as an intern in college, I spent an entire summer rendering bar graphs in Javascript. Now, it takes just a few minutes of choosing the right CSS property.

numeral.js for formatting
----

Formatting numbers isn't built-in to Javascript. I grabbed the numeral.js library to make this easy.

If I wanted to turn "26312.35266" into "26,312.35", I did this:

<pre class="prettyprint">
return numeral(number).format("0,00.00");
</pre>

Domain Specific Language for updatable equations
----

This feature will get its own blog post as it takes some explaining. Here is a short preview.

I implemented a tiny language for building templates for "steps of an equation". Here's what one of the equation steps looks like, with its two states shown:

![equation1](/static/images/20131120-eq1.png)

![equation2](/static/images/20131120-eq2.png)

The code that creates this equation step look like this:

<pre class="prettyprint">
return model.equationTemplate(
  "E_H2O = ([m_H2O]) * [c_pH2O] * ([T_B] - [T_A])"
);
</pre>

You can also do things like convert the variables to different units or format the output number. The following template converts the `E_H2O` quantity to kiloJoules and formats it with one digit after the decimal point.

<pre class="prettyprint">
return model.equationTemplate(
  "OTE = [E_H2O kJ -f 0.0] / [E_fuel kJ -f 0.0]"
);
</pre>

I originally fiddled with using a parser generator (PEG.js) for this feature. However, I found it was more straightforward to build on top of the underscore.js templating code (which in turn is built on top of John Resig's micro-templating example)

Conclusions
---

Backbone.JS the implementation of the WBT Buddy quite enjoyable. Binding events between the inputs, equation model, and calculation outputs was logical. The abstractions in Backbone.JS are flexible. I never found myself fighting against the framework to get something done. I would reach for these tools again in future projects.



