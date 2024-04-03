from distutils.sysconfig import get_python_lib
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from backend.health_router import router
from uvicorn import run


def create_app():
    app = FastAPI(
        title="Backend Server",
    )
    app.include_router(router)

    client_path = f"{get_python_lib()}/vite_project"
    app.mount("/assets", StaticFiles(directory=f"{client_path}/assets"), name="assets")
    app.mount("/static", StaticFiles(directory=f"{client_path}/static"), name="static")

    @app.get("/{catchall:path}")
    async def serve_react_app(catchall: str):
        return FileResponse(f"{client_path}/index.html")

    return app


def main():
    app = create_app()
    run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
