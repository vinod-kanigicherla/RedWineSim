import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import warnings

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder

github_url = 'https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv'
red_wine_data = pd.read_csv(github_url)
print('Wine Quality Dataset:')

dividers = [2, 6, 8]  # Adjust the upper bin to include 8
possible_preds = ['high', 'low']
red_wine_data['quality'] = pd.cut(red_wine_data['quality'], bins=dividers, labels=possible_preds)

print(red_wine_data['quality'].value_counts())

if len(red_wine_data['quality'].value_counts()) == 2:
    label_quality = LabelEncoder()
    red_wine_data['quality'] = label_quality.fit_transform(red_wine_data['quality'])
else:
    print("Binning did not result in two distinct categories.")

X = red_wine_data.drop('quality', axis=1)
y = red_wine_data['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

random_forest = RandomForestClassifier(n_estimators=100, random_state=42)

random_forest.fit(X_train, y_train)

y_pred = random_forest.predict(X_test)

print("Classification_Report - ")
print(classification_report(y_test, y_pred))
print("Accuracy - ", accuracy_score(y_test, y_pred))

# Outputs whether the wine is low (0) or high (1) quality based on Random Forest Model
def wineEvaluator(wine_feature_vector, random_forest):
    warnings.filterwarnings('ignore')
    y_pred = random_forest.predict(np.array(wine_feature_vector).reshape(1, -1))
    return y_pred[0]
