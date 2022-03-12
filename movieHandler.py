import os, shutil, time, cv2

def movieHandler(rootPath, rawPath, trainPath, annotationPath, jpegQuality):
    for f in os.scandir(rootPath):
        fileExist = False
        if f.is_file() and f.name.endswith(".avi"):
            for x in os.scandir(rawPath):
                if x.is_file() and x.name == f.name:
                    fileExist = True
                    break
            if not fileExist:
                shutil.copy(f, rawPath)
                movieTrainDestination = trainPath + '\\' + f.name
                os.mkdir(movieTrainDestination)
                movieAnnotationDestination = annotationPath + '\\' + f.name
                os.mkdir(movieAnnotationDestination)
                movieLocation = rawPath + '\\' + f.name
                capture = cv2.VideoCapture(movieLocation)
                frameNr = 1
                while (True):
                   success, frame = capture.read()
                   if success:
                       frameTrainDestination = movieTrainDestination+'\\'+'frame_'+str(frameNr)+'.png'
                       frameAnnotationDestination = movieAnnotationDestination+'\\'+'frame_'+str(frameNr)+'.jpg'
                       cv2.imwrite(frameTrainDestination, frame)
                       cv2.imwrite(frameAnnotationDestination, frame, [int(cv2.IMWRITE_JPEG_QUALITY), jpegQuality])
                   else:
                       break
                   frameNr += 1
                capture.release()
    


rootPath = r'C:\Users\YAKIRSHCHIGELSKI\Documents\MyLearning\playground\python_scripts\SightX\root'
rawPath = r'C:\Users\YAKIRSHCHIGELSKI\Documents\MyLearning\playground\python_scripts\SightX\raw'
trainPath = r'C:\Users\YAKIRSHCHIGELSKI\Documents\MyLearning\playground\python_scripts\SightX\train'
annotationPath = r'C:\Users\YAKIRSHCHIGELSKI\Documents\MyLearning\playground\python_scripts\SightX\annotation'

while True:
    movieHandler(rootPath, rawPath, trainPath, annotationPath, 95)
    time.sleep(15)
    continue
