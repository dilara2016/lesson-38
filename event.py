from tkinter import*
window=Tk()
window.title('Event handler')
window.geometry("300x300")
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.chair)
window.bind("<Key>", handle_keypress)
def handle_click(event):
        print("dilara has clicked the button")
button = Button(text="press me")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()
