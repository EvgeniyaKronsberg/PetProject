from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql.schema import ForeignKey

from webapp.db import Base, engine


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    password_hash = Column(String)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)

    def __str__(self):
        return f'<User id: {self.id}, login: {self.login}, name: {self.name}, email: {self.email}, phone_number: {self.phone_number}>'

    
class Good(Base):
    __tablename__ = 'good'
    id = Column(Integer, primary_key=True)
    producer = Column(String)
    model = Column(String)
    category = Column(String)

    def __str__(self):
        return f'<Good id: {self.id}, producer: {self.producer}, model: {self.model}, category: {self.category}>'


class Store(Base):
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)

    def __str__(self):
        return f'<Store id: {self.id}, name: {self.name}, url: {self.url}>'


class Search(Base):
    __tablename__ = 'search'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    good_id = Column(Integer, ForeignKey('good.id'))
    search_date = Column(DateTime)

    def __str__(self):
        return f'<Search id: {self.id}, user_id: {self.user_id}, good_id: {self.good_id}, search_date: {self.search_date}>'


class Find(Base):
    __tablename__ = 'find'
    id = Column(Integer, primary_key=True)
    search_id = Column(Integer, ForeignKey('search.id'))    
    find_date = Column(DateTime)
    store_id = Column(Integer, ForeignKey('store.id'))
    url = Column(String)
    price = Column(Float)
    stock = Column(Integer)

    def __str__(self):
        return f'<Find id: {self.id}, search_id: {self.search_id}, find_date: {self.find_date}, store_id: {self.store_id}' \
            + f'url: {self.url}, price: {self.price}, stock: {self.stock}>'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
        