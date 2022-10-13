import unittest
from models.session import Session
from models.activity import Activity


class TestSession(unittest.TestCase):
    def setUp(self):

        self.activity = Activity("Cycling")
        self.session = Session(1200, 45, self.activity, 1)

    def test_session_has_start_time(self):
        self.assertEqual(1200, self.session.time)

    def test_session_has_duration(self):
        self.assertEqual(45, self.session.duration)

    def test_session_has_duration(self):
        self.assertEqual("Cycling", self.session.activity.name)

    def test_session_has_id(self):
        self.assertEqual(1, self.session.id)
