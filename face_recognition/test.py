import face_recognition
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise Exception("Could not open video device")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB (face_recognition uses RGB format)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Finding face locations in the frame
    face_locations = face_recognition.face_locations(rgb_frame)

    # Drawing rectangles
    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
