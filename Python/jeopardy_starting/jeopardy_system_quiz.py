# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:21:15 2020
In this version of Jeopardy, there is no round variation.
But there is a question counter, category information and price accumulation as long as the answers are correct

@author: chris
"""

import pandas as pd
from random import randint

jeopardy = pd.read_csv('jeopardy.csv')
#print(jeopardy.head())
jeopardy.columns = ['show_number', 'air_date', 'round', 'category', 'value', 'question', 'answer']
jeopardy['float_value'] = jeopardy['value'].apply(lambda x: float(x[1:].replace(',', '')) if x != 'None' else 0)

ask = True
counter = 1
answer = ''
price = 0
while(ask):
    random_question = randint(0, len(jeopardy))
    # inform question number and price money of the question
    print('Question #{} - Category: {} - Price Money: ${}'.format(counter, jeopardy.loc[random_question, 'category'], jeopardy.loc[random_question, 'float_value']))
          
    print(jeopardy.loc[random_question, 'question'], end=' ')
    answer = input()
    if(answer.lower() == jeopardy.loc[random_question, 'answer'].lower()):
        price += jeopardy.loc[random_question, 'float_value']
        print('You are correct! You win {}! Your money is now {}!'.format(jeopardy.loc[random_question, 'float_value'], price))
    else:
        print("You're answer was incorrect... The correct answer is [" + jeopardy.loc[random_question, 'answer'] + ']')
        ask = False
    counter += 1
    print()
# output price money if there is one
print()
if(price > 0):
    print('Congratulations! You won ${}!'.format(price))
else:
    print('Sorry, please try again another time...')