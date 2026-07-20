import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

#Load dataset 
df = pd.read_csv('churn.csv')

#preprocession :Drop unique ID and handle missing total charges
df.drop('customerID',axis=1,inplace = True)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'],errors = 'coerce')

#encoding categorical data 
le = LabelEncoder()
for col in df.select_dtypes(include =['object']).columns:
    df[col]=le.fit_transform(df[col])

x = df.drop('Churn',axis = 1)
y = df['Churn']

#Train model
x_train,x_test,y_train,y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
) 
model = xgb.XGBClassifier(use_label_encoder=False,eval_metrics='logloss')
model.fit(x_train,y_train)

#save the model 
with open('churn_model.pkl','wb') as f:
    pickle.dump(model,f)

