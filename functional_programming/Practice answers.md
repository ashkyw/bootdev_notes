CH8 - L3:

```py
def configure_plugin_decorator(func):
    def wrapper(*args):
        dict_args = dict(args)
        return func(**dict_args)
    return wrapper
```
