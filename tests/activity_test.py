import unittest
from models.activity import Activity


class TestActivity(unittest.TestCase):
    def setUp(self):

        self.activity = Activity("Aerobics", "Body Pump", 1)

    def Test_activity_has_name(self):
        self.assertEqual("Aerobics", self.activity.name)

    def Test_activity_has_title(self):
        self.assertEqual("Body Pump", self.activity.title)

    def Test_activity_has_id(self):
        self.assertEqual(1, self.activity.id)
