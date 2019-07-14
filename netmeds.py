import requests
import bs4
from urllib.error import HTTPError,URLError
import lxml
from requests.exceptions import ConnectionError
import re
import io


def urlopen(url):
    try:
        data = requests.get(url)

    except HTTPError as e:
        print(e)

    except URLError as e:
        print(e)

    except ConnectionError as e:
        print(e)

    return data



data = urlopen("https://www.netmeds.com/prescriptions")

fdata = bs4.BeautifulSoup(data.text , "lxml")
# print(fdata)

    

# a = fdata.select(".drug-list-col")
a =fdata.find("div",{"class":"drug-list-col"})
# a =fdata.find("div",{"class":"ln-a"})

# a_list = a.select(".alpha-drug-list")
# a = fdata.select(".drug-list-col ln-a")
# print(a.get_text())
# a_list = a.select(".alpha-drug-list")
# print(a_list)

# b = fdata.find("div",{"class":"drug-list-col"})


# print(b)


def degit_remove(item):

    dj = ['1','2','3','4','5','6','7','8','9',')','(','0']
    answer = ''
    for char in item :
        if char not in dj :
            answer += char

    return answer



b = fdata.find_all("ul",{"class":"alpha-drug-list"})
l=[]
for item in b:
    for med in item:
        name = med.get_text()
        l.append(name)

# print(l)
new =[]
for item in l:
    x = degit_remove(item).strip()
    new.append(x)

with io.open("file1.csv","w",encoding="utf8") as f1:
    f1.write("MEDICINE DETAILS \n")


# print(new)
all =[]


for item in new :
    
    x = item

    new_url = "https://www.netmeds.com/prescriptions/"+item 
    new_data = urlopen(new_url)
    fnew_data = bs4.BeautifulSoup(new_data.text , 'lxml')
    
    all_tab = fnew_data.find_all("ul",{"class":"alpha-drug-list"})
    s =[]    
    for item in all_tab:
        for med in item:
            name = med.find("div",{"class":"panel-body"})

            with io.open("file1.csv","a",encoding="utf-8") as f1:

                f1.write(x + "\n")
                f1.write(name.get_text() + "\n")
            

            # print(name.get_text())
            
#         print(s)
#         all.append(s)
#         print("done")

# print(all)




    
