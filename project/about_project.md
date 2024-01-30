In this directory, you will find the Red Wine Making Simulator game created using PyGame.

### Our Project Plan:

Data analytics 
Clustering of data, regression line
Help wine maker make better wine
Map the 11 variables to 1 variable
- Given a set of data for a wine -> predict its quality
- Recommend a manufacturer on where to improve
Multi regression model
Support vector machine   
Heap map (for correlation)
K-means clustering (grouping similar data point together)
Factors 
1 - fixed acidity (tartaric acid - g / dm^3)
2 - volatile acidity (acetic acid - g / dm^3)
3 - citric acid (g / dm^3)
4 - residual sugar (g / dm^3)
5 - chlorides (sodium chloride - g / dm^3
6 - free sulfur dioxide (mg / dm^3)
7 - total sulfur dioxide (mg / dm^3)
8 - density (g / cm^3)
9 - pH
10 - sulphates (potassium sulphate - g / dm3)
11 - alcohol (% by volume)

Buttons 
Choose grapes  → tartaric acid → determines fixed acidity 
Type 
Ripeness 
When to harvest 
Early → too sour → more acid 
Middle → medium sugar, correct acidity
Late → sweet, but volatile acidity 
Adding sugar → residual sugar vs. alcohol level 
Too much? → volatile acidity 
Fermentation → alcohol level, citric acid (GOOD from grape types, decrease during fermentation), volatile acidity (BAD, comes from poor sanitation), 
Duration 
Temperature 
Higher temperature can increase volatile acidity
Fixed and free sulfur dioxide (antioxidant, prevent wine from spoiling (bacteria growth)) 
Have to be added before or after fermentation? 
Can’t be too much? 
pH → overall how much acid content 


Chloric 
Naturally present 
Density 
Alcohol level 
Alcohol: 
Higher is better 13 to 11
Sulphates: 
Higher is better 0.65 to 0.90
pH 
Lower is better, less significant 3.2 to 3.4 
Density 
Lower is better, less significant 0.9965 to 0.994
Total Sulfur dioxide, free sulfur dioxide
Does not seem to matter → some outliers and seems to be higher for 5 and 6 groups 
Residual sugar, chloride
Does not seem to matter, → A LOT OF outliers for 5 and groups 
Citric acid 
Higher ie better 0.4 to 0.6
Fixed acidity 
Does not seem to matter 
Volatile acidity 
Lower is better 0.5 to 0.2


Games to make wine
1. Choose among three types of grapes
	- Determines acidity (tartaric acid) —>
2. Adding sugar
	- Sugar level increases,  catalyzes fermentation
3. Fermentation time
	- Sugar level drops, alcohol level increases (density decreases)
4. Adding yeast
	- Catalyze fermentation

Choose grapes type then confirm
Hover to see the grapes feature? 
Becomes present starting now → Control temperature

Juice the grapes - Add sulfur dioxide (as preservant, A MUST as preservant)
Choose and add yeast 
Similar to choosing grapes? 
Thee above can’t go back, and is sequential 

Below they can’t be done at the same time 
Add sugar 
Add citric acid
(add chloride, warning) 

Fermentation + confirm button 
Once started → can’t stop → can’t add more ingredients in 
Choose when to stop the fermentation 

Stop fermentation 
Pour out wine, taste it 
Rate the wine

The pH will generally rise .15 to .3 during primary fermentation and malolactic fermentation. To achieve the target balance at the time of bottling, the grapes will need to be picked with a bit more acid to compensate for this loss.
Grapes will be picked with very high sugar levels, but this does not mean they will be sweet. For a dry wine, nearly all of this sugar is converted to alcohol. More sugar means more alcohol. If you know the target alcohol number, divide it by .57 to get an estimate of the percent sugar needed to achieve the target. 

Yeast info
https://winemakermag.com/resource/yeast-strains-chart

Titratable Acidity
https://vinmetrica.com/managing-ph-and-ta-in-wine/

Grape Info
https://www.smartwinemaking.com/post/optimal-sugar-and-acid-levels-for-popular-wine-grape-varieties
