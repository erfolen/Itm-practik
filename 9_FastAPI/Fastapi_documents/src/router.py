from fastapi import APIRouter, UploadFile
from repository import DocumentsDB
import shutil

router = APIRouter(
    prefix="",
    tags=["API"]
)


@router.post('/upload_doc')
async def upload_file(file: UploadFile):
    """загрузка файла в папку 'Documents'"""
    if file.content_type.split('/')[0] == 'image':
        with open(f'documents/{file.filename}', 'wb') as f:
            shutil.copyfileobj(file.file, f)
    doc_id = await DocumentsDB.add_doc(file.filename)
    return {'ok': True, 'doc_name': file.filename, 'id': doc_id}


@router.delete('/doc_delete ')
async def delete_file():
    pass


@router.get('/doc_analyse/{doc_id}')
async def add_text():
    pass
