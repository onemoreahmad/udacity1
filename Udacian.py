class Udacian():

    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status

    def print_udacian(self):

        return self.name + " is enrolled in " + self.city + " studying " + self.nanodegree + " in " + self.enrollment[0] + " " + self.enrollment[1] + " with " + self.enrollment[2]

Msg= Udacian('Ahmad', 'Riyadh', ('Sat', 'AM', 'MS. Lujain'), 'FSND', 'Ontrack')

print(Msg.print_udacian())
