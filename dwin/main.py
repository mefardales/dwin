from _modules import cache_decorator, DwinCache

# Initialize the cache with a custom expiration time (in seconds)
cache = DwinCache(db_path='path/to/your/cache.db', expire_after=1800)

@cache_decorator
def getProjects(request):
    # Add request to external API
    pass

def getProjects(request):
    # Add an indented block of code here
    pass
    