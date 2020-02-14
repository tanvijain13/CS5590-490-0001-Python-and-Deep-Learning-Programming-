import pandas as pd
#reading the training dataset
train_df= pd.read_csv('train.csv')
#dropping Survived from the train set
X_train= train_df.drop("Survived",axis=1)
Y_train= train_df["Survived"]
#training on sex column
train_df['Sex'] = train_df['Sex'].map({'female': 1, 'male': 0}).astype(int)
#calculating correlation between survived number and sex of passengers
print(train_df['Survived'].corr(train_df['Sex'])*100)
