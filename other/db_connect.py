import asyncpg


class Request:

    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_user_contact(self, user_id: int, name: str, phone: str, user_url: str):
        query = '''
            INSERT INTO users (user_id, name, phone, user_url) VALUES ($1, $2, $3, $4);
        '''
        await self.connector.execute(query, user_id, name, phone, user_url)

    async def get_users(self) -> str:
        query = '''
            SELECT created_at, name, phone, user_url FROM users ORDER BY created_at DESC;
        '''
        users = await self.connector.fetch(query)
        res = 'Дата добавления; Имя; Телефон; Ссылка\n\n'
        res += '\n\n'.join(list(item['created_at'].strftime('%d.%m.%Y %H:%M') + '; ' + item['name'] + '; ' + item['phone'] + '; ' + item['user_url'] for item in users))
        return res
