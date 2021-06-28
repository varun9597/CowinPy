# CowinPy

We all know how difficult it is to find a slot on CoWin Website. If you are not alert and quick, you might miss your chance!
This small prototype has helped me and my friends book vaccination slots in nearby area as soon as they open up.

Just a few steps for initialization and you are good to go!


## Basic Steps for initialization

## Create a Twilio Account

1. Visit https://www.twilio.com/console

2. Create a new account or login using existing one.

3. Copy the account SID and Auth Token in the code

4. Go to Phone Numbers tab.

5. Buy a Phone Number (US/UK). You have a 7 day free trial. No credit card information required!!

6. Once bought, click on the phone number which will take you to configurrartion page.

7. Under - "A call comes in" tab, paste this URL - "http://static.fullstackpython.com/phone-calls-python.xml"
This is a standard text and is not that relevant.

8. Change drop-down to HTTP GET 

9. Click on Save

10. Copy this number and paste in the code.

You have now setup your phone number from which you will receive calls as soon as a slot opens.

## EDIT CODE

1. Edit the MY_PINCODE variable with the nearby pincodes where vaccination drive is happening. These pincodes will be used to check if any slot is available on CoWin.
2. Edit the DISTRICT_CODE varible using the district_mapping.csv file.
3. Edit DIAL_NUMBERS variable and enter the number on which you want to get the call.

### NOTE -  The current code works for - DOSE 1 for 18+ Citizen and once you get the call, you will have to register using the Cowin App
#### PS. It took 1 hour to develop this code, and I was vaccinated within the next 12 hours.
