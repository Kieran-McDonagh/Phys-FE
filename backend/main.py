import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from backend.routes.user_routes import router as user_router
from backend.routes.workout_routes import router as workout_router
from backend.routes.nutrition_routes import router as nutrition_router
from backend.routes.login import router as login_router

from backend.models.user_models.new_user import NewUser as User
from backend.models.user_models.user import User as UserInDB
from backend.security.authentication import Authenticate
from typing import Annotated


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


app.include_router(login_router)
app.include_router(user_router, prefix="/api")
app.include_router(
    workout_router,
    prefix="/api",
    dependencies=[Depends(Authenticate.get_current_active_user)],
)
app.include_router(
    nutrition_router,
    prefix="/api",
    dependencies=[Depends(Authenticate.get_current_active_user)],
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
