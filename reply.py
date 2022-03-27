import random
from typing import TYPE_CHECKING
from fastapi import Response

from sql_req import get_response



from sqlalchemy.ext.asyncio.session import AsyncSession

async def reply_to_message(messege_text: str, vk_api, user_id: int, session:AsyncSession):

    replies = await get_response(session, messege_text)

    for reply in replies:
        reply_text = reply.answer
        vk_api.messages.send(
            user_id = user_id,
            message = reply_text,
            random_id = random.randint(0, 5000000000000000000000000),
            v=5.131
        )

