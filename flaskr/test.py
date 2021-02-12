from flaskr import app

@app.route('/test')
def test():
    return 'Test'
