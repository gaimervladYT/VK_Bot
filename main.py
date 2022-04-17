import uvicorn
import vk
from fastapi import FastAPI, Request, Response, Depends
from pydantic import BaseSettings

from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.asyncio import engine
from sqlalchemy.ext.asyncio.session import AsyncSession

from reply import reply_to_message, start

class Setting(BaseSettings):
    confirmation_string:str
    group_id: int
    vk_token:str
    sqlite_config:str
    class Config:
        env_file =".env"


settings = Setting()

vk_session = vk.Session(access_token=settings.vk_token)
vk_api = vk.API(vk_session)
 
engine = engine.create_async_engine(
    settings.sqlite_config,echo=True)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)



async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


app = FastAPI()


@app.post('/main')
async def authorize(
    req: Request,
    session: AsyncSession = Depends(get_session)
    ):
    req_body = await req.json()
    print(req_body)
    if req_body['type'] == 'confirmation' and req_body['group_id'] == settings.group_id:
        print('okay')
        print(settings.confirmation_string)
        return Response(content=settings.confirmation_string, media_type="application/json")
    elif req_body['type'] == 'message_new':
        if "payload" in req_body['object']['message']:
            pd = req_body ['object']['message']['payload']
            if pd == '{"command":"start"}':
                await start(vk_api, req_body['object']['message']['from_id'])

            
        else:
            await reply_to_message(
                req_body['object']['message']['text'],
                vk_api,
                req_body['object']['message']['from_id'],
                session
            )
    return Response('ok', media_type='application/json')
if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)

    