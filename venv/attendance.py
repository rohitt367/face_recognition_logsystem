import cv2
from cv2 import destroyAllWindows
import numpy as np
import face_recognition
import os
from email.message import EmailMessage
from datetime import datetime
import imghdr
import smtplib

from sympy import false
from gtts import gTTS
# from PIL import ImageGrab


known_face_names = ["UTKARSH","ROHIT"]
 
path = 'ImageAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)   
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
 
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
 
def markAttendance(name):
    with open('venv/Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        timeList=[]
        minList=[]
        now = datetime.now()
        dtString = now.strftime('%D:%H;%M')
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        for time in myDataList:
            entry = line.split(',')
            timeList.append(entry[1])
        for min in timeList:
            entry = line.split(':',2)
            minList.append(entry[2])
        if name in nameList:
            if now.strftime('%M') not in minList:

                now = datetime.now()
                dtString = now.strftime('%D:%H:%M') 
                m=int(now.strftime('%M'))
                
                f.writelines(f'\n{name},{dtString}')
                name = classNames[matchIndex].upper()
                language='en'
                i=0
                mytext=('%s your attendance is marked'%name.lower())
                output=gTTS(text=mytext,lang=language,slow=False)
                output.save('output.mp3')
                os.system('start output.mp3')
        



        

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%D:%H:%M') 
            m=int(now.strftime('%M'))
            
            f.writelines(f'\n{name},{dtString}')
            name = classNames[matchIndex].upper()
            language='en'
            i=0
            mytext=('%s your attendance is marked'%name.lower())
            output=gTTS(text=mytext,lang=language,slow=False)
            output.save('output.mp3')
            os.system('start output.mp3')


 
encodeListKnown = findEncodings(images)
print('Encoding Complete')
 
cap = cv2.VideoCapture(0) 
 
while True:
    success, img = cap.read()
    #img = captureScreen()  
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
 
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
 
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):

        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)
        name = classNames[matchIndex].upper()


        if name not in known_face_names :
            i=0

            while i < 2:
                print("sending image on mail")
                return_value, image = cap.read()
                cv2.imwrite('opencv.png', image)
                i += 1
                Sender_Email = "test.raspberry.pi.23@gmail.com"
                Reciever_Email = "rohitt3678@gmail.com"
                Password = "gtavicecity123" #type your password here
                newMessage = EmailMessage()                         
                newMessage['Subject'] = "unkown person entered" 
                newMessage['From'] = Sender_Email                   
                newMessage['To'] = Reciever_Email                   
                newMessage.set_content('Let me know what you think. Image attached!') 
                with open('opencv.png', 'rb') as f:
                    image_data = f.read()
                    image_type = imghdr.what(f.name)
                    image_name = f.name
                newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(Sender_Email, Password)   
                    smtp.send_message(newMessage)
                        
 
        if matches[matchIndex]:
        

            


           
            print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)

            cv2.imshow('Webcam',img)

    '''name = classNames[matchIndex].upper()
    language='en'
    i=0
    mytext=('%s your attendance is marked'%name.lower())
    output=gTTS(text=mytext,lang=language,slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')'''
        

    
            
    if cv2.waitKey(10)==13:
        break

cv2.imshow('Webcam',img)
    

    