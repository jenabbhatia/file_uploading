import os
from flask import Flask,redirect,url_for,request,render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory


ALLOWED_EXTENSION=set(['pdf','jpg','png','jpeg','txt'])

app=Flask(__name__)
app.config['UPLOAD_FOLDER']='uploads/'

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1] in ALLOWED_EXTENSION

@app.route('/')
def index():
    return render_template('index.html')

#route that process the file upload

@app.route('/upload/',methods=["GET","POST"])
def upload():
    #get the name of the uploaded file
    file=request.files['file']
    
    #check if the file is of the allowed extension
    if file and allowed_file(file.filename):
        filename=secure_filename(file.filename)
        
        #move the file from temporary folder to the folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return redirect(url_for('uploaded_file',filename=filename))
        
@app.route('/uploads/<filename>')
def uploaded_file(filename):
     return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
     
if __name__ == '__main__':
    app.run(
        host="localhost",
        port=int("5000"),
        debug=True
    )

        
    
    

    
            
    
    
    

