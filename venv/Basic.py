import cv2
import numpy as np
import face_recognition


imgChetan=face_recognition.load_image_file('ImagesBasic/Rohit.jpg')
imgChetan=cv2.cvtColor(imgChetan,cv2.COLOR_BGR2RGB)
imgChetan


imgTest = face_recognition.load_image_file('ImagesBasic/Rohit3.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgChetan)[0]
encodeChetan = face_recognition.face_encodings(imgChetan)[0]
print(encodeChetan)
cv2.rectangle(imgChetan,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,0),4)


results = face_recognition.compare_faces([encodeChetan],encodeTest)
faceDis = face_recognition.face_distance([encodeChetan],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)



cv2.imshow('Chetan_Bhagat',imgChetan)
cv2.imshow('ChetanBhagat2',imgTest)

cv2.waitKey(0)