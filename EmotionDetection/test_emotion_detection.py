from emotion_detection import emotion_detector
from emotion_detection import emotion_predictor

import unittest

class TestCalculations(unittest.TestCase):

    def test_sentiment_analyzer(self):
        self.assertEqual(emotion_predictor('I am glad this happened'), 'joy')
        self.assertEqual(emotion_predictor('I am really mad about this'), 'anger')
        self.assertEqual(emotion_predictor('I feel disgusted just hearing about this'), 'disgust')
        self.assertEqual(emotion_predictor('I am so sad about this'), 'sadness')
        self.assertEqual(emotion_predictor('I am really afraid that this will happen'), 'fear')

if __name__ == '__main__':
    unittest.main()