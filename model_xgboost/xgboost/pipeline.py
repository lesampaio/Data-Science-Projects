from train_model import train
from predict_model import test
from utils.model_services import save_model_to_pkl

if __name__ == 'main':
    data_path = "/home/leticia/GitHub/Data-Science-Projects/model_xgboost/data/raw_data.csv"

    trained_model = train(data_path)
    test(data_path)

    save_model_to_pkl("/home/leticia/GitHub/Data-Science-Projects/model_xgboost/models/xgboost_model.pkl", trained_model)