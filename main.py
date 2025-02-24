import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import lxml, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# URL_FLIPKART = "https://www.flipkart.com/motorola-edge-40-neo-black-beauty-128-gb/p/itm01cc46d96a79f?pid=MOBGQFX6JGTWFSGD&lid=LSTMOBGQFX6JGTWFSGDB2AE0L&marketplace=FLIPKART&q=motorola+edge+40+neo&store=tyy%2F4io&srno=s_1_3&otracker=search&otracker1=search&iid=42de1e08-13d6-43ba-8fa4-4799c5c9d745.MOBGQFX6JGTWFSGD.SEARCH&ssid=mp0xajz7y80000001699178472604&qH=1f37101527ee1311"
# URL_FLIPKART = "https://www.flipkart.com/marq-flipkart-1-5-ton-3-star-split-ac-white/p/itmfdfjx3arqvngw?pid=ACNFU3XZGGXGX4RK&lid=LSTACNFU3XZGGXGX4RKWZRWKC&marketplace=FLIPKART&q=ac+1.5+ton&store=j9e%2Fabm%2Fc54&srno=s_1_1&otracker=AS_Query_HistoryAutoSuggest_1_6_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_6_na_na_na&fm=search-autosuggest&iid=9622f87a-2392-4bf2-a87c-fcb3287cc7e8.ACNFU3XZGGXGX4RK.SEARCH&ppt=sp&ppn=sp&ssid=owmu5ifya80000001699181924257&qH=09362e2862616907"
# URL_FLIPKART = "https://www.flipkart.com/marq-flipkart-2023-range-1-5-ton-4-star-split-inverter-4-in-1-convertible-turbo-cool-technology-ac-white/p/itmc5cf16283e54b?pid=ACNGH7EZ2ZHHGQ6H&lid=LSTACNGH7EZ2ZHHGQ6HJNCNFH&marketplace=FLIPKART&q=ac+1.5+ton&store=j9e%2Fabm%2Fc54&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=en_LPDFcIF3GiHyPb5Btxpv1cO2NxZxBOnMKcFAYjHppHQgyLD0b6gTdCqahfrPjdVNqUuPyB9PAKWA-pKNkRX2tg%3D%3D&ppt=sp&ppn=sp&ssid=q5h3mnly7k0000001699266918080&qH=09362e2862616907"
URL_FLIPKART = 'https://www.flipkart.com/samsung-galaxy-s23-ultra-5g-green-256-gb/p/itm77dc35f7779a4?pid=MOBGMFFX32WUYXUJ&lid=LSTMOBGMFFX32WUYXUJEUVNIW&marketplace=FLIPKART&q=samsung+s23+ultra&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_HistoryAutoSuggest_8_0_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_8_0_na_na_na&fm=organic&iid=2a236251-7b2a-4ff0-8696-7db9a194c65e.MOBGMFFX32WUYXUJ.SEARCH&ppt=hp&ppn=homepage&ssid=znmgqd0hps0000001705689269637&qH=7f515a0e0499d18d'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL_FLIPKART)
price = driver.find_element(By.CLASS_NAME, "_16Jk6d").text
amount = (price.split('₹')[1].split(','))
float_amount = ''
for item in amount:
    float_amount = float_amount + item
float_amount = float(float_amount)
title = driver.find_element(By.CLASS_NAME, "B_NuCI").text
print(float_amount)
print(title)
try:
    sold = driver.find_element(By.CLASS_NAME, '_16FRp0').text
except:
    if float_amount < 23000:
        sender_email = "manyasah.lko@gmail.com"
        sender_password = ""
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = 'manyasah12b1@gmail.com'
        msg['Subject'] = "Hurry!"
        html_part = MIMEText(f'<p>{title} is now {price}\n{URL_FLIPKART}<br><br><a href="https://manyasahlko.wixsite.com/bargainhunt">Unsubscribe here</a> to stop recieving notifications.</p>','html')
        msg.attach(html_part)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connections:
            connections.starttls()
            connections.login(user="manyasah.lko@gmail.com", password="")
            connections.sendmail(from_addr="manyasah.lko@gmial.com", to_addrs="manyasah12b1@gmail.com", msg=msg.as_string().encode("utf-8"))

else:
    print("sold out")
    # pass

driver.quit()
