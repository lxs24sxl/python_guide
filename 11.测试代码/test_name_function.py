import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
  """测试name_function.py"""

  def test_first_last_name(self):
    """测试能否正确地处理Janis Joplin这样的姓名"""
    formatted_name = get_formatted_name("Janis", "Joplin")
    self.assertEqual(formatted_name, "Janis Joplin")
  def test_first_last_middle_name(self):
    formatted_name = get_formatted_name("Wolfgang","Mozart", "Amadeus")
    self.assertNotEqual(formatted_name, "Wolfgang Amadeus Mozart")

unittest.main()