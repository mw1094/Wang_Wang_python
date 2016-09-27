# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 02:38:14 2016

@author: Meng Wang
"""

"""
Created on Sun Sep 11 00:09:52 2016

Homework 1 Group C

@author: Meng Wang
"""

#question1

##Prof G - Define this inside the function or as a parameter to the function
dic1={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"år"}#creat a dictionary

def translate(English):
    """
    This function translate a list of English words into Swedish Words.
    My thought: find the matched words in dic and creat a new list.
    
    Parameter:
    A list
    
    Returns:
    A new list consists of translated words
    """
    Swedish=[]#creat an empty list "Swedish"
    for k in English: #input a lsit 'English'
        if k in dic1:
            Swedish.append(dic1[k]) #dic1[k] mathch the keys to their values in dict1. Return the mathced results and add them up to list.
        else:
            ##Prof G - Nice way to handle, make sure to say why. There is an
            ##Prof G - unstated assumption here.
            Swedish.append(k) #in case of words not in dictionary
    return(Swedish)
    
print(translate(['merry','christmas','and','happy','new','year']))

#question2
def char_freq(string):
    '''
    This function return the frequency listing of characters contained in it.
    My thought: Let letters be the keys and frequency be the values in dictionary.
    
    Parameter:
    A string
    
    Returns:
    A dictionary showing frequency ofcharaters
    '''
    freq={} #freq is a dictionary
    for i in string:
        if i in freq:
            freq[i]=freq[i]+1 #if i repeat one time in string, the values of "i" in freq add 1
        else:
            freq[i]=1 #if i does not repeat in string, the value of i is 1, meaning there is only 1 i in the string
    return freq
    
print(char_freq("abbabcbdbabdbdbabababcbcbab"))

#question3

##Prof G - Define inside the function or as a paraemter. 
key={'a':'n', 'b':'o','c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v',
'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j',
'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X',
'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L',
'Z':'M'}

def encoderdecoder(code):
    '''
    This function can encode and decode string using dictionary "key".
    My thought: find the values of every letters in code, and add them up. For punctuations, when can not find 
    keys in "key", keep them and also add them up.
    
    Parameter:
    A string
    
    Returns:
    Decoded string
    '''
    answer="" #creat an empty "answer" 
    for i in code:
        if i in key:
            answer=answer+key[i] #key[i] can find the mathaced values in dictionary. Add the value up to form a word or sentence
        else:
            answer=answer+i #for punctuations and spaces, keep them and also add them up to form a sentence
    return answer
    
print(encoderdecoder('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))

#question4
import re #import regular expression module
def correct(string):
    '''
    Define a simple "spelling correction" function correct()that takes a
    string and sees to it that 1) two or more occurrences of the space
    character is compressed into one, and 2) inserts an extra space
    after a period if the period is directly followed by a letter.
    My thought: use regular expression, correct the sentence in two steps.
    
    Parameter:
    A string
    
    Returns:
    Correct string
    '''
    string=re.sub('\ +',' ',string) #substitute one or more spaces between two words to one space
    string=re.sub('\.','. ',string) #substitute period end with no space to period end with one space
    return(string)

##Prof G - Works well except there's an extra space if the period is followed
##Prof G - by many spaces. See how I modified your test case below.    
print(correct("This  is very.          funny    and cool.Indeed!"))

#question5
def make_3sg_form(word):
    '''
    This function make_3sg_form() gives a verb in infinitive
    form returns its third person singular form. Rules are as follows.
    a. If the verb ends in y, remove it and add ies b. If the verb ends in o, ch, s, sh, x
    or z, add es c. By default just add s
    My thought: Use endswith and replace.
    
    Parameter:
    A string(word)
    
    Returns:
    Third person sigular form of the word
    '''
    es=('o','ch','s','sh','x','z')
    if word.endswith('y'):
        word=word.replace(word[-1],'ies') #replace words end with'y' to 'ies'
    elif word.endswith(es):
        word=word +'es' #add 'es' to words end with 'o','ch','s','sh','x','z'
    else:
        word=word+'s' #by default, add 's'
    return word
    
print(make_3sg_form('satisfy'))
print(make_3sg_form('catch'))
print(make_3sg_form('work'))

#question6
##Prof G - Define inside function or as a parameter
con="qwrtzpsdfghjklyxcvbnm"
vowel="aeiuo" 
def make_ing_form(word):
    '''
    This function make_ing_form() which given a verb in infinitive form returns its present participle form.Rules are as follows:
    a. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.) b. If the verb ends in ie, change ie to y and
    add ing c. For words consisting of consonant-vowel-consonant, double the final letter before adding ing d. By default just add ing
    My thought: Use replace function.
    
    Parameter:
    A string(word)
    
    Returns:
    Present participle form of the word.
    '''
    ##Prof G - Good way to handle exceptions! Is there a way to handle these 
    ##Prof G - in the logic? Are these the only exceptions in the English 
    ##Prof G - language?
    exception=['be','see','flee','knee'] #exception, as rule a requires
    if word.endswith('ie'):
        word=word.replace(word[-2:],'y')+'ing' #if word end with "ie", replace with "y" and add "ing"
    elif word.endswith('e') and word not in exception:
        word=word.replace(word[-1],'ing') #if word end with "e", delete it and add "ing"
    elif word[-3] in con and word[-2] in vowel and word[-1] in con: #consonant-vowel-consonant
        word=word+word[-1]+'ing' #double the final letter before adding ing
    else:
        word=word+'ing' #By default just add ing
    return word
    
print(make_ing_form('lie'))
print(make_ing_form('flee'))
print(make_ing_form('bite'))
print(make_ing_form('dive'))
print(make_ing_form('code'))
print(make_ing_form('work'))

#question7
from functools import reduce  #import reduce module

##Prof G - Good use of reduce()!
def max_in_list(list1):
    '''
    This function uses the higher order function reduce() to takes a list of numbers and returns the largest
    one.
    
    Parameter:
    A list of numbers
    
    Returns:
    The maximum number
    '''
    return reduce(max,list1) #compare the first two numbers, and then compare the largest number in the first two with the thrid number, and so on.

print(max_in_list([1,2,3,4,5]))

#question8
def listlength(word):
    '''
    The following functions map a list of words into a list of integers
    representing the lengths of the correponding words. Three functions are written using a for-loop.
    
    Parameter:
    A list of words
    
    Returns:
    A new list consists of the lengths of each words
    '''
    length = [] #empty list
    for i in word:
        length.append(len(i)) #add the length of each word in list"word" to list"length"
    return length
    
print(listlength(['I','love','python']))

##Prof G - Nice alternative using map() generator    
def listlength2(word):
    '''
    The following functions map a list of words into a list of integers
    representing the lengths of the correponding words. Three functions are written using the higher order
    function map().
    
    Parameter:
    A list of words
    
    Returns:
    A new list consists of the lengths of each words
    '''
    return list((map(len,word))) #substitute the length of word to word in list using map function
    
print(listlength2(['I','love','python']))

##Prof G - Nice alernative using list comprehension  
def listlength3(word):
    '''
    The following functions map a list of words into a list of integers
    representing the lengths of the correponding words. Three functions are written using list comprehensions.
    
    Parameter:
    A list of words
    
    Returns:
    A new list consists of the lengths of each words
    '''
    length=[len(i) for i in word] #put length of each word in "word" list into "length" list
    return length
    
print(listlength3(['I','love','python']))

#question9
def find_longest_word(list1):
    '''
    This function find_longest_word() takes a list of words
    and returns the length of the longest one using only higher order
    functions.
    
    Parameter:
    A list of words
    
    Returns:
    The length of the longest word
    '''
    return max(map(len,list1)) #use map function to substitute list 1 with length of each word in list1, then use max function to find the longest one

print(find_longest_word(['i','love','python']))

#question10
def filter_long_words(list1, n):
    '''
    This function filter_long_words()that takes a list of words and an integer
    and returns the list of words that are longer than n.
    
    Parameter:
    A list of words and a number n
    
    Returns:
    A list of words that are longer than n
    '''
    return(list(filter(lambda x:len(x)>n,list1))) #lambda function len(x)>n can see if length of word in list1 >n. filter function pick those words up.

print(filter_long_words(['i','love','python'], 3))

#question11
dictionary={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"år"} #creat a dictionary
def translate(list1):
    '''
    This function uses the higher order function map()to write
    a function translate() that takes a list of English words and
    returns a list of Swedish words.
    My thought: Use map function to substitute the matched values in list to string.
    
    Parameter:
    A list of words
    
    Returns:
    A list consists of translated words
    '''
    return list(map(dictionary.get,list1))#find matched words in dictionary, substitue words and list them out

print(translate(['merry','christmas','and','happy','new','year']))

#question12
##Prof G - Rename these functions to avoid ambiguity with built-in functions
def mymap(function,list1):
    '''
    Implement the higher order functions map()
    Creat a new list, function old list, and add to new list.
    
    Parameter:
    A function and a list
    
    Returns:
    A proceed list using function
    '''
    newlist=[]#creat an empty new list
    for i in list1:
        newlist.append(function(i))#fuction(i) are added up to new list
    return newlist
    
print(mymap(lambda x: x+1,[1,2,3,4,5]))
    
def myfilter(function,list1):
    '''
    Implement the higher order functions map(), filter()
    Creat a new list. If function is true, add to new list.
    
    Parameter:
    A function and a list
    
    Returns:
    A list filtered by function
    '''
    newlist=[]#creat a new list
    for i in list1:
        if function(i)==True:
            newlist.append(i) #if Ture, add to newlist
    return newlist
    
print(myfilter(lambda x:x>4,[1,2,3,4,5,6]))
    
def myreduce(function,list1):
    '''
    Implement the higher order functions reduce(). 
    Function i in list and its next.
    
    Parameter:
    A function and a list
    
    Returns:
    A proceed list using function
    '''
    accum=list1[0] #let accum be the first iterator in list1
    for i in list1[1:]: #for every i starting from the second place in list1
       accum=function(accum,i) #funciton accum and i, and let accum be the result
    return accum

print(myreduce(max,[1,2,3,4,5,6]))