from django.contrib.auth.hashers import make_password,check_password
from cryptography.fernet import Fernet
import datetime
import time
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from myapp.settings import EMAIL_HOST_USER

key = b'wvq8tuxUG7e08mpXxSnWSnMlbshTx0BhU9ZLTNQscDw=' 
fernet = Fernet(key)
def create_token(username):
    verify = (make_password(username+'user'))
    expire = str(datetime.datetime.now()+datetime.timedelta(minutes=10))
    expire = fernet.encrypt(expire.encode())
    expire = expire.decode("utf-8") 
    resp = {"verify":verify , "user":username,"token":expire}
    return resp
def verify_token(verify , username, token):
    token = bytes(token, 'utf-8')
    dec = fernet.decrypt(token).decode()
    exprie = datetime.datetime.strptime(dec,'%Y-%m-%d %H:%M:%S.%f')
    if(datetime.datetime.now()<exprie):
        if check_password(username+'user',verify):
            return True
        else:
            return False
    else:
        return False
def send_token(request,username,name):
    token = create_token(username)
    token['host'] = request.get_host()
    subject = str(name) +' verification'
    html_message = render_to_string('email.html', token)
    plain_message = strip_tags(html_message)
    from_email = EMAIL_HOST_USER
    # to = 'Navneet.cyberflax@gmail.com'
    to = username
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
