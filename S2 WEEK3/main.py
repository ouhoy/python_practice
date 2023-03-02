from student import Student
from lecturer import Lecturer
from program import Program
from course import Course
from school import School

student_one = Student("Abdallah", "Dahmou", 23)
student_two = Student("Rania", "Samih", 22)

quality_software = Course("Developing Quality Software and Systems", 30, "Building high-quality software systems.")
web_development = Course("Web development", 25, "Building web applications with NodeJS and ReactJS.")

lecturer_one = Lecturer("Younes", "El Amrani", [quality_software])

SE = Program("Software Engineering", [quality_software, web_development], [student_one])
BA = Program("Business Management", [quality_software], [student_two])

SIST = School("SIST", "School of software engineering and business", [SE, BA])


# List enrolled students
def enrolled_students(program):
    for num, student in enumerate(program):
        first_name = student.get_fullname()["firstname"]
        last_name = student.get_fullname()["lastname"]

        print(f"{num + 1} - {first_name} {last_name}")


enrolled_students(SE.get_students())
