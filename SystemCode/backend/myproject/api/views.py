
from rest_framework import viewsets, status
from rest_framework.response import Response 
from .models import AudioFile
from .serializers import AudioFileSerializer
from .softvoting_implemention import extract_features,load_sklearn_model,predict
import librosa
import numpy as np
import torch
import torch.nn.functional as F
import io
import joblib
import torch
import torch.nn as nn
import torch.optim as optim
import os

class AudioFileViewSet(viewsets.ModelViewSet):
    queryset = AudioFile.objects.all()
    serializer_class = AudioFileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            audio_file = serializer.instance.audio_file
            audio_path = audio_file.path

            # Load the audio file
            if os.path.exists(audio_path):
                audio_data, sr = librosa.load(audio_path, sr=None)
                print("audio load success")
            else:
                print("audio load failed")


            audio_data, sr = librosa.load(audio_path, sr=None)

            features = extract_features(audio_data, sr)

            voting_classifier= load_sklearn_model(r'./detection/voting_classifier.joblib')
            voting_probabilities = predict(voting_classifier, features)

            # Determine the predicted label based on the voting classifier's probabilities
            predicted_label_voting = np.argmax(voting_probabilities)

            # Print the results
            print(f"Voting Classifier - Predicted Label: {predicted_label_voting}, Probabilities: {voting_probabilities}")
            labels = [ 'Deception','Truth']
            # Print the predicted label and lying probability for the Voting classifier
            print(f"\nVoting Classifier Prediction: {labels[predicted_label_voting]}, Lying Probability: {voting_probabilities[0]}")         
            return Response({
                'Predicted Label': predicted_label_voting,
                'Voting Classifier Prediction': labels[predicted_label_voting],
                'Deception Probability': voting_probabilities[0]}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
