from database import async_session_fabric
from models import Documents, DocumentsText
import shutil


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
