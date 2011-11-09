#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from QtMobility.Messaging import *
from QtMobility.Contacts import *
from PySide.QtCore import *

def format_addressee(adr):
	if adr == '/org/freedesktop/Telepathy/Account/ring/tel/ring':
		return 'you'
	else:
		return adr

app = QCoreApplication(sys.argv)

acc_id = QMessageAccount.defaultAccount(QMessage.Sms)
mgr = QMessageManager()
f = QMessageFilter.byParentAccountId(acc_id)
s = QMessageSortOrder()
s.byTimeStamp()
msg_ids = mgr.queryMessages(f, s)

#cf = QContactFilter()
#cf.MatchFlag = QContactFilter.MatchPhoneNumber
#cfr = QContactFetchRequest()
#cfr.setFilter(cf)
print '*' * 25, '25 MOST RECENT', '*' * 25 
for msg_id in msg_ids[-25:]:
	m = QMessage(msg_id)
	print '***', format_addressee(m.from_().addressee()), '->', format_addressee(m.to()[0].addressee()), '***'
	if not QMessage.Read == m.status():
		print '*** NEW SMS ***'
	print m.textContent() + '\n'
"""
acc_id = QMessageAccount.defaultAccount(QMessage.Sms)
acc = QMessageAccount(acc_id)

f = QMessageFilter.byParentAccountId(acc_id)
print f, f.isEmpty()
"""

""" SEND MESSAGE:
a = QMessageAddress(QMessageAddress.Phone, 'NUMBER')
m = QMessage()
m.setType(QMessage.Sms)
m.setTo(a)
m.setBody('hurra, her er en sms')
s = QMessageService()
if s.send(m):
	print 'sent'
else:
	print 'damn'
"""
