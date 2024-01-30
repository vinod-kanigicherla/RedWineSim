
# Outputs whether the wine is low (0) or high (1) quality based on Random Forest Model
def wineEvaluator(wine_feature_vector):
    # Data Loading + Feature Engineering + Model Creation
    import numpy as np
    import pandas as pd
    import warnings

    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import LabelEncoder

    red_wine_data = pd.read_csv("./project/winequality-red.csv")

    dividers = [2, 6, 8]  # Adjust the upper bin to include 8
    possible_preds = ['high', 'low']
    red_wine_data['quality'] = pd.cut(red_wine_data['quality'], bins=dividers, labels=possible_preds)

    if len(red_wine_data['quality'].value_counts()) == 2:
        label_quality = LabelEncoder()
        red_wine_data['quality'] = label_quality.fit_transform(red_wine_data['quality'])

    X = red_wine_data.drop('quality', axis=1)
    y = red_wine_data['quality']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    random_forest = RandomForestClassifier(n_estimators=100, random_state=42)

    random_forest.fit(X_train, y_train)

    y_pred = random_forest.predict(X_test)

    warnings.filterwarnings('ignore')
    y_pred = random_forest.predict(np.array(wine_feature_vector).reshape(1, -1))
    return y_pred[0]