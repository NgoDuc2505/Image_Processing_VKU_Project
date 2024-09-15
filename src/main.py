import cv2 as cv
from absPath import *


folderSavedImgName = makeFolder('imgDplicated')
pathResize = resize("img/g.png","res.png", dirSaveImg=folderSavedImgName)
pathCrop = cropImg("img/g.png","croped.png",dirSaveImg=folderSavedImgName)
pathFlip = flipImage("img/g.png","flipped.png", dirSaveImg=folderSavedImgName)
k = cv.waitKey(0) 