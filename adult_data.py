import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# code to display 16 columns in run tool
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 30)
# reading the csv file
df = pd.read_csv('adult_csv.csv', na_values=['#NAME?'])
#
print(df['classs'].value_counts())
#
df['classs'] = [0 if x == '<=50K' else 1 for x in df['classs']]
#
data_frame_features = df.drop('classs', 1)
data_frame_outcome = df.classs
print(data_frame_features.head(5))
print(f'\noutcome {data_frame_outcome.head(5)}')
# education is a categorical features
print(df['education'].head(5))
# creating dummies for education
# dummies using pandas ( another example is one hot encoding using scikit learn)
dummies_education = pd.get_dummies(data_frame_features['education'])
print(dummies_education.head(5))
# check how many unique categories are there and decide which categories needs dummies
for col_name in data_frame_features.columns:
    if data_frame_features[col_name].dtype == 'object':
        unique_categories = len(data_frame_features[col_name].unique())
        print(f'Feature {col_name} has {unique_categories} Unique Categories')
# Taking a look at native-country which has 42 unique categories
print(f'\nnative-country categories')
# Creating dummy list for every column (categorical)
todummy_list = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
# Creating a dummy for native-country as US and other
data_frame_features['native-country'] = ['US' if x == 'United-States' else 'Other' for x in
                                         data_frame_features['native-country']]
print(data_frame_features['native-country'].value_counts().sort_values(ascending=False))

def dummy_list(data_frame_features, todummy_list):
    for x in todummy_list:
        dummies = pd.get_dummies(data_frame_features[x], prefix=x, dummy_na=False)
        data_frame_features = data_frame_features.drop(x, 1)
        data_frame_features = pd.concat([data_frame_features, dummies], axis=1)
    return data_frame_features, todummy_list


dummies_list_values = dummy_list(data_frame_features, todummy_list)
dummies_list_values_array = []
for i in dummies_list_values:
    dummies_list_values_array.append(dummies_list_values)

print(f'\ndummy values')
print(dummies_list_values)
print(data_frame_features['workclass'].head(5), data_frame_features['native-country'].head(5))
#calculating how much data is missing
print(data_frame_features.isnull().sum().sort_values(ascending=False))
# filling the missing values with median
imp = SimpleImputer(missing_values='NAN', strategy='median', fill_value=None)
data_frame_features = pd.DataFrame(data=imp.transform(data_frame_features), columns=data_frame_features.columns)

imp.fit(data_frame_features)

print(f'\nRecalculated')
print(data_frame_features.isnull().sum().sort_values(ascending=False))