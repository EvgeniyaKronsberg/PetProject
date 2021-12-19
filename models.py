from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql.schema import ForeignKey

from db import Base, engine


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True)
    password = Column(String)
    name = Column(String)

    def __repr__(self):
        return f'<User id = {self.id}, user_name = {self.user_name}>'
        

class Good(Base):
    __tablename__ = 'good'
    id = Column(Integer, primary_key=True)
    producer = Column(String)
    model = Column(String)

    def __repr__(self):
        return f'<Good id = {self.id}, producer = {self.producer}, model = {self.model}>'


class Store(Base):
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'<Store id = {self.id}, name = {self.name}>'


class Search(Base):
    __tablename__ = 'search'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    good_id = Column(Integer, ForeignKey('good.id'))
    search_date = Column(DateTime)

    def __repr__(self):
        return f'<Search id = {self.id}, user_id = {self.user_id}, good_id = {self.good_id}, search_date = {self.search_date}>'


class Find(Base):
    __tablename__ = 'find'
    id = Column(Integer, primary_key=True)
    search_id = Column(Integer, ForeignKey('search.id'))    
    find_date = Column(DateTime)
    store_id = Column(Integer, ForeignKey('store.id'))
    price = Column(Float)
    stock = Column(Integer)

    def __repr__(self):
        return f'<Find id = {self.id}, search_id = {self.search_id}, find_date = {self.find_date}, store_id = {self.store_id}>'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
        