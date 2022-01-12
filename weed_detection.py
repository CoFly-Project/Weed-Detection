import tensorflow as tf
import segmentation_models as sm
import glob
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import datetime 
import sys
from tensorflow import keras

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2" # Optional for hiding the tensorflow messages

def winapi_path(dos_path, encoding=None):
	if (not isinstance(dos_path, str) and encoding is not None): 
		dos_path = dos_path.decode(encoding)
	path = os.path.abspath(dos_path)
	if path.startswith(u"\\\\"):
		return u"\\\\?\\UNC\\" + path[2:]
	return u"\\\\?\\" + path

images = winapi_path(sys.argv[1])
save_dir = winapi_path(sys.argv[2])
results_dir = os.path.join(save_dir, 'results')
os.makedirs(results_dir, exist_ok=True)
sm.set_framework('tf.keras')

extensions = ["*.png", "*.jpg", ".jpeg"]
start_sc = datetime.datetime.now()

original_shapes = []
predict_imgs = []
for ext in extensions:
	for img_path in glob.glob(os.path.join(images, ext)):
		img = cv2.imread(img_path, cv2.IMREAD_COLOR)
		height, width, channels = img.shape

		q_height, mod_height = divmod(height, 32)
		if mod_height != 0:
			new_height = (q_height + 1)*32
		else:
			new_height = height

		q_width, mod_width = divmod(width, 32)
		if mod_width != 0:
			new_width = (q_width + 1)*32
		else:
			new_width = width

		result = cv2.copyMakeBorder(img, 0, int(new_height-height), 0, int(new_width-width), cv2.BORDER_CONSTANT, None, value = 0)
		img_reshaped = cv2.cvtColor(result, cv2.COLOR_BGR2RGB) 
		original_shapes.append(img.shape)
		predict_imgs.append(img_reshaped)
	   
predict_imgs_arr = np.array(predict_imgs)

classes = ['weeds', 'background']
activation = 'sigmoid' if len(classes) == 1 else 'softmax'

BACKBONE = 'efficientnetb1'
preprocess_input = sm.get_preprocessing(BACKBONE)

model = sm.Unet(BACKBONE, classes=len(classes), activation=activation)
model.load_weights('./weights0300.hdf5')

os.chdir(results_dir)
times = []
for i, (pred_img, original_shape) in enumerate(zip(predict_imgs_arr, original_shapes)):
	pred_img_input = np.expand_dims(pred_img, 0)
	test_img_input = preprocess_input(pred_img_input)

	start = datetime.datetime.now()
	mask_unet = model.predict(test_img_input)
	stop = datetime.datetime.now()
	times.append((stop-start).total_seconds())
	
	mask = np.argmax(mask_unet, axis=3)[0,:,:]*255	
	mask_3ch = np.stack((mask, )*3, axis = -1)
	mask_3ch[mask==255] = [51, 153, 255]
	mask_3ch = mask_3ch.astype('int8')

	result = cv2.addWeighted(pred_img, 1, mask_3ch, 0.7, 0.7, dtype = cv2.CV_8UC2)
	result_reshaped = result[:original_shape[0], :original_shape[1]]

	f = plt.figure()
	f.set_figheight(result_reshaped.shape[0] / f.get_dpi())
	f.set_figwidth(result_reshaped.shape[1] / f.get_dpi())
	ax = plt.Axes(f, [0., 0., 1., 1.])
	ax.set_axis_off()
	f.add_axes(ax)
	ax.imshow(result_reshaped)
	f.savefig('ID_{}.png'.format(i))
	plt.close()

stop_sc = datetime.datetime.now()
print('Average prediction time for each image: {}s'.format(sum(times[1:])/len(times)))
print('Execution time of this module: {}s'.format(stop_sc-start_sc))
print('Done!')
