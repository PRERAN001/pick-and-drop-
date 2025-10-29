import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
data=pd.read_csv("linearregression.csv")
dataframe=pd.DataFrame(data)
x=dataframe[["choose ur columns"]]
y=dataframe["choose ur columns"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
x_train_scaled=scalar.fit_transform(x_train)
x_test_scaled=scalar.transform(x_test)
model=LinearRegression()
model.fit(x_train_scaled,y_train)
y_pred=model.predict(x_test_scaled)
for actual,predicted in zip(y_test,y_pred):
    print(f"actual: {actual}, predicted: {predicted}")
mse=np.mean((y_test - y_pred) ** 2)
print(f"mean Squared Error: {mse}")
r2_score=model.score(x_test_scaled,y_test)
print(f"R^2 Score: {r2_score}") 

