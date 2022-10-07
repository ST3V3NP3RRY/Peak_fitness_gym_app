import unittest
from datetime import datetime
from models.session import Session
from models.activity import Activity
from models.member import Member


class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session()
