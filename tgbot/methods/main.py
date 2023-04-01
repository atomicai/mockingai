from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declared_attr, sessionmaker
db_url = ''

engine = create_engine(db_url, echo=False)

session = sessionmaker(bind=engine)()


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, autoincrement=True)


class User(Base):
    tg_id = Column(Integer, primary_key=True, )
    group = Column(String(5))
    subgroup = Column(Integer, default=1)
    role = Column(Integer, default=0)  # 0- студент, 1 - редактор, 2 - староста, 3 - учитель, 4 - руководство
    name = Column(String(60), default='0')
    social_credit = Column(Integer, default=0)


class Homework(Base):
    deadline = Column(Date)
    group = Column(String(5))
    subgroup = Column(Integer)
    lesson = Column(String(30))
    text = Column(String)
    images = Column(String, default='')
    users_completed = Column(String, default='-1,')

    def is_complete(self, user_id: int):
        completed_list = self.users_completed.split(",")
        if str(user_id) in completed_list:
            return True
        return False

    def is_completed(self, user_id: int):
        self.users_completed += f"{str(user_id)},"


class Schedule(Base):
    week = Column(Integer)
    day = Column(Integer)
    group = Column(String(5))
    subgroup = Column(Integer)
    para = Column(Integer)
    lesson = Column(String(30))
    teacher = Column(String, default='0')
    cabinet = Column(String, default='0')


class DefaultSchedule(Base):
    week = Column(Integer)
    day = Column(Integer)
    group = Column(String(5))
    subgroup = Column(Integer)
    para = Column(Integer)
    lesson = Column(String(30))
    teacher = Column(String, default='0')
    cabinet = Column(String, default='0')




