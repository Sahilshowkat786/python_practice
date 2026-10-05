import win32com.client

items = ["welcome Sahil", "welcome arsalan", "welcome nadeem", "welcome fatima", "welcome ishfaq ahmad "]

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for item in items:
    print("Speaking:", item)
    speaker.Speak(item)