import requests
from model.user_model import User

api_login = 'http://localhost:8004/apiprov/login.php'
api_register = 'http://localhost:8004/apiprov/register.php'
api_get_rule = 'http://localhost:8004/apiprov/getdatarule.php'
api_join_telegram = 'http://localhost:8004/apiprov/telegram.php'
api_get_telegram = 'http://localhost:8004/apiprov/telegram_getdata.php'
api_activity = 'http://localhost:8004/apiprov/activity.php'

class Login:
    def __init__(self,username,password):
        body = {"username":username,"password":password}
        response = requests.post(api_login,json=body)
        user = response.json()
        User.name=user[0]['name']
        User.password=user[0]['password']
        User.email=user[0]['email']
        User.telp=user[0]['telp']
        User.catagory=user[0]['catagory']

class Register:
    def __init__(self,username,password,telp,email,gender,department,catagory,group,idtelegram):
        body = {"username":username,
                "password":password,
                "telp":telp,
                "email":email,
                "gender":gender,
                "department":department,
                "catagory":catagory,
                "group":group,
                "idtelegram":idtelegram}
        requests.post(api_register,json=body)

class get_rule:
    def __init__(self,username):
        body={"username":username}
        response=requests.post(api_get_rule,json=body)
        rule = response.json()

class register_telegram:
    def __init__(self,username,telegram):
        body={"username":username,"telegram":telegram}
        requests.post(api_join_telegram,json=body)

class get_telegram:
    def __init__(self):
        response = requests.get(api_get_telegram)
        telegram = response.json()
        User.telegram=telegram
        #for i in telegram:
        #    User.telegram.append(i['telegramid'])

class activity:
    def __init__(self,username,activity) -> None:
        body={"username":username,"activity":activity}
        requests.post(api_activity,json=body)
        