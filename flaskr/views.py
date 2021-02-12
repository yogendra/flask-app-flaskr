from flask import url_for,request,render_template
from markupsafe import escape
from flaskr import app

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



@app.route('/login', methods=['GET'])
def login():
  return render_template('login.html')



def valid_login (username, password):
  valid = True
  valid &= username == password
  return valid

@app.route('/login', methods=['POST'])
def do_login():
    username=request.form['username']
    password=request.form['password']
    if valid_login(username,password):
        return log_the_user_in(username)
    else:
      return render_template('login.html', error="Invalid username/password")

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
