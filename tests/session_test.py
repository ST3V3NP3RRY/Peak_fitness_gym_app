import unittest
from datetime import datetime
from models.session import Session
from models.member import Member
from models.activity import Activity


class TestSession(unittest.TestCase):
    def setUp(self):

        self.member = Member("John Harris", 35, "Ferry Road")
        self.activity = Activity("Cycling", 1200, 45)
        self.session = Session(self.member, self.activity, datetime.date(2022, 10, 7))

    def test_session_has_member(self):
        self.assertEqual(("John Harris", 35, "Ferry Road"), self.session.member)
