# -*- coding: utf-8 -*-

from fastapi import APIRouter, status
from pydantic import BaseModel

import pandas as pd
from pickle import load

router = APIRouter()


class pretictItem(BaseModel):

    inputXPath: str
    inputyPath: str
    modelFilePath: str
    resultFilePath: str

@router.post("/api/v1/modelPretiction/LR/", status_code=status.HTTP_200_OK)
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

    return  {"resultPath": resultPath, "score": score, "message": "success"}