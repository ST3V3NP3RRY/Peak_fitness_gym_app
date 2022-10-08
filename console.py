import pdb

# import models to use classes
from models.session import Session
from models.member import Member
from models.activity import Activity

# import repositories to use the functions
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

# Empty out data from db
session_repository.delete_all()
activity_repository.delete_all()
member_repository.delete_all()

member1 = Member("Lucy Diamond", 45, "Carnaby Street")
member_repository.save(member1)

member2 = Member("Eleanor Rigby", 19, "Liverpool Road")
member_repository.save(member2)

member3 = Member("Maxwell Edison", 24, "Wallaby Way")
member_repository.save(member3)

activity1 = Activity("Body Blast", "Aerobic")
activity_repository.save(activity1)

activity2 = Activity("Spin Attack", "Cycling")
activity_repository.save(activity2)

activity3 = Activity("Lane swim", "Swimming")
activity_repository.save(activity3)

session1 = Session(member1, activity2, 2022107, 1400, 60)
session_repository.save(session1)

session2 = Session(member3, activity1, 2022107, 1800, 45)
session_repository.save(session2)

session3 = Session(member2, activity3, 2022107, 1000, 30)
session_repository.save(session3)

session4 = Session(member2, activity1, 2022109, 1730, 45)
session_repository.save(session4)

active = member_repository.activity(session4)

activity_session = session_repository.activity(session1)
members_session = session_repository.member(session2)


print(members_session.id)
print(activity_session.title)
