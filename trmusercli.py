# -*- coding: utf-8 -*-
import mechanize
import argparse
import getpass
import re

class corobienie:
	def __init__(self,br):
		#trza będzie zrobić polecenia w różnych językach
		polecenia = ('stankonta', 'wypozyczenia')
		self.polecenia = polecenia
		corobic = self.zdobadzpolecenie()
		if corobic == 'stankonta':
			self.stankonta(br, "n")
		elif corobic == 'wypozyczenia':
			self.wypozyczenia(br)
		elif corobic == 'histtransakcji':
			self.histtransakcji(br)
		else:
			#lang: bladcorobicia
			print u'Błąd w kwestii informacji co robić'
			quit()
	def zdobadzpolecenie(self):
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
	def stankonta(self, br, dajreada):
		import re
		balansowanie = br.open('https://trm24.pl/panel-trm/balance.jsp')
		balansowac = balansowanie.read()
		balanoss = str(re.search(r'strong.*?PL', str(re.search(r'wynosi.*strong.*?PL', balansowac, re.S).group()), re.S).group())
		#try: 
		#balansik = int(str(re.search(r'(\d*.\d{2})', balanoss, re.S).group()))
		balansik = int(str(re.sub(r'\D', "", balanoss)))/100
		#except:
		#	balansik = int(str(re.sub(r'([^0-9.])', '', str(re.search(r'(\d*.\d{2})', balanoss, re.S).group())))
			#try:
			#	print u'Błąd/Eraron/Error: Niepoprawny/Malkorektan/Incorrect "balanoss" value/wartość [try]: %s' % balanoss
			#except:
			#print 'Eraron Error Niepoprawny Malkorektan Incorrect balanoss value-wartosc ---- '
			#print balanoss
			#print 'UP balanoss ----'
			#print balansik
			#print 'UP balansik ----'
			#quit()
		#lang: stantwojegokontawynosi
		print 'Stan twojego konta na TRM24.pl wynosi: %#.2f PLN' % balansik
		if dajreada == "n":
			return balansik
		elif dajreada == "y":
			tuplebalansikiread = (balansik, balansowac)
			return tuplebalansikiread
	def wypozyczenia(self, br):
		import re
		wypozyczania = br.open('https://trm24.pl/panel-trm/borrow.jsp')
		#wypozyczanie = wypozyczania.read()
		#lang: terazwybierzdatypoczatkowaikoncowa
		#print "Teraz wybierz datę początkową i końcową:"
		#print mechanize.ParseResponse(wypozyczania, backwards_compat=False)
		#for form in br.forms():
		#	print form
		#	print "_____--"
		#	try:
		#		print form.find_control('data_od')
		#	except:
		#		print "Nie"
		#print "----"
		br.select_form(nr=0)
		#print mechanize.ParseResponse(wypozyczania, backwards_compat=False)[0].find_control("startDate", type="text")
		#print br.form
		#lang: datapoczątkowa, rok, miesiąc, dzień
		odyear = int(raw_input("Data początkowa: rok [XXXX]: "))
		odmonth = int(raw_input("Data początkowa: miesiąc [1-12]: "))
		odday = int(raw_input("Data początkowa: dzień: "))
		startdate = "%04d-%02d-%02d" % (odyear, odmonth, odday)
		#lang: wybrano datę początkową
		print "Wybrano datę początkową %s " % startdate
		br['startDate'] = startdate
		#lang: datakońcowa, rok, miesiąc, dzień
		doyear = int(raw_input("Data końcowa: rok: "))
		domonth = int(raw_input("Data końcowa: miesiąc [1-12]: "))
		doday = int(raw_input("Data końcowa: dzień: "))
		enddate = "%04d-%02d-%02d" % (doyear, domonth, doday)
		#lang: wybrano datę końcową
		print "Wybrano datę końcową %s " % enddate
		br['endDate'] = enddate
		wypostronka = br.submit()
		tabwypfull = str(re.search(r'table.*?Rower.*?Slot.*?Koszt.*?/table', wypostronka.read(), re.S).group())
		tabo1 = str(re.sub(r'table', "", tabwypfull))
		tabo2 = str(re.sub(r'<', "", tabo1))
		tabo3 = str(re.sub(r'>', "", tabo2))
		tabo4 = str(re.sub(r'/', "uu", tabo3))
		tabo5 = str(re.sub('\n', "", tabo4))
		tabo6 = str(re.sub(r'thead', "", tabo5))
		tabi0 = re.findall(r'tr.*?uutr', tabo6, re.S)
		tabila = []
		for uuh in tabi0:
			tabi1 = re.findall(r'th.*?uuth', uuh, re.S)
			tabulacja = "True"
			tabila.append(tabi1)
		print tabila
		return tabila
	def histtransakcji(self, br):
		stankontatuple = self.stankonta(br, "y")
		stankonta = stankontatuple[0]
		histrw = [stankonta]
		historiowanie = stankontatuple[1]
		#tu będzie cała przeróbka tabeli historii transakcji
		#trza bedzie to bazowac na klasie wypozyczenia, bedzie latwiej bo bez wpisywania dat
		#appendowac dane do histrw jako tuple(l.mn)
		hista = histrw.tuple()
		#lang: tubedziehisttransakcji
		print "Tu potem będzie historia transakcji tj. doładowań"
		return hista

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


assert br.viewing_html()
print br.title()
print odpoa.geturl()
#print odpoa.info()
#print odpoa.read()
while True:
	corobienie(br)


	
