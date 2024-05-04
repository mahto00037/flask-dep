from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
   return("home fffpage")

@app.route('/register')
def register():
   return("register page")

if __name__ == '__main__':
   app.run(debug=True)
