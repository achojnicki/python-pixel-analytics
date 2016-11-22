#!/usr/bin/python
import cgi, cgitb
import sys, os
import config
import db


class analitycs:
    def __init__(self):
        if config.misc.debug:
            cgitb.enable()
        self.baza=db.Db(self)
        
        self.form=cgi.FieldStorage()
        self.identyfikator=self.form.getvalue('s')
        if not self.identyfikator:
            print
            sys.exit(0)
        self.ip=os.environ['REMOTE_ADDR']
        self.user_agent=os.environ['HTTP_USER_AGENT']
        p=open('pixel.png','r')
        self.pixel=p.read()
        p.close()
    def showImage(self):
        print "Content-Type: Image/Png\n"
        print self.pixel
    
    def start(self):
        self.baza.insert(self.identyfikator,self.ip,self.user_agent)
        self.baza.close()
        self.showImage()


a=analitycs()
a.start()


