#coding: utf-8

import recastai

from pandas import read_csv
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_extraction import DictVectorizer

print('Reading dummy data ... ')
df = read_csv('flight_data.csv')
print('[Done]')

# 'Current time at origin',
# 'Current time at destination',
columns = ['Age', 'Nationality',
           'Sleep quality (1-5)']

print('Training on past data ... ')
df = df[columns].to_dict(orient='records')
# grd = GradientBoostingClassifier(n_estimators=10)
vectorizer = DictVectorizer(sparse=False)
X_train = vectorizer.fit_transform(df)
print('[Done]')

token = '87a01f56c6f1cb0a2020b6568f6b80c5'

if __name__ == '__main__':

    while True:
        request = recastai.Request(token, 'en')
        text = raw_input('You: ')
        response = request.converse_text(text)
        print('Bot: %s' % response.reply)

    # if response.intent:
    #     print(response.intent.slug)
    # if response.intent.slug == 'YOUR_EXPECTED_INTENT':
    #     """Do your code..."""
