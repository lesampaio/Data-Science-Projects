import pickle
from pathlib import Path

def save_model_to_pkl(path_to_save_pkl: Path, trained_model):
    """
    Save trained model to pkl file format in a determined directory.

    Args:
        path_to_save_pkl: Path to directory to save pkl file.
        trained_model: Trained ML model.
    """
    with open(path_to_save_pkl, 'wb') as file:
        pickle.dump(trained_model, file)