import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from backend_v2.routes.user_routes import router as user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return RedirectResponse(url="/docs")

app.include_router(user_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)