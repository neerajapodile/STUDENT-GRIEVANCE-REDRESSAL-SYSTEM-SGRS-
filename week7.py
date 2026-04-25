class Record:

    def __init__(self, date):
        self.date = date

class Grievance(Record):

    def __init__(self, date, gid, issue):
        super().__init__(date)
        self.gid = gid
        self.issue = issue

    def show(self):
        print("Date :", self.date)
        print("Grievance ID :", self.gid)
        print("Issue :", self.issue)

g1 = Grievance("25-04-2026", "G101", "Hostel Food")

g1.show()
