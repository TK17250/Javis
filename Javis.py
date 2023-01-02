import pyttsx3 as tx
import speech_recognition as sr
import os

engine = tx.init()

# Setting Speak
TH = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI" # เพิ่มเสียงภาษาไทย
engine.setProperty("voice", TH)
engine.setProperty('rate', 190)

def speak(audio):
    engine.say(audio) # ให้ Ai พูด
    engine.runAndWait() # รอพูดจนจบ

# การทำงาน
def command():
    r = sr.Recognizer() # รับค่าจากการฟัง

    with sr.Microphone() as source:
        print("กำลังฟัง...")
        r.pause_threshold = 1 # รอคำสั่ง 1 วิ
        r.adjust_for_ambient_noise(source, duration= 1) # ปรับเสียงรบกวน
        audio = r.listen(source)

    try: # รับค่าเสียงได้
        print("รับค่าเสียง...")
        query = r.recognize_google(audio, language='th-TH')
        print(f"คุณพูดว่า >>> {query}\n")

    except  Exception as e:
        print(e)
        print("คุณพูดใหม่ได้ไหม")
        return  "None"
    return query

# คำสั่งต่างๆ
while True:
    query = command().lower()

    if query in query:
        speak(f"คุณพูดว่า >>> {query}")