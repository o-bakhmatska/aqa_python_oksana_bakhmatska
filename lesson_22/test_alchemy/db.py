from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
DATABASE_URL = "sqlite:///C:/Users/OKSANA/PycharmProjects/aqa_python_oksana_bakhmatska/lesson_22/test_alchemy/homework_22.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()