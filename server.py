"""
Your module docstring here describing the purpose of server.py
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """
    Docstring explaining the purpose of render_index_page function.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_app():
    """
    Docstring explaining the purpose of emotion_app function.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return 'Invalid text! Please try again!.'

    response = emotion_predictor(text_to_analyze)
    dominant_emotion = response.get("dominant_emotion")

    if dominant_emotion is None:
        return 'Invalid text! Please try again!.'

    formatted_string = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']}, 'sadness': {response['sadness']}, "
        f"and 'dominant_emotion': {dominant_emotion}"
    )

    print("Formatted string:", formatted_string)
    return formatted_string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
