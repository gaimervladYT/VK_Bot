from sqlalchemy import text
from sqlalchemy.ext.asyncio.session import AsyncSession

async def get_response(session: AsyncSession, req: str):
    sql_text = text(f"SELECT answer FROM phrases WHERE phrase ='{req}'")
    responce = await session.execute(sql_text)
    await session.commit()
    return responce.all()