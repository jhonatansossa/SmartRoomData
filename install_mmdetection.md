## mmdetection installation
```
pip install -U openmim
mim install mmengine
mim install "mmcv>=2.0.0"
mim install mmdet

```

## Download model config and weights

```
mim download mmdet --config rtmdet_tiny_8xb32-300e_coco --dest .
```

All the other detection model configs can be found [here](https://github.com/open-mmlab/mmdetection?tab=readme-ov-file#:~:text=Architectures-,Object%20Detection,-Instance%20Segmentation)
