import pdb

# import models to use classes
from models.session import Session
from models.member import Member
from models.activity import Activity

# import repositories to use the functions
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository
import datetime

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

activity1 = Activity("Aerobics", 1400, 45)
activity_repository.save(activity1)

activity2 = Activity("Spin Class", 1330, 30)
activity_repository.save(activity2)

activity3 = Activity("Gym Session", 1000, 45)
activity_repository.save(activity3)

session1 = Session(member1, activity2, datetime.date(2022, 10, 7))
session_repository.save(session1)

session2 = Session(member3, activity1, datetime.date(2022, 10, 9))
session_repository.save(session2)

session3 = Session(member2, activity3, datetime.date(2022, 10, 10))
session_repository.save(session3)

session4 = Session(member2, activity1, datetime.date(2022, 10, 7))
session_repository.save(session4)

session1 = Session(member2, activity2, datetime.date(2022, 10, 7))
session_repository.save(session1)


active = member_repository.activities(session4)

activity_session = session_repository.activity(session1)
members_session = session_repository.member(session2)
