from fastapi import APIRouter


router = APIRouter(prefix='/booking', tags=['booking'])


@router.get('')
async def booking():
    return {'status': 'ok'}

