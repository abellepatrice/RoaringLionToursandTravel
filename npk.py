from flask import*
import pymysql
from functions import*
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

def send_email(first_name, last_name, email_address, form_data):
    port = 465
    smtp_server = "mail.roaringliontours.co.ke"
    login = "sender@roaringliontours.co.ke"  # Update with your email login
    password = "your_email_password"  # Update with your email password

    sender_email = "sender@roaringliontours.co.ke"
    receiver_email = "requests@example.com"  # Update with the recipient's email address

    text = f"Dear {first_name} {last_name},\n\nThank you for your inquiry. Below is the information provided:\n\n"
    for key, value in form_data.items():
        text += f"{key}: {value}\n"

    text += "\n\nBest regards,\nRoaring Lion Tours"

    message = MIMEText(text, "plain")
    message["Subject"] = "Thank you for your inquiry"
    message["From"] = sender_email
    message["To"] = email_address

    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, [receiver_email], message.as_string())

@app.route ('/')
def home():
    return render_template("home.html")

@app.route('/tours')
def tours():
    return render_template("tours.html")

@app.route('/destinations')
def destinations():
    return render_template("destinations.html")
@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    if request.method == 'GET':
        return render_template("contactus.html")
    else:
        # Extract form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email_address = request.form['email_address']
        form_data = request.form

        # Save form data to database
        connection = pymysql.connect(host='localhost', user='root', password='', database='roaringl_requestquote')
        cursor = connection.cursor()
        sql = "INSERT INTO requestquote (first_name, last_name, email_address) VALUES (%s, %s, %s)"
        cursor.execute(sql, (first_name, last_name, email_address))
        connection.commit()

        # Send confirmation email
        send_email(first_name, last_name, email_address, form_data)

        return render_template("contactus.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/requestquote', methods=['GET', 'POST'])
def requestquote():
    if request.method == 'GET':
        return render_template("requestquote.html")
    else:
        # Extract form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email_address = request.form['email_address']
        form_data = request.form

        # Save form data to database
        connection = pymysql.connect(host='localhost', user='root', password='', database='roaringl_requestquote')
        cursor = connection.cursor()
        sql = "INSERT INTO requestquote (first_name, last_name, email_address) VALUES (%s, %s, %s)"
        cursor.execute(sql, (first_name, last_name, email_address))
        connection.commit()

        # Send confirmation email
        send_email(first_name, last_name, email_address, form_data)

        return render_template("requestquote.html")

@app.route('/amboseli')  
def amboseli():
    return render_template("amboseli.html")

@app.route('/mountkilimanjaro')
def mountkilimanjaro():
    return render_template("mountkilimanjaro.html")

@app.route('/nairobinationalpark')
def nairobinationalpark():
    return render_template("nairobinationalpark.html")

@app.route('/gateaway1')
def gateaway1():
    return render_template("gateaway1.html")

@app.route('/gateaway2')
def gateaway2():
    return render_template("gateaway2.html")


@app.route('/southisland')
def southisland():
    return render_template("southisland.html")

@app.route('/mountkenya')
def mountkenya():
    return render_template("mountkenya.html")

@app.route('/sibiloi')
def sibiloi():
    return render_template("sibiloi.html")

@app.route('/lakenakuru')
def lakenakuru():
    return render_template("lakenakuru.html")

@app.route('/lakenaivasha')
def lakenaivasha():
    return render_template("lakenaivasha.html")

@app.route('/serengeti')
def serengeti():
    return render_template("serengeti.html")

@app.route('/ngorongorocrater')
def ngorongorocrater():
    return render_template("ngorongorocrater.html")

@app.route('/lakemanyara')
def lakemanyara():
    return render_template("lakemanyara.html")

@app.route('/contactus')
def contactus():
    if request.method == 'GET':
        return render_template("contactus.html")
    else :
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        country = request.form['country']
        phone_number = request.form['phone_number']
        email_address = request.form['email_address']
        duration_of_tour = request.form['duration_of_tour']
        start_date = request.form['start_date']
        no_of_adults = request.form['no_of_adults']
        no_of_children = request.form['no_of_children']
        age_of_children = request.form['age_of_children']
        estimated_budget = request.form['estimated_budget']
        currency = request.form['currency']
        type_of_safari = request.form['type_of_safari']
        tour_description = request.form['tour_description']
        how_to_contact_you = request.form['how_to_contact_you']
       

        connection = pymysql.connect(host ='localhost',user='root', password='',database='roaringl_requestquote')
        cursor = connection.cursor()

        sql = "INSERT INTO requestquote (first_name,last_name,country,phone_number,email_address,duration_of_tour,start_date,no_of_adults,no_of_children,age_of_children,estimated_budget,currency,type_of_safari,tour_description,how_to_contact_you) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,(first_name,last_name,country,phone_number,email_address,duration_of_tour,start_date,no_of_adults,no_of_children,age_of_children,estimated_budget,currency,type_of_safari,tour_description,how_to_contact_you))
        connection.commit()

        return render_template("contactus.html")

@app.route('/tarangire')
def tarangire():
    return render_template("tarangire.html")


@app.route('/nakurudaytrip')
def nakurudaytrip():
    return render_template("nakurudaytrip.html")

@app.route('/akagera')
def akagera():
    return render_template("akagera.html")

@app.route('/nyungwe')
def nyungwe():
    return render_template("nyungweforest.html")

@app.route('/lakekivu')
def lakekivu():
    return render_template("lakekivu.html")

@app.route('/genocidemuseum')
def genocidemuseum():
    return render_template("genocidemuseum.html")

@app.route('/volcanoesnationalpark')
def volcanoesnationalpark():
    return render_template("volcanoes.html")

@app.route('/queenelizabeth')
def queenelizabeth():
    return render_template("queenelizabeth.html")

@app.route('/murchisonfalls')
def murchisonfalls():
    return render_template("murchisonfalls.html")

@app.route('/bwindiforest')
def bwindiforest():
    return render_template("bwindiforest.html")

@app.route('/kidepovalley')
def kidepovalley():
    return render_template("kidepovalley.html")

@app.route('/privacypolicy')
def privacypolicy():
    return render_template("privacypolicy.html")

@app.route('/termsandconditions')
def termsandconditions():
    return render_template("termsandconditions.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")

@app.route('/nairobidaytrip')
def nairobidaytrip():
    return render_template("nairobidaytrip.html")

@app.route('/naivashadaytrip')
def naivashadaytrip():
    return render_template("naivashadaytrip.html")

@app.route('/malindi')
def malindi():
    return render_template("malindi.html")

@app.route('/lamu')
def lamu():
    return render_template("lamu.html")

@app.route('/watamu')
def watamu():
    return render_template("watamu.html")

@app.route('/mombasa')
def mombasa():
    return render_template("mombasa.html")

@app.route('/diani')
def diani():
    return render_template("diani.html")

@app.route('/daynightpackage1')
def daynightpackage1():
    return render_template("daynightpackage1.html")

@app.route('/daynightpackage2')
def daynightpackage2():
    return render_template("daynightpackage2.html")

@app.route('/samburu')
def samburu():
    return render_template("samburu.html")
    



    
if"__main__"==__name__:
    app.run(debug=True)
    