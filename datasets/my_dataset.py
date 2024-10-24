""" CUB-200-2011 (Bird) Dataset
Created: Oct 11,2019 - Yuchong Gu
Revised: Oct 11,2019 - Yuchong Gu
"""
import os
import pdb
from PIL import Image
from torch.utils.data import Dataset
from utils import get_transform
import numpy as np
import torch
import torch
import random
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms


DATAPATH = 'D:\\project\\WS-DAN\\datasets\\CUB_200_2011(V2)'
image_path = {}
image_label = {}
mask_path = {}


class MyDataset(Dataset):
    """
    # Description:
        Dataset for retrieving CUB-200-2011 images and labels

    # Member Functions:
        __init__(self, phase, resize):  initializes a dataset
            phase:                      a string in ['train', 'val', 'test']
            resize:                     output shape/size of an image

        __getitem__(self, item):        returns an image
            item:                       the idex of image in the whole dataset

        __len__(self):                  returns the length of dataset
    """

    def __init__(self, phase='train', resize=500):
        assert phase in ['train', 'val', 'test']
        self.phase = phase
        self.resize = resize
        self.image_id = []
        self.num_classes = 2

        # get image path from images.txt
        with open(os.path.join(DATAPATH, 'images.txt')) as f:
            for line in f.readlines():
                id, path = line.strip().split(' ')
                image_path[id] = path

        with open(os.path.join(DATAPATH, 'masks.txt')) as f:
            for line in f.readlines():
                id, path = line.strip().split(' ')
                mask_path[id] = path


        # get image label from image_class_labels.txt
        with open(os.path.join(DATAPATH, 'image_class_labels.txt')) as f:
            for line in f.readlines():
                id, label = line.strip().split(' ')
                image_label[id] = int(label)

        # get train/test image id from train_test_split.txt     ----- 可改
        with open(os.path.join(DATAPATH, 'train_test_split(test).txt')) as f:    # train
        # with open(os.path.join(DATAPATH, 'train_test_split(val).txt')) as f:  # val
        # with open(os.path.join(DATAPATH, 'train_test_split(test).txt')) as f:  # test
            for line in f.readlines():
                image_id, is_training_image = line.strip().split(' ')
                is_training_image = int(is_training_image)

                if self.phase == 'train' and is_training_image:
                    self.image_id.append(image_id)
                if self.phase in ('val', 'test') and not is_training_image:
                    self.image_id.append(image_id)

        # transform
        self.transform = get_transform(self.resize, self.phase)

        # print(self.image_id)
        self.image_label = image_label
        self.image_path = image_path
        self.mask_path = mask_path

        # print(len(self.image_label))   # 11788
        # print(len(self.image_path))  # 11788
        # print(len(self.mask_path))  # 11788




    def __getitem__(self, item):
        # get image id
        image_id = self.image_id[item]
        # print(len(self.image_id))    # 11788
        # print(len(self.image_path))    # 11788
        # print(len(self.image_label))    # 11788
        # print(item,image_id)

        # image
        # print(os.path.join(DATAPATH, 'images'))
        # print(image_path)
        image = Image.open(os.path.join(DATAPATH, 'images', self.image_path[image_id])).convert('RGB')  # (C, H, W)
        image = self.transform(image)

        mask_img = Image.open(os.path.join(DATAPATH, self.mask_path[image_id])).convert('L')
        new_size =(int(self.resize[0]), int(self.resize[1]))
        mask_img = mask_img.resize(new_size)
        mask_np = np.array(mask_img)
        mask_np_bin = mask_np == 0  # 原图masks反转，值为0的区域为True，255的区域为False
        mask_tensor = torch.tensor(mask_np_bin, dtype=torch.bool)  # 转换为 PyTorch 张量
        mask_tensor = mask_tensor.unsqueeze(0)  # 在通道维度上增加一个维度


        # return image and label
        # print(mask_tensor.shape, image.shape)
        return mask_tensor, image, self.image_label[image_id] - 1  # count begin from zero

    def __len__(self):
        return len(self.image_id)



# if __name__ == '__main__':
#     ds = MyDataset('train')

#     print(len(ds))
#     for i in range(0, 1):
#         mask,image, label = ds[i]

#         tensor_np = mask.numpy()
#         image_np = np.uint8(tensor_np * 255)
#         cv2.imshow('Mask Image', image_np)    # 背景（感兴趣区域）白色255 True，其他（标出的不感兴趣区域）黑色0 False
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#         print(image.shape,label)