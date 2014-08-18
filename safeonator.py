# -*- coding: utf-8 -*-
class safeonator:
	"To jest klasa konwertująca znaczki natio na znaczki bezpieczne."
	pltoang_tab = {u'ą':'a', u'ć':'c', u'ę':'e', u'ł':'l', u'ń':'n', u'ó':'o', u'ś':'s', u'ż':'z', u'ź':'z'}
	def __init__(text):
		return ''.join( pltoang_tab.get(char, char) for char in text )
