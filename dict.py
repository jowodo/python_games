
#TODO
#zahlen statt buchstaben im menue
#random auf beiden sprachen?
#random als lernkartei


import json
import sys
import random



def version():
    if (sys.version.split('.')[0] != '3'):
        print("This script is written for python3")
        exit()


#TODO
def header():
    print('')
    print('bebibebibebibebibebibebibebibebibebi')
    print('bebi||                        ||bebi')
    print('bebi||  header in progress..  ||bebi')
    print('bebi||                        ||bebi')
    print('bebibebibebibebibebibebibebibebibebi')

def pi():
	print(',-,,-,,-,')
	print('|U||U||U|')
	print('|.||.||.|')
	print('|.||.||.| ____')
	print('| || || |/  __ \ ')
	print('( (  (  (  |  \_\ ')
	print('|          |__/ /')
	print('|            __/')
	print('|          /')

def menu():
    print('')
    print('~~~~~~~~|[menu-header]|~~~~~~~')
    print('\t (h) hamsara dictionary')
    print('\t (d) german dictionary')
    print('\t (z) time dictionary')
    print('\t (a) add new word')
    print('\t (t) translate')
    print('\t (q) quit')

def menu_select(selction):
    if selection == 'h':
        dictionary(hr)
    elif selection == 'd':
        dictionary(de)
    elif selection == 'z':
        date_dict(de,date)
    elif selection == 'a':
        add(de,date)
    elif selection == 't':
        transl(de,hr)
    elif selection=='quit()' or selection=='quit' or selection=='exit' or selection==':q':
        exit()
    else:
        rand(de,hr)

def dictionary(de):
    sde=sorted(de.keys())
    for i in sde:
        if (len(i) >= 8):
            print(i+'\t'+de[i])
        else:
            print(i+'\t\t'+de[i])
    
def date_dict(de,date):
    for i in date:
        if (len(de[i]) >= 8):
            print(de[i]+'\t'+i)
        else:
            print(de[i]+'\t\t'+i)
            
def update_hr(de):
    hr = {v:k for k,v in de.items()}
    return hr

def add(de,date):
    print('Type exit/quit to abbort')
    deutsch = input('german: ')
    if deutsch=='quit()' or deutsch=='quit' or deutsch=='exit' or deutsch==':q':
        return
    hamsara = input('hamsara: ')
    if hamsara=='quit()' or hamsara=='quit' or hamsara=='exit' or hamsara==':q':
        return
    de[deutsch]=hamsara
    date.append(deutsch)
    hr = update_hr(de)
    print('...word added successfully...')

#TODO please more elegant
def transl(de,hr):
    wort = input('Zu uebersetzen: ')
    try:
        print(de[wort])
    except KeyError:
        try:
            print(hr[wort])
        except:
            print("not a word")

def rand(de,hr):
    if (random.randint(0,1)):
        base = de
    else:
        base = hr
    words = list(base.keys())
    number = random.randint(0,len(words))
    if (number == len(words)):
        pi()
    else:
        print(words[number])


def ending():
	print('  ____     ...   ')
	print(' //o o\\\ c/o o\  ')
	print(' || u ||  \ u /  ')
	print('  _||_    _||_   ')
	print(' |.  .\  /.  .|  ')
	print(' ||  |\\\//|  ||  ')
	print(' O| .| @@ | .|O  ')
	print('  | ||    | ||   ')
	print('  | ||    | ||   ')
	print('  \'-`-`   \'-`-`  ')

############################################
############################################

version()
header()

########
# READ #
########
#TODO read in jason file 
#file_name1='dick.json'
filename_de='dict.json'
filename_time='timeline.json'
try:
    dic = open(filename_de)
    de_str = dic.read()
    de = json.loads(de_str)
    hr = {v:k for k,v in de.items() }
except:
    print('file not found')
    print(filename_de+' should be in same directory')
    yesno= input('wanna start with empty dictionary? (yes/no): ')
    if (yesno == 'no'):
        exit()
finally:
    dic.close()
try:
    tmln = open(filename_time)
    time_str = tmln.read()
    date = json.loads(time_str)
except:
    print(filename_time+' could not be found')
    exit()
finally:
    tmln.close()

##############
#### MAIN ####
##############
selection=''
while selection != 'q':
    menu()
    selection = input()
    menu_select(selection)

#########
# WRITE #
#########
text = json.dumps(de)
dic= open(filename_de, 'w')
dic.write(text)
dic.close()

ttext = json.dumps(date)
tmln = open(filename_time, 'w')
tmln.write(ttext)
tmln.close()

ending()

