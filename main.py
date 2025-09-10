from flask import Flask, render_template , redirect, url_for, request
from forms import MyForm
from flask_bootstrap import Bootstrap5
from datetime import datetime
from smtplib import SMTP

year=datetime.today().year
#Function for sending message through SMPTlib
EMAIL='umidraxmatullayev2005@gmail.com'
EMAIL_PASSWORD='x t u u v m q x t a y n w s h u'
import smtplib, ssl

def send_message(name, email, phone, message):
    try:
        smtp_server = "smtp.gmail.com"
        port = 465
        receiver_email = "umidraxmatullayev96@gmail.com"
        msg = f"Subject: New Contact Message\n\nFrom: {name}\nPhone: {phone}\nEmail: <{email}>\n\n{message}"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(EMAIL, EMAIL_PASSWORD)
            server.sendmail(EMAIL, receiver_email, msg)

        return True
    except Exception as e:
        print("Email sending failed:", e)
        return False
          
app=Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "cdhclicvchc782749472"
@app.route('/')
def home():
    return render_template('index.html', year=year)
    
    

@app.route('/about')
def about():
    return render_template('about.html' , year=year)


@app.route('/mywork')
def my_work():
    return render_template('my_work.html', year=year)
    
@app.route('/contact' ,methods=['GET','POST'])
def contact():
    form=MyForm()
    sent = request.args.get('sent')
    if form.validate_on_submit():
        print('checking')
        send_message(form.name.data, form.email.data, form.phone.data, form.message.data)
        print("Done")
        
        return redirect(url_for('contact',sent=True))
    else:
        return render_template('contact.html',form=form, year=year, sent=sent)

if __name__=='__main__':
    app.run(debug=True)