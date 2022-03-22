import tkinter as tk
from transcriber import Transcriber
from os.path import exists



class Window: 

    def __pump(self):
        if self.transcriber:
            try:
                words = next(self.it)
                if words:
                    self.output.insert(tk.END, str(words) + '\n')
            except StopIteration:
                self.transcriber = None
                self.output.insert(tk.END, '<<END>>\n')
        self.window.after(1000, self.__pump)

    def __transcribe(self):
        path = self.file_input_entry.get()
        lang = self.lang_input_entry.get()

        self.output.delete('1.0', tk.END)
        if exists(path):
            self.transcriber = Transcriber(path, lang)
            self.it = iter(self.transcriber.audio())
        else: 
            self.output.insert(tk.END, 'ERROR: NO FILE')

    def __init__(self):
        self.transcriber = None
        self.window = tk.Tk()

        self.file_input_label = tk.Label(text='File')
        self.file_input_entry = tk.Entry()
        self.lang_input_label = tk.Label(text='Language')
        self.lang_input_entry = tk.Entry()
        self.file_input_button = tk.Button(text='Transcribe', comman=lambda: self.__transcribe())
        self.output = tk.Text()

        self.file_input_label.pack()
        self.file_input_entry.pack()
        self.lang_input_label.pack()
        self.lang_input_entry.pack()
        self.file_input_button.pack()
        self.output.pack()
        self.__pump()

    def run(self):
        self.window.mainloop()