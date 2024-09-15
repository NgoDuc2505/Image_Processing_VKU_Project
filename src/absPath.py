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
        if (not os.path.exists(f'{ROOT_DIR}{path}')):
            os.makedirs(f'{ROOT_DIR}{path}')
        return path
    except Exception as e:
        print(f"Error when load file: {e}")
        return None

def readImg(path: str) -> cv.typing.MatLike:
    try:
        return cv.imread(load(path))
    except:
        return None
    
def saveImage(newName: str, image: cv.typing.MatLike) -> str:
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

def cropComponent(imgSrc: cv.typing.MatLike) -> cv.typing.MatLike:
    try:
        percentCropBlockWidth = m.floor(0.1 * imgSrc.shape[0])
        percentCropBlockHeight = m.floor(0.1 * imgSrc.shape[1])
        crop = imgSrc[percentCropBlockWidth:(imgSrc.shape[0]-percentCropBlockWidth), percentCropBlockHeight:imgSrc.shape[1]]
        return crop
    except:
        return None

def cropImg(imgPath: str, imgNewSaveName: str, dirSaveImg: str = FOLDER_DEFAULT)-> str:
    try:
        img = readImg(imgPath)
        percentCropBlockWidth = m.floor(0.1 * img.shape[0])
        percentCropBlockHeight = m.floor(0.1 * img.shape[1])
        crop = img[percentCropBlockWidth:(img.shape[0]-percentCropBlockWidth), percentCropBlockHeight:img.shape[1]-percentCropBlockHeight]
        fullPath = saveImage(f'{dirSaveImg}/{imgNewSaveName}',crop)
        print(f"Crop Image has been saved at: {fullPath}")
        return fullPath
    except:
        return None
    
def flipImage(imgPath: str, imgNewSaveName: str, dirSaveImg: str = FOLDER_DEFAULT) -> list[str]:
    try:
        img = readImg(imgPath)
        flipImage = cv.flip(img, 1)
        cropedFlipImage = cropComponent(flipImage)
        fullPath = saveImage(f'{dirSaveImg}/{imgNewSaveName}',flipImage)
        bonusPath = saveImage(f"{dirSaveImg}/CROPBONUS{imgNewSaveName}", cropedFlipImage)
        print(f"Flip Image has been saved at: {fullPath} \n with bonus: {bonusPath}")
        return [fullPath, bonusPath]
    except:
        return None
    
def flipComponent(img: cv.typing.MatLike) -> cv.typing.MatLike:
    try:
        flipImage = cv.flip(img, 1)
        return flipImage
    except:
        return None

def rotateImage(imgPath: str, imgNewSaveName: str, dirSaveImg: str = FOLDER_DEFAULT, angle:int = 10) -> list[str]:
    try:
        img = readImg(imgPath)
        (h, w, l) = img.shape
        mask = cv.getRotationMatrix2D((w//2, h//2), angle, 1.0)
        rotated = cv.warpAffine(img, mask, dsize=(w,h))
        rotateWithFlip = flipComponent(rotated)
        fullPath = saveImage(f"{dirSaveImg}/{imgNewSaveName}", rotated)
        bonusPath = saveImage(f"{dirSaveImg}/FLIPBONUS{imgNewSaveName}", rotateWithFlip)
        print(f"Rotate Image has been saved at: {fullPath} \n with bonus: {bonusPath}")
        return [fullPath, bonusPath]
    except:
        return None