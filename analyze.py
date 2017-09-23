from pandas import read_csv
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_extraction import DictVectorizer

df = read_csv('flight_data.csv')

# 'Current time at origin',
# 'Current time at destination', 
columns = ['Age', 'Nationality',
           'Sleep quality (1-5)']

df = df[columns].to_dict(orient='records')
# grd = GradientBoostingClassifier(n_estimators=10)

vectorizer = DictVectorizer(sparse=False)
X_train = vectorizer.fit_transform(df)
# vec_x_cat_test = vectorizer.transform( x_cat_test )
