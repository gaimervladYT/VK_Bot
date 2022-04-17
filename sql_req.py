from sqlalchemy import text, true
from sqlalchemy.ext.asyncio.session import AsyncSession

async def get_response(session: AsyncSession, req: str):
    sql_text = text(f"SELECT answer FROM phrases WHERE phrase ='{req}'")
    responce = await session.execute(sql_text)
    await session.commit()
    return responce.all()

async def write_new_phrase(session: AsyncSession, phrase: str, answer: str):
    sql_text = text(f"""
        SELECT id FROM phrases ORDER BY id DESC
    """)
    result = await session.execute(sql_text)
    result =result.all()
    last_id = result[0].id
    sql_text = text(f"""
        INSERT into phrases VALUES ({last_id+1}, '{phrase}', '{answer}')
    """)
    result = await session.execute(sql_text)
    await session.commit()
    return true