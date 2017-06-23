import requests
from bs4 import BeautifulSoup

reservation = "https://inbox.hostelworld.com/booking/view/293725228"

with requests.Session() as c:
    url = "https://inbox.hostelworld.com/inbox/trylogin.php"
    id = "273910"
    user = "minihotel"
    password = "Fede@2001"

    login = requests.get("https://inbox.hostelworld.com/inbox/index.php")
    soup = BeautifulSoup(login.text, 'lxml')

    formToken = soup.find("form").findChildren('input')[0].get('value')

    login_data = {'formToken':formToken,
                  'SessionLanguage': 'English',
                  'HostelNumber': id,
                  'Username': user,
                  'Password': password}

    c.post(url, data=login_data, headers={"Referer":"https://inbox.hostelworld.com/inbox/index.php"})

    manage_rooms = "https://inbox.hostelworld.com/manage/rooms"
    rooms_rates = c.post(manage_rooms).json()
    # soup_of_rooms = BeautifulSoup(rooms_rates.content, 'lxml')
    print rooms_rates

    # page = c.get(reservation)
    # print page.content
