import requests
from bs4 import BeautifulSoup
import time
# italian passport slots check everybody who has italian passport can never
# get appoiment so i decided to create  this code 
# to improve my chances of getting a italian passport renew 

#url the web address you would liek to use to check for the slots 
url = "https://conslondra.esteri.it/en/news/dal_consolato/2021/06/prenot-mi-2/"

def check_appointment_availability():
    # this function ill perform 
    #the task of checking for appointment
    
    response = requests.get(url)# library to send an HTTP GET request to 
    # the speciffied URL
    
    if response.status_code == 200:# HTTP reponse status is 200, wich indicates a sucessfull request
        soup = BeautifulSoup(response.text, 'html.parser')

        #  Check if a specific span element with class "availability" exists
        availability_element = soup.find('span', class_='availability')

        if availability_element and 'available' in availability_element.text.lower():
            print("Slots are available!")# if slots are find we ill get a message notification
            return True
        else:
            print("No available slots.")# if there is not slost this message ill be printed every 1 min
            return False
    else:
        print("Error accessing the website. Status code:", response.status_code)
        return False # any issue to ascess the website a Error message ill be displayed

if __name__ == "__main__":
    while True:# while loop ill keep checking for slots until; it find one 
        if check_appointment_availability():
            # If slots are available, exit the loop
            break
        else:
            # If no slots are available, wait for 1 minutes before checking again
            print("Waiting for 1 minutes before checking again...")
            time.sleep(60)  # 60 seconds = 1 minutes
