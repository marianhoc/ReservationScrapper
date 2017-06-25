import requests
from bs4 import BeautifulSoup


login_form_action = "https://inbox.hostelworld.com/inbox/trylogin.php"
reservation_page = "https://inbox.hostelworld.com/booking/view/"

def getToken():
    login = requests.get("https://inbox.hostelworld.com/inbox/index.php")
    soup = BeautifulSoup(login.text, 'lxml')
    return soup.find("form").findChildren('input')[0].get('value')

def getLogin_data(id, user, password):
    login_data = {'formToken': getToken(),
                  'SessionLanguage': 'English',
                  'HostelNumber': id,
                  'Username': user,
                  'Password': password}
    return login_data

def getReservationPage(id,user, password, reservation_number):
    with requests.Session() as c:
        login_data = getLogin_data(id, user, password)
        c.post(login_form_action, data=login_data, headers={"Referer":"https://inbox.hostelworld.com/inbox/index.php"})

        return c.get(reservation_page + str(reservation_number)).content
