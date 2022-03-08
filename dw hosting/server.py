from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('dw_fe.html')

@app.route('https://www.affirmations.dev/')
def my_link():
  print ('I got clicked!')

  return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)