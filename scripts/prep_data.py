import pandas as pd
from sklearn.preprocessing import LabelEncoder
#from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler


# Drop column
def drop_columns():
    df = df.drop([col1,col2],axis=1)

#prepare data for modelling
def feature_scaling(data:pd.DataFrame,col1:str):
    data[col1].replace(to_replace = dict(M = 0, B = 1), inplace = True)
    
    cols = data.columns.to_list()
    if col1 in cols:
        cols.remove(col1)
        
    scaled_features = data.copy()
    features = scaled_features[cols]
    scaler = StandardScaler()

    scaled_features[cols] = scaler.fit_transform(features.values)
    return scaled_features

# Save data
def to_csv(df):
    df.to_csv('../data/processed_data.csv',index=False)
    print('Data saved successfully...')

