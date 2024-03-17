import os
import shutil
import pytesseract
from PIL import Image

from fastapi import APIRouter, UploadFile

from repository import DocumentsDB

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
async def delete_file(doc_id: int):
    """Удаление документа"""
    path = await DocumentsDB.get_path(doc_id)
    if os.path.isfile(path):
        os.remove(path)
        await DocumentsDB.del_doc(doc_id)
        return {'ok': True}


@router.get('/doc_analyse/{doc_id}')
async def add_text(doc_id: int):
    """Запись текста с картинки"""
    path = await DocumentsDB.get_path(doc_id)
    text = pytesseract.image_to_string(Image.open(path))
    print(text)


@router.get('/get_text/{doc_id}')
async def get_text(doc_id: int):
    pass
