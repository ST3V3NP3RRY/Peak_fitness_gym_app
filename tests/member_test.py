import unittest
from models.member import Member


class TestMember(unittest.TestCase):
    def setUp(self):

        self.member = Member("Felix Kay", 1)

    def test_member_has_name(self):
        self.assertEqual("Felix Kay", self.member.name)

    def test_member_has_id(self):
        self.assertEqual(1, self.member.id)
