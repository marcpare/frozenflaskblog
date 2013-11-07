title: Dictionary of Computer Science

Computer Science Concepts 
=========================

demonstrated in Javascript
--------------------------

_Inversion of Control_

Inversion of Control and Dependency Injection are closely related concepts. Basically, the coupling between objects is determined a run-time, not compile-time.

In BackboneJS, the event listener `on` has a corresponding 'listenTo' method.

With `on`, an object reacts to one of its own events.

With `listenTo`, an object can listen to events from another object.

For example, in a Todo list application, the view object that displays the list of Todo items would `listenTo` changes in the object representing a collection of Todos. 

This is called an Inversion of Control because it is not known until run time which object(s) will be receiving events. With the `on` method, you would could determine this lexically based on which objects defined the `on` method.

_Closure_

A closure is said to "close around" variables. It is a function with a reference to an execution environment (usually a number of non-local variables).

<pre>
var make_adder = function (y) {
  return function (x) {
    return x + y;
  }
}

var add_two = make_adder(2);

add_two(5); // 7
</pre>

Here the `make_adder` function creates a function that closes around the `x` variable.

You would say `make_adder` _returns a closure_ containing a reference to the variable `y`, which, in the case of `add_two`, equals `2`.

_Lexical Scoping_

"Scope" is about the rules that determine whether a variable name is valid and what its contents are.

Lexical scoping is determined by the program's _text_ (hence "lexical"). A variable exists while the function that defined it exists. It disappears afterward.

In Javascript, functions are the only unit of structure that determine scope.

<pre>
var x = 5;
function f () { 
  var x = 10;
}
function g () {
  return x;
}
g(); // 5
</pre>

In a dynamically scoped language, the definition of `x` from function `f` would be available to `g`, meaning the return value would be 10.



