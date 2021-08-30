# Breast cancer casualty 
The objective of this project is to 
* Perform Casualty Inference on [Brest cancer](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data) data set from Kaggle using Judea Pearl and his research groups framework.
* Infer the causal graph from observational data and then validate the graph.
* Merge machine learning with causal inference.

## Folders
Folder structure of the project.

data:

folder containing the data set of breast cancer downloaded. The data set contains 569 rows and 33 columns

notebook:

this folder contain notebooks files that are necessary for data exploration and to get more indepth analysis on the data set.
* DataExploration: Notebook file for making exploratory data analysis to help us understand more about the data.
* Causal_learnining: Contains causal_graphs and modelling

scripts:

contains python modules. The purpose of this forlder is for code modularization to increase code reusability.
* causal.py: python module to perfom causal learnin, graph, jaccard comparison etc
* data_exploration.py: python module to understand dataset
* modelling.py: different model package
* plots.py: python module to help visualize and make plots
* prep_data.py: python module used to standardize, clean, save and prepare data for modelling

