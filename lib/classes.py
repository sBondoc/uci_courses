class Department:
    def __init__(self,name = "empty_department"):
        self.name = name

class Course:
    def __init__(self,title = "",dept = Department(),num = 0,units = "",design = "",desc = "",prereq = []):
        self.name = str(dept.name) + " " + str(num)
        self.title = title
        self.dept = dept
        self.num = num
        self.units = units
        self.desc = desc
        self.design = design
        self.prereq = prereq

    def get_unit_min(self):
        return float(self.units[0:self.units.index("-")])

    def get_unit_max(self):
        str_buffer = self.units + " "
        return float(str_buffer[str_buffer.index("-") + 1:-1])

