import datetime
from typing import Annotated

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]


class Documents(Base):
    __tablename__ = 'documents'

    id: Mapped[intpk]
    path: Mapped[str]
    date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class DocumentsText(Base):
    __tablename__ = 'documents_text'

    id: Mapped[intpk]
    id_doc: Mapped[int] = mapped_column(ForeignKey('documents.id', ondelete='CASCADE'))
    text: Mapped[str]
