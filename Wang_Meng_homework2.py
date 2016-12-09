# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 08:25:23 2016

@author: Meng Wang
"""

#question 1
def is_palindrome(string):
    '''    
    This function is a palindrome recogniser that read a string and
    return TRUE if it's a palindrome or FLASE if else.
    
    Parameter:
    A string
    
    Returns:
    True if palindrome
    False if not palindrome
    '''
    string = string.lower() #lower case of each letter
    puncspace="`~!@#$%^&*()_-=+[]{}\|;:,<.>/? "
    for k in string:
        if k in puncspace:
            string=string.replace(k,'')#no spaces and punctuations in string
    if not string.isalpha():
        return False     # return false if there is non-character in it
    if string[::-1] == string: # if the reverse is the same as itself
        return True
    else:
        return False   

def palindrome_file(file):
    '''
    This function palindrome_file() reads a file and apply palindrome function
    to all lines then return lines that are palindrome
    
    Parameter:
    A file
    
    Return:
    Lines that are palindrome   
    '''
    file1 = open(file) # open a file
    for line in file1.read().split('\n'): # read file by lines
        if is_palindrome(line):
            print(line) # print the line if it is a palindrome
    return None
#e.g.        
palindrome_file('name1.txt')#name1.txt is a local file


#question 2
def semord(file):
    '''
    This function works as a semordnilap recogniser that accepts a file name 
    (pointing to a list of words) from the user and finds and prints all pairs 
    of words that are semordnilaps to the screen.
    
    Parameter:
    A file 
    
    Returns
    A list containing paired words
    '''
    list1=list(open(file).read().split())#convert a text file into a list
    puncspace="`~!@#$%^&*()_-=+[]{}\|;:,<.>/?"
    for k in list1:
        k=k.lower()#lower case of every character
        if k in puncspace:
            list1=list1.replace(k,'')#no punctuations in string
    new=[]#creat an empty list
    for i in list1:
        if i[::-1] in list1 and len(i)>1: #if the length of word is not 1 
                                          #and the backward word in the list
            new.append(i+' '+i[::-1])#word+space+backward word
    return new
 #e.g.   
semord('name1.txt')#'name1.txt' is a local file


#question 3
def char_freq_table(file):
    '''
    This function accepts a file name from the user, builds a frequency listing of
    the characters contained in the file, and prints a sorted and
    nicely formatted character frequency table to the screen.
    
    Parameter:
    A file
    
    Returns:
    Dictionary(Table) showing frequency of characters
    '''
    string=open(file).read()#open a file and read lines
    dic= {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,
          'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,
          'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}#formated dictionary
    string=string.lower()#lower case of each letter
    string=string.replace('\n','')
    for i in string:
        if i in dic:
            dic[i]+=1#check frequency
    import operator
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(0))#convert into a
                                                                #list and sort
    return sorted_dic
#e.g.    
char_freq_table('name1.txt')#'name1.txt' is a local file


#question4
def speak_ICAO(string,ICAOpause=1,wordpause=3):
    '''
    This function translate string into ICAO words and speak the out.
    Apart from the text to be spoken, the procedure also needs to accept two 
    additional parameters: a float indicating the length of the pause between 
    each spoken ICAO word, and a float indicating the length of the pause 
    between each word spoken.
    
    Parameter:
    A string
    
    Returns:
    Speak ICAO words
    '''
    import os
    import time
    ICAO = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 
 	'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 
 	'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 
 	'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 
 	'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 
 	'z':'zulu'} # define dictionary dic
    for k in string.split():#split a string into words
        for i in k:#i represents each character
            if i not in "`~!@#$%^&*()_-=+[]{}\|;:,<.>/?0123456789": #only letter
                os.system('say '+ICAO[i.lower()])#speak
                time.sleep(ICAOpause)#pasue between ICAO words
        time.sleep(wordpause)#pause between words
#e.g.
speak_ICAO('When I met your mother',1,3)


#question 5
def hapax(file):
    '''
    Define a function that gives the file name of a text will return all its hapaxes.
    Capitalization and punctuations are ignored.
    
    Parameter:
    A file
    
    Returns:
    A list containing all hapaxes
    '''
    string=open(file).read()#read each line in the file
    string=string.lower()#lower case of each letter
    puncspace="`~!@#$%^&*()_-=+[]{}\|;:,<.>/?"
    for k in string:
        if k in puncspace:
            string=string.replace(k,'')#no punctuations in string
    hapaxes=[]#empty list
    for i in string.split():
        if string.count(i)==1:#if the word shows up only once
            hapaxes.append(i)#add it into the list
    return hapaxes
#e.g.
hapax('name1.txt') #'name1.txt' is a local file    
    
    
#question 6
def numberfile(file):
    '''
    This function gives a text file will create a new text file in
    which all the lines from the original file are numbered from 1 to n.
    
    Parameter:
    A file
    
    Returns:
    A new file with numbered lines
    '''
    file1=open(file).readlines()#file1 is a list
    file2=open('New.txt','w')#new empty file
    for i in range(len(file1)):
        file2.write('line'+str(i+1)+': '+file1[i])#add 'line#: ' to the 
    #begining of each line, put them together into line2
    file2.close()#save and close
#e.g.
numberfile('name1.txt')#'name1.txt' is a local text file


#question 7
def ave(file):
    '''
    This function calculates the average word length of a text
    stored in a file
    
    Parameter:
    A file
    
    Returns:
    A number(the sum of all the lengths of the word tokens in
    the text, divided by the number of word tokens)
    '''
    string=open(file).read()#open and read file
    puncspace="`~!@#$%^&*()_-=+[]{}\|;:,<.>/? "
    string=string.replace('\n',' ')# no'\n' in string
    wordnumber=len(string.split())#caculate the number of words
    for k in string:
        if k in puncspace:
            string=string.replace(k,'')#no spaces and punctuations in string
    charnumber=len(string)#caculate the number of characters
    return charnumber/wordnumber
#e.g.
ave('name1.txt')#'name1.txt' is a local text file


#question 8
'''
This is a program able to play the "Guess the number" game.

Parameter:
Name and a number

Returns:
Strings and how many times taken
'''
name=input('What is your name? ')#input name
chance=1
import random
b=random.randint(0,20)
while True:
    number=int(input(name+', I am thinking of a number between 1 and 20. Take a guess. '))#input a number
    if number==18:
        print('Good job, {}! You guessed my number in {} guesses!'.format(name,chance))#
        break#stop the program when guess the number
    elif number<18:
        print('Your guess is too low. Take a guess.')
        chance+=1#times taken+1
    else:
        print('Your guess is too high. Take a guess.')
        chance+=1#times taken+1
#e.g
#This program need to be saved and imported so it can run
        

#question 10
def lingo(answer):
    '''
    lingo game: The object of the game is to find this word by guessing, and in
    return receive two kinds of clues: 1) the characters that are fully
    correct, with respect to identity as well as to position, and 2) the
    characters that are indeed present in the word, but which are
    placed in the wrong position. Write a program with which one can
    play Lingo. Use square brackets to mark characters correct in the
    sense of 1), and ordinary parentheses to mark characters correct in
    the sense of 2)
    
    Parameter:
    a word as answer
    
    Returns:
    word after proceed
    '''
    while True:
        new=''
        guess=input('take a guess(only 5 characters!): ')#guess a word
        for i in range(len(guess)):
            if guess[i]==answer[i]:#if identity and and position are both correct
                new+='['+guess[i]+']'#add '[]' to the character
            elif guess[i] in answer:#if only identity is correct
                new+='('+guess[i]+')'#add '()' to the character
            else:
                new+=guess[i]#if neither is correct, just add character
        if guess==answer:
            print('Clue: '+new)
            print('You are right! Good job!')
            break#stop the program
        else:
            print('Clue: '+new)
#e.g.
lingo('catch')
            
        
#question 11
punc='?!'
lower='abcdefghijklmnopqrstuvwxyz'
cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num='0123456789'
title=['Mr','Mrs','Dr']
punctuation="`~!@#$%^&*()_-=+[]{}\|;:,<.>/?"
def splitter(file):
    '''
    This function opens a txt file and works as a sentence splitter to
    write its sentences with each sentences on a separate line.
    Sentence boundaries occur at one of "." (periods), "?" or "!", except that
    a. Periods followed by whitespace followed by a lower case letter
    are not sentence boundaries.
    b. Periods followed by a digit with no intervening whitespace are
    not sentence boundaries.
    c. Periods followed by whitespace and then an upper case letter,
    but preceded by any of a short list of titles are not sentence
    boundaries. Sample titles include Mr., Mrs., Dr., and so on.
    d. Periods internal to a sequence of letters with no adjacent
    whitespace are not sentence boundaries (for example,
    www.aptex.com, or e.g).
    e. Periods followed by certain kinds of punctuation (notably comma
    and more periods) are probably not sentence boundaries.   
    
    Parameter:
    A text file (the input file will be overwritten by the function!)
    
    Returns:
    A text file (the input file will be overwritten by the function!)
    '''
    string=open(file,'r').read()#open file for read
    for i in range(1,len(string)-2):
        if string[i]=='.':#period
            if string[i+1]==' 'and string[i+2] in lower:
                string=string #Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
            elif string[i+1] in num:
                string=string #Periods followed by a digit with no intervening whitespace are not sentence boundaries.
            elif (string[i-2:i] or string[i-3:i]) in title and string[i+1]==' ' and string[i+2] in cap:
                string=string #Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are not sentence boundaries
            elif string[i-1]!=' ' and string[i+1]!=' ':
                string=string #Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries 
            elif string[i+1] in punctuation:
                string=string #Periods followed by certain kinds of punctuation
            else:
                string=string[:i+1]+'\n'+string[i+2:] #else, add '\n' after period (new line)
        elif string[i] in punc:
            string=string[:i+1]+'\n'+string[i+2:]#for sentences end with '?' and '!', seperate new line
    file1=open(file,'w')#open for write, warning: this function will overwrite your file
    file1.write(string)#write string into it
    file1.close()#save and close
#e.g
splitter('name1.txt') #'name1.txt' is a local file