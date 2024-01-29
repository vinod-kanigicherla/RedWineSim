# Red Wine Making Simulator

Creators: Vinny Kanigicherla, Leo Chang, Kyle Yin

**Description:** "Red Wine Making Simulator" is a game where players choose grapes, manage fermentation, and adjust wine composition to produce and rate their own red wines. This interactive simulator combines real winemaking processes with engaging gameplay. Discover the intricacies of wine production, from grape selection to the final taste test.

### Key Libraries:
- **Pygame** - Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.
- **Pandas** - pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.
- **Scikit-Learn** - Scikit-Learn, also known as sklearn is a python library to implement machine learning models and statistical modelling. 
- **Seaborn** - Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

### Key Files:
1. RedWineNotebook.ipynb - The Singlestore Notebook
2. RedWineMakingSimulator.py - The Game

#### Our Final Model:
**Random Forest Classifier**

**What and why?**

A Random Forest Classifier is a machine learning model that builds several decision trees and merges their outcomes. It is like a team of decision trees where each gives their decision, and the final decision is made based on the majority vote. This model is especially useful for handling datasets with many features, like in the red wine quality dataset. The red wine dataset likely includes various attributes like acidity, alcohol content, and sugar levels. Random Forest works well for the Red Wine Dataset because:
1. Handles Complex Interactions: It can understand complex relationships between these features and how they affect wine quality.
2. Reduces Overfitting: Unlike a single decision tree, which might focus too much on the training data (overfitting), Random Forest balances this by considering the insights of multiple trees.
3. Improves Accuracy: With multiple trees, it’s more likely to catch patterns and trends that a single tree might miss, leading to more accurate classifications of wine quality.
4. Feature Importance: Random Forest can also tell which features (like acidity or sugar level) are more important in determining the quality of the wine, providing valuable insights for wine analysis.
