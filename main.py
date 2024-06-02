import os
from settings import BASE_FOLDER, SECURITY_USER
from flask import Flask, render_template, request, send_from_directory, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return "InDEx_别搞事"

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    # POST方法且是安全员即可上传
    if request.method == 'POST' and request.form['username'] in SECURITY_USER:
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(BASE_FOLDER, filename))
            response =  make_response("File uploaded successfully", 201)
            return response
    # 否则一直是上传页面
    return render_template('upload.html')

@app.route('/download/', methods=['GET'])
def download_file():
    # 带有安全员身份则可以下载
    if request.args.get('username') in SECURITY_USER:
        file = request.args.get('file')
        return send_from_directory(BASE_FOLDER, file, as_attachment=True)
    # 否则只能查看文件
    else:
        files = [f for f in os.listdir(BASE_FOLDER) if os.path.isfile(os.path.join(BASE_FOLDER, f))]
        return render_template('file_list.html', files=files)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)