import tkinter as tk
import datetime as dt

root = tk.Tk()

# configure window
root.geometry("600x300")
root.resizable(False, False)
root.title("Digital Clock")

# Function to get time


def getTime():
    now = dt.datetime.now()
    time = now.strftime("%I:%M:%S %p")
    clockLabel.config(text=time)
    clockLabel.after(1000, getTime)  # Update time every second


# Frame for clock
clockFrame = tk.Frame(root, bg="#151546").pack(
    expand=True, fill="both")

# Label for clock
clockLabel = tk.Label(clockFrame,
                      font=("Arial", 50), fg="#fff", bg="#151530", anchor='center', padx=20, pady=10)

# Place label in center of the clock frame
clockLabel.place(relx=0.5, rely=0.5, anchor='center')

# Call function to get time
getTime()

root.mainloop()
