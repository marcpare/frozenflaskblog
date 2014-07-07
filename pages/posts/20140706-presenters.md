
Presenters in Python
===

Presenters [1] are a nice way to rip rendering logic out of models that we can use  in nearly any Python web framework: Django, Flask, Pylons, and more.

In a simple application, it's easy enough to put view-specific code directly in a Model.

    class PartAttribute
      def render(self):
        if self.unit == 'inches':
          return self.value + '"'
        else:
          return self.value

But you may end up with another model that wants to share this same logic:

[image from mcmaster]

    class Filter
      def render(self):
        # render the same way...            

We can just pull out this rendering logic into a new object and mix it into out desired model classes.

      class DimensionedRender:
          def render(self)
            # ...
    
      class PartAttribute(DimensionedRender):
        # ...
      
      class Filter(DimensionedRender):
        # ...

This is basically the technique implemented by the Ruby [Draper](https://github.com/drapergem/draper) gem and described in [this blog post](http://www.bignerdranch.com/blog/creating-view-centric-interfaces-with-the-decorator-pattern/).

But this hurts because it's a flagrant violation of the Single Responsibility Principle (SRP). Why should the model care about how it's rendered?

Another variation is to take advantage of duck typing, defining a Presenter as a function that takes any object with a `unit` and `value` field.

    # presenters.py
    def dimensioned_value(obj):
        if obj.unit == 'inches':
          return obj.value + '"'
        else:
          return obj.value

We pass the Presenter to the template and invoke it when we need to render something:

    # Controller
    def show(self):
      c.presenter = presenters.dimensioned_value
      return render('show.html', c)
      
    # Template show.html
    ...
    ${c.presenter(filter)}
    ${c.presenter(part.attribute['diameter'])}

This sets us up to do something pretty awesome: we can swap out our rendering code on the fly. And we don't have to touch the models to do it!

    
    # presenters.py
    def dimensioned_value(obj):
      # same as before...
    
    def metric_value(obj):
        if obj.unit == 'meters':
          return obj.value + 'm'
        else:
          return obj.value
          
    value_presenters = {
      'english': dimensioned_value,
      'metric': metric_value
    }

    
    # controller.py
    def show(self):
      c.presenter = presenters.value_presenters[user.favorite_unit_system]
      return render('show.html')

This is a great example of why the Single Responsibility Principle usually leads us down the right road. When the models had the responsibility of rendering, the code became tangled as soon as we wanted to expand the rendering capabilities of our app. Splitting this code out into an object (or, in this case, a function) with this single responsibility allowed us to specify only exactly what changed.

[1] A note on terminology. You can call what I'm describing below a "View", "View Model", or "Presenter". I use "Presenter" because, to me, it seems to emphasize best what's going on and avoids the heavily overloaded term "View".








    
    def metal_widget_presenter(obj):
      # ...
    
    def widget_presenter(obj):
      # ...
    
    config.value_presenter = {
      'MetalWidget': metal_widget_presenter
      'Widget': widget_presenter
    }
    
    config.get_value_presenter(obj):
      return config.value_presenter(obj.__class__.__name__)













Consider this future scenario: we want to implement the rendering routine in metric units instead of English units.

We could specify this in a global config, but that really starts to smell...

    class DimensionedRender:
        def render(self)
          if config.unitType == 'metric'
            ...
          elif config.unitType == 'english'
            ...

No, we would prefer to be able to swap out the `DimensionedRender` for `MetricDimensionedRender` somehow.






Another situation: what if the rendering routine needs to be slightly different for the Filter class?

Rendering logic really doesn't belong in a model. What happens if you want to implement different types of user interfaces? (HTML, mobile, audio!) What happens if multiple models should be rendered identically?





As applications grow, it's common to find that the representation of objects in a database steadily diverges from what you show on the screen. That is, you find that add more transformations to data over time.

For example, you start with a simple user interface in HTML. Then, you decide to implement an interface for mobile phone. Then an audio-based interface. The data in the database stays the same, but you've got now three different ways to present it.

[diagram?]

Another situation is to find different objects that share presentation logic. You don't want to 

 it's almost guaranteed that the representation of an object in the database won't match exactly what you want to display. Furthermore, you'll find that you want to display multiple different objects using the same API.



