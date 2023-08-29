import cv2

# Loading the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# Initializing the webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    raise Exception("Could not open video device")


while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # If the frame was not captured successfully, exit the loop
    if not ret:
        break

    # Convert the frame to grayscale (face detection works on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame with face detections
    cv2.imshow('Face Detection', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

