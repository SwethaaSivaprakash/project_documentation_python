#from flask import Flask ,render_template,request
import xlrd
import os
import urllib.request
from flask import Flask, flash, request, redirect, render_template,url_for,abort,send_file
from werkzeug.utils import secure_filename
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
ALLOWED_EXTENSIONS = set([ 'pdf', 'docx','doc'])
app = Flask(__name__) 
app.secret_key = "secret key"



def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/index',methods=['GET','POST'])	
def index():
	return render_template("upload.html")

@app.route('/upload1', methods=['GET', 'POST'])
def upload():
	if "others" in request.form:
		UPLOAD_FOLDER = 'D:\project_documentation\static\others'
	elif "machine_learning" in request.form:
		UPLOAD_FOLDER = 'D:\project_documentation\static\machine learning'
	elif "Iot" in request.form:
		UPLOAD_FOLDER = 'D:\project_documentation\static\Iot'
	elif "mobile_technologies" in request.form:
		UPLOAD_FOLDER = 'D:\project_documentation\static\mobile technologies'
	elif "cloud_computing" in request.form:
		UPLOAD_FOLDER = 'D:\project_documentation\static\cloudd'
	elif "data_science" in request.form:
		UPLOAD_FOLDER = 'D:\project_documentation\static\data science'
	'''elif "artificial_intelligence" in request.form:
		UPLOAD_FOLDER = 'D:\project_documentation\static\artificial intelligence'	
		'''
	app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
	app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
	if request.method == 'POST':
        # check if the post request has the files part
		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')
		for file in files:
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				flash('File(s) successfully uploaded')
		return redirect(url_for('index'))


@app.route('/download1', defaults={'req_path': ''},methods=['GET', 'POST'])
@app.route('/<path:req_path>')
def download1(req_path):
	BASE_DIR = 'D:\project_documentation\static\machine learning'
	abs_path = os.path.join(BASE_DIR, req_path)
	print(abs_path)
	if not os.path.exists(abs_path):
		return abort(404)
	if os.path.isfile(abs_path):
		return send_file(abs_path)
	files=os.listdir(abs_path)
	return render_template('files.html', files=files)
@app.route('/download2', defaults={'req_path': ''},methods=['GET', 'POST'])
@app.route('/<path:req_path>')
def download2(req_path):
	BASE_DIR = 'D:\project_documentation\static\Iot'
	abs_path = os.path.join(BASE_DIR, req_path)
	print(abs_path)
	if not os.path.exists(abs_path):
		return abort(404)
	if os.path.isfile(abs_path):
		return send_file(abs_path)
	files=os.listdir(abs_path)
	return render_template('files1.html', files=files)

@app.route('/download3', defaults={'req_path': ''},methods=['GET', 'POST'])
@app.route('/<path:req_path>')
def download3(req_path):
	BASE_DIR = 'D:\project_documentation\static\mobile technologies'
	abs_path = os.path.join(BASE_DIR, req_path)
	print(abs_path)
	if not os.path.exists(abs_path):
		return abort(404)
	if os.path.isfile(abs_path):
		return send_file(abs_path)
	files=os.listdir(abs_path)
	return render_template('files2.html', files=files)
@app.route('/download4', defaults={'req_path': ''},methods=['GET', 'POST'])
@app.route('/<path:req_path>')
def download4(req_path):
	BASE_DIR = 'D:\project_documentation\static\data science'
	abs_path = os.path.join(BASE_DIR, req_path)
	print(abs_path)
	if not os.path.exists(abs_path):
		return abort(404)
	if os.path.isfile(abs_path):
		return send_file(abs_path)
	files=os.listdir(abs_path)
	return render_template('files3.html', files=files)
@app.route('/download5', defaults={'req_path': ''},methods=['GET', 'POST'])
@app.route('/<path:req_path>')
def download5(req_path):
	BASE_DIR = 'D:\project_documentation\static\cloudd'
	print("b=",BASE_DIR)
	print("r=",req_path)
	abs_path = os.path.join(BASE_DIR, req_path)
	print(abs_path)
	if not os.path.exists(abs_path):
		return abort(404)
	if os.path.isfile(abs_path):
		return send_file(abs_path)
	files=os.listdir(abs_path)
	print(files)
	return render_template('files4.html', files=files)
@app.route('/download6', defaults={'req_path': ''},methods=['GET', 'POST'])
@app.route('/<path:req_path>')
def download6(req_path):
	BASE_DIR = 'D:\project_documentation\static\others'
	abs_path = os.path.join(BASE_DIR, req_path)
	print(abs_path)
	if not os.path.exists(abs_path):
		return abort(404)
	if os.path.isfile(abs_path):
		return send_file(abs_path)
	files=os.listdir(abs_path)
	return render_template('files5.html', files=files)


@app.route('/facultylogin',methods=['GET', 'POST']) 
def faculty_login(): 
   return render_template("login.html")
@app.route('/login1',methods=['GET', 'POST']) 
def login1():
    if request.method == "POST":
        username = request.form["uname"]
        password= request.form["psw"]
        with app.app_context():
            df = (r'D:\project_documentation\login.xlsx')
            wb = xlrd.open_workbook(df) #opens the excel sheet
            sheet = wb.sheet_by_index(0) #gets the first sheet
            sheet.cell_value(0,0)
            for i in range(sheet.nrows-1):
                col=sheet.cell_value(i+1,1)
                col1=sheet.cell_value(i+1,2)
                if col==username and col1==password:
                    print ("success")
                    return render_template("upload.html")   
             					
@app.route('/studentlogin',methods=['GET', 'POST']) 
def student_login(): 
   return render_template("logins.html")
@app.route('/logins',methods=['GET', 'POST']) 
def logins():
    if request.method == "POST":
        username = request.form["uname"]
        password= request.form["psw"]
        with app.app_context():
            df = (r'D:\project_documentation\login.xlsx')
            wb = xlrd.open_workbook(df) #opens the excel sheet
            sheet = wb.sheet_by_index(0) #gets the first sheet
            sheet.cell_value(0,0)
            for i in range(sheet.nrows-1):
                col=sheet.cell_value(i+1,1)
                col1=sheet.cell_value(i+1,2)
                if col==username and col1==password:
                    print ("success")
                    return render_template("option.html")  
                
@app.route('/')
def base():
	return render_template("main.html")
                
if __name__ == '__main__': 
   app.debug=True
   app.run() 
   