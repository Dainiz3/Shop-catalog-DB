
from tkinter import Tk, Canvas, Button
from PIL import ImageTk, Image
import tkinter.font as font

class Main_window(Tk):

    def __init__(self) -> None:
        super().__init__()

        self.window_config()
        self.canvas: Canvas = Canvas(self, width = 1400, height = 1130)
        self.widgets()
        self._apply_canvas()
        

    def _apply_canvas(self) -> None:
        self.canvas.pack()
        self.canvas.create_image( 0, 0, image = self.img, anchor = "nw")
        self.canvas.create_text(650, 150, text="Welcome to our shop", fill="Purple", font=self.myFont)

        
    def window_config(self):
        self.title("WEB shop catalogue (Main window)")
        self.geometry("1400x900")

        self.bgcolor = '#333359'
        self['background']=self.bgcolor
        self.img = ImageTk.PhotoImage(Image.open("Shop-catalog-DB/icons/berlinki.PNG"))
        self.myFont = font.Font(family='Bookman Old Style', size=50, weight='bold')
        # self.bg = ImageTk.PhotoImage(file = "images/background.jpg")

    def widgets(self):
        button_search = Button(self.canvas, text="Search", borderwidth=0)
        button_create= Button(self.canvas, text="Create", borderwidth=0)
        self.canvas.create_window(10, 10, anchor="nw", window=button_search)
        self.canvas.create_window(70, 10, anchor="nw", window=button_create)

if __name__ == "__main__":
    app = Main_window()
    app.mainloop()


# window = Tk()
# window.attributes('-fullscreen', True)
# window.title("Hello, welcome to catalogue")

# window.mainloop()