import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def start():
    return {'Hi'}

# if __name__ == '__main__':
#     uvicorn main: app --reload
