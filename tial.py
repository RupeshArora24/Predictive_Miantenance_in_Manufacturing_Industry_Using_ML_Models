import pickle
import pandas as pd
data=pickle.load('clean_hepatitis_dataset.csv')
with open('knn_hepB_model.pkl', 'rb') as f:
        data1 = pickle.load(f)
