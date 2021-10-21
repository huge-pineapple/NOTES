import cv2 as cv
import numpy as np
import os

def getFiles(path):
    filesList = []
    filesPath = []
    for root, dirs, files in os.walk(path):
        for file in files:
            FileName, FileType = os.path.splitext(file)
            #print file.decode('gbk')    #文件名中有中文字符时转码
            if FileType == '.jpg' or FileType == '.JPG':
                t = FileName
                h = os.path.join(path, FileName+FileType)
                filesList.append(t)
                filesPath.append(h)
    return filesList, filesPath #or
    # filesPath

dataDir = "image\\sanxia"
resDir = os.path.join(dataDir, "result")

if not os.path.exists(resDir):
    os.makedirs(resDir)

nameList, pathList = getFiles(os.path.join(dataDir, "image"))

for name in nameList:
    imagePath=os.path.join(dataDir, "image", name+".JPG")
    maskPath = os.path.join(dataDir, "mask", name+".JPG")
    predictPath = os.path.join(dataDir, "predict", name+".png")

    image=cv.imread(imagePath, cv.IMREAD_UNCHANGED)
    mask=cv.imread(maskPath)
    predict=cv.imread(predictPath)
    ret, predict = cv.threshold(predict, 127, 255, cv.THRESH_BINARY_INV)

    result = np.zeros((512, 1536, 3), np.uint8)
    result[:,0:512, :] = image[:, :, :]
    result[:,512:1024, :] = mask[:, :, :]
    result[:,1024:, :]=predict[:, :, :]

    cv.imwrite(os.path.join(resDir, name+".png"), result)


