from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.get('/company/<company>')
def show_user_profile(company):
    return f'company {escape(company)}'

@app.post('/post')
def show_post(post_id):
    return f'Post {post_id}'