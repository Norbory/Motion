import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture('Video.mp4')

detector = PoseDetector()
posList = []
while True:
    #lee la imagen sacada del video
    success, img = cap.read()
    # Detecta las poses del video
    img = detector.findPose(img)
    #Pone las marcas de los Joint y genera una caja
    lmlist, bboxInfo = detector.findPosition(img)

    if bboxInfo:
        lmString = ''
        #Separa cada array con las marcas de los Joint con su
        #respectiva posicion para mandarlos a un archivo
        for lm in lmlist:
            #print(lm)
            lmString += f'{lm[1]},{img.shape[0]-lm[2]},{lm[3]},'
        #El origen en python es en la esquina superior izquierda
        #pero en Unity es en la parte inferior asi que hay que modificar las coordenadas
        posList.append(lmString)

    print(len(posList))
    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        with open("AnimationFile.txt",'w') as f:
            #Escribe por cada valor de posList
            f.writelines(["%s\n" % item for item in posList])