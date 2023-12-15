def cachable(cache, key):
    def decorator(func):
        def wrapper(*args, **kargs):
            if key not in cache:
                cache[key] = func(*args, **kargs)

            return cache[key]

        return wrapper

    return decorator

def self_cachable():
    def decorator(func):
        def wrapper(self, *args, **kargs):
            return cachable(self.cache, func.__name__ + type(self).__name__ + "".join(args) + "".join(kargs))(func)( self, *args, **kargs)

        return wrapper

    return decorator

class PageObject:
    def __init__(self, driver_manager):
        self.cache = {}
        self.driver_manager = driver_manager
        self.xpath = {}

    def invalidate(self):
        self.cache = {}
#   Getters

#   Actions

#   Methods

