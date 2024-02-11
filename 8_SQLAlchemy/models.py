import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, str_150, str_15, num_12_2
from typing import Annotated, List

intpk = Annotated[int, mapped_column(primary_key=True)]


class Employees(Base):
    __tablename__ = 'employees'

    id: Mapped[intpk]
    last_name: Mapped[str_150]
    first_name: Mapped[str_150]
    surname: Mapped[str_150]
    job_title: Mapped[str_150]
    address: Mapped[str]
    home_phone: Mapped[str_15]
    dob: Mapped[datetime.date]
    orders: Mapped[List['Orders']] = relationship(back_populates='employee')


class Shippers(Base):
    __tablename__ = 'shippers'

    id: Mapped[intpk]
    name: Mapped[str_150]
    agent: Mapped[str_150]
    fio: Mapped[str_150]
    phone: Mapped[str_15]
    address: Mapped[str_150]
    supplies: Mapped[List['Supplies']] = relationship(back_populates='shipper')


class Supplies(Base):
    __tablename__ = 'supplies'

    id: Mapped[intpk]
    shippers_id: Mapped[int] = mapped_column(ForeignKey('shippers.id', ondelete='CASCADE'))
    delivery_date: Mapped[datetime.date]
    shipper: Mapped['Shippers'] = relationship(back_populates='supplies')
    products: Mapped[List['Products']] = relationship(back_populates='supplier')


class Products(Base):
    __tablename__ = 'products'

    id: Mapped[intpk]
    supplies_id: Mapped[int] = mapped_column(ForeignKey('supplies.id', ondelete='CASCADE'))
    supplier: Mapped['Supplies'] = relationship(back_populates='products')
    name: Mapped[str_150]
    specifications: Mapped[str | None]
    description: Mapped[str | None]
    images: Mapped[str_150]
    cost: Mapped[num_12_2]
    quantity: Mapped[int]
    price: Mapped[num_12_2]
    orders: Mapped[List['Orders']] = relationship(back_populates='product')


class Customers(Base):
    __tablename__ = 'customers'

    id: Mapped[intpk]
    fio: Mapped[str]
    address: Mapped[str]
    phone: Mapped[str_15]
    orders: Mapped[List['Orders']] = relationship(back_populates='customer')


class Orders(Base):
    __tablename__ = 'orders'

    id: Mapped[intpk]
    employees_id: Mapped[int] = mapped_column(ForeignKey('employees.id'))
    employee: Mapped['Employees'] = relationship(back_populates='orders')
    products_id: Mapped[int] = mapped_column(ForeignKey('products.id', ondelete='CASCADE'))
    product: Mapped['Products'] = relationship(back_populates='orders')
    date_create: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    date_did_order: Mapped[datetime.datetime]
    customers_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))
    customer: Mapped['Customers'] = relationship(back_populates='orders')
