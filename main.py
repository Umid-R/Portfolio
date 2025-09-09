from flask import Flask, render_template , redirect, url_for, request
from forms import MyForm
from flask_bootstrap import Bootstrap5
from datetime import datetime
from smtplib import SMTP

year=datetime.today().year
#Function for sending message through SMPTlib
EMAIL='umidraxmatullayev2005@gmail.com'
EMAIL_PASSWORD='x t u u v m q x t a y n w s h u'
def send_message(name,email,phone,message):
    with SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=EMAIL_PASSWORD)
            connection.sendmail(from_addr=EMAIL,to_addrs='umidraxmatullayev96@gmail.com',msg=f'Subject:New Message \n\n{name}\n{email}\n{phone}\n{message}')
          
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