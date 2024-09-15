import os
from PIL import Image
import cv2 as cv
import math as m

ROOT_DIR = 'D:/PersonProject/Project_with_Py/ImageProcessing/'
FOLDER_DEFAULT = "resultSet"


def load(path: str):
    try:
        return os.path.join(ROOT_DIR, path)
    except:
        return False

def rootDir():
    return ROOT_DIR


def makeFolder(path: str=FOLDER_DEFAULT):
    try:
        os.makedirs(f'{ROOT_DIR}{path}')
        return path
    except:
        return None

def readImg(path: str) -> cv.typing.MatLike:
    try:
        return cv.imread(load(path))
    except:
        return None
    
def saveImage(imgPath: str,newName: str, image: cv.typing.MatLike) -> str:
    try:
        path = f'{ROOT_DIR}{newName}'
        cv.imwrite(path, image)
        return path
    except:
        return None
    
def showImage(path: str):
    try:
        img = Image.open(f'{ROOT_DIR}{path}')
        img.show()
    except:
        return None

def showImageFullPath(path: str):
    try:
        img = Image.open(path)
        img.show()
    except:
        return None
    
def cvShow(imgName: str, frameName='cvshow'):
    try:
        img = readImg(imgName)
        cv.imshow(frameName, img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except:
        return None

def cvShowFullPath(imgPath: str, frameName='cvshow'):
    try:
        img = cv.imread(imgPath)
        cv.imshow(frameName, img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except:
        return None
    
def resize(imgPath:str, newName:str, w=900, h=500, dirSaveImg: str = FOLDER_DEFAULT) -> str:
    try:
        img = readImg(imgPath)
        resizedImg = cv.resize(img, dsize=(w,h))
        newPath = f'{dirSaveImg}/{newName}'
        fullPath = saveImage(newPath,resizedImg)
        print(f"Resized Image has been saved at: {fullPath}")
        return fullPath
    except:
        return None

def resizeHalf(image: cv.typing.MatLike) -> cv.typing.MatLike:
    try:
        return cv.resize(image, dsize=None, fx=0.5, fy=0.5)
    except:
        return None

def cropImg(imgPath: str, imgNewSaveName: str, dirSaveImg: str = FOLDER_DEFAULT)-> str:
    try:
        img = readImg(imgPath)
        percentCropBlockWidth = m.floor(0.1 * img.shape[0])
        percentCropBlockHeight = m.floor(0.1 * img.shape[1])
        crop = img[percentCropBlockWidth:(img.shape[0]-percentCropBlockWidth), percentCropBlockHeight:img.shape[1]-percentCropBlockHeight]
        fullPath = saveImage(f'{dirSaveImg}/{imgNewSaveName}',crop)
        print(f"Resized Image has been saved at: {fullPath}")
        return fullPath
    except:
        return None