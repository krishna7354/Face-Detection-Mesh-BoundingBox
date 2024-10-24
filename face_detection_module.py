import os
import cv2
import mediapipe as mp
import time


class faceDetection():
    def __init__(self, min_detection_confidence=0.7, model_selection=0):
        self.min_detection_confidence = min_detection_confidence
        self.model_selection = model_selection

        self.mpFaceDetection = mp.solutions.face_detection
        self.faceDetect = self.mpFaceDetection.FaceDetection(self.min_detection_confidence, self.model_selection)
        self.mpDraw = mp.solutions.drawing_utils


    def findFace(self, frame, draw=True):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.result = self.faceDetect.process(imgRGB)
        if self.result.detections:
            if draw:
                for id, detection in enumerate(self.result.detections):
                    self.mpDraw.draw_detection(frame, detection)
        else:
            print("No face detected")

    def markBoxOnFace(self, frame, draw=True):
        boxList = []
        if self.result.detections:
            for id, detection in enumerate(self.result.detections):
                h, w, c = frame.shape
                boundingBox = detection.location_data.relative_bounding_box
                box = int(boundingBox.xmin * w), int(boundingBox.ymin * h), int(boundingBox.width * w), int(boundingBox.height * h)

                if draw:
                    cv2.rectangle(frame, box, (0, 255, 0), 2)
                    cv2.putText(frame, f'{int(detection.score[0] * 100)}%', (box[0], box[1] - 5), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

                boxList.append([id, box, f'score: {detection.score[0]}'])
        else:
            print("No face detected in markBoxOnFace")

        return boxList, box

    def markEdgeOnBox(self, frame, box, length=30, thick=8, draw=True):
        x, y, w, h = box
        x1, y1 = x + w, y + h
        if draw:
            # top left corner
            cv2.line(frame, (x, y), (x + length, y), (0,0,255), thick)
            cv2.line(frame, (x, y), (x, y + length), (0,0,255), thick)
            # top right corner
            cv2.line(frame, (x1, y), (x1 - length, y), (0,0,255), thick)
            cv2.line(frame, (x1, y), (x1, y + length), (0,0,255), thick)
            # bottom left corner
            cv2.line(frame, (x, y1), (x + length, y1), (0,0,255), thick)
            cv2.line(frame, (x, y1), (x, y1 - length), (0,0,255), thick)
            # bottom right corner
            cv2.line(frame, (x1, y1), (x1 - length, y1), (0,0,255), thick)
            cv2.line(frame, (x1, y1), (x1, y1 - length), (0,0,255), thick)

def main():
    video = cv2.VideoCapture(0)
    cTime = 0
    pTime = 0
    detector = faceDetection()
    while True:
        r, frame = video.read()
        if r == True:
            frame = cv2.resize(frame, (720, 480))
            detector.findFace(frame, draw=True)
            boxList, box = detector.markBoxOnFace(frame, draw=True)
            print([boxList])
            detector.markEdgeOnBox(frame, box)
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(frame, str(int(fps)), (5, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            cv2.imshow('video', frame)
            if cv2.waitKey(1) & 0xFF == ord('p'):
                break

        else:
            print("Failed to read frame")
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
