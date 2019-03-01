from html.parser import HTMLParser
from classes import *
import urllib.request

### CONST ###

catalogue_url = "http://catalogue.uci.edu/allcourses/"
departments_start = "A"
departments_stop = "footer"
department_marker = "/allcourses/"
courses_start = "//]]>"
courses_stop = "UC Regents"
course_stop = "Units.  "

### VARS ###

lst_departments_raw = []
lst_departments = [] ## Final department list product
lst_courses_raw = []
lst_courses = [] ## Final course list product

### PARSE ###

class DepartmentParserHTML(HTMLParser): ## HTML parser for department list page
    def handle_starttag(self,tag,attrs):
        if attrs != []:
            lst_departments_raw.append(attrs[0][1])

class CourseParserHTML(HTMLParser): ## HTML parser for courses on individual department pages
    def handle_data(self,data):
        if data.isspace() == False:
            lst_courses_raw.append(str(data))

def substring_index(sub,lst): ## Gets index of first character of first instance of a substring found in a list of strings
    indicies = [i for i, s in enumerate(lst) if sub in s]
    return indicies[0]

def parse_page(link,parser): ## Uses selected predefined HTML parser to generate a list of string values
    response = urllib.request.urlopen(link)
    data = response.read()
    text = data.decode(encoding = "utf-8")
    response.close()
    parser.feed(text)

### EXEC ###

parse_page(catalogue_url,DepartmentParserHTML())
lst_departments_raw = lst_departments_raw[substring_index(departments_start,lst_departments_raw) + 1:substring_index(departments_stop,lst_departments_raw)] ##

for i in range(len(lst_departments_raw)): ## Processes raw department data and generates department list
    if lst_departments_raw[i].startswith(department_marker):
        lst_departments.append(Department(lst_departments_raw[i][len(department_marker):-1]))

for i in range(len(lst_departments)): ## Generates course list 
    parse_page(catalogue_url + lst_departments[i].name,CourseParserHTML())
    lst_courses_raw = lst_courses_raw[substring_index(courses_start,lst_courses_raw):substring_index(courses_stop,lst_courses_raw)]
    str_dpt = lst_departments[i].name.replace("_"," ")
    str_dpt = str_dpt.upper()
    str_dpt = str_dpt.replace(" ","\xa0")
    department = Department(str_dpt)
    course = Course()
    print("Generating " + department.name + " courses...")
    for j in range(len(lst_courses_raw)): ## Processes raw course data
        if lst_courses_raw[j].startswith(str_dpt) and lst_courses_raw[j].endswith(course_stop): ## Marks start of new course and gets basic properties
            if course != Course():
                lst_courses.append(course) ## Appends processed course to list
                course = Course() ## Resets course variable to new course to be appended
            
            course_raw = lst_courses_raw[j].split(sep = "  ")
            course.dept = department
            course.num = course_raw[0][len(department.name) + 1:-2]
            course.name = course.dept.name + " " + course.num
            course.title = course_raw[1][0:-1]
            course.units = course_raw[2][0:-len(" Units.")]
