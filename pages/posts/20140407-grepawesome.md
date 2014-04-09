title: grep awesome
published: !!timestamp '2014-04-04 11:00:00'
active_page: blog
tags:
    - javascript


I happened to search my entire javascript codebase for the word "awesome" last week. I stumbled into this little gem in the jQuery source:

<pre class="prettyprint">
// A tribute to the "awesome hack by Dean Edwards"
// Chrome < 17 and Safari 5.0 uses "computed value" 
// instead of "used value" for margin-right
// Safari 5.1.7 (at least) returns percentage for a 
// arger set of values, but width seems to be reliably 
// pixels this is against the CSSOM draft spec: 
// http://dev.w3.org/csswg/cssom/#resolved-values
if ( rnumnonpx.test( ret ) && rmargin.test( name ) ) {

	// Remember the original values
	width = style.width;
	minWidth = style.minWidth;
	maxWidth = style.maxWidth;

	// Put in the new values to get a computed value out
	style.minWidth = style.maxWidth = style.width = ret;
	ret = computed.width;

	// Revert the changed values
	style.width = width;
	style.minWidth = minWidth;
	style.maxWidth = maxWidth;
}
</pre>


What a gnarly little piece of code. The best explanation I found about this is at [heygrady](http://heygrady.com/blog/2011/12/21/length-and-angle-unit-conversion-in-javascript/). Shows how the effort required to provide compatibility across browser versions grows exponentially rather than linearly – getting those last little things right takes hacks, workaround, and black magic.