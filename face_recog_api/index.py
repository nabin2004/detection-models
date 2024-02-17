import face_recognition
import cv2
import os
import csv

stored_encodings = {}
with open('encodings.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        name, encoding_str = row
        encoding_float = [float(x) for x in encoding_str.split(',')]
        stored_encodings[name] = encoding_float

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    face_locations = face_recognition.face_locations(frame)
    recognized_names = []

    if face_locations:
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for encoding in face_encodings:
            recognized_name = None

            if len(encoding) > 0:
                for name, stored_encoding in stored_encodings.items():
                    result = face_recognition.compare_faces([stored_encoding], encoding)

                    if result[0]:
                        recognized_name = name
                        break

                if recognized_name:
                    recognized_names.append(recognized_name)

        for (top, right, bottom, left), name in zip(face_locations, recognized_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, f"Person recognized: {name}", (left, bottom + 20), font, 0.6, (0, 255, 0), 1)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
