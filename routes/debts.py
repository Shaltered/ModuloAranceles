from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Debt
from schemas import DebtCreate, DebtUpdate, Debt

router = APIRouter(
    prefix="/api/v1/debts",
    tags=["Debts"]
)

@router.post("/", response_model=Debt)
def create_debt(debt: DebtCreate, db: Session = Depends(get_db)):
    new_debt = Debt(**debt.model_dump())  # Usa model_dump en lugar de dict
    db.add(new_debt)
    db.commit()
    db.refresh(new_debt)
    return new_debt

@router.get("/{debt_id}", response_model=Debt)
def get_debt(debt_id: int, db: Session = Depends(get_db)):
    debt = db.query(Debt).filter(Debt.id == debt_id).first()
    if not debt:
        raise HTTPException(status_code=404, detail="Debt not found")
    return debt

@router.put("/{debt_id}", response_model=Debt)
def update_debt(debt_id: int, debt_update: DebtUpdate, db: Session = Depends(get_db)):
    debt = db.query(Debt).filter(Debt.id == debt_id).first()
    if not debt:
        raise HTTPException(status_code=404, detail="Debt not found")
    for key, value in debt_update.dict().items():
        setattr(debt, key, value)
    db.commit()
    db.refresh(debt)
    return debt

@router.delete("/{debt_id}")
def delete_debt(debt_id: int, db: Session = Depends(get_db)):
    debt = db.query(Debt).filter(Debt.id == debt_id).first()
    if not debt:
        raise HTTPException(status_code=404, detail="Debt not found")
    db.delete(debt)
    db.commit()
    return {"detail": "Debt deleted"}
