from flask import Flask
from flask import url_for
from flask import request
from markupsafe import escape

app = Flask(__name__)

############################
# Route Variables Examples #
############################

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

# Converter Example 1 (integer)
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

# Converter Example 2 (path)
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

#############################
#   HTTP Methods Examples   #
#############################

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return 'Login Successful?'
#     else:
#         return 'Log In Here'

@app.get('/login')
def login_get():
    return 'Log In Here'

@app.post('/login')
def login_post():
    return 'Login Successfull?'