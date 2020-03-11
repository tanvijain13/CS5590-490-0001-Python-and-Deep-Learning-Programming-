import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.preprocessing import StandardScaler

# Dataset: https://www.kaggle.com/ronitf/heart-disease-uci
train = pd.read_csv('heart.csv')

# fetching top 4 features
numeric_features = train.select_dtypes(include=[np.number])
corr = numeric_features.corr()
plt.figure(figsize=(20,20));
sns.heatmap(corr, annot=True, cmap="YlGnBu")
plt.show();
print (corr['age'].sort_values(ascending=False)[:4], '\n')

# Printing the Null values
nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

# Handling the missing value
data = train.select_dtypes(include=[np.number]).interpolate().dropna()
print(sum(data.isnull().sum() != 0))

# Encoding the categorial feature
data_binary = pd.get_dummies(train)
data_binary.head()


# Spliting Test and Train data
x_train, x_test, y_train, y_test = train_test_split(data_binary,train['age'])
performance = []


# ------------ Using Naive Bayes classification --------------
GNB = GaussianNB()

# Training Model
GNB.fit(x_train,y_train)
train_score = GNB.score(x_train,y_train)

# Predicting Output
test_score = GNB.score(x_test,y_test)
print(f'Gaussian Naive Bayes : Training score: {train_score}, Test score: {test_score}')


# -------------- Using KNN classification --------------
knn = KNeighborsClassifier(n_neighbors=5)

# Training Model
knn.fit(data_binary,train['age'])
knn.score(x_train,y_train)

# Predicting Output
train_score = knn.score(x_train,y_train)
test_score = knn.score(x_test,y_test)
print(f'K Neighbors : Training score: {train_score}, Test score: {test_score}')


# -------------- creating SVM classification --------------
svc = svm.SVC(kernel='linear')

# Training Model
scaler = StandardScaler()
scaler.fit(data_binary,train['age'])
x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)
svc.fit(x_train_scaled,y_train)

# Predicting Output
train_score = svc.score(x_train_scaled,y_train)
test_score = svc.score(x_test_scaled, y_test)
print(f'SVM : Training score: {train_score}, Test score: {test_score}')
