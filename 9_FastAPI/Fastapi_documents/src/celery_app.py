from celery import Celery

from database import session_fabric
from models import DocumentsText
from repository import DocumentsTextDB
from PIL import Image
import pytesseract

session = session_fabric()
# Создаем экземпляр Celery
# celery -A celery_app:celery_app worker --loglevel=INFO
# result_backend='rpc://root:12345678@rabbitmq:5672'

celery_app = Celery('task', result_backend='rpc://root:12345678@rabbit_app:5672/vdata', broker='amqp://root:12345678@rabbit_app:5672/vdata',
                    broker_connection_retry_on_startup=True)


#
@celery_app.task
def scan_text_on_img(path, doc_id):
    img = Image.open(path)
    text = pytesseract.image_to_string(img, lang='eng+rus')
    # text = DocumentsText(id_doc=doc_id, text=text)
    # session.add(text)
    # session.commit()
    # print(text)
    DocumentsTextDB.add_text(doc_id, text)
