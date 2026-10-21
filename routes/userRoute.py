from fastapi import status, APIRouter
from controllers.userController import userServiceController


userRouter = APIRouter(prefix='/users', tags=['Users'])


@userRouter.get('/')
async def getAllUsers():
    ctrl = userServiceController()
    allUsers = await ctrl.userNames()
    return {"userList":allUsers} 

