from student import Student
from lecturer import Lecturer
from program import Program
from course import Course

student_one = Student("Abdallah", "Dahmou", 23)
student_two = Student("Rania", "Samih", 22)

quality_software = Course("Developing Quality Software and Systems", 30, "Building high-quality software systems.")
web_development = Course("Web development", 25, "Building web applications with NodeJS and ReactJS.")

lecturer_one = Lecturer("Younes", "El Amrani", [quality_software])

SE = Program("Software Engineering", [quality_software, web_development], [student_one])
BA = Program("Business Management", [quality_software], [student_two])

# List enrolled software engineering students
for num, student in enumerate(SE.get_students()):
    first_name = student.get_fullname()["firstname"]
    last_name = student.get_fullname()["lastname"]

    print(f"{num + 1} - {first_name} {last_name}")
