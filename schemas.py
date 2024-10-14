from pydantic import BaseModel

class DebtBase(BaseModel):
    student_id: int
    amount: float

class DebtCreate(DebtBase):
    pass  # No incluye el campo 'id'

class DebtUpdate(DebtBase):
    status: str

class Debt(DebtBase):
    id: int | None = None  # El id puede ser None porque es generado automáticamente
    status: str = "pending"

    class Config:
        from_attributes = True  # Pydantic v2 usa 'from_attributes' en lugar de 'orm_mode'
