from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, DATE, ForeignKey
from models.Base import Base
from datetime import datetime
from Veiculo_model import Veiculo
class CtEngate(Base):
    __tablename__ = "CTENGATE"
    ID:          Mapped[int]      = mapped_column(INTEGER, nullable=False, primary_key=True)
    DTENGATE:    Mapped[datetime] = mapped_column(DATE,    nullable=False)
    DTDESENGATE: Mapped[datetime] = mapped_column(DATE,    nullable=True)
    NRFROTA:     Mapped[int]      = mapped_column(INTEGER, nullable=False)
    NRCONJUNTO:  Mapped[int]      = mapped_column(INTEGER, nullable=False)
    IDVEICULO:   Mapped[int]      = mapped_column(INTEGER, ForeignKey(Veiculo.idVeiculo), nullable=False)