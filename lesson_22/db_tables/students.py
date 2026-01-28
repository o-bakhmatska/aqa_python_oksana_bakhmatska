from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lesson_22.test_alchemy.db import Base
from lesson_22.db_tables.relations_students_courses import Enrollment


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    courses = relationship(
        "Course",
        secondary=Enrollment.__table__,
        back_populates="students",
    )
