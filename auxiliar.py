from tkinter import *
from tkinter.filedialog import askopenfilenames

window = Tk()

selected_files_frame = LabelFrame(window, text='Files selected')
selected_files_frame.pack(fill='both',)

def func(files_selected):
    if files_selected:
        def fill_names(files_selected):
            printt = Button(window, text='Print', command=fill_names(files_selected))
            printt.pack()
        fill_names(files_selected)
    else:
        def select_files():
            files_selected = askopenfilenames(filetypes=(("Planilhas", "*.xlsx"),))
            return func(files_selected)
        select_files()


select_files_button = Button(window, text='Select files', command=func(files_selected={}))
select_files_button.pack()

file_names = Label(selected_files_frame, text='')
file_names.pack()

window.mainloop()
