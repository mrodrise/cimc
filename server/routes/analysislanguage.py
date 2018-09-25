import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions

from credentials_cimc import natural_language_understanding

class analysisLanguage(object):

    def __init__(self, text, target):

        self.response = natural_language_understanding.analyze(text=text, features=Features(
            sentiment=SentimentOptions(
            targets=[target])))

    def get_sentiment(self):
#        result = json.dumps(self.response, indent=2)
#        print(result)
        return str(self.response['sentiment']['document']['label'])
