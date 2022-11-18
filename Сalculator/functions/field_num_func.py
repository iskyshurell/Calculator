from tkinter import Label


def num_func(field: Label, text: str):
	if field['text'] == 'Сначала введите число!':
		field.configure(text = text)
	else:
		field.configure(text = f'{field["text"]}{text}')
