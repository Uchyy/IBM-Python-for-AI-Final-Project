import requests
import json
#import numpy as np

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=myobj, headers=header)
    
    return response.text

def emotion_predictor(text_to_analyze):
    response = emotion_detector(text_to_analyze)
    format = json.loads(response)

    anger = format['emotionPredictions'][0]['emotion']['anger']
    disgust = format['emotionPredictions'][0]['emotion']['disgust']
    fear = format['emotionPredictions'][0]['emotion']['fear']
    joy = format['emotionPredictions'][0]['emotion']['joy']
    sadness = format['emotionPredictions'][0]['emotion']['sadness']

    arr = [anger, disgust, fear, joy, sadness]
    arr.sort()
    thisdict = {
                "anger": anger,
                "disgust": disgust,
                "fear": fear,
                "joy": joy,
                "sadness": sadness
                }
    thisdict_sorted = sorted(thisdict.items(), key=lambda x:x[1])
    dominant_emotion = thisdict_sorted[4][0]

    format_emotion = format['emotionPredictions'][0]['emotion']
    y = {"dominant_emotion" : dominant_emotion}

    format_emotion.update(y)

    return format_emotion
    #return dominant_emotion