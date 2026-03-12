import speech_recognition as sr
import tkinter as tk

r = sr.Recognizer()

def speak():
    with sr.Microphone() as mic:
        status_label.config(text="Listening...")
        window.update()
        r.adjust_for_ambient_noise(mic, duration=0.5)
        audio = r.listen(mic)

    try:
        text = r.recognize_google(audio)
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, text)
        status_label.config(text="Done")
    except:
        status_label.config(text="Could not understand")

window = tk.Tk()
window.title("Voice to Text")
window.geometry("400x300")

btn = tk.Button(window, text="Speak", command=speak, font=("Arial", 14))
btn.pack(pady=10)

text_box = tk.Text(window, height=5, font=("Arial", 12))
text_box.pack(pady=10)

status_label = tk.Label(window, text="Click Speak", font=("Arial", 10))
status_label.pack()

window.mainloop()
