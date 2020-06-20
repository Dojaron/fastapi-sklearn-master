# -*- coding: utf-8 -*-

from fastapi import APIRouter
from pydantic import BaseModel

import pandas as pd
from joblib import dump, load
from sklearn.linear_model import LogisticRegression

router = APIRouter()


class trainItem(BaseModel):
    inputXPath: str
    inputyPath: str
    modelFilePath: str

@router.post("/api/v1/modelTrain/LR/", status_code=200)
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