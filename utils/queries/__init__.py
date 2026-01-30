from core.db_settings import execute_query
from core.models import users


async def create_table():
    execute_query(query=users)