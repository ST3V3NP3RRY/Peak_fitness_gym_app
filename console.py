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

# MEMBERS
member1 = Member("Lucy Diamond", 45, "34 Carnaby Street, Shieldhill, G43 7RW")
member_repository.save(member1)

member2 = Member("Eleanor Rigby", 19, "78 Pike View, Stirling")
member_repository.save(member2)

member3 = Member("Maxwell Edison", 24, "FlatB, Wallaby Way, Falkirk, TH8 L9Y")
member_repository.save(member3)

member4 = Member("Jacob Mitchell", 48, "34 Johnstone Terrace, Linlithgow, QR7 TYZ")
member_repository.save(member4)

member5 = Member("Francis Lane", 22, "45 Claymore Drive, Alloa, GY5 78L")
member_repository.save(member5)

member6 = Member("Micheal Stewart", 53, "89 Johnstone Avenue, Kincardine, J8G YUH")
member_repository.save(member6)


activity1 = Activity("Aerobics", 1000, 30)
activity_repository.save(activity1)

activity2 = Activity("Spin Class", 1400, 30)
activity_repository.save(activity2)

activity3 = Activity("Keep Fit", 1600, 45)
activity_repository.save(activity3)

activity4 = Activity("Aqua Aerobics", 1000, 45)
activity_repository.save(activity4)

activity5 = Activity("Metafit", 1000, 45)
activity_repository.save(activity5)

# Session1 Aerobics --------------------------------------------------------
session1 = Session(member1, activity1, datetime.date(2022, 10, 14))
session_repository.save(session1)

session1 = Session(member2, activity1, datetime.date(2022, 10, 14))
session_repository.save(session1)

session1 = Session(member4, activity4, datetime.date(2022, 10, 14))
session_repository.save(session1)

# Session2 Spin Class --------------------------------------------------------
session2 = Session(member6, activity2, datetime.date(2022, 10, 14))
session_repository.save(session2)

session2 = Session(member3, activity2, datetime.date(2022, 10, 14))
session_repository.save(session2)

# Session3 --------------------------------------------------------
session3 = Session(member5, activity3, datetime.date(2022, 10, 14))
session_repository.save(session3)

session3 = Session(member4, activity3, datetime.date(2022, 10, 14))
session_repository.save(session3)

# Session 4 --------------------------------------------------------
session4 = Session(member4, activity4, datetime.date(2022, 10, 15))
session_repository.save(session4)

session4 = Session(member2, activity4, datetime.date(2022, 10, 15))
session_repository.save(session4)

session4 = Session(member6, activity2, datetime.date(2022, 10, 15))
session_repository.save(session4)

session4 = Session(member5, activity2, datetime.date(2022, 10, 15))
session_repository.save(session4)

# Session 4 --------------------------------------------------------
session5 = Session(member4, activity1, datetime.date(2022, 10, 17))
session_repository.save(session5)

session5 = Session(member2, activity2, datetime.date(2022, 10, 17))
session_repository.save(session5)

session5 = Session(member6, activity2, datetime.date(2022, 10, 17))
session_repository.save(session5)

# Session1 --------------------------------------------------------
session6 = Session(member4, activity4, datetime.date(2022, 10, 19))
session_repository.save(session6)

session6 = Session(member5, activity2, datetime.date(2022, 10, 19))
session_repository.save(session6)

session6 = Session(member1, activity3, datetime.date(2022, 10, 19))
session_repository.save(session6)

session6 = Session(member2, activity2, datetime.date(2022, 10, 19))
session_repository.save(session6)


# Session 4 --------------------------------------------------------
session7 = Session(member6, activity3, datetime.date(2022, 10, 20))
session_repository.save(session7)

session7 = Session(member1, activity2, datetime.date(2022, 10, 20))
session_repository.save(session7)

session7 = Session(member2, activity2, datetime.date(2022, 10, 20))
session_repository.save(session7)

session7 = Session(member4, activity1, datetime.date(2022, 10, 20))
session_repository.save(session7)
