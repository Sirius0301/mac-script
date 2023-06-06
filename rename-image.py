import os 
import time 
from os import path 

inputDir = '/Users/shimin/Desktop/wechat-image/' 
outputDir = '/Users/shimin/Desktop/wechat-image/' 

def formatDate(ctime):     
    """
    Formats the creation time of the file into a YYYY-MM-DD string format
    """
    return time.strftime("%Y-%m-%d", time.localtime(ctime)) 

def read_file_list():     
    """
    Reads each file in the directory and groups them into a dictionary based on date
    """
    fileDict = {}     
    for file in os.listdir(inputDir):
        if '.jpg' in file:         
            fileName = path.join(inputDir, file)
            fileInfo = os.stat(fileName)         
            fileDate = formatDate(fileInfo.st_birthtime)         
            if fileDate in fileDict.keys():
                fileDict[fileDate].append(file)         
            else:
                fileDict[fileDate] = [file]     
    return fileDict 

def rename_file_list():     
    """
    Loops through the files in each date group
    Renames each file to have the date and a number in the name
    """
    fileDict = read_file_list()     
    for fileOnDate in fileDict:
        fileList = fileDict[fileOnDate]         
        for i, file in enumerate(fileList):             
            oldFile = path.join(inputDir, file)             
            newFileName = f"{fileOnDate}-{i}.jpg"             
            newFile = path.join(outputDir, newFileName)             
            os.rename(oldFile, newFile) 

if __name__ == '__main__':
    rename_file_list()
