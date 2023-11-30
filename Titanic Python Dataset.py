# -*- coding: utf-8 -*-

import seaborn as sns

titanic = sns.load_dataset("titanic")
print(titanic.info())
#print('\n\n\n\n',titanic.describe())
print('\n\n',titanic.columns)
titanic.head()

titanic.isna().sum()

#Example hypothesis: maybe the people on the upper decks were more likely to survive!
#(For reference, the decks are ordered in alphabetical order, so deck A was at the top, and G at the bottom of the ship).
sns.barplot(data=titanic, x = 'deck', y = "survived")

"""As we can see, it seems like there is not much of a correlation between the deck and the survival rate! (In case you are curious, the column "deck" is actually missing a lot of entries. You can confirm this by running::
 titanic.isna().sum()

 So, just in the case of using the deck, the database is not really reliable.)
"""

#1 Maybe number of survived femals were bigger than survided males as they used the lifeboat first
sns.barplot(data=titanic, x = 'sex', y = titanic["survived"]*100) # or use this methode to scale

#matplotlib.pyplot.ylim -> to change the scale

#true

##2 Maybe most of people died where from the second and second and third class
sns.barplot(data=titanic, x = 'survived', y = "class")

#true as we can see from graph that most of people who survived were from First, then second then thirs class

# 2 using countplot()
sns.countplot(titanic, x="class", hue="survived")

#3 maybe the majority of the people who died from the third class were over 60
sns.boxplot(data=titanic, x = 'age', y = "class", hue='survived')

#I don't think that's true as people over 60 in the third class are mostly outliers because the major distribution
#of age is between 0 and 50,
#but taking into consideration that the age column has 177 missing/na values, the age might not be a very accurate parameter to use

#4 maybe no one survived above 80 years old
sns.displot(data=titanic, x="age", hue = "survived")

#false some survived

#4 continued:  but We can definitely see that those who survived above 80 an outlier
sns.boxplot(data=titanic, x = 'survived', y = "age")

#but again age is not a reliable factor as age data is missing 177 value

#5 Maybe if a person isn't alone his chances to survive will be bigger
sns.pairplot(titanic, x_vars="sex",y_vars="alone",hue="survived")


#most of Males who were alone survived
#and
#and most of women who were alone died

#an observation

#I think what is most difficult for me is to understand what each column refers to

#Ex: Parch/sibsp/embarked/fare

#So Parch col has a value of 2 which totally doesn't make any sense and this goes also do the rest of the cols mentioned

#import pandas as pd

#titanicDF= pd.DataFrame(sns.load_dataset('titanic'))

#filtered_data = titanicDF.groupby(['pclass','sex','survived','alone','adult_male'])['survived'].count()\
#.unstack('pclass',fill_value='-')\




#gfg = sns.swarmplot(data=filtered_data, x='adult_male', y='alone', hue='survived')

#filtered_data

#gfg = sns.pairplot(filtered_data, x_vars='adult_male',y_vars='alone',hue="survived")
#[(titanic['pclass']==1) &( titanic['sex']=='male')]

# How to chnage the scale of the figure?
