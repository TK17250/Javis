import pyttsx3 as tx
import speech_recognition as sr
import os

engine = tx.init()

# Setting Speak
TH = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI" # เพิ่มเสียงภาษาไทย
engine.setProperty("voice", TH)
engine.setProperty('rate', 190)
volume = engine.getProperty('volume')

def speak(audio):
    engine.say(audio) # ให้ Ai พูด
    engine.runAndWait() # รอพูดจนจบ

# การทำงาน
def command():
    r = sr.Recognizer() # รับค่าจากการฟัง

    with sr.Microphone() as source:
        print("กำลังฟัง...")
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
speak("สวัสดีครับ ผมชื่อ จาวิส มีอะไรให้ผมช่วยก็บอกมาเลยนะครับ") # คำพูดเริ่มต้น
while True:
    query = command().lower()

    # เปิด ไฟล์
    if "เปิดไฟล์" in query:
        os.startfile("D:")

    # เรียกหา
    elif "จาวิส" and "จาร์วิส" in query:
        speak("มีอะไรให้ช่วยครับ")

    # เปิด vs code
    elif "เปิด vscode" and "เปิด vs code" in query:
        os.startfile("E:\Visual Studio code\Microsoft VS Code\Code.exe")

    # เปิดระบบ
    elif "เปิดระบบ" in query:
        engine.setProperty('volume',1)
        speak("ทำการเปิดระบบใหม่อีกครั้ง")

    # ปิดระบบ
    elif "ปิดระบบ" in query:
        speak("ทำการปิดระบบ")
        engine.setProperty('volume',0)
