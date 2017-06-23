import requests
from bs4 import BeautifulSoup
# from BeautifulSoup import *
html = ""
guest = []


with open("C:/Users/Mariano/Desktop/test-scrapper/georgia.html", 'r')as input:
    html = input.read()

soup = BeautifulSoup(html, 'lxml')

ulChildren = soup.find("div", {"class", "content"})
# ulChildren = BeautifulSoup(ulChildren.finfChildren("ul"), 'lxml')

# ========Customer details div
customerDetail = ""
for line in soup.find_all("ul", {"class", "customer-details"}):
    customerDetail = customerDetail + str(line)

customerDetail = BeautifulSoup(customerDetail, 'lxml')

# =============  payment div =========================
payment = soup.find('div', {'prices-total'})
payment = BeautifulSoup(str(payment.findChildren("li")), 'lxml')


for x in range(1, len(customerDetail.find_all("li")), 2):
    guest.append(customerDetail.find_all("li")[x].text)

print "---------------------------------------"
#  ---------- - -----NAME------------- - - -----"
print guest[0]
# -=-=-=-==-=-=EMAIL -=-=-=-=-=-=-
print str(guest[1]).strip(" ")

# ---------------telephone
print guest[2]


print "- - - - - - - - - -check in - - - - - - - - - - - - -"
# -------------------- check in ---------------
print ulChildren.findChildren('ul')[1].findChildren('li')[0].text

print "- - - - - - - - - NIGHTS- - - - - - - - - - - - - -"
# --------------------NIGHTS ---------------
print len(ulChildren.findChildren('ul')) - 1

print "- - - - - - - - - Adults- - - - - - - - - - - - - -"
# --------------------NIGHTS ---------------
print ulChildren.findChildren('ul')[1].findChildren('li')[3].text

# --$-$-$-$-$-$-$-$-$- TOTAL ---------------
print "- - - - - - - - - TOTAL- - - - - - - - - - - - - -"
print str(payment.findChildren('li')[7].text).split(" ")[1]
