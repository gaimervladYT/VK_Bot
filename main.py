from tokenize import group
from click import confirmation_option
import uvicorn

from fastapi import FastAPI, Request, Response
from pydantic import BaseSettings

class Setting(BaseSettings):
    confirmation_string:str
    group_id: int
    class Config:
        env_file =".env"

settings = Setting()

app = FastAPI()

@app.post('/main')
async def authorize(red: Request):
    req_body = await red.json()
    print(req_body)
    if req_body['type'] == 'confirmation' and req_body['group_id'] == settings.group_id:
        print('okay')
        print(settings.confirmation_string)
        return Response(content=settings.confirmation_string, media_type="application/json")
    else:
        return False
if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)

    