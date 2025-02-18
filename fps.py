import tkinter as tk
import random

def update_counter():
    # Generate a random number between 450 and 599
    counter = random.randint(450, 599)
    # Update the label text
    label.config(text=str(counter))
    # Call this function again after 1 second
    window.after(1000, update_counter)

# Create the main window
window = tk.Tk()
window.title("Random Counter")
window.geometry("200x100")  # Set the window size

# Remove window borders and title bar
window.overrideredirect(1)

# Set the window to be transparent
window.configure(bg='black')  # Make the background black for now
window.attributes('-transparentcolor', 'black')  # Set the color that will be transparent (black)

# Make the window always stay on top of other windows
window.attributes('-topmost', True)

# Create a label to display the counter with smaller and thinner text
label = tk.Label(window, font=('Arial', 18), fg='white', bg='black', bd=0)
label.pack(expand=True)

# Start the counter update
update_counter()

# Start the Tkinter event loop
window.mainloop()
