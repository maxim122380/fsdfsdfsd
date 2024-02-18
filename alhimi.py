from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'  # Название таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Первичный ключ товара
    name = Column(String)  # Название товара
    price = Column(Integer)  # Цена товара

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price}, category={self.category})>"

class User(Base):
    __tablename__ = 'users'  # Название таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Первичный ключ
    name = Column(String)  # Столбец для имени пользователя
    balance = Column(Integer)  # Столбец для баланса пользователя

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, balance={self.balance})>"

class Database:
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///base.db')  # Создаем соединение с базой данных
        Base.metadata.create_all(self.engine)  # Создаем таблицы, если они еще не существуют
        Session = sessionmaker(bind=self.engine)  # Создаем класс сессии для взаимодействия с базой данных
        self.session = Session()  # Создаем объект сессии

    def get_user(self, id):
        return self.session.query(User).filter_by(id=id).first()  # Запрос пользователя по его id

    def register(self, id, name):
        user = User(id=id, name=name, balance=0)  # Создаем нового пользователя
        self.session.add(user)  # Добавляем пользователя в сессию
        self.session.commit()  # Фиксируем изменения в базе данных
        return True

    def update_balance(self, id, balance, status):
        user = self.get_user(id)  # Получаем пользователя из базы данных
        balance = float(balance)
        if user:
            if status:
                user.balance += balance  # Увеличиваем баланс пользователя
            else:
                user.balance -= balance  # Уменьшаем баланс пользователя
            self.session.commit()  # Фиксируем изменения в базе данных
            return user.balance  # Возвращаем обновленный баланс
        else:
            return None
    def get_balance(self, id):
        user = self.get_user(id) 
        return user.balance
        
    def __del__(self):
        self.session.close()  # Закрытие сессии при уничтожении объекта

    def add_product(self, name, price):
        product = Product(name=name, price=price)
        self.session.add(product)
        self.session.commit()
        return True
    
    def get_all_products(self):
        return self.session.query(Product).all()

