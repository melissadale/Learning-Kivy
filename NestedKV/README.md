**Problem**: 
When nesting KV files, the style components transfered, however the python code did not want to link up. 

**Almost Asked Question**

I want to prevent a massive God Class scenario for my kv files, so I am attempting to break my tabbed panels into separate kv files. I am able to transfer the styles successfully, however I am having difficulty connecting to the python components. 

I've created a simple demo below to illustrate the issue I'm running into. When the button is pressed, I get a `AttributeError: 'Foo' object has no attribute 'hello'` error. 

Attempted:
* Changing locations of the `Builder.load_file('stylesheets/PanelOne.kv')`


**Stopped editing question when figured out the solution**
