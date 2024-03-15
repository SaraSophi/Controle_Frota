from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, CHAR, SMALLINT, DATE, NUMERIC, ForeignKey
import datetime
from sqlalchemy.schema import Sequence
class Base(DeclarativeBase):
    pass