import pandas as pd
pd.set_option('display.max_colwidth', -1)
df = pd.read_csv('jeopardy.csv')
#print(df.info())

# 2
df.columns = ['show_number', 'air_date', 'round', 'category', 'value', 'question', 'answer']
# print(df.info())

# 3, 4
words = [' king ', ' England ']
def filter(data, words):
    filter_question = lambda question: all(word.lower() in question.lower() for word in words)
    filtered = data.loc[data.question.apply(filter_question)]
    return filtered

# 5
df['float_value'] = df['value'].apply(lambda x: float(x[1:].replace(',', '')) if x != 'None' else 0)


filtered = filter(df, words)
print(filtered['float_value'].mean())

# 6
def unique_count(filtered):
    return filtered['answer'].value_counts()

answer_count = unique_count(filtered)

# 7
# value of prices in each air_date
air_dates = df.groupby('air_date').float_value.sum().reset_index().sort_values(by='float_value', ascending=False)
print(air_dates)

# computer in questions throughout time
computer_90s = filter(df, [' computer '])[(df['air_date'] > '1990-01-01') & (df['air_date'] < '1999-12-31')]
# Asked 57 times in the 1990s
computer_2000s = filter(df, [' computer '])[(df['air_date'] > '2000-01-01') & (df['air_date'] < '2009-12-31')]
# Asked 167 times in the 2000s

# What's the most answered answered in relation to a question about computer
computer = filter(df, [' computer ']).groupby('answer').show_number.count().reset_index().sort_values(by='show_number', ascending=False)

# Relation between round and the categories
round_categories = df.groupby(['round', 'category']).show_number.count().reset_index().sort_values(by=['round', 'show_number'], ascending=False)