version = 'VVV4-18'
storage = '1'
epoch = '6'

# choose_name = ''            # train
# choose_name = '(test-1066)'     # test
# choose_name = '(val)'     # test
# choose_name = '(train)'     # test
# choose_name = '(test-5585+587)'   # test
# choose_name = '(test)'   # test
choose_name = '(all)'    # test
# choose_name = '(4096)'50    # test 4096
# choose_name = '(2034)'    # test 2034




##################################################
# Training Config
##################################################
GPU = '0'                   # GPU
workers = 0                 # number of Dataloader workers
epochs = 160                # number of epochs
batch_size = 16            # batch size  16
learning_rate = 1e-4        # initial learning rate

##################################################
# Model Config
##################################################
image_size = (448, 448)     # size of training images
# image_size = (224, 224)     # size of training images
net = 'resnet50'  # feature extractor  # 'vgg19', 'vgg19_bn', 'resnet34', 'resnet50', 'resnet101', 'resnet152', 'inception_mixed_6e', 'inception_mixed_7c'
num_attentions = 32         # number of attention maps
beta = 5e-2                 # param for update feature centers

##################################################
# Dataset/Path Config
##################################################
tag = 'mydataset'                # 'aircraft', 'bird', 'car', or 'dog'

# saving directory of .ckpt models


save_dir = './FGVC/CUB-200-2011/' + 'ckpt - ' + version + ' - storage/' + storage + '/'   # storage
# save_dir = './FGVC/CUB-200-2011/ckpt - ' + version + '/'   # 没storage/
model_name = 'model_epoch_' + epoch + '.ckpt'
log_name = 'train.log'


# checkpoint model for resume training
ckpt = False
# ckpt = save_dir + model_name

##################################################
# Eval Config
##################################################
visualize = False
eval_ckpt = save_dir + model_name
eval_savepath = './FGVC/CUB-200-2011/visualize - ' + version + '/'