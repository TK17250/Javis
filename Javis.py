import pyttsx3 as tx
import speech_recognition as sr
import os
import random

engine = tx.init()

# อาหารแต่ละมื้อ
Food = ["ยำไข่ดาว","กระเพราหมูกรอบ","ส้มตำ","กระเพราหมูสับ","ข้าวผัด","สเต็ก"]

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

# Login
# bin to text > ประมวลข้อความ > ถ้าผ่านก็เข้าระบบได้
# สร้างตัวแปร = Binary
A = str("01000001")
B = str("01000010")
C = str("01000011")

pas = str(f"{A} {B} {C}") # บวกข้อความ Binary

speak("คุณต้องยืนยันตัวตนถึงจะใช้งานได้")
Binary = str(input("ใส่รหัส A B C >>> ")) # input เลข Binary

if Binary == str(pas):
    # คำสั่งต่างๆ
    speak("เข้าสู่ระบบสำเร็จ")
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

      # สุ่มอาหาร
      elif "มื้อนี้กินอะไรดี" in query:
         speak(f"ผมว่าอาหารมื้อนี้กิน {random.choice(Food)} นะครับ")

      # เปิดเพลง
      elif "เปิดเพลง" in query:
          os.startfile("D:\Desktop\YouTube Music.lnk")

      # เปิดDiscord
      elif "เปิดDiscord" or "เปิดดิสคอร์ด"  in query:
          os.startfile("D:\Desktop\Discord.lnk")

else:
    speak("เกิดข้อผิดพลาด")