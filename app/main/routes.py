from . import app

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'