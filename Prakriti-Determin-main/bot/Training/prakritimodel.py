import os
from joblib import dump
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

PATH = os.getcwd()
df = pd.read_csv(rf"C:\Users\Muska\Downloads\Prakriti-Determin-main\Prakriti-Determin-main\bot\dataset\data.csv")
X = df.drop(columns="Dosha")
Y = df["Dosha"]

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
model = RandomForestClassifier()
model.fit(x_train, y_train)

dump(model,rf"C:\Users\Muska\Downloads\Prakriti-Determin-main\Prakriti-Determin-main\bot\models\trained_model")