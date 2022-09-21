

import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression



df = pd.read_csv('ptt_data(output)/final_sumweek.csv')
df[['Close', 'points', 'status']] = df[['Close', 'points', 'status']].shift(-1)


df = df.dropna().drop(['points', 'Close'], axis=1)


plt.figure(figsize=(10,10),dpi=200)
sns.heatmap(df.corr(),cmap="Blues",
            vmin=-1,
            vmax=1,
            square=True,
            annot=True)



x = df.iloc[:,3:-1].values
y = df[['status']].values

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.1)



Regression = LogisticRegression()
scaler = StandardScaler()
scaler = scaler.fit(train_x)

train_x = scaler.transform(train_x)
test_x = scaler.transform(test_x)

from sklearn.metrics import r2_score
model = Regression.fit(train_x,train_y)
pred_y = model.predict(test_x)
print(accuracy_score(test_y,pred_y))
print('訓練集: ',model.score(train_x,train_y))
print('測試集: ',model.score(test_x,test_y))



from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.naive_bayes import GaussianNB



models = {
    "                   Logistic Regression": LogisticRegression(),
    "                 KNeighbors Classifier": KNeighborsClassifier(),
    "                                   SVC": SVC(),
    "              Decision Tree Classifier": DecisionTreeClassifier(),
    "               RandomForest Classifier": RandomForestClassifier(),
    "           GradientBoosting Classifier": GradientBoostingClassifier(),
    "            GaussianProcess Classifier": GaussianProcessClassifier(),
    "                           Gaussian NB": GaussianNB(),
    }

for name, model in models.items():
    model.fit(train_x, train_y)
    print(name + " trained.")



for name, model in models.items():
    print(name + " accuracy_score Score: {:.5f}".format(model.score(test_x, test_y)))




