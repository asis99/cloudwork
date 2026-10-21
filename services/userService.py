import uuid

class UserService:
    def __init__(self):
        pass

    async def listOfUsers(self):
        users = ['Rama', 'Rekha', 'Bunty', 'Peter']
        userwithIDs = {user:str(uuid.uuid4()) for user in users}
        return userwithIDs

    