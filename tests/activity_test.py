import unittest
from models.activity import Activity


class TestActivity(unittest.TestCase):
    def setUp(self):

        self.activity = Activity("Aerobics", "1200", 1)

    def test_activity_has_name(self):
        self.assertEqual("Aerobics", self.activity.name)

    def test_activity_has_start_time(self):
        self.assertEqual("1200", self.activity.start_time)

    def test_activity_has_id(self):
        self.assertEqual(1, self.activity.id)
