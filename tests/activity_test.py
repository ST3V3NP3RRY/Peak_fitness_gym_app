import unittest
from models.activity import Activity


class TestActivity(unittest.TestCase):
    def setUp(self):
        self.activity = Activity("Body Pump", "Aerobics", 1)

    def Test_activity_has_name(self):
        self.assertEqual("Body Pump", self.activity.name)

    def Test_activity_has_type(self):
        self.assertEqual("Aerobics", self.activity.type)
