from tkinter import ttk


def load_text_field(c_object):
	root = c_object.root

	field = ttk.Label(
		root, text = '',
		font = 1,
	)
	field.place(
		x = 20,
		y = 20,
		width = 730, height = 80
	)

	return field
