import pdb

# import models to use classes
from models.session import Session
from models.member import Member
from models.activity import Activity
from models.booking import Booking

# import repositories to use the functions
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository
import repositories.booking_repository as booking_repository
import datetime

# Empty out data from db
booking_repository.delete_all()
session_repository.delete_all()
activity_repository.delete_all()
member_repository.delete_all()

# -------------
# ACTIVITIES
# -------------
member1 = Member("Lucy Diamond", 45, "34 Carnaby Street, Linlithgow, KU5 7GD")
member_repository.save(member1)

member2 = Member("Eleanor Rigby", 19, "78 Pike View, Cumbernauld, YH7 9GD")
member_repository.save(member2)

member3 = Member("Max Edison", 24, "45 Accacia Avenue, Falkirk, GT6 9YH ")
member_repository.save(member3)

member4 = Member("James Doherty", 34, "12 Johnstone Place, Stirling, DF6 8GD")
member_repository.save(member4)

member5 = Member("Alison Killbie", 55, "67 Albert Drive, Alloa, FTH 7PF")
member_repository.save(member5)

member6 = Member("George Lennie", 19, "78 George Street, Bannockburn, HJ7 8KL")
member_repository.save(member6)

# -------------
# ACTIVITIES
# -------------

activity1 = Activity("Aerobics")
activity_repository.save(activity1)

activity2 = Activity("Metafit")
activity_repository.save(activity2)

activity3 = Activity("Keep fit")
activity_repository.save(activity3)

activity4 = Activity("Gymnastics")
activity_repository.save(activity4)

activity5 = Activity("Swimming")
activity_repository.save(activity5)

activity6 = Activity("Grit Cardio")
activity_repository.save(activity6)

activity7 = Activity("Gym Circuits")
activity_repository.save(activity7)

# -------------
# SESSIONS
# -------------

session1 = Session(1000, 45, activity1)
session_repository.save(session1)

session2 = Session(1130, 30, activity2)
session_repository.save(session2)

session3 = Session(1200, 35, activity3)
session_repository.save(session3)

session4 = Session(1300, 45, activity4)
session_repository.save(session4)

session5 = Session(1330, 40, activity1)
session_repository.save(session5)

session6 = Session(1300, 45, activity3)
session_repository.save(session6)

session7 = Session(1330, 40, activity5)
session_repository.save(session7)

session8 = Session(1445, 50, activity6)
session_repository.save(session8)

session9 = Session(1530, 60, activity4)
session_repository.save(session9)

session10 = Session(1630, 35, activity5)
session_repository.save(session10)

# -------------
# BOOKINGS
# -------------

booking1 = Booking(member1, session2)
booking_repository.save(booking1)

booking2 = Booking(member2, session2)
booking_repository.save(booking1)

booking3 = Booking(member2, session1)
booking_repository.save(booking3)


# WORKING
# all_activities = activity_repository.select_all()
# for activity in all_activities:
#     print(activity.name)

# WORKING
# all_members = member_repository.select_all()
# for member in all_members:
#     print(member.name)

all_sessions = session_repository.select_all()

for session in all_sessions:
    print(session.activity.name)
