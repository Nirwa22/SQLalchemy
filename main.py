from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = "People"
    SSN = Column("SSN", Integer, primary_key=True)
    Firstname = Column("Firstname", String)
    Lastname = Column("Lastname", String)
    Age = Column("Age", Integer)
    Gender = Column("Gender", CHAR)

    def __init__(self, ssn, first, last, age, gender):
        self.SSN = ssn
        self.Firstname = first
        self.Lastname = last
        self.Age = age
        self.Gender = gender

    def __repr__(self):
        return f"({self.Firstname} {self.Lastname} {self.SSN} {self.Age} {self.Gender})"


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

P1 = Person(45278, "Fatima", "Gul", 25, "f")
P2 = Person(45619, "Fatima", "Rashid", 22, "f")
P3 = Person(27398, "Ali", "Gul", 21, "m")
P4 = Person(10976, "Alina", "Gul", 29, "f")
P5 = Person(28465, "Haris", "Rashid", 35, "m")
P6 = Person(89453, "Sarah", "Gul", 30, "f")

session.add(P1)
session.add(P2)
session.add(P3)
session.add(P4)
session.add(P5)
session.add(P6)
session.commit()