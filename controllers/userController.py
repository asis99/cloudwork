from services.userService import UserService

class userServiceController:
    def __init__(self):
        pass

    async def userNames(self):
        user = UserService()
        users = await user.listOfUsers()
        return users


