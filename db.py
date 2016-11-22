import config
import MySQLdb as baza
import time
class Db:
    def __init__(self,parent):
        self.parent=parent
        self.dbInit()
    def dbInit(self):
        self.baza=baza.connect(host=config.database.host, user=config.database.user, passwd=config.database.password, charset="utf8",use_unicode=True)
        self.kursor=self.baza.cursor()
        self.setup()

    def setup(self):
        self.kursor.execute("set names utf8;")
        try:
            self.kursor.execute(u'use {0};'.format(config.database.database))
        except:
            self.kursor.execute(u'create database {0} CHARACTER SET utf8 COLLATE utf8_general_ci'.format(config.database.database))
            self.kursor.execute(u'use {0};'.format(config.database.database))
            self.kursor.execute(u'create table if not exists wejscia(id int auto_increment primary key not null, identyfikator text not null, data datetime not null, ip text not null, user_agent text not null );')
    def close(self):
        self.kursor.close()
        self.baza.commit()
        self.baza.close()
    def insert(self, identyfikator, ip, user_agent):
        data=time.strftime('%Y-%m-%d %H:%M:%S')

        zapytanie="""insert into wejscia(identyfikator, data, ip,user_agent) values(%s,%s,%s,%s);"""
        
        self.kursor.execute(zapytanie,(identyfikator,data, ip,user_agent))
        self.commit()
    def commit(self):
        self.baza.commit()