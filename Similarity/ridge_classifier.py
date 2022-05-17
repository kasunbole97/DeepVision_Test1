import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import _pickle as cPickle

data_df = pd.read_csv('data/data.csv')
# print(data_df.head)

x = data_df.drop(['Meal Plan No', 'Percentage'], axis=1).values
y = data_df['Meal Plan No'].values

# print(x)
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

scaler = StandardScaler()

x_train_s = scaler.fit_transform(x_train)
x_test_s = scaler.fit_transform(x_test)


rgc = RidgeClassifier(alpha=10, random_state=42)
rgc.fit(x_train_s, y_train)

y_pred = rgc.predict(x_test_s)
score = rgc.score(x_test_s, y_test)
print(score)

acc = accuracy_score(y_test, y_pred)
print(acc)


# save the classifier
with open('ridge_model.pkl', 'wb') as fid:
    cPickle.dump(rgc, fid)






