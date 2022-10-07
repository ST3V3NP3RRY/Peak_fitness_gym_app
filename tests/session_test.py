import unittest
from datetime import datetime
from models.session import Session
from models.member import Member
from models.activity import Activity


class TestSession(unittest.TestCase):
    def setUp(self):

        self.member = Member("John Harris", 2)
        self.activity = Activity("Cycling", "Spin-it to win it", 3)
        self.session = Session(
            self.member, self.activity, datetime.date(2022, 10, 7), 1400, 60
        )

    def Test_session_has_member(self):
        self.assertEqual(("John Harris", 2), self.session.member)
