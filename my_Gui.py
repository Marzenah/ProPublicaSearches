from tkinter import*
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import search3
from search_modules import*

def main():
    window = Tk()

    window.title('   Welcome to ProPublica Sample Searches')
    window.iconbitmap('small_Logo.ico')
    window.geometry('672x580')
    my_img = ImageTk.PhotoImage(Image.open('GUI_image_.png'))
    gui_app = GuiApp(window, my_img)
    window.mainloop()

class GuiApp():
    def __init__(self, parentWindow, topFramePic):

        self.window = parentWindow
        self.topPicture = topFramePic
        self.choice_var = IntVar()
        self.last_name = StringVar()
        self.first_name = StringVar()
        self.state_code = StringVar()


        picture = Label(self.window, image=self.topPicture)
        picture.grid(row=0, columnspan=3, sticky=N)

        label_main = Label(self.window, pady = 10, text='Choose search type', font='Halvetica 16 bold')
        label_main.grid(row=1, columnspan=3)

        rd1 = Radiobutton(self.window, text='1: Search current representative by name', variable=self.choice_var, value=1)
        rd1.grid(row=2, column=0, padx=12, sticky=W)

        label1_search1 = Label(self.window, text="Enter last name: ")
        label1_search1.grid(row=2, column=1, sticky=W)

        entry_last_name = Entry(self.window, textvariable=self.last_name, bg="light grey")
        entry_last_name.grid(row=2, column=2, sticky=W)

        label2_search1 = Label(self.window, text="Enter first name: ")
        label2_search1.grid(row=3, column=1, sticky=W)

        entry_first_name = Entry(self.window, textvariable=self.first_name, bg="light grey")
        entry_first_name.grid(row=3, column=2, sticky=W)

        rd2 = Radiobutton(self.window,text='2: Get list of Congressional representatives for a state', variable=self.choice_var, value=2)
        rd2.grid(row=5, column=0, padx=12, sticky=W)

        label1_search2 = Label(self.window, text="Enter two-letter code for state: ")
        label1_search2.grid(row=5, column=1, pady=15, sticky=W)

        entry_state = Entry(self.window, textvariable=self.state_code, justify=LEFT, bg="light grey")
        entry_state.grid(row=5, column=2, pady=15, sticky=W)

        rd3 = Radiobutton(self.window, text='3: Get historical data on average age in Congress', variable=self.choice_var, value=3)
        rd3.grid(row=7, column=0, padx=12, sticky=W)

        btn_search = Button(self.window, text='Search', bg='red', fg='white', command=self.show_data)
        btn_search.grid(row=8, columnspan=3, pady=5)

        btn_quit = Button(self.window, text="Exit Program", command=self.window.quit)
        btn_quit.grid(row=9, columnspan=3, pady=15)

    def show_data(self):
        search_num = self.choice_var.get()
        if search_num == 3:
            search3.run_search3()
        else:
            results = Tk()
            results.title('  Search Results ')
            results.iconbitmap('small_Logo.ico')
            results.resizable(True, True)

            txt_box = Text(results, wrap=WORD)
            txt_box.pack()

            if search_num == 1:
                first_name = str(self.first_name.get())
                last_name = str(self.last_name.get())
                # !!! result = search1.SomeMethod(first_name, last_name)
                # !!! txt_box.insert(END, result)
            elif search_num == 2:
                state_code = str(self.state_code.get())
                txt_box.insert(END, state_code)
                # !!! result = search2.SomeMethod(state_code)
                # !!! txt_box.insert(END, result)
            else:
                pass

if __name__ == '__main__':
    main()
