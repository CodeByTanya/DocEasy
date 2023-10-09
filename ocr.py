# ------------------------------  DocEasy  ------------------------------------
# importing the necessary libraries
import pytesseract
from PIL import Image
from flask import Flask, render_template, request
import webbrowser
import os

# setting the tesseract-ocr executable file path
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# creating a flask object
app = Flask(__name__)

# defining a folder to store and later serve the images
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# defining a downloads folder
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# allowing files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
# function to check the file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# function to extract text from image
def text_extract(img_path):
    val=Image.open(img_path)
    global text
    custom_config = r'--oem 3 -l eng --psm 6'
    text=pytesseract.image_to_string(val,config=custom_config)   
    text=text.replace('\n',' ')
    text=text.rstrip()
    return text

# function to change the file format
def change_ext(val):
    if val is None:
        ext='txt'
    else:
        ext=val
    filename="result.txt"
    fh=open(filename,'w+')
    fh.write(text)
    fh.close()
    split = os.path.splitext(filename)[0]
    os.rename(+filename, str(split) +'.'+ ext)
    return filename

@app.route('/', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # checking if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')
        if file and allowed_file(file.filename):
            text = text_extract(file)
            ext_val=request.form.get('ext')
            print(ext_val)
            filename="result."+str(ext_val)
            with open(filename, "w") as fh:
                fh.write(text)
            return render_template('upload.html', msg='Successfully processed', extracted_text=text, img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')
    
def window():
    webbrowser.open_new('http://127.0.0.1:5000/')

# driver code    
if __name__=='__main__':
    window()
    app.run()

