from fastapi import APIRouter
from models.blogpost import BlogPost
from db.db_operations import get_all_posts, get_post, create_post

router = APIRouter()


@router.get("/posts/")
def read_posts():
    return get_all_posts()


@router.get("/posts/{post_id}")
def read_post(post_id: int):
    return get_post(post_id)


@router.post("/posts/")
def create_new_post(post: BlogPost):
    return create_post(post)
