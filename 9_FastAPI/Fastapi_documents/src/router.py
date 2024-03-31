import os
import shutil

from fastapi import APIRouter, UploadFile

from repository import DocumentsDB, DocumentsTextDB
from celery_app import scan_text_on_img

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
    scan_text_on_img.delay(path, doc_id)
    return {'ok': True}


@router.get('/get_text/{doc_id}')
async def get_text(doc_id: int):
    """Вывод текста из картинки"""
    text = await DocumentsTextDB.get_text(doc_id)
    return {'ok': True, 'text': text}