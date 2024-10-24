import cv2
import time
import mediapipe as mp
import face_detection_module as fdm
import face_mesh_module as fmm

video = cv2.VideoCapture(0)
pTime=0

faceDetector = fdm.faceDetection()
faceMesh = fmm.faceMeshDectection()
while True:
    r, frame = video.read()
    if r==True:
        frame = cv2.resize(frame, (800,600))
        frame  = cv2.flip(frame, 1)

        face = faceMesh.faceMarksDetection(frame)
        faceDetector.findFace(frame, draw=False)
        boxlist, box = faceDetector.markBoxOnFace(frame, draw=True)
        if boxlist:
            print(boxlist)
        faceDetector.markEdgeOnBox(frame, box)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime=cTime

        cv2.putText(frame, str(int(fps)), (5,30), 2, cv2.FONT_HERSHEY_PLAIN, (0,0,255), 2)
        cv2.imshow('video', frame)

        if cv2.waitKey(1) & 0xff == ord('p'):
            break

    else:
        break
cv2.destroyAllWindows()