from . import Route


# theory (?)

# a dependency on a local route is effectively an 'abstract' route
# the role is enforcing that you have a package that handles something
# but leaves it to you to define what that is


class LocalRoute(Route):

    def _uid(self):
        return None
        
    def __unicode__(self):
        return None


    def is_valid(self, identifier):
        return False
    
    def fetch(self, identifier):
        return None
