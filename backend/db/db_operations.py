# Aqui é onde você iria definir as funções que interagem com o seu banco de dados.
# Como exemplo, vou apenas utilizar uma lista em memória.

posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post.", "published": True},
    {"id": 2, "title": "Second Post", "content": "This is the second post.", "published": False},
]

def get_all_posts():
    return posts

def get_post(post_id: int):
    post = next((post for post in posts if post["id"] == post_id), None)
    return post

def create_post(post):
    new_post_id = max(post["id"] for post in posts) + 1
    new_post = post.dict()
    new_post["id"] = new_post_id
    posts.append(new_post)
    return new_post
