from tkinter import Tk
from ..load_btn import load_buttons
from ..load_act_btn import load_act_buttons
from ..load_text_field import load_text_field


class Main:
	def __init__(self):
		self.root = Tk()

		self.root.title('Calculator')
		self.root.geometry('960x560')
		self.root.configure(bg = '#E6E6E6')
		self.root.resizable(False, False)

		self.first_num = None
		self.second_num = None
		self.action = None

		self.field = load_text_field(self)
		self.buttons = load_buttons(self)
		self.act_buttons = load_act_buttons(self)
		self.root.mainloop()
