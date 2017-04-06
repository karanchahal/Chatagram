import faceRecognizer
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_socketio import SocketIO, send, emit
import base64
import Image


faceRecognizer.enroll_faces()
app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
dir_path = os.path.dirname(os.path.realpath(__file__))

app.config['UPLOAD_FOLDER'] = 'user_uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])




@socketio.on('faceverify')
def faceverify(payload):
    img_data = payload['picture'][23:]
    imgdata = base64.b64decode(payload['picture'][23:])

    fh = open("./dump/imageToSave.webp", "wb")
    fh.write(img_data.decode('base64'))
    fh.close()

    im = Image.open("./dump/imageToSave.webp").convert("RGB")
    im.save("./actual/final_image.jpg","jpeg")
    try:
        account_id = faceRecognizer.facerec(dir_path + '/actual/final_image.jpg')
        print('AccountId: ',account_id)
        emit('faceverify',{'acc_no':account_id})
    except:
        print('Boohoo')
        emit('faceverify',{'acc_no':0})




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file',
                                filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    faceRecognizer.enroll_faces() #TO-DO: Yeh bakwass hai faaltu ka slowdown. Remove this in the future
    account_id = faceRecognizer.facerec(dir_path + '/user_uploads/'+ filename)
    return account_id
    #print account_id
    #return send_from_directory(app.config['UPLOAD_FOLDER'],
    #                          filename)

#Use port 7979 for listening in. Cheers bruh
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug = True, port = 3111, use_reloader = True) #Open localhost:3110 to run this in your browser -.-
