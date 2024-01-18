# Res2former
![pytorch](https://img.shields.io/badge/pytorch-v1.7.1-green.svg?style=plastic)
## Introduction
This is a pytorch implementation for the Visformer models. This project is based on the training code in [DeiT](https://github.com/facebookresearch/deit) and the tools in [timm](https://github.com/rwightman/pytorch-image-models).

## Usage
Clone the repository:
```bash
git clone https://github.com/hand-Max/Res2former.git
```
Install pytorch, timm and einops:
```bash
pip install -r requirements.txt
```
## Data Preparation
The layout of Imagenet data:
```bash
/path/to/imagenet/
  train/
    class1/
      img1.jpeg
    class2/
      img2.jpeg
  val/
    class1/
      img1.jpeg
    class2/
      img2.jpeg
```
## Network Training
Res2former models
```bash
python -m torch.distributed.launch --nproc_per_node=8 --use_env main.py --model Res2former --batch-size 64 --data-path /path/to/imagenet --output_dir /path/to/save --amp --qk-scale-factor=-0.5
python -m torch.distributed.launch --nproc_per_node=4 --use_env main.py --model Res2foremr --batch-size 256 --drop-path 0.03 --data-path /path/to/imagenet --output_dir /path/to/save --amp --qk-scale-factor=-0.5
```
The model performance:

|        model        | top-1 (%) | FLOPs (G) | paramters (M) | 
|:-------------------:|:---------:|:---------:|:-------------:|
|      Res2former     |   80.7    |    2.0    |     12.7      |

pre-trained models:

|                       model                       |   model    |                                                 log                                                 | top-1 (%) | 
|:-------------------------------------------------:|:----------:|:---------------------------------------------------------------------------------------------------:|:---------:|
|                     Res2former                    | [github](https://github.com/hand-Max/Res2former/releases/tag/1) |   [github](https://github.com/hand-Max/Res2former/releases/tag/1)    |   80.7   |
