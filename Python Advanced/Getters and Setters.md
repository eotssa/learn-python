That's totally understandable! The syntax for using `property` decorators is a bit unique, especially if you're coming from a programming language that handles getters and setters differently. Let's dig deeper into what's happening behind the scenes.

### @property Decorator

1. **`@property`**: This is a built-in decorator in Python that turns a method into a "getter" for a read-only property. When you decorate a method with `@property`, you're telling Python that this method can be accessed like an attribute, without parentheses.

   ```python
   @property
   def money(self):
       return self.__money
   ```

   Here, `money` becomes a read-only property. If you try to access `wallet.money`, it will call the `money` method and return `self.__money`.

2. **`.setter` Decorator**: After defining a property with `@property`, you can further define a setter for that property using the `.setter` decorator. It must have the same name as the property.

   ```python
   @money.setter
   def money(self, money):
       if money >= 0:
           self.__money = money
       else:
           raise ValueError("The amount must not be below zero")
   ```

   Here, `@money.setter` tells Python that this method is a setter for the `money` property. When you try to assign a value to `wallet.money`, it will call this method with the value you're assigning.


-  The getter method, i.e. the @property decorator, must be introduced before the setter method, or there will be an error when the class is executed. This is because the @property decorator defines the name of the "attribute" offered to the client. The setter method, added with .setter, simply adds a new functionality to it.
### `ValueError`
**- When a value supplied is clearly wrong, it is usually a good idea to raise an exception and thus let the client know. In this case the exception should probably be of type ValueError to signify that the value supplied was unacceptable.**
### Behind the Scenes

- When you define a method with the `@property` decorator, it's stored as a "getter" for a property with the same name as the method.
- When you access the property (e.g., `wallet.money`), Python calls the getter method for that property and returns its value.
- When you define a method with the `.setter` decorator (after defining a corresponding `@property`), it's stored as a "setter" for that property.
- When you assign a value to the property (e.g., `wallet.money = 50`), Python calls the setter method for that property with the assigned value.
- You can add logic inside the getter and setter methods, like validation or computation. The client code that uses the object doesn't see this logic; it interacts with the properties as if they were regular attributes.

This approach encapsulates the details of how the properties are accessed and modified, allowing you to change the implementation without affecting the code that uses the object. It also provides a more idiomatic and elegant interface, letting you interact with methods as if they were attributes.

It's perfectly normal to find this syntax unfamiliar at first. As you work with it more, it will likely become more intuitive. It's a powerful feature that adds to the expressiveness and flexibility of Python's object-oriented programming model.