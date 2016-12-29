import os
import json
import codecs
import logging
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import smtplib
from mail_util import mail
from logging.handlers import RotatingFileHandler

from email.mime.text import MIMEText

app = Flask(__name__)
appendtext = "Hello "

app.config['UPLOAD_FOLDER'] = 'uploads/'

app.config['ALLOWED_EXTENSIONS'] = set(['html', 'pdf','PROJECT','log'])

filename = ""



def sendMail(name,mailid,subject,content):
    for _id in mailid:     
        mail(name,_id,subject,content)
        
    return


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/test/<args>',methods=['POST'])
def test(args):
    return str(args)

@app.route('/newcampaign')
def newcampaign():
    contacts = request.args.get('editor1')
    print "jhgfudsf",contacts
    return render_template('newcampaign.html')

@app.route('/newcampaign', methods = ['POST'])
def accept_campaign():
    name = request.form['name']
    mailid = request.form['mailid']
    content = request.form['editor1']
    subject = request.form['subject']
    print name,mailid,content,subject
    sendMail(name,mailid.split(","),subject,content)
    return str(content)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/upload', methods=['POST'])
def upload():
    global filename
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        
        filename = secure_filename(file.filename)
        
        # Move the file form the temporal folder to
        # the upload folder we setup
        print "type:",type(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        txt = codecs.open('uploads/'+ filename, 'r')
        txt = txt.read()
        mailList = request.form['mailList']
        sendMail(txt,mailList.split(","))  
        # Redirect the user to the uploaded_file route,        
        return redirect(url_for('uploaded_file',
                                filename=filename))
        #return redirect(url_for('/parse'))

  
@app.route('/unsubscribe/<mailid>')
def unsubscribe(mailid):
	print mailid
	return "Unsubscribed!"

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/input', methods=['POST'])
def input():
    text = request.form['text']
    mailList = request.form['mailList']
    sendMail(text,mailList.split(","))
    
    return render_template('index.html')

if __name__ == '__main__':
    logging.basicConfig(filename='example.log',level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    app.run(
        host="0.0.0.0",
        port=int("2251"),
        debug=True 
    )
