#Thank you LazyDeveloper for helping me in this journey !
#Must Subscribe On YouTube @LazyDeveloperr 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@movies_x_store'

if __name__ == "__main__":
    app.run()
