from fastapi import FastAPI
from routes.userRoute import userRouter

app = FastAPI()

app.include_router(router=userRouter)