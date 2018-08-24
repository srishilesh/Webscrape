import requests 
from bs4 import BeautifulSoup
from prettytable import PrettyTable

t=PrettyTable(['Title','Description'])

url = 'https://www.amrita.edu/events/all'

response = requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')

main_div=soup.find_all('div',class_='view-content')
#print(len(main_div))
#print((main_div))
first_event=main_div[0]

first_div1=first_event.find('div',class_='views-row views-row-1 views-row-odd views-row-first')

first_div2=first_div1.find('div',class_='views-field views-field-title')


first_span=first_div2.find('span',class_='field-content')


title1=first_span.h2.text
first_desc=first_div1.find('div',class_='views-field views-field-field-description-event')
des1=first_desc.p.text
'''t.add_row(title,des)
t.align="l"
print(t)'''
second_event=main_div[0]
print("TITLE 1 IS \n",title1)
print("DESCRIPTION 1 IS \n",des1)


a=[]
j=0
for i in range(2,9):
    if(i%2==0):
        a.append('views-row views-row-'+str(i)+' views-row-even')
    else:
        a.append('views-row views-row-'+str(i)+' views-row-odd')
    second_div1=second_event.find('div',class_=a[j])
    j+=1
    second_div2=second_div1.find('div',class_='views-field views-field-title')
    second_span=second_div2.find('span',class_='field-content')
    title2=second_span.h2.text
    sec_desc=second_div1.find('div',class_='views-field views-field-field-description-event')
    des2=sec_desc.p.text
    t.add_row([title2,des2])
    #title2.align="l"
    #des2.align='r'
    t.align['Title']="l"
    t.align['Description']="r"
    t.align='l'
    #print("TITLE "+str(i)+" IS \n",title2)
    #print("DESCRIPTION "+str(i)+" IS \n",des2)
print(t)
last_div1=first_event.find('div',class_='views-row views-row-10 views-row-even views-row-last')

last_div2=last_div1.find('div',class_='views-field views-field-title')


last_span=last_div2.find('span',class_='field-content')


title3=last_span.h2.text
last_desc=last_div1.find('div',class_='views-field views-field-field-description-event')
des3=last_desc.p.text
print("TITLE 10 IS \n",title3)
print("DESCRIPTION 10 IS \n",des3)
    
#t.add_row(title,des)
#t.align="l"
#print(t)
    


