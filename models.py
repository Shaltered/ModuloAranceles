from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Debt(Base):
    __tablename__ = "debts"

    id = Column(Integer, primary_key=True, index=True)  # El 'id' es generado automáticamente por la base de datos
    student_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default="pending")
