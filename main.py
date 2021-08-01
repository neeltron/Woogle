from flask import Flask, render_template, request, make_response, redirect, url_for
from flask_socketio import SocketIO
from replit import db

app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

# Index page and Rendering Basic Templates
@app.route('/', methods= ["GET", "POST"])
def index():
  for i in db:
    print(db[i])
  return render_template('index.html')


@app.route('/push', methods= ["GET", "POST"])
def push():
  if request.method == "POST":
    print("here")
    user = request.form.get('title')
    i1 = request.form.get('i1')
    i2 = request.form.get('i2')
    i3 = request.form.get('i3')
    lst = [i1, i2, i3]
    db[user] = lst
    print(user, i1, i2, i3)
    return redirect("https://woogle.neeltron.repl.co")



# File Uploads (needs an HTML Form)
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#   if request.method == 'GET':
#     file = request.files['filename']
#     file.save('uploads/upload.txt')



def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)



if __name__ == '__main__':
  socketio.run(app, host = '0.0.0.0', debug=True, port = 8080)
