from tkinter import Label


def test_func(value):
	print(value)


def field_test_func(field: Label, text: str):
	field.configure(text = f'{field["text"]}{text}')
