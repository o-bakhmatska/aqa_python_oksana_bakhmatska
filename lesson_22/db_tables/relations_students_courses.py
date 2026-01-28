from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from lesson_22.test_alchemy.db import Base


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint("student_id", "course_id", name="uq_student_course"),
    )