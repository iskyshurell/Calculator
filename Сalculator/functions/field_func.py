import math


def summ(c_object):
	try:
		c_object.first_num = float(c_object.field['text'])
		c_object.action = '+'
		c_object.field['text'] = ''
	except ValueError:
		c_object.field['text'] = 'Сначала введите число!'


def minn(c_object):
	try:
		c_object.first_num = float(c_object.field['text'])
		c_object.action = '-'
		c_object.field['text'] = ''
	except ValueError:
		c_object.field['text'] = 'Сначала введите число!'


def div(c_object):
	try:
		c_object.first_num = float(c_object.field['text'])
		c_object.action = '/'
		c_object.field['text'] = ''
	except ValueError:
		c_object.field['text'] = 'Сначала введите число!'


def mult(c_object):
	try:
		c_object.first_num = float(c_object.field['text'])
		c_object.action = '*'
		c_object.field['text'] = ''
	except ValueError:
		c_object.field['text'] = 'Сначала введите число!'


def degree(c_object):
	try:
		c_object.first_num = float(c_object.field['text'])
		c_object.action = '**'
		c_object.field['text'] = ''
	except ValueError:
		c_object.field['text'] = 'Сначала введите число!'


def sqrt(c_object):
	c_object.field['text'] = math.sqrt(float(c_object.field['text']))


def full_div(c_object):
	try:
		c_object.first_num = float(c_object.field['text'])
		c_object.action = '//'
		c_object.field['text'] = ''
	except ValueError:
		c_object.field['text'] = 'Сначала введите число!'


def perc_div(c_object):
	try:
		c_object.first_num = float(c_object.field['text'])
		c_object.action = '%'
		c_object.field['text'] = ''
	except ValueError:
		c_object.field['text'] = 'Сначала введите число!'


def equal(c_object):
	c_object.second_num = c_object.field['text']

	try:
		action = c_object.action

		if action == '+':
			c_object.field['text'] = float(c_object.first_num) + float(c_object.second_num)

		elif action == '-':
			c_object.field['text'] = float(c_object.first_num) - float(c_object.second_num)

		elif action == '*':
			c_object.field['text'] = float(c_object.first_num) * float(c_object.second_num)

		elif action == '**':
			c_object.field['text'] = float(c_object.first_num) ** float(c_object.second_num)

		elif action == '/':
			c_object.field['text'] = float(c_object.first_num) / float(c_object.second_num)

		elif action == '//':
			c_object.field['text'] = float(c_object.first_num) // float(c_object.second_num)

		elif action == '%':
			c_object.field['text'] = float(c_object.first_num) % float(c_object.second_num)

		c_object.first_num = None
		c_object.second_num = None
		c_object.action = None

	except BaseException:
		c_object.field['text'] = 'Сначала введите число!'


def clear(c_object):
	c_object.first_num = None
	c_object.second_num = None
	c_object.action = None
	c_object.field['text'] = ''
