#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser, Menu, Spinbox, scrolledtext, messagebox as mb, filedialog as fd

from gtts import gTTS
import os

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""
    #===========================================
    def __init__(self, title, icon, theme):
        super().__init__()
        self.style = ttk.Style(self)
        self.style.theme_use(theme)
        self.resizable(False, False)
        self.title(title)
        self.iconbitmap(icon)

        self.init_UI()
        self.init_events()

    # INITIALIZER ==============================
    @classmethod
    def create_app(cls, app):
        return cls(app['title'], app['icon'], app['theme'])

    def init_events(self):
        self.bind('<Return>', self.evt_gorun)

    # WIDGETS ----------------------------------
    def init_UI(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        label = ttk.Label(self.main_frame, text='PRESS ENTER TO HEAR THE TEXT')
        label.pack(side=tk.TOP)

        self.text = tk.StringVar()
        entry = ttk.Entry(self.main_frame, textvariable=self.text)
        entry.pack(fill=tk.BOTH, expand=True)
        self.text.set('Example of text')

        label = ttk.Label(self.main_frame, text='Choose language (default is english=en)')
        label.pack(side=tk.TOP)

        self.lang = tk.StringVar()
        self.lang.set('en')
        entry = ttk.Entry(self.main_frame, textvariable=self.lang)
        entry.pack(fill=tk.BOTH, expand=True)

        label = ttk.Label(self.main_frame, text='Name of the file')
        label.pack(side=tk.TOP)

        self.filename = tk.StringVar()
        self.filename.set('myaudio')
        entry = ttk.Entry(self.main_frame, textvariable=self.filename)
        entry.pack(fill=tk.BOTH, expand=True)

    # EVENTS ------------------------------------
    def evt_gorun(self, event):
        s = gTTS(self.text.get(), lang=self.lang.get())
        s.save(f'{self.filename.get()}.mp3')
        filename = f'{self.filename.get()}.mp3'
        os.system(f'start {filename}')

#===========================
# Start GUI
#===========================

def main(config):
    app = App.create_app(config)
    app.mainloop()

if __name__ == '__main__':
    main({
        'title' : 'Text to Speech Version 1.0',
        'icon' : 'python.ico',
        'theme' : 'clam'
        })