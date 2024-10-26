import librosa
import numpy as np
import torch
import torch.nn.functional as F
import io
import joblib



def load_sklearn_model(model_path):
    model = joblib.load(model_path)
    return model


def extract_features(audio_data, sr):
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sr, n_mfcc=13)
    mfccs_mean = np.mean(mfccs.T, axis=0)
    return mfccs_mean

def predict(model, features):

    if isinstance(model, torch.nn.Module):
        features_tensor = torch.tensor(features, dtype=torch.float32).unsqueeze(0)
        with torch.no_grad():
            output = model(features_tensor)
            probabilities = F.softmax(output, dim=1).numpy().flatten()
    else:
        features = features.reshape(1, -1)
        probabilities = model.predict_proba(features)[0]

    return probabilities
    