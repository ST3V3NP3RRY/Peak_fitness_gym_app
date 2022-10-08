class Session:
    def __init__(
        self, member, activity, date_of_class, time_of_class, duration, id=None
    ):
        self.member = member
        self.activity = activity
        self.date_of_class = date_of_class
        self.time_of_class = time_of_class
        self.duration = duration
