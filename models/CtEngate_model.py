from sqlalchemy.orm import  mapped_column, Mapped
from sqlalchemy import Integer, DATE, ForeignKey
from models import Base, Veiculo_model

class CtEngate_model(Base):
    _tablename_= "CTENGATE"
    id:             Mapped[int] = mapped_column(Integer, nullable=False, primary_key=True, autoincrement=True)
    dtEngate:       Mapped[DATE]= mapped_column(DATE, nullable=False)
    dtDesengate:    Mapped[DATE]= mapped_column(DATE, nullable=True)
    veiculoIdVeic:  Mapped[int] = mapped_column(Integer, ForeignKey(Veiculo_model.idVeic))
