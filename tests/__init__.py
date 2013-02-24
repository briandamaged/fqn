from fqn import get_object

from unittest import TestCase

import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "..", "fake_modules")))


class Test_get_object(TestCase):
  def test_it_raises_an_ImportError_when_the_object_does_not_exist(self):
    self.assertRaises(ImportError, get_object, "foo.oops")

  def test_it_returns_the_module_when_given_a_name_with_one_component(self):
    obj = get_object("foo")
    import foo
    self.assertEqual(id(obj), id(foo))

  def test_it_returns_the_module_when_given_a_module_name_with_multiple_components(self):
    obj = get_object("foo.bar.core")
    import foo.bar.core
    self.assertEqual(id(obj), id(foo.bar.core))

  def test_it_can_return_objects_belonging_to_a_module(self):
    obj = get_object("foo.bar.core.Bar")
    from foo.bar.core import Bar
    self.assertEqual(id(obj), id(Bar))

  def test_it_can_crawl_through_multiple_objects(self):
    obj = get_object("foo.bar.core.Bar.method")
    from foo.bar.core import Bar
    
    # Hmm.  It appears that calling getattr(...) to obtain a
    # class method returns a new instance of the method each
    # time.  So, we need to do an equivalence check rather
    # than a sameness check.
    self.assertEqual(obj, Bar.method)

  def test_it_can_return_objects_that_were_imported_from_other_modules(self):
    # foo.quux imports Bar from foo.bar.core
    obj = get_object("foo.quux.Bar")
    
    from foo.bar.core import Bar
    self.assertEqual(id(obj), id(Bar))