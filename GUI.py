from tkinter import*
from tkinter import messagebox as msg
from PIL import ImageTk, Image
import search1
import search2
import search3
from search_modules import*


def main():
    '''This is the main driver to start the whole program of Propublica Sample Searches'''

    window = Tk()   # this is the container for GUI

    # customizing the window container
    window.title('   Welcome to ProPublica Sample Searches')
    window.iconbitmap('GUI_small_Logo.ico')
    window.geometry('672x580')

    # getting the image to be inserted into GUI
    my_img = ImageTk.PhotoImage(Image.open('GUI_image_.png'))

    # creating the instance of the GUI withing the window container
    gui_app = GuiApp(window, my_img)

    # activating the GUI window
    window.mainloop()

class GuiApp():
    '''This class is a blueprint for the GUI window'''

    def __init__(self, parentWindow, topFramePic):
        self.window = parentWindow
        self.topPicture = topFramePic
        self.choice_var = IntVar()
        self.last_name = StringVar()
        self.first_name = StringVar()
        self.state_code = StringVar()

        picture = Label(self.window, image=self.topPicture)
        picture.grid(row=0, columnspan=3, sticky=N)

        label_main = Label(self.window, pady = 5, text='Choose search type', font='Georgia 16 bold')
        label_main.grid(row=1, columnspan=3)

        rd1 = Radiobutton(self.window,text='1: Get the list of current Congressional representatives for a given state', variable=self.choice_var, value=1)
        rd1.grid(row=2, column=0, padx=15, pady=18, sticky=W)

        label1_search1 = Label(self.window, text="Enter a two-letter postal code for the state:   ")
        label1_search1.grid(row=2, column=1, pady=18, sticky=E)

        entry_state = Entry(self.window, textvariable=self.state_code, justify=LEFT, bg="light grey")
        entry_state.grid(row=2, column=2, pady=18, sticky=W)

        rd2 = Radiobutton(self.window, text='2: Search current or past representative by name', variable=self.choice_var, value=2)
        rd2.grid(row=3, column=0, padx=15, pady=5, sticky=W)

        label1_search2 = Label(self.window, text="Enter last name:   ")
        label1_search2.grid(row=3, column=1, sticky=E)

        entry_last_name = Entry(self.window, textvariable=self.last_name, bg="light grey")
        entry_last_name.grid(row=3, column=2, sticky=W)

        label2_search2 = Label(self.window, text="Enter first name:   ")
        label2_search2.grid(row=4, column=1, sticky=E)

        entry_first_name = Entry(self.window, textvariable=self.first_name, bg="light grey")
        entry_first_name.grid(row=4, column=2, sticky=W)

        rd3 = Radiobutton(self.window, text='3: Get historical data on average age in Congress', variable=self.choice_var, value=3)
        rd3.grid(row=6, column=0, padx=15, sticky=W)

        btn_search = Button(self.window, text='Search', bg='red', fg='white', command=self.show_data)
        btn_search.grid(row=8, columnspan=3, pady=5)

        btn_quit = Button(self.window, text="Exit Program", command=self.window.quit)
        btn_quit.grid(row=9, columnspan=3, pady=10)

    def show_data(self):
        '''This method generates the results of the search requested by the user'''

        search_num = self.choice_var.get()   #variable to hold the number of the user-chosen search

        if search_num == 3:
            search3.run_search3()

        elif search_num == 1 or search_num == 2:
            results = Tk()
            results.title('  Search Results ')
            results.iconbitmap('GUI_small_Logo.ico')
            results.resizable(True, True)
            txt_box = Text(results)
            txt_box.pack()

            if search_num == 1:
                state_code = str(self.state_code.get())
                txt_box.insert(END, search1.results_string(state_code))

            else:
                first_name = str(self.first_name.get())
                last_name = str(self.last_name.get())
                txt_box.insert(END, search2.results_string(first_name, last_name))


        else:
            message = "No input data. Try again."
            msg.showinfo("  Alert!", message)

if __name__ == '__main__':
    main()
