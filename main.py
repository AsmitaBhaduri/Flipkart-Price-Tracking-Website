import requests
from urllib.parse import quote
from flask import Flask,request
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import lxml, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

today_date = datetime.date.today()   #Today's date

# fetching user information
info = requests.get("https://api.sheety.co/459bcd038f36ffc952b27b5a90e867ef/contactInformation (responses)/formResponses1")
unsubscribe = requests.get("https://api.sheety.co/459bcd038f36ffc952b27b5a90e867ef/unsubscribe (responses)/formResponses1")
for item in info.json()['formResponses1']:
        signin_date = (item["timestamp"]).split()[0]    #date of registration
        day_thirty = datetime.datetime.strptime(signin_date,'%d/%m/%Y').date() + datetime.timedelta(days=30)     #30 days date of registration
        if(today_date>day_thirty):            #checking for validity of search
            requests.delete(url=f'https://api.sheety.co/459bcd038f36ffc952b27b5a90e867ef/contactInformation (responses)/formResponses1/{item["id"]}')  #deleting the row

        URL_FLIPKART = item['urlOfProduct']

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(URL_FLIPKART)
        price = driver.find_element(By.CLASS_NAME, "_16Jk6d").text
        amount = (price.split('₹')[1].split(','))
        float_amount = ''
        for i in amount:
            float_amount = float_amount + i
        float_amount = float(float_amount)
        title = driver.find_element(By.CLASS_NAME, "B_NuCI").text

        try:
            sold = driver.find_element(By.CLASS_NAME, '_16FRp0').text    #checking if item is available
        except:
            if float_amount < item['price']:                             #if item is available then ckeck if it is less than desired price
                sender_email = "your_gmail_id@gmail.com"
                sender_password = "your_password"
                msg = MIMEMultipart('alternative')
                msg['From'] = sender_email
                msg['To'] = item['email']
                msg['Subject'] = "Hurry! Bargain price met"
                user_id = item["id"]
                base_url = 'http://127.0.0.1:5500/unsubscribe.html'
                unsubscribe_link = f"{base_url}?user_id={user_id}"
                # html_part = MIMEText(f'<p>{title} is now {price}\n{URL_FLIPKART}<br><br><a href="https://docs.google.com/forms/d/e/1FAIpQLSdgx-h7FIefrVnOOjdgLzDgt0L0rXiWIyTifUjh8PqHUo5VrQ/viewform?usp=sf_link">Unsubscribe here</a> to stop recieving notifications. Your unique id = {item["id"]}.</p>','html')
                html_part = MIMEText(f'<p>{title} is now {price}\n{URL_FLIPKART}<br><br><a href={unsubscribe_link}>Unsubscribe here</a> to stop recieving notifications.</p>','html')
                msg.attach(html_part)

                with smtplib.SMTP("smtp.gmail.com", port=587) as connections:
                    connections.starttls()
                    connections.login(user="your_gmail_id@gmail.com", password="your_password")
                    connections.sendmail(from_addr="your_gmail_id@gmail.com", to_addrs=item['email'], msg=msg.as_string().encode("utf-8"))

        else:
            #print("sold out")
             pass

        driver.quit()
