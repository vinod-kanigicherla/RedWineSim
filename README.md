# Red Wine Making Simulator

![Image of Red Wine Making Simulator Interface](https://github.com/vinod-kanigicherla/RedWineSim/blob/main/images%2Bfonts/thumbnail.png?raw=true)

**Creators:** Vinny Kanigicherla, Leo Chang, Kyle Yin

**Description:** "Red Wine Making Simulator" is a game where players choose grapes, manage fermentation, and adjust wine composition to produce and rate their own red wines. This interactive simulator combines real winemaking processes with engaging gameplay. Discover the intricacies of wine production, from grape selection to the final taste test.

---

### How to Run:
1. Install python libries:
```
pip install pygame
pip install pygame_widgets
pip install scikit-learn
pip install pandas
pip install numpy
```

2. Run **GameFinal.py**

*Note: When running **GameFinal.py**, make sure you are in the **RedWineSim** directory.*

---

### Key Libraries:
- **Pygame** - Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.
- **Pandas** - pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.
- **Scikit-Learn** - Scikit-Learn, also known as sklearn is a python library to implement machine learning models and statistical modelling. 
- **Seaborn** - Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

---

### Key Files:
1. RedWineNotebook.ipynb - The Singlestore Notebook

- **Notebook Contents**:
   * Data Processing and Analysis: The notebook starts by loading a wine dataset, which includes various properties of wine samples along with their quality ratings. It involves cleaning the data, handling missing values, and possibly normalizing or standardizing the features. Then, it performs exploratory data analysis (EDA) to uncover trends and patterns, using visualizations like histograms and scatter plots to understand the relationships between different wine properties and quality.
   * Pattern Recognition and Insights: Through EDA, the notebook identifies critical factors that affect wine quality, such as acidity, sugar content, and alcohol level. These insights are essential for both improving the machine learning model's accuracy and informing game mechanics in the "Red Wine Making Simulator".
   * Machine Learning Model - Wine Evaluator: The notebook uses the processed data to develop a machine learning model that predicts the quality of wine based on its physicochemical properties. Techniques like Random Forest and Support Vector Machines are utilized, and the model's performance is evaluated using metrics like precision, recall, and F1-score.

2. RedWineMakingSimulator.py - The Simulator
- **Description:** "Red Wine Making Simulator" is a game where players choose grapes, manage fermentation, and adjust wine composition to produce and rate their own red wines. This interactive simulator combines real winemaking processes with real red wine quality data. Discover the intricacies of wine production, from grape selection to the final rating.
   
**Project Milestones/Key Solved Challenges:**
- Developed a simulation that mirrors real-life winemaking, aligning with an 11-feature input for the random forest model.
- Improved the model's performance in predicting wine quality through effective feature engineering.

---

### Our Final Model: **Random Forest Classifier**

**What and why?**

A Random Forest Classifier is a machine learning model that builds several decision trees and merges their outcomes. It is like a team of decision trees where each gives their decision, and the final decision is made based on the majority vote. This model is especially useful for handling datasets with many features, like in the red wine quality dataset. The red wine dataset likely includes various attributes like acidity, alcohol content, and sugar levels. Random Forest works well for the Red Wine Dataset because:
1. Handles Complex Interactions: It can understand complex relationships between these features and how they affect wine quality.
2. Reduces Overfitting: Unlike a single decision tree, which might focus too much on the training data (overfitting), Random Forest balances this by considering the insights of multiple trees.
3. Improves Accuracy: With multiple trees, it’s more likely to catch patterns and trends that a single tree might miss, leading to more accurate classifications of wine quality.
4. Feature Importance: Random Forest can also tell which features (like acidity or sugar level) are more important in determining the quality of the wine, providing valuable insights for wine analysis.
