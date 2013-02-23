fqn
==================

The acronym "fqn" stands for "Fully-Qualified Names".  While
using this library, please be sure to make liberal use of
exclamations, such as "This is a good fqn library!"

Usage
==================

The main purpose of this library is to allow for objects to
be retrieved from Python modules without polluting the current
namespace.  Consider the following example:

    from library import BaseClass1, BaseClass2
    
    class MyClass1(BaseClass1):
      def __init__(self):
        ...
    
    class MyClass2(BaseClass2):
      def __init__(self):
        ...

Looks reasonable, right?  Sure, but what happens if a developer runs the 'dir' command against your module?  Answer: they'll discover that your module contains *4* classes.  How are people supposed to know which classes were actually defined by your module, and which classes were imported from elsewhere?

Enter 'fqn.get\_object`.  'fqn.get\_object' allows you to access objects from other modules without
importing the object into the current namespace.  For instance:

    import fqn
    
    class MyClass1(fqn.get_object('library.BaseClass1')):
      def __init__(self):
        ...
    
    class MyClass2(fqn.get_object('library.BaseClass2')):
      def __init__(self):
        ...

Notice that we're no longer importing BaseClass1 and BaseClass2.  Instead, we're only referencing them
while MyClass1 and MyClass2 are being defined.  Once we have finished defining our classes, these
references to the base classes go out of scope.  As a result, the references do not pollute our module's
namespace.

