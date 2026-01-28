from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lesson_22.test_alchemy.db import Base
from lesson_22.db_tables.relations_students_courses import Enrollment


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)

    students = relationship(
        "Student",
        secondary=Enrollment.__table__,
        back_populates="courses",
    )
