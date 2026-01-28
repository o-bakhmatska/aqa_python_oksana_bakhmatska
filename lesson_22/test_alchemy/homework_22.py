from faker import Faker
import random
from lesson_22.test_alchemy.db import Base, engine, SessionLocal
from sqlalchemy import select
from lesson_22.db_tables.courses import Course
from lesson_22.db_tables.relations_students_courses import Enrollment
from lesson_22.db_tables.students import Student

fake = Faker("uk_UA")

COURSES = [
    ("Python", "Python Basics"),
    ("SQL", "Data Bases, SQL"),
    ("Web", "Web-development"),
    ("JavaScript", "Front-end Full Stack"),
    ("English", "English Intermediate"),
]

def seed_courses(session):
    exists = session.execute(select(Course)).scalars().first()
    if exists:
        return

    for title, desc in COURSES:
        session.add(Course(title=title, description=desc))
    session.commit()

def seed_students(session, n=20):
    courses = session.execute(select(Course)).scalars().all()
    if not courses:
        raise RuntimeError("No courses. Create courses at first")
    for _ in range(n):
        name = fake.name()
        student = Student(name=name)

        k = random.randint(1, min(3, len(courses)))
        student.courses = random.sample(courses, k)

        session.add(student)
    session.commit()


Base.metadata.create_all(bind=engine)

session = SessionLocal()
seed_courses(session)
seed_students(session, 20)
session.close()

def add_student_and_enroll(session, name, course_title):
    course = session.execute(select(Course).where(Course.title == course_title)).scalars().first()
    if not course:
        raise ValueError(f"Course '{course_title}' is not found")
    student = Student(name=name)
    student.courses.append(course)
    session.add(student)

def get_students_by_course(session, course_title):
    course = session.execute(select(Course).where(Course.title == course_title)).scalars().first()
    if not course:
        return []
    return course.students

def get_courses_by_student(session, student_name):
    student = session.execute(select(Student).where(Student.name == student_name)).scalars().first()
    if not student:
        return []
    return student.courses



new_name = fake.name()
added = add_student_and_enroll(session, new_name, "JavaScript")
print("Added:", new_name)

students = get_students_by_course(session, "Python")
print("\nStudents in course 'Python':")
for s in students[:10]:
    print(" -", s.name)


courses = get_courses_by_student(session, new_name)
print(f"\nCourses of student:")
for c in courses:
    print(" -", c.title)



