import cv2
import mediapipe as mp
import time

class faceMeshDectection():
    def __init__(self, imageMode=False, maxFaces=2, refineLandmarks=False, detectionConfidance=0.75, trackingConfidance=0.75):
        self.imageMode = imageMode
        self.maxFaces = maxFaces
        self.refineLandmarks = refineLandmarks
        self.detectionConfidance = detectionConfidance
        self.trackingConfidance = trackingConfidance

        self.mpface = mp.solutions.face_mesh
        self.faceMesh = self.mpface.FaceMesh(self.imageMode, self.maxFaces, self.refineLandmarks, self.detectionConfidance, self.trackingConfidance)
        self.mpdraw = mp.solutions.drawing_utils
        self.drawspac = self.mpdraw.DrawingSpec(color=(0,0,255),thickness=1, circle_radius=1)


    def faceMarksDetection(self, frame, draw=True):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.faceMesh.process(imgRGB)
        faces=[]

        if result.multi_face_landmarks:
            for face in result.multi_face_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(frame, face, self.mpface.FACEMESH_CONTOURS, self.drawspac, self.drawspac)
                face_landmark=[]
                for id, lm in enumerate(face.landmark):
                    h, w, c = frame.shape
                    x, y = int(lm.x*w), int(lm.y*h)
                    # cv2.putText(frame, str(id), (x, y), 1, cv2.FONT_HERSHEY_PLAIN, (0, 0, 255), 1)
                    face_landmark.append([id, x, y])
                faces.append(face_landmark)
        else:
            print('face was not detected so, no able to show mesh')
        return faces

def main():
    video = cv2.VideoCapture(0)
    pTime = 0
    detector = faceMeshDectection()

    while True:
        r, frame = video.read()

        if r == True:
            frame = cv2.resize(frame, (800,600))
            frame = cv2.flip(frame, 1)

            faces = detector.faceMarksDetection(frame)
            
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(frame, str(int(fps)), (5, 30), 2, cv2.FONT_HERSHEY_PLAIN, (0, 0, 255), 2)

            cv2.imshow('video', frame)

            if cv2.waitKey(1) & 0xFF == ord('p'):
                break
        else:
            print('video was not running')
            break

if __name__ == '__main__':
    main()