import unittest
from models.member import Member


class TestMember(unittest.TestCase):
    def setUp(self):

        self.member = Member("Felix Kay", 45, "12 Carnaby Street", 1)

    def test_member_has_name(self):
        self.assertEqual("Felix Kay", self.member.name)

    def test_member_has_age(self):
        self.assertEqual(45, self.member.age)

    def test_member_has_address(self):
        self.assertEqual("12 Carnaby Street", self.member.address)

    def test_member_has_id(self):
        self.assertEqual(1, self.member.id)
