import requests
from bs4 import BeautifulSoup
import time
import winsound

def beep(number):
    for i in range(number):
        winsound.Beep(500, 500)
        time.sleep(0.5)

while True:
    url = "https://examresults.dcu.ie/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    if str(soup.text).find("Examination results will be available on Thursday, June 25, 2020.") != -1:
        print("Exam Results Not Out Yet")
        time.sleep(120)
    else:
        print("Results are out")
        beep(25)