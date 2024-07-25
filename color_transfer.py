import numpy as np
import cv2
import os


sourcesFolder = '/Users/ls2n/Downloads/colorTransfert/source'
targetFileName = '/Users/ls2n/Downloads/colorTransfert/target/IMG_4458.JPG'


def get_mean_and_std(x):
	x_mean, x_std = cv2.meanStdDev(x)
	x_mean = np.hstack(np.around(x_mean,2))
	x_std = np.hstack(np.around(x_std,2))
	return x_mean, x_std

def color_transfer_new(sourceFilename, t_mean, t_std):
	sc = cv2.imread(sourceFilename)
	sc = cv2.cvtColor(sc, cv2.COLOR_BGR2LAB)
	s_mean, s_std = get_mean_and_std(sc)
	img_n=((sc-s_mean)*(t_std/s_std))+t_mean
	img_n = np.clip(img_n, 0, 255)
	dst = cv2.cvtColor(cv2.convertScaleAbs(img_n), cv2.COLOR_LAB2BGR)
	return dst




t = cv2.imread(targetFileName)
t = cv2.cvtColor(t,cv2.COLOR_BGR2LAB)
t_mean, t_std = get_mean_and_std(t)


sourcesDirectory = os.fsencode(sourcesFolder)
for sourceFile in os.listdir(sourcesDirectory):
	sourceFilename = os.fsdecode(sourceFile)
	sourceFilepath = os.path.join(sourcesFolder, sourceFilename)
	if sourceFilename.endswith(".JPG"):
		print('processing ', sourceFilename)
		dst = color_transfer_new(sourceFilepath, t_mean, t_std)
		cv2.imwrite('result/' + sourceFilename, dst)
	else:
		print('WARNING file not processed: ', sourceFilepath)
