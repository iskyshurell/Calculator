from tkinter import ttk
from typing import List
from Сalculator.functions import summ, div, mult, degree, minn, sqrt, equal, clear, full_div, perc_div

BTN_HEIGHT = 100
BTN_WIDTH = BTN_HEIGHT * 175 / 100
Y_POS = 220
X_POS = 20 + (BTN_WIDTH + 10) * 3
CONST_X = BTN_WIDTH + 10


def load_act_buttons(c_object) -> List[ttk.Button]:
	root = c_object.root

	buttons = list()

	button_plus = ttk.Button(
		root, text = '+',
		command = lambda: summ(c_object),
	)

	button_plus.place(
		x = X_POS,
		y = Y_POS + BTN_HEIGHT + 10,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_plus)

	button_minus = ttk.Button(
		root, text = '-',
		command = lambda: minn(c_object),
	)

	button_minus.place(
		x = X_POS,
		y = Y_POS + (BTN_HEIGHT + 10) * 2,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_minus)

	button_divide = ttk.Button(
		root, text = '/',
		command = lambda: div(c_object),
	)

	button_divide.place(
		x = X_POS,
		y = Y_POS,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_divide)

	button_equal = ttk.Button(
		root, text = '=',
		command = lambda: equal(c_object),
	)

	button_equal.place(
		x = X_POS,
		y = Y_POS - BTN_HEIGHT - 10,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_equal)

	button_mult = ttk.Button(
		root, text = '*',
		command = lambda: mult(c_object),
	)

	button_mult.place(
		x = X_POS - BTN_WIDTH - 10,
		y = Y_POS - BTN_HEIGHT - 10,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_mult)

	button_degree = ttk.Button(
		root, text = '**',
		command = lambda: degree(c_object),
	)

	button_degree.place(
		x = X_POS - (BTN_WIDTH + 10) * 2,
		y = Y_POS - BTN_HEIGHT - 10,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_degree)

	button_sqrt = ttk.Button(
		root, text = 'sqrt',
		command = lambda: sqrt(c_object),
	)

	button_sqrt.place(
		x = X_POS - (BTN_WIDTH + 10) * 3,
		y = Y_POS - BTN_HEIGHT - 10,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_sqrt)

	button_clear = ttk.Button(
		root, text = 'C',
		command = lambda: clear(c_object),
	)

	button_clear.place(
		x = X_POS + (BTN_WIDTH + 10),
		y = Y_POS - (BTN_HEIGHT + 10),
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_clear)

	button_full_div = ttk.Button(
		root, text = '//',
		command = lambda: full_div(c_object),
	)
	button_full_div.place(
		x = X_POS + (BTN_WIDTH + 10),
		y = Y_POS,
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_full_div)

	button_pc_div = ttk.Button(
		root, text = '%',
		command = lambda: perc_div(c_object),
	)
	button_pc_div.place(
		x = X_POS + (BTN_WIDTH + 10),
		y = Y_POS + (BTN_HEIGHT + 10),
		width = BTN_WIDTH, height = BTN_HEIGHT
	)
	buttons.append(button_pc_div)

	return buttons
