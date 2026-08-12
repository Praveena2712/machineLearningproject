print("starting")

import src.logger
print("logger ok")

from src.pipeline.predict_pipeline import CustomData, PredictPipeline
print("pipeline ok")

import dill
model = dill.load(open("artifacts/model.pkl", "rb"))
print("model ok:", type(model))

pre = dill.load(open("artifacts/preprocessor.pkl", "rb"))
print("preprocessor ok:", type(pre))

print("all good")