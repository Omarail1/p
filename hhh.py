# pip install googlesearch-python==1.0.1
import os
from time import sleep as t
from googlesearch import search
class Omar:
    def __init__(self):
        self.Fileoffline = open("omar.txt",'r')
        self.list_id=self.Fileoffline.readlines()
        self.Fileoffline.close() 
    def google_se(self) : #Omar  str
        for i in self.list_id: # file => php?id=1
            lu = i.rstrip('\n') 
            t(20)
            for ur in search(lu, num_results=1000): # google => search
                print(ur)
                file = open("url_SQL.txt","a")
                file.write(ur+"\n")
                file.close()
    # def SQL_if(self) -> str:
# A = Omar()
# A.google_se()
