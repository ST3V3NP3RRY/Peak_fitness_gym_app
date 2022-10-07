class Session:
    def __init__(self, member, activity, date, time, duration, id=None):
        self.member = member
        self.activity = activity
        self.date = date
        self.time = time
        self.duration = duration
