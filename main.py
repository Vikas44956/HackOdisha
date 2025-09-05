import tkinter as tk

root = tk.Tk()
root.title("EMERGENCY SOS")
root.geometry("900x900")
root.config(bg="gray20")

tk.Label(root,text="EMERGNECY SOS APP",font=("bold",50),fg="white",bg="gray20").pack(padx=50)

canvas = tk.Canvas(root, width=400, height=400, bg="gray20", highlightthickness=0)
canvas.pack()

circle = canvas.create_oval(125, 125, 275, 275, fill="red", outline="")
text = canvas.create_text(200, 200, text="SOS", fill="white", font=("Arial", 25, "bold"))
msg1 = canvas.create_text(190,300,text="Emergency Help",fill="white",font=("arail",15, "bold"))



canvas.tag_bind(circle, "<Button-1>", sos_action)
canvas.tag_bind(text, "<Button-1>", sos_action)

root.mainloop()
