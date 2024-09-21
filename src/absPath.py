import os
from PIL import Image
import cv2 as cv
import math as m
import numpy as np
from termcolor import colored

# ROOT_DIR = 'D:/PersonProject/Project_with_Py/ImageProcessing/'
ROOT_DIR = os.getcwd().split('src')[0]
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
        if (not os.path.exists(f'{ROOT_DIR}/{path}')):
            os.makedirs(f'{ROOT_DIR}/{path}')
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
        path = f'{ROOT_DIR}/{newName}'
        cv.imwrite(path, image)
        return path
    except:
        return None
    
def showImage(path: str):
    try:
        img = Image.open(f'{ROOT_DIR}/{path}')
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
    
def perspectiveTranform(imgPath: str, imgNewSaveName: str, dirSaveImg: str = FOLDER_DEFAULT) -> list[str]:
    try:
        img = readImg(imgPath)
        (h, w, l) = img.shape
        pts1 = np.float32([[100,50],[h-50,50],[50,w-50],[h-50,w-50]])
        pts2 = np.float32([[0,0],[h,80],[100,w],[h,w]])
        mask = cv.getPerspectiveTransform(pts1,pts2)
        output = cv.warpPerspective(img, mask, dsize=(w,h))
        outputWithFlip = flipComponent(output)
        fullPath = saveImage(f"{dirSaveImg}/{imgNewSaveName}", output)
        bonusPath = saveImage(f"{dirSaveImg}/FLIPBONUSTRANS{imgNewSaveName}", outputWithFlip)
        print(f"Rotate Image has been saved at: {fullPath} \n with bonus: {bonusPath}")
        return [fullPath, bonusPath]
    except:
        return None
    
def duplicate_folder_image(folderPathName:str, resultFolderName:str = FOLDER_DEFAULT, isoValue:int = 30) -> list[dict]:
    try:
        imgDict: list[dict] = []
        folderSavedImgName = makeFolder(resultFolderName)
        fullPathFolder = load(folderPathName)
        for filename in os.listdir(fullPathFolder):
            fileNameFilter = filename.split(".")[0]
            pathResize = resize(f"{folderPathName}/{filename}",f"{fileNameFilter}resize.png", dirSaveImg=folderSavedImgName)
            pathCrop = cropImg(f"{folderPathName}/{filename}",f"{fileNameFilter}croped.png",dirSaveImg=folderSavedImgName)
            pathFlip = flipImage(f"{folderPathName}/{filename}",f"{fileNameFilter}flipped.png", dirSaveImg=folderSavedImgName)
            pathRotate = rotateImage(f"{folderPathName}/{filename}",f"{fileNameFilter}rotated.png", dirSaveImg=folderSavedImgName)
            patPperspecitveTrans = perspectiveTranform(f"{folderPathName}/{filename}",f"{fileNameFilter}trans.png", dirSaveImg=folderSavedImgName)
            pathChangeISO = isoConfig(f"{folderPathName}/{filename}",f"{fileNameFilter}iso.png", dirSaveImg=folderSavedImgName, valOfv= isoValue)
            dictObject = {
                'pathResize': pathResize,
                'pathCrop' : pathCrop,
                'pathFlip' : pathFlip,
                'pathRotate': pathRotate,
                'patPperspecitveTrans' : patPperspecitveTrans,
                'pathChangeISO' : pathChangeISO
            }
            imgDict.append(dictObject)
        
        return imgDict
    except Exception as e:
        print(e)
        return None
    
#v1.1.0
def iso_increase_decrease_switching(v: cv.typing.MatLike, valueOfV: int, mode:int = 0) -> cv.typing.MatLike:
    #0: increase | 1: decrease
    try:
        if (mode > 1 and mode < 0): raise Exception 
        v = cv.add(v, valueOfV) if mode == 0 else cv.add(v, -valueOfV)
        v[v > 255] = 255
        v[v < 0] = 0
        return v
    except Exception as e:
        print(f"MODE has to be 1 or 0 !!:: {e}")
        return None

def isoConfig(imgPath: str, imgNewSaveName: str, valOfv:int = 30, dirSaveImg: str = FOLDER_DEFAULT) -> list[str]: 
    try:
        img = readImg(imgPath)
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        (h,s,v) = cv.split(hsv) 
        v1 = iso_increase_decrease_switching(v, valOfv, 0)
        v2 = iso_increase_decrease_switching(v, valOfv, 1)
        result_hsv1 = cv.merge((h, s, v1))
        result_hsv2 = cv.merge((h, s, v2))
        imgRs = cv.cvtColor(result_hsv1, cv.COLOR_HSV2BGR)
        imgRs2 = cv.cvtColor(result_hsv2, cv.COLOR_HSV2BGR)
        fullPath1 = saveImage(f"{dirSaveImg}/Increase{imgNewSaveName}", imgRs)
        fullPath2 = saveImage(f"{dirSaveImg}/Decrease{imgNewSaveName}", imgRs2)
        print(f"ISO change has been saved at: {fullPath1} and {fullPath2}")
        return [fullPath1, fullPath2]
    except:
        return None
    
#v1.2.0

def rename_file_in_folder(folderName: str, startAt:int) -> int:
    try:
        folderFullPath = f"{ROOT_DIR}/{folderName}"
        startCache = startAt
        for fileName in os.listdir(folderFullPath):
            oldName = f"{folderFullPath}/{fileName}"
            newName = f"{folderFullPath}/g{startAt}.png"
            if(not os.path.exists(newName)):
                os.rename(oldName, newName)
            print(f"Rename: {newName}")
            startAt += 1
        imgProcessed = startAt - startCache
        print(colored(f"{imgProcessed} images have been changed !!!", "black", "on_white"))
        return imgProcessed
    except Exception as e:
        print(colored(f"Invalid path::: {e}", "red", on_color="on_light_grey"))