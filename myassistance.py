import pyttsx3 as pt
import os 
import speech_recognition as sr
p=pt.speak(" hello      i     am     lani     what     can    i     help you ")

while True:
	r=sr.Recognizer()
	with sr.Microphone() as source:
   		print(" Listening...............")
   		audio= r.listen(source)
		r.energy_threshold = 300 
   		text= r.recognize_google(audio)
   		print('you said: ' , text)

	if (("Run" in text) or ("execute" in text) or ("open" in text) or ("run" in text)) and (("Chrome" in text ) or ("chrome" in text ) or ("browser" in text)):
		pt.speak("Launching     Chrome     Browser")
		os.system("chrome")
	elif (("Run" in text) or ("execute" in text) or ("open" in text) or ("run" in text)) and (("notepad" in text ) or ("text editor" in text ) or ("Notepad" in text)):
		pt.speak("Launching     Notepad     Editor")
		os.system("notepad")
	elif (("Run" in text) or ("execute" in text)or ("open" in text) or ("run" in text)) and (("camera" in text ) or ("Camera" in text ) ):
		pt.speak("Launching        Camera ")
		os.system("start microsoft.windows.camera:")
	elif (("close" in text) or ("stop" in text)or ("Close" in text) or ("Stop" in text)) and (("Chrome" in text ) or ("chrome" in text ) ):
		pt.speak("Closing       Chrome Browser ")
		os.system("TASKKILL/IM chrome.exe")
	elif (("Run" in text) or ("execute" in text) or ("open" in text) or ("run" in text)) and (("notepad" in text ) or ("text editor" in text ) or ("Notepad" in text)):
		pt.speak("Closing       Notepad Editor ")
		os.system("TASKKILL/IM notepad.exe")
	elif (("Run" in text) or ("execute" in text)or ("open" in text) or ("run" in text)) and (("camera" in text ) or ("Camera" in text ) ):
  		os.system("TASKKILL/IM camera.exe")
	elif (("Run" in text) or ("execute" in text)or ("open" in text) or ("run" in text)) and ((" WinSCP" in text ) or ("winscp" in text ) or ("win scp" in text ) or ("Win SCP" in text ) ):
  		os.system("C:\Program Files (x86)\WinSCP\WinSCP.exe")
	elif (("play" in text) or ("execute" in text)or ("open" in text) or ("Play" in text)) and ((" music" in text ) or ("Music" in text ) or ("MUSIC" in text )  ):
  		os.system("E:\lalit  drive\songs\i know what you did last summer.mp3")
	elif (("exit" in text) or ("close" in text) ) and (("app" in text ) or ("assistance" in text ) ):
  		break

	else:
		print("not support")
		pt.speak(" Not       Support     Please     do          Try      Again ")


