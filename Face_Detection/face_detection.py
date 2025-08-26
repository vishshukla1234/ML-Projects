import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)

    cv.imshow('Detected Face', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
