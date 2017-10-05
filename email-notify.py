# -*- coding: utf-8 -*- 



import smtplib


with open('data.csv') as data:
    for d in data.readlines()[1:]: # [1:] e per saltare la linea di intestazione
        nome,cognome,to,voto = d.rstrip().split(',')
        soggetto = 'Voti' 
        print(nome,cognome,to,voto)
        gmail_user = 'MAIL@gmail.com' # cambiare con la propria mail
        gmail_pwd = 'PASSWD' # cambiare con la propria password
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_pwd)
        header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:'+soggetto+'\n'
        print header
        msg = header + '\nCiao ' + nome +' '+ cognome +',\nil tuo voto della verifica e: '+str(voto)+'\n\n'
        smtpserver.sendmail(gmail_user, to, msg)
        print 'done!'
        smtpserver.close()
        
    
