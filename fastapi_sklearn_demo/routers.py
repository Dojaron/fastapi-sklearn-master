# -*- coding: utf-8 -*-

from fastapi import APIRouter

from train import fastapi_train
from predict import fastapi_predict


router = APIRouter()

router.include_router(fastapi_train.router, prefix="/api/v1")
router.include_router(fastapi_predict.router, prefix="/api/v1")