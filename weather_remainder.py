import schedule
import smtplib
import requests
from bs4 import BeautifulSoup
import time  
import pywhatkit as pyw

def wp_umbrella_reminder(hrs, mins, phone_number, msg_body):
    print(msg_body)
    pyw.sendwhatmsg(phone_no= phone_number, message= msg_body, time_hour= int(hrs), time_min= int(mins))

def umbrella_reminder(body, mail, password):
    try:
        # Connect to SMTP server
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_object.starttls()  # Start TLS encryption
        smtp_object.login(mail, password)  # Authenticate
        
        # Set email details
        subject = "Umbrella Reminder"
        msg = f"Subject: {subject}\n\n{body}"
        
        # Send email
        smtp_object.sendmail(mail, mail, msg)
        smtp_object.quit()
        print("✅ Email Sent Successfully!")
    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication error: Check your email or app password settings.")
    except smtplib.SMTPException as e:
        print(f"❌ SMTP error occurred: {e}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


def check_weather():
    city = input("🌍 Hey there! What's the name of your city? 🏙️: ")
    mail = input("📧 Drop your email address here to stay updated: ")
    password = input("🔒 Enter your email password (safe with us 🤞): ")
    hrs = int(input("Enter hours in 24 hours format: "))
    mins = int(input("Enter mins in 24 hours format: "))
    phone_number = input("Enter the phone number with country code: ")
    url = f"https://www.google.com/search?q=weather+{city}"
    
    try:
        # Scrape weather data
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        sky = time_sky.split('\n')[1]

        # Check for rainy conditions
        if sky.lower() in ["rainy", "rain and snow", "showers", "haze", "cloudy"]:
            body = (
                f"🌂 Don't forget your umbrella before heading out!\n"
                f"🌦️ Today's forecast: {sky} with a temperature of {temperature} in {city}.\n\n"
                f"Stay dry and stylish! ✨\n"
                f"Cheers, 🌟\nYour Weather Bot 🤖"
            )
            wp_umbrella_reminder(hrs, mins, phone_number, body)
            umbrella_reminder(body, mail, password)
            print(body)
        else:
            body = (
                f"☀️ Good news! No rain today. 😎\n\n"
                f"Weather for today in {city}: {sky}\n"
                f"🌡️ Temperature: {temperature}\n\n"
                f"Enjoy your day! 🌈\nYour Weather Bot 🤖"
            )
            wp_umbrella_reminder(hrs, mins, phone_number, body)
            umbrella_reminder(body, mail, password)
            print("Scheduled umbrella reminder.")
            print(f"Today's weather in {city} is {sky}. No umbrella needed.")

        # Schedule email reminder
        schedule.every().day.at(f"{hrs:02}:{mins:02}").do(umbrella_reminder, body=body, mail=mail, password=password)

    except Exception as e:
        print(f"Error fetching weather data: {e}")

# Call weather function
check_weather()

# Run scheduled tasks
while True:
    schedule.run_pending()
      

