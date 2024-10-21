from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette import status

from dummy import dummy_router

DEBUG = True

app = FastAPI(
    title="Bndar Bant",
    debug=DEBUG,
    docs_url="/documentation"
)

app.include_router(dummy_router)


@app.get('/')
async def check_status():
    return JSONResponse({'status': 'I am fine !! \n Thanks for checking in.'}, status_code=status.HTTP_200_OK)
