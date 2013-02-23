
def get_object(fullname):
  """
  This function retrieves a specific object from a module
  without polluting the current namespace.
  
    q = get_object("foo.bar.quux")
    
  is equivalent to:
  
    from foo.bar import quux as q
    
  """
  components = fullname.split(".")
  try:
    retval = __import__(fullname, level = 0)
  except ImportError:
    retval = __import__(".".join(components[:-1]), level = 0)
  
  for c in components[1:]:
    retval = getattr(retval, c)
  
  return retval


def get_fullname(object):
  """
  Returns the full name for the given object.  The object must
  define both the __name__ and __module__ attributes.
  """
  return "%s.%s" % (object.__module__, object.__name__)