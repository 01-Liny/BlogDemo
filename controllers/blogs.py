from app import app
from models.blog import Blog


@app.route('/add')
def add():
    blogs = Blog(title='hello', content='nice')
    blogs.save()
    return str(blogs.id)


@app.route('/')
def index():
    blogs = Blog.objects().all()
    data = {}
    for blog in blogs:
        data[str(blog.id)] = blog.to_dict()

    import json
    string = json.dumps(data, indent=4)
    print(string)
    return "Hello World! {}".format(string)
