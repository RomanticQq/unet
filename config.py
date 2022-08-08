# -- coding: utf-8 --
"""
@time : 2022/8/7 15:27
@author : fuqiang
@file : config.py
@project : Pytorch-UNet
"""


class TrainConfig:
    epochs = 5
    batch_size = 1
    lr = 1e-5
    load = False
    scale = 0.5
    val = 10.0
    amp = True
    bilinear = False
    classes = 2


class PredictConfig:
    model = './checkpoints/checkpoint_epoch1.pth'
    input = './data/imgs/'
    output = './result/'
    mask_threshold = 0.5
    scale = 0.5
    bilinear = False
    no_save = False
    viz = True


train_config = TrainConfig
predict_config = PredictConfig

