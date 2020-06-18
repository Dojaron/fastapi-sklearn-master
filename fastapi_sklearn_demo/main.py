# -*- coding: utf-8 -*-

from fastapi import FastAPI, status
from pydantic import BaseModel, FilePath
from sklearn.linear_model import LogisticRegression
from joblib import dump, load
import pandas as pd
import numpy as np


app = FastAPI()




@app.get("/api/v1/")
def read_root():
    return {"Hello": "World"}


class trainItem(BaseModel):
    inputXPath: str
    inputyPath: str
    modelFilePath: str


class pretictItem(BaseModel):

    inputXPath: str
    inputyPath: str
    modelFilePath: str
    resultFilePath: str



@app.post("/api/v1/modelTrain/LR/", status_code=200)
def post_train(item: trainItem):

    XtrainPath = item.inputXPath
    # ytrainPath = item.get('outputPath')
    ytrainPath = item.inputyPath
    modelPath = item.modelFilePath


    Xtrain = pd.read_csv(XtrainPath)
    ytrain = pd.read_csv(ytrainPath)
    # print(ytrain.shape)

    clf = LogisticRegression(solver='lbfgs')
    clf.fit(Xtrain, ytrain.iloc[:,1])


    try:
        with open(modelPath, 'wb') as f:
            dump(clf, f)
        f.close()
    except Exception:
        raise Exception("Error occurs whiling dumping model!")


    return {"modelPath": modelPath, "message": "success"}



@app.post("/api/v1/modelPretiction/LR/", status_code=status.HTTP_200_OK)
def post_predict(item: pretictItem):


    XtestPath = item.inputXPath
    ytestPath = item.inputyPath
    modelPath = item.modelFilePath
    resultPath = item.resultFilePath

    Xtest = pd.read_csv(XtestPath)
    ytest = pd.read_csv(ytestPath)


    try:
        with open(modelPath, 'rb') as f:
            clf = load(f)
        f.close()
    except Exception:
        raise Exception("Error occurs whiling loading model!")

    predictResult = clf.predict(Xtest)
    print(predictResult)

    try:
        predictResult = pd.DataFrame(predictResult)
        predictResult.to_csv(resultPath)
    except Exception:
        raise Exception("Error occurs whiling saving result!")

    score = clf.score(Xtest, ytest.iloc[:,1])

    return  {"resultPath": resultPath, "score": score,"message": "success"}




if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)