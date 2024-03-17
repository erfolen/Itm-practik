from database import async_session_fabric
from models import Documents, DocumentsText
from sqlalchemy import select, delete


class DocumentsDB:
    @staticmethod
    async def add_doc(file_name):
        async with async_session_fabric() as session:
            doc = Documents(path=f'documents/{file_name}')
            session.add(doc)
            await session.flush()
            doc_id = doc.id
            await session.commit()
            return doc_id

    @staticmethod
    async def get_path(doc_id):
        async with async_session_fabric() as session:
            query = select(Documents).filter(Documents.id == doc_id)
            result = await session.execute(query)
            return result.scalar_one().path

    @staticmethod
    async def del_doc(doc_id):
        async with async_session_fabric() as session:
            query = delete(Documents).filter_by(id=doc_id)
            await session.execute(query)
            await session.commit()

