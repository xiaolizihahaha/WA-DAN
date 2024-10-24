##################################################
# Training Config
##################################################
GPU = '0'                   # GPU
workers = 4                 # number of Dataloader workers
epochs = 160                # number of epochs
batch_size = 12             # batch size
learning_rate = 1e-3        # initial learning rate

##################################################
# Model Config
##################################################
image_size = (448, 448)     # size of training images
net = 'resnet50'  # feature extractor  # 'vgg19', 'vgg19_bn', 'resnet34', 'resnet50', 'resnet101', 'resnet152', 'inception_mixed_6e', 'inception_mixed_7c'
num_attentions = 32         # number of attention maps
beta = 5e-2                 # param for update feature centers

##################################################
# Dataset/Path Config
##################################################
tag = 'mydataset'                # 'aircraft', 'bird', 'car', or 'dog'

# saving directory of .ckpt models
save_dir = './FGVC/CUB-200-2011/ckpt - 1/'
model_name = 'model_epoch_4.ckpt'
log_name = 'train.log'

# checkpoint model for resume training
ckpt = False
# ckpt = save_dir + model_name

##################################################
# Eval Config
##################################################
visualize = True
eval_ckpt = save_dir + model_name
eval_savepath = './FGVC/CUB-200-2011/visualize/'