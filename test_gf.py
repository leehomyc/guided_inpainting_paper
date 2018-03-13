import caffe
import numpy as np
from PIL import Image
import skimage
import scipy
caffe.set_mode_cpu()

w = '/home/eeb433/Documents/caffe/matlab/FaceCompletion_testing/model/Model_G.caffemodel'
net = caffe.Net(
    '/home/eeb433/Documents/caffe/matlab/FaceCompletion_testing/model/Model_G.prototxt', w, caffe.TEST)

image_file = '/home/eeb433/Documents/caffe/matlab/FaceCompletion_testing/TestImages/182659.png'
image_file = '/home/eeb433/Documents/faces/000189_input_image.png'
image_file = '/home/eeb433/Documents/faces/000194_input_image.png'
image_file = '/home/eeb433/Documents/faces/000197_input_image.png'
image_file = '/home/eeb433/Documents/faces/000200_input_image.png'

image = np.array(Image.open(image_file))
image = skimage.transform.resize(image, (128, 128))

# preprocessing the image to fit the net requirement
input_ = image

mx = 161
my = 68

mx = 110
my = 156

mx = 79
my = 134

mx = 86
my = 80

masksize_x = 225 - mx
masksize_y = 146 - my

masksize_x = 162 - mx
masksize_y = 232 - my

masksize_x = 209 - mx
masksize_y = 248 - my

masksize_x = 178 - mx
masksize_y = 150 - my

mx = mx/2
my = my/2
masksize_x = masksize_x/2
masksize_y = masksize_y/2

input_[my:my+masksize_y, mx:mx+masksize_x,
       :] = np.random.uniform(0, 1, (masksize_y, masksize_x, 3))

input_ = input_ * 2 - 1


input_ = input_.transpose(2, 1, 0)
input_ = input_[np.newaxis, ...]

net.blobs['data'].reshape(*input_.shape)
net.blobs['data'].data[...] = input_
output = net.forward()

image_o = output['reconstruction_new'][0]
image2 = image_o.transpose(2, 1, 0)
#image2 = np.rot90(image2, -1)
#image2 = np.flipud(image2)
image3 = (image2+1)/2
image3[image3 > 1] = 1
image3[image3 < 0] = 0
image3 = image3*255
image3 = image3.astype('uint8')
o_img = image * 255
o_img = o_img.astype('uint8')
o_img[my:my+masksize_y, mx:mx+masksize_x,
      :] = image3[my:my+masksize_y, mx:mx+masksize_x, :]
scipy.misc.imsave('res.jpg', o_img)
scipy.misc.imsave('res2.jpg', image3)
