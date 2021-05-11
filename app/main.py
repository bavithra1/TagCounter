import uvicorn
from config import config
from api.root_api import router

def start_app():
    app = config.app
    app.include_router(router)
    return app
if __name__ == '__main__':
    app = start_app()
    uvicorn.run(app, host="0.0.0.0", port=8080)
else:
   app = start_app()
    