from datetime import date
from typing import Any, Dict, List

from sqlalchemy import Date, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import JSON

from app.db.base import Base

class Ordem_entrega(Base):
    __tablename__ = "ordem_entrega"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    tipo: Mapped[str] = mapped_column(Text, nullable=False)
    data_entrega: Mapped[date] = mapped_column(Date, nullable=False)
    nf: Mapped[List[Dict[str, Any]]] = mapped_column(JSON, nullable=False)
    chapa: Mapped[int] = mapped_column(primary_key=True, index=True)
