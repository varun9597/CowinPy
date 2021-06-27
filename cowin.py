import requests
import datetime
import json
import time

from twilio.rest import TwilioRestClient

centre_det = []

#Edit this variable with the nearby pincodes
MY_PINCODE = [400608,400708,421308,400607,400602,400606,400605,400601,400710,400709,400602,400603,400703,400604]
TWILIO_PHONE_NUMBER = "+15103943669"

# list of one or more phone numbers to dial, in "+19732644210" format
DIAL_NUMBERS = ["+91123456789"]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
accountSID = "ENTER-YOUR-ACCOUNT-SID"
authToken = "ENTER-YOUR-AUTH-TOKEN"

client = TwilioRestClient(accountSID, authToken)

def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")

while(True):
    #print('Hi')
#GET THE REQUIRED DATES
    dateneed = datetime.date.today() + datetime.timedelta(days=1)
    tom_date = dateneed.strftime('%d/%m/%Y')
    tod_date = datetime.datetime.today().strftime('%d/%m/%Y')

#FETCH RESPONSE FROM COWIN FOR THANE AND TOMORROW'S DATE
    responses = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=392&date={0}".format(tod_date))
    responses2 = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=392&date={0}".format(tom_date))
    #print(responses.json())

#SAVE RESPONSES IN A JSON FILE
    with open('sample.json',"w") as json_file_write:
        json.dump(responses.json(),json_file_write,indent=6)

    with open('sample.json') as json_file_read:
        response_dict = json.load(json_file_read)
    
    with open('sample2.json',"w") as json_file_write:
        json.dump(responses2.json(),json_file_write,indent=6)

    with open('sample2.json') as json_file_read:
        response_dict2 = json.load(json_file_read)

    #print(response_dict['sessions'][0])
    
    #print(response_dict2)

#RUN LOOP ON THE RESPONSE, START CALL WHEN AGE LIMIT IS 18 AND DOSE1 IS AVAILABLE AND PINCODE IS IN LIST
    for i in range(0,len(response_dict['sessions'])) :
        if(response_dict['sessions'][i]['min_age_limit']<45
        and response_dict['sessions'][i]['available_capacity_dose1']>2
        and response_dict['sessions'][i]['pincode'] in MY_PINCODE
        #and response_dict['sessions'][i]['vaccine']=='COVISHIELD'
        ):

            centre_det.append(response_dict['sessions'][i])
            print(str(response_dict['sessions'][i]['pincode'])  +","+response_dict['sessions'][i]['name'])

    for i in range(0,len(response_dict2['sessions'])) :
        if(response_dict2['sessions'][i]['min_age_limit']<45
        and response_dict2['sessions'][i]['available_capacity_dose1']>2
        and response_dict2['sessions'][i]['pincode'] in MY_PINCODE
        #and response_dict2['sessions'][i]['vaccine']=='COVISHIELD'
        ):

            centre_det.append(response_dict2['sessions'][i])
            print(str(response_dict2['sessions'][i]['pincode'])+","+response_dict2['sessions'][i]['name'])

#CALL IF ANY CENTRE IS AVAILABLE
    if(len(centre_det)>0):
        dial_numbers(DIAL_NUMBERS)
        time.sleep(30)
        centre_det = []
    
        


