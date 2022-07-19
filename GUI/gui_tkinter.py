
from tkinter import Tk, Canvas
# from PIL import ImageTk, Image
import tkinter.font as font

class Main_window(Tk):

    def __init__(self) -> None:
        super().__init__()

        self.window_config()
        self.canvas1.pack()
        self.canvas1.create_text(300, 50, text="Welcome to our shop", fill="black", font=self.myFont)


    def window_config(self):
        self.title("WEB shop catalogue (Main window)")
        self.geometry("600x500")
        self.canvas1 = Canvas(self, width = 300, height = 250)
        self.bgcolor = '#333359'
        self['background']=self.bgcolor
        # self.img = ImageTk.PhotoImage(Image.open("images/bot_picture1.PNG"))
        self.myFont = font.Font(family='Bookman Old Style', size=12, weight='bold')
        # self.bg = ImageTk.PhotoImage(file = "images/background.jpg")

if __name__ == "__main__":
    app = Main_window()
    app.mainloop()


# window = Tk()
# window.attributes('-fullscreen', True)
# window.title("Hello, welcome to catalogue")

# window.mainloop()