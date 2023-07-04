from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import blog_posts

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blog_posts.router)

# teste
