#!/usr/bin/python3
import math as m
import random
d=3
field=[]
for i in range(d*d):
    field.append(i+1)
#field=[1,2,3,4,5,6,7,8,9]
signs=["x","o"]

def print_field(field):
#    d=int(m.sqrt(len(field)))
    for i in range(d):
        for j in range(d):
            if len(str(field[i*d+j])) == len(str(d*d)):
                print ("|"+str(field[i*d+j]),end="")
            else:
                print ("|"+" "*1+str(field[i*d+j]),end="")
        print("|")

def draw_on_field(field,pos,char):
    while field[pos] != pos+1:
        pos=int(input("please chose from free fields: "))-1
    field[pos]=char
        
def get_position():
    print("Free fields: ", get_free_fields(field))
    return int(input("where do you want to draw? "))-1
def game_running(field):
    if len(get_free_fields(field)) == 0:
        return False
    return True
def get_free_fields(field):
    free=[]
    for i in field:
        if i in range(len(field)+1):
            free.append(i)
    return free
def choose_sign():
    char=""
    while char not in signs:
        char=input("Choose x or o: ")
    robochar = signs[(signs.index(char)+1)%2]
    return char,robochar
char,robochar=choose_sign()

###GAME 
print_field(field)
while game_running(field): 
    draw_on_field(field,get_position(),char)
    if game_running(field):
        draw_on_field(field,random.choice(get_free_fields(field))-1,robochar)
    print_field(field)
print("game over")
