import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from typing import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]


class Documents(Base):
    __tablename__ = 'documents'

    id: Mapped[intpk]
    psth = Mapped[str]
    date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class DocumentsText(Base):
    __tablename__ = 'documents_text'

    id: Mapped[intpk]
    id_doc: Mapped[int] = mapped_column(ForeignKey('documents.id', ondelete='CASCADE'))
    text: Mapped[str]
