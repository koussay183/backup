import win32com.client as w
speak = w.Dispatch('SAPI.SpVoice')
v = input('enter text :')
while True :
    speak.Speak(v)

