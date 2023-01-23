from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(blog_url)
all_posts = response.json()

@app.route('/')
def home():
    return render_template('index.html', posts=all_posts, year=datetime.now().year)


@app.route('/<int:num>')
def blog(num):
    return render_template('post.html', posts=all_posts, id=num, year=datetime.now().year)


if __name__ == '__main__':
    app.run(debug=True)
