# variables: patientid, termnamemapped, result_name, value
# outcome: termnamemapped
# predictors: result_name, value

import pandas as pd
ms = pd.read_csv(r'C:\Users\mandyho\Desktop\data_MS_5000.csv')
ts = pd.read_csv(r'C:\Users\mandyho\Desktop\data_TS_5000.csv')


ms.head(5)
ts.head(5)

# data processing: change long to wide
ts['idx'] = ts['encounterid']
ts['result'] = ts["result_name"]
ts_temp = ts.groupby(['encounterid', 'result_name']).first()
ts_wide = ts_temp.pivot(index = 'idx', columns = 'result', values = 'value')

ms['idx'] = ms['encounterid']
ms['result'] = ms["result_name"]
ms_temp = ms.groupby(['encounterid', 'result_name']).first()
ms_wide = ms_temp.pivot(index = 'idx', columns = 'result', values = 'value')

# add outcome
ts_wide['outcome'] = 1
ms_wide['outcome'] = 0




# combine 
frame = [ms_wide, ts_wide]
combine = pd.concat(frame)

# check dimension
combine.shape
ms_wide.shape
ts_wide.shape

# check missing value
combine.isna().sum()

# drop cholesterol, contain too many missing value
combine = combine.drop("CHOLESTEROL", axis=1)

#	missing values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='median', axis=0)
imputer = imputer.fit(combine)
combine_impute = imputer.transform(combine)
# Labels are outcome
labels = combine_impute[:,4]
# Remove the labels as features data
features = combine_impute[:,0:4]

# normalization
features_df['n0'] = (features_df.iloc[:,0] - features_df.iloc[:,0].mean())/features_df.iloc[:,0].std()
features_df['n1'] = (features_df.iloc[:,1] - features_df.iloc[:,1].mean())/features_df.iloc[:,1].std()
features_df['n2'] = (features_df.iloc[:,2] - features_df.iloc[:,2].mean())/features_df.iloc[:,2].std()
features_df['n3'] = (features_df.iloc[:,3] - features_df.iloc[:,3].mean())/features_df.iloc[:,3].std()

features_new = features_df.iloc[:,4:]

# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features_new, labels, test_size = 0.3, random_state = 42)

print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)

from sklearn.ensemble import RandomForestClassifier

# Create the model with 100 trees
model = RandomForestClassifier(n_estimators=500,
                               bootstrap = True,
                               max_features = 'sqrt')
# Fit on training data
model.fit(train_features, train_labels)

# Import the model we are using
# from sklearn.ensemble import RandomForestRegressor
# Instantiate model with 500 decision trees
# rf = RandomForestRegressor(n_estimators = 500, random_state = 42)
# Train the model on training data
# rf.fit(train_features, train_labels)

# Use the forest's predict method on the test data
predictions = model.predict(test_features)
print(predictions)
rf_probs = model.predict_proba(test_features)[:,1]
print(rf_probs)

from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 

results = confusion_matrix(test_labels, predictions) 
print('Confusion Matrix :') 
print(results) 
print('Accuracy Score :',accuracy_score(test_labels, predictions) )
print('Report : ') 
print(classification_report(test_labels, predictions)) 



