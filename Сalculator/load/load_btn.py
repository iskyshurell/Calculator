from tkinter import ttk
from typing import List
from Сalculator.functions import num_func

BTN_HEIGHT = 100
BTN_WIDTH = BTN_HEIGHT * 175 / 100
Y_POS = 220
X_POS = 20
CONST_X = BTN_WIDTH + 10


def load_buttons(c_object) -> List[ttk.Button]:
	root = c_object.root
	field = c_object.field

	buttons = list()

	button_one = ttk.Button(
		root, text = '1',
		command = lambda: num_func(field, button_one['text']),
	)

	button_one.place(
		x = X_POS,
		y = Y_POS,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_one)

	button_two = ttk.Button(
		root, text = '2',
		command = lambda: num_func(field, button_two['text']),
	)

	button_two.place(
		x = X_POS + BTN_WIDTH + 10,
		y = Y_POS,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_two)

	button_three = ttk.Button(
		root, text = '3',
		command = lambda: num_func(field, button_three['text']),
	)

	button_three.place(
		x = X_POS + (BTN_WIDTH + 10) * 2,
		y = Y_POS,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_three)

	button_four = ttk.Button(
		root, text = '4',
		command = lambda: num_func(field, button_four['text']),
	)

	button_four.place(
		x = X_POS,
		y = Y_POS + BTN_HEIGHT + 10,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_four)

	button_five = ttk.Button(
		root, text = '5',
		command = lambda: num_func(field, button_five['text']),
	)
	button_five.place(
		x = X_POS + BTN_WIDTH + 10,
		y = Y_POS + BTN_HEIGHT + 10,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_five)

	button_six = ttk.Button(
		root, text = '6',
		command = lambda: num_func(field, button_six['text']),
	)
	button_six.place(
		x = X_POS + (BTN_WIDTH + 10) * 2,
		y = Y_POS + BTN_HEIGHT + 10,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_six)

	button_seven = ttk.Button(
		root, text = '7',
		command = lambda: num_func(field, button_seven['text']),
	)
	button_seven.place(
		x = X_POS,
		y = Y_POS + (BTN_HEIGHT + 10) * 2,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_seven)

	button_eight = ttk.Button(
		root, text = '8',
		command = lambda: num_func(field, button_eight['text']),
	)
	button_eight.place(
		x = X_POS + BTN_WIDTH + 10,
		y = Y_POS + (BTN_HEIGHT + 10) * 2,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_eight)

	button_nine = ttk.Button(
		root, text = '9',
		command = lambda: num_func(field, button_nine['text']),
	)
	button_nine.place(
		x = X_POS + (BTN_WIDTH + 10) * 2,
		y = Y_POS + (BTN_HEIGHT + 10) * 2,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_nine)

	button_point = ttk.Button(
		root, text = '.',
		command = lambda: num_func(field, button_point['text']),
	)
	button_point.place(
		x = X_POS + (BTN_WIDTH + 10) * 4,
		y = Y_POS + (BTN_HEIGHT + 10) * 2,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_point)

	return buttons
