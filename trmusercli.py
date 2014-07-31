# -*- coding: utf-8 -*-
import mechanize
import argparse
import getpass

br = mechanize.Browser()
br.open("https://trm24.pl/panel-trm/index.jsp")
br.select_form(name="login")
#lang: wpiszidklienta
AjDi = raw_input("Wpisz ID klienta: ")
br["clientId"] = AjDi
#lang: wpiszhaslo
Paslord = getpass.getpass("Wpisz hasło: ")
br["clientPass"] = Paslord
odpoa = br.submit()

assert br.viewing_html()
print br.title()
print odpoa.geturl()
print odpoa.info()
print odpoa.read()
