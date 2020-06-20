# -*- coding: utf-8 -*-

from fastapi import FastAPI

from routers import router

def get_app() -> FastAPI:
    fast_app = FastAPI()
    fast_app.include_router(router, tags=['model'])

    return fast_app

app = get_app()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)