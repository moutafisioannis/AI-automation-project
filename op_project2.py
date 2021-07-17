# Importing required modules
import pyttsx3
import stoixeia
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
    # Method to take coice commands as input
def takeCommands():
    engine = pyttsx3.init('sapi5')

    # Setting voice type and id
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say('Tell me the message you want to send.')
    engine.runAndWait()

    # Using Recognizer and Microphone Method for input voice commands
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')

        # Number pf seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 1
        audio = r.listen(source)

        # Voice input is identified
        try:

            # Listening voice commands in english
            print("Recognizing")
            query = r.recognize_google(audio, language='el')

            # Displaying the voice command
            print("the query is printed='", query, "'")

        except Exception as e:

            # Displaying exception
            print(e)
            # Handling exception
            print("Say that again sir")
            return "None"
        user = stoixeia.user # Your username inside ''
        pw = stoixeia.pw  # Your password inside ''
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get('https://el-gr.facebook.com/')
        cookies = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]")
        cookies.click()
        username = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
        username.click()
        username.send_keys(user)
        password = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input")
        password.click()
        password.send_keys(pw)
        password.send_keys(Keys.RETURN)
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[2]/span/div/div[1]").click()
        time.sleep(6)
        search = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/div/label/input")
        search.click()
        engine.say('Where do you want to send the message?')
        engine.runAndWait()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening')

            # Number pf seconds of non-speaking audio before
            # a phrase is considered complete
            r.pause_threshold = 1
            audio = r.listen(source)

            # Voice input is identified
            try:

                # Listening voice commands in english
                print("Recognizing")
                member = r.recognize_google(audio, language='el')

                # Displaying the voice command
                print("the query is printed='", member, "'")

            except Exception as e:

                # Displaying exception
                print(e)
                # Handling exception
                print("Say that again sir")
                return "None"


        time.sleep(1)
        member.strip()
        first = member[0].capitalize()
        member2 = member.replace(member[0], first, 1)
        search.send_keys(member2)
        time.sleep(4)
        driver.find_element_by_partial_link_text(member2).click()  # Where will you send the message , inside ""
        time.sleep(2)
        text = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div")
        text.click()
        text.send_keys(query)  # Your message inside ' '
          # Seconds waiting before send the message inside ()
        text.send_keys(Keys.RETURN)
        time.sleep(2)
    return query

takeCommands()
