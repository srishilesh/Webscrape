import requests 
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import urllib

t=PrettyTable(['Recent Posts'])

workshop = PrettyTable(['Workshops'])
winner = PrettyTable(['Winners'])
conferences = PrettyTable(['Conferences'])

url = 'https://www.amrita.edu/events/all'
posts = []

#while(x>0)
#url1='https://www.amrita.edu/events/all?page={}',x


response = requests.get(url)
#print(response.raise_for_status())
soup=BeautifulSoup(response.text,'html.parser')

main_div=soup.find_all('div',class_='view-content')
#print(len(main_div))
#print((main_div))

#FOR THE FIRST EVENT IN THE PAGE
first_event=main_div[2]
first_div1 = first_event.find('div',class_='views-row views-row-1 views-row-odd views-row-first')
#print(first_div1)
first_div2 = first_div1.find('div',class_='views-field views-field-title')
first_span = first_div2.find('span',class_='field-content')
title1 = first_span.text
# first_desc=first_div1.find('div',class_='views-field views-field-field-description-event')
# des1=first_desc.p.text
posts.append(title1)
t.add_row([title1])
t.align['Title']="l"
# t.align['Description']="r"
# t.align="l"
#print(t)

second_event=main_div[1]
# #print("TITLE 1 IS \n",title1)
# #print("DESCRIPTION 1 IS \n",des1)


#FOR THE SECOND EVENT AND THE SECOND LAST EVENT
a=[]
j=0
for i in range(2,7):
    if(i%2==0):
        a.append('views-row views-row-'+str(i)+' views-row-even')
    else:
        a.append('views-row views-row-'+str(i)+' views-row-odd')
    second_div1=second_event.find('div',class_=a[j])
    j+=1
    second_div2=second_div1.find('div',class_='views-field views-field-title')
    second_span=second_div2.find('span',class_='field-content')
    title2=second_span.text
    posts.append(title2)
    t.add_row([title2])
    t.align['Title']="l"
    # t.align['Description']="r"
    t.align='l'
#     #print("TITLE "+str(i)+" IS \n",title2)
#     #print("DESCRIPTION "+str(i)+" IS \n",des2)
# #print(t)


# #FOR THE LAST EVENT IN THE PAGE
# last_div1=first_event.find('div',class_='views-row views-row-10 views-row-even views-row-last')
# last_div2=last_div1.find('div',class_='views-field views-field-title')
# last_span=last_div2.find('span',class_='field-content')
# title3=last_span.h2.text
# last_desc=last_div1.find('div',class_='views-field views-field-field-description-event')
# des3=last_desc.p.text
# t.add_row([title3,des3])
# t.align['Title']="l"
# t.align['Description']="r"
# t.align="l"


# print(t)
# #print("TITLE 10 IS \n",title3)
# #print("DESCRIPTION 10 IS \n",des3)
    
# #t.add_row(title,des)
# #t.align="l"
print(t)
    
win = ['Wins','win','bags']
bootcamp = ['Bootcamp','Workshop']
conference = ['Conference']
#print(posts)
for i in posts:
    if 'Wins' in i:
        winner.add_row([i])
        winner.align['Winners'] = 'l'
    elif 'Bootcamp' in i or 'Workshop' in i:
        workshop.add_row([i])
        workshop.align['Workshops'] = 'l'
    elif 'Conference' in i:
        conferences.add_row([i])
        conferences.align['Conferences'] = 'l'
print()
print(winner)
print()
print(conferences)
print()
print(workshop)

