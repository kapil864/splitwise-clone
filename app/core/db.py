from os import environ

from motor.motor_asyncio import AsyncIOMotorClient

DATABASE = environ.get('DATABASE', 'splitwise')
USER_COLLECTION = environ.get('USER_COLLECTION', 'users')
EXPENSE_COLLECTION = environ.get('EXPENSE_COLLECTION', 'expenses')
GROUP_COLLECTION = environ.get('GROUP_COLLECTION', 'groups')
MONGODB_URL = environ.get('MONGODB_URL', None)

client = AsyncIOMotorClient(
    MONGODB_URL,
    username='user',
    password='pass',
)

db = client[DATABASE]

user_collection = db[USER_COLLECTION]
expense_collection = db[EXPENSE_COLLECTION]
group_collection = db[GROUP_COLLECTION]
