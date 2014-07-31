# -*- coding: utf-8 -*-
import mechanize
import argparse
import getpass
import re

polecenia = ('stankonta', 'wypozyczenia')
br = mechanize.Browser()
br.open('https://trm24.pl/panel-trm/index.jsp')
br.select_form(name='login')
#lang: wpiszidklienta
AjDi = raw_input('Wpisz ID klienta: ')
br['clientId'] = AjDi
#lang: wpiszhaslo
Paslord = getpass.getpass('Wpisz hasło: ')
br['clientPass'] = Paslord
odpoa = br.submit()

def zdobadzpolecenie(polecenia):
#lang: dostepnepolecenia
	print 'Dostępne polecenia: '
	print polecenia
	#lang: wpiszpolecenie
	polec = raw_input('Wpisz polecenie: ')
	try:
		polecenia.index(polec)
		run = polec
		return run
	except:
		#lang: nie znaleziono polecenia
		print 'Nie znaleziono polecenia: %s' % polec
		runu = zdobadzpolecenie(polecenia)
		return runu

assert br.viewing_html()
print br.title()
print odpoa.geturl()
print odpoa.info()
#print odpoa.read()
corobic = zdobadzpolecenie(polecenia)
if corobic == 'stankonta':
	balansowanie = br.open("https://trm24.pl/panel-trm/balance.jsp")
	balansowac = balansowanie.read()
	balanoss = str(re.search(r'strong.*?PLN', str(re.search(r'wynosi.*strong.*?PLN', balansowac, re.S).group()), re.S).group())
	try: 
		balansik = int(str(re.search(r'(\d*.\d{2})', balanoss, re.S).group()))
	except:
		balansik = int(str(re.sub(r'([^0-9.])', '', str(re.search(r'(\d*.\d{2})', balanoss, re.S).group())))
		#try:
		#	print u'Błąd/Eraron/Error: Niepoprawny/Malkorektan/Incorrect "balanoss" value/wartość [try]: %s' % balanoss
		#except:
		print 'Eraron Error Niepoprawny Malkorektan Incorrect balanoss value-wartosc ---- '
		print balanoss
		print 'UP balanoss ----'
		print balansik
		print 'UP balansik ----'
		quit()
	print 'Stan twojego konta na TRM24.pl wynosi: %#.2f PLN' % balansik
elif corobic == 'wypozyczenia':
	br.open('https://trm24.pl/panel-trm/borrow.jsp')
else:
	#lang: bladcorobicia
	print u'Błąd w kwestii informacji co robić'
	quit()