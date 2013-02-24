
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
  
  try:
    for c in components[1:]:
      retval = getattr(retval, c)
  except AttributeError:
    raise ImportError("cannot import name " + c)
  
  return retval


def get_fullname(object):
  """
  Returns the full name for the given object.  The object must
  define both the __name__ and __module__ attributes.
  """
  return "%s.%s" % (object.__module__, object.__name__)



def _defined_by(module):
  for name in dir(module):
    o = getattr(module, name)
    if hasattr(o, "__module__") and o.__module__ == module.__name__:
      yield name

def defined_by(module):
  """
  Returns the list of objects that were actually defined by the
  specified module.  In other words: this will not list the objects
  that were imported from other modules.
  """
  return list(_defined_by(module))

