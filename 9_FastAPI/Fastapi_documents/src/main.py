import uvicorn
from fastapi import FastAPI
from router import router
app = FastAPI()


@app.get('/')
def start():
    return {'Hi'}


app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
