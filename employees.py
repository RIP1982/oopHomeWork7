from people import People


class Employees(People):
    def __init__(self, constant_number, last_name, name, birthday, department):
        super().__init__(last_name, name, birthday)
        self.constant_number = constant_number
        self.department = department

    def constant_number(self):
        return self.constant_number

    def get_last_name(self):
        return self.last_name

    def get_name(self):
        return self.name

    def get_birthday(self):
        return self.birthday

    def get_department(self):
        return self.department

    def __str__(self):
        return ("constant_number: " + str(self.constant_number) + ", " + "last_name: " + self.last_name +
                ", " + "name: " + self.name + ", " + "birthday: " + str(self.birthday) + ", " +
                "department: " + self.department)




