from abc import ABC, abstractmethod

class CacheInterface(ABC):
    @abstractmethod
    def get(self, key):
        pass
    
    @abstractmethod
    def set(self, key, value):
        pass
    
    @abstractmethod
    def delete(self, key):
        pass

class DwinCache(CacheInterface):
    pass

def cache_decorator(func):
    def wrapper(self, key, *args, **kwargs):
        # Check if the key is already in the cache
        if key in self.cache:
            return self.cache[key]
        
        # If not, call the original method
        result = func(self, key, *args, **kwargs)
        
        # Store the result in the cache
        self.cache[key] = result
        
        return result
    
    return wrapper

class DwinCache(CacheInterface):
    def __init__(self):
        self.cache = {}
    
    @cache_decorator
    def get(self, key):
        # Implementation of the get method
    
    @cache_decorator
    def set(self, key, value):
        # Implementation of the set method
    
    @cache_decorator
    def delete(self, key):
        # Implementation of the delete method