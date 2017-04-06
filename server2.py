import faceRecognizer
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))

app.config['UPLOAD_FOLDER'] = 'user_uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

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
    app.run(
        host="0.0.0.0",
        port=int("7979"),
        debug=True
    )

    
