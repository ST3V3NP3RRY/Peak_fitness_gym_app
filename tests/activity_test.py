import unittest
from models.activity import Activity


class TestActivity(unittest.TestCase):
    def setUp(self):

        self.activity = Activity("Aerobics")

    def test_activity_has_name(self):
        self.assertEqual("Aerobics", self.activity.name)
