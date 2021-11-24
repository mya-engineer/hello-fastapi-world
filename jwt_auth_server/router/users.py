from fastapi import APIRouter
from models import User


router = APIRouter(prefix='/users')


@router.get('/')
def users_list():
    return []


@router.post('/', status_code=201)
def create_user(user: User):
    return user
