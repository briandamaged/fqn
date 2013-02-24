
from fqn import get_object

from unittest import TestCase


class Test_get_object(TestCase):
  def test_it_raises_an_ImportError_when_the_object_does_not_exist(self):
    self.assertRaises(ImportError, get_object, "sys.oops")
