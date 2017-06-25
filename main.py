from bs4 import BeautifulSoup
import GetRoomID


def import_reservation(gds, guest):
    xml =   '<Bookings><Authentication username="bframe" password="bframe" />' \
            '<Hotel id="'+ gds +'" />' \
            '<Booking id="" type="Book" createDateTime="" source="HW">' \
            '<RoomStay roomTypeID="Dorm6" ratePlanID="" roomTypeName="">' \
            '<StayDate arrival="'+ guest['check_in'] +'" departure="" />' \
            '<RoomCount NumberOfUnits="'+ guest['adults'] +'" />' \
            '<GuestCount adult="'+ guest['adults'] +'" child="0" baby="0" />' \
            '<PerDayRates CurrencyCode="USD">' \
            '<PerDayRate stayDate="" baseRate="" />' \
            '<PerDayRate stayDate="" baseRate="" />' \
            '<PerDayRate stayDate="" baseRate="" /></PerDayRates>' \
            '<Total AmountAfterTaxes="" CurrencyCode="" />' \
            '<GuestNames><Name givenName="'+ str(guest['name']).split()[0] +'" surname="'+ str(guest['name']).split()[1] +'" /></GuestNames>' \
            '</RoomStay><PrimaryGuest>' \
            '<Name givenName="'+ str(guest['name']).split()[0] +'" surname="'+ str(guest['name']).split()[1] +'" /><Address Street="" Zip="" City="" /><Country CountryName="" iso2="" iso3="" /><Language iso2="" />' \
            '<Email>'+ guest['email'] +'</Email><Phone>'+ guest['phone'] +'</Phone><Fax></Fax>' \
            '<CreditCard Type="" Number="" NameOnCard="" Expirationdate="" />' \
            '</PrimaryGuest><Remarks></Remarks>' \
            '<ResGlobalInfo><Timespan arrival="" departure="" /><Total AmountAfterTaxes="' + guest['total'] + '" CurrencyCode="USD" />' \
            '</ResGlobalInfo></Booking></Bookings>'

    return xml

with open("C:/Users/Mariano/Desktop/test-scrapper/georgia.html", 'r')as input:
    html = input.read()

# hostel_id = raw_input("hostel ID = ")
# user = raw_input("user = ")
# password = raw_input("password = ")
# res_number = raw_input("reservation number = ")


# html = GetRoomID.getReservationPage(hostel_id, user, password, res_number)

soup = BeautifulSoup(html, 'lxml')
guest = {}
guest['name'] = soup.find("ul", {"class", "customer-details"}).findChildren("li")[1].text
guest['email'] = soup.find("ul", {"class", "customer-details"}).findChildren("li")[3].text
guest['phone'] = soup.find("ul", {"class", "customer-details"}).findChildren("li")[5].text

# =============  payment div =========================
payment = soup.find('div', {'prices-total'})
payment = BeautifulSoup(str(payment.findChildren("li")), 'lxml')

ulChildren = soup.find("div", {"class", "content"})
guest['check_in'] = ulChildren.findChildren('ul')[1].findChildren('li')[0].text
guest['room_type'] = ulChildren.findChildren('ul')[1].findChildren('li')[2].text.encode('utf-8')[53:-101]
guest['nights'] = len(ulChildren.findChildren('ul')) - 1
guest['adults'] = ulChildren.findChildren('ul')[1].findChildren('li')[3].text
guest['total'] = str(payment.findChildren('li')[7].text).split(" ")[1]


line = "{},{},{},{},{},{},{},{},{}".format(str(guest['name']).split()[0],
                                        str(guest['name']).split()[1],
                                            guest['email'],
                                            guest['phone'],
                                            guest['check_in'],
                                            guest['room_type'],
                                            guest['nights'],
                                            guest['adults'],
                                            guest['total'])
print line

print import_reservation("fedetest", guest)