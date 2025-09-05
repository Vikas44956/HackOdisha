import tkinter as tk
import pywhatkit
import threading
import time
import pygame
import geocoder

# Get current location
g = geocoder.ip('me')
lat, lon = g.latlng

targetnum = "+917877756421"
msg = f"🚨 EMERGENCY ALERT \n🚨This is an SOS message from Vikas\n📍 Location: {lat,lon}\nPlease help immediately!"

cancel_flag = False

def send_sos():
    try:
        pywhatkit.sendwhatmsg_instantly(targetnum, msg, wait_time=15, tab_close=True)
        pygame.mixer.init()
        pygame.mixer.music.load("siren.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print("Error:", e)

def start_countdown():
    """Start 5 second countdown with Cancel option"""
    def countdown():
        global cancel_flag
        cancel_flag = False
        for i in range(5, 0, -1):
            if cancel_flag:
                label.config(text="🚫 Cancelled")
                return
            label.config(text=f"Sending SOS in {i} sec...")
            time.sleep(1)
        label.config(text="🚨 SOS Triggered 🚨")
        send_sos()
    threading.Thread(target=countdown).start()

def cancel_sos():
    """Cancel SOS process"""
    global cancel_flag
    cancel_flag = True

# Canvas click handler
def sos_action(event):
    start_countdown()

# -------------------- GUI --------------------
root = tk.Tk()
root.title("EMERGENCY SOS")
root.geometry("900x900")
root.config(bg="gray20")

tk.Label(root, text="EMERGENCY SOS APP", font=("bold",50), fg="white", bg="gray20").pack(pady=20)

canvas = tk.Canvas(root, width=400, height=400, bg="gray20", highlightthickness=0)
canvas.pack()

circle = canvas.create_oval(125, 125, 275, 275, fill="red", outline="")
text = canvas.create_text(200, 200, text="SOS", fill="white", font=("Arial", 25, "bold"))
msg1 = canvas.create_text(200, 300, text="Emergency Help", fill="white", font=("Arial", 15, "bold"))

# Label for countdown messages
label = tk.Label(root, text="", font=("Arial", 20), fg="white", bg="gray20")
label.pack(pady=20)

# Bind click
canvas.tag_bind(circle, "<Button-1>", sos_action)
canvas.tag_bind(text, "<Button-1>", sos_action)

# Optional Cancel Button
cancel_btn = tk.Button(root, text="Cancel", command=cancel_sos, bg="gray", fg="white", font=("Arial",15))
cancel_btn.pack(pady=10)

root.mainloop()
