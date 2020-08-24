from vncorenlp import VnCoreNLP
from nltk.parse import CoreNLPParser

DEFAULT_LOCAL_ADDRESS = "http://127.0.0.1"
DEFAULT_VI_NER_PORT = 9001
DEFAULT_EN_NER_PORT = "9000"


class NER(object):
    TIT_KEY = 'title'
    PER_KEY = 'person'
    ORG_KEY = 'organization'
    LOC_KEY = 'location'

    def __init__(self, text):
        self.textMap = {}
        for line in text.split("\n"):
            self.textMap[line] = {
                self.TIT_KEY: 0,
                self.PER_KEY: 0,
                self.ORG_KEY: 0,
                self.LOC_KEY: 0,
            }

    def result(self):
        self.vn_ner()
        self.en_ner()
        self.calculateResult()
        return self.textMap

    def calculateResult(self):
        for line, point in self.textMap.items():
            totalPoint = sum(point.values())
            if totalPoint == 0:
                continue
            for key in point.keys():
                point[key] = float(point[key]) / float(totalPoint) 

    def vn_ner(self):
        annotator = VnCoreNLP(address=DEFAULT_LOCAL_ADDRESS, port=DEFAULT_VI_NER_PORT) 
        for line in self.textMap.keys():
            taggedText = annotator.annotate(line)
            try:
                taggedText = taggedText['sentences'][0]
                for value in taggedText:
                    if value['nerLabel'] in ['B-PER', 'I-PER']:
                        self.textMap[line][self.PER_KEY] += 1
                    if value['nerLabel'] in ['B-LOC', 'I-LOC']:
                        self.textMap[line][self.LOC_KEY] += 1
                    if value['nerLabel'] in ['B-ORG', 'I-ORG']:
                        self.textMap[line][self.ORG_KEY] += 1
            except Exception as e:
                print("Unable to anotate "+str(line))
                print(e)
                return e

    def en_ner(self):
        ner_tagger = CoreNLPParser(url=DEFAULT_LOCAL_ADDRESS + ":" + DEFAULT_EN_NER_PORT, tagtype='ner')
        for line in self.textMap.keys():
            taggedText = ner_tagger.tag((line.split()))
            try:
                for text, value in taggedText:
                    if value in ['PERSON']:
                        self.textMap[line][self.PER_KEY] += 1
                    if value in ['LOCATION']:
                        self.textMap[line][self.LOC_KEY] += 1
                    if value in ['ORGANIZATION']:
                        self.textMap[line][self.ORG_KEY] += 1
                    if value in ['TITLE']:
                        self.textMap[line][self.TIT_KEY] += 1
                    if value in ['NUMBER']:
                        continue

            except Exception as e:
                print("Unable to anotate "+str(line))
                print(e)
                return e


