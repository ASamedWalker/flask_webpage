from flask_webpage import app
from flask import Flask

app.config['SECRET_KEY'] = 'secret!'

if __name__ == '__main__':
  app.run(debug=True)