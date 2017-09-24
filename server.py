# coding: utf-8

import recastai
import webbrowser
import numpy as np

from pandas import read_csv
from sys import platform

from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz

print('Reading dummy data ... ')
df = read_csv('flight_data.csv')
print('[Done]')

# 'Current time at origin',
# 'Current time at destination',
columns = ['Age', 'Nationality',
           'Sleep quality (1-5)']

le = LabelEncoder()
y = le.fit_transform(df['Light Color'].values)

print('Training on past data ... ')
df = df[columns].to_dict(orient='records')
vectorizer = DictVectorizer(sparse=False)
X = vectorizer.fit_transform(df)

X_train = X[:-1]
y_train = y[:-1]

grd = GradientBoostingClassifier(n_estimators=10)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
print('[Done]\n')

# dot_data = export_graphviz(clf, out_file=None,
#                            feature_names=vectorizer.feature_names_,
#                            class_names=le.classes_.tolist(),
#                            filled=True, rounded=True,
#                            special_characters=True,
#                            max_depth=3)
# try:
#     import graphviz
#     graph = graphviz.Source(dot_data)
#     # graph.view()
# except ImportError as e:
#     pass

banner = ("""

   ###    ##        #######  ########  ####    ###    
  ## ##   ##       ##     ## ##     ##  ##    ## ##   
 ##   ##  ##       ##     ## ##     ##  ##   ##   ##  
##     ## ##       ##     ## ##     ##  ##  ##     ## 
######### ##       ##     ## ##     ##  ##  ######### 
##     ## ##       ##     ## ##     ##  ##  ##     ## 
##     ## ########  #######  ########  #### ##     ## 

""") # noqa

# token = '87a01f56c6f1cb0a2020b6568f6b80c5'
token = '39ee3477451f32a0b5917fb01103b66e'

if __name__ == '__main__':

    is_american = 1
    is_chinese = 0
    is_french = 0

    print(banner)
    while True:
        request = recastai.Request(token, 'en')
        text = raw_input('You: ')
        response = request.converse_text(text)
        if response.intent.slug == 'goodbye':
            break
        elif response.intent.slug == 'rest-yes':
            print('Bot: What is your age?')
            age = int(raw_input('You: '))
            print('Determining the optimal lighting for age %d...'
                   % (age))
            y_out = clf.predict(np.array([age, is_american, is_chinese, is_french,
                                          5.])[None, :])
            y_out = le.inverse_transform(y_out)[0]
            url = 'lighting/%s.html' % y_out
            if platform == "linux" or platform == "linux2":
                webbrowser.open(url)
            else:
                client = webbrowser.get("open -a /Applications/Firefox.app %s")
                client.open(url)
        else:
            print('Bot: %s' % response.reply)
            continue
