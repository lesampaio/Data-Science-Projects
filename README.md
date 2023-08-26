# Data-Science-Projects
Data science projects.

## [Machine Learning Model - XGBoost](/model_xgboost/)
Model definition: XGBoost Regressor model that predicts user queue waiting time.

About algorithm: XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework.

About data: Queue data of users in banks. Columns: bank,week,day,num,arrival_time,waiting_time,time_spent,exit_time,people_in_queue

### How to run

**Install python enviroment**

`
pip install -r requirements.txt 
`

**Run model pipeline**

`
python pipeline.py
`

### ML XGBoost Regressor Directory Structure

        ├── model_xgboost               <- "model_xgboost" XGBoost model package
        │   ├── __init__.py             <- This file makes "model_xgboost" a "Python package"
        │   └── data                    <- Data from third party sources
        │   │   └── raw_data.csv
        │   │
        │   ├── models                  <- Trained and serialized models, model predictions, or model summaries
        │   │
        │   └── requirements.txt        <- The requirements file for reproducing the analysis environment, e.g.
        │   │                     generated with `pip freeze > requirements.txt`
        │   │
        │   └── xgboost                 <- Scripts to train models and then use trained models to make predictions
        │   │   │   __init__.py         <- Makes "xgboost" a "Python subpackage"      
        │   │   ├── pipeline.py         <- Run model pipeline          
        │   │   ├── preprocess_data.py        
        │   │   ├── predict_model.py
        │   │   └── train_model.py
        │   │
        │   └── tests                   <- Tests folder