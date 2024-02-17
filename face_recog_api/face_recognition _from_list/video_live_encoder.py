import face_recognition
import os

# List all files in the directory
all_files = os.listdir("./photos")

# Filter for image files (e.g., .jpg, .png, .jpeg)
img_path = [filename for filename in all_files if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.gif', '.bmp'))]

stored_encodings = {}

for i in img_path:
    picture_of_me = face_recognition.load_image_file(f"./photos/{i}")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    stored_encodings[i] = my_face_encoding
    
    
print(img_path)
print(stored_encodings)


# cap = cv2.VideoCapture(0)

# recognition_threshold = 0.5

# while True:
#     ret, frame = cap.read()

#     # Performing face recognition on the frame using face_recognition library
#     face_locations = face_recognition.face_locations(frame)
#     recognized_names = []

#     if face_locations:
#         face_encodings = face_recognition.face_encodings(frame, face_locations)

#         for encoding in face_encodings:
#             recognized_name = None

#             # Step 3: Compare new encodings with stored encodings
#             if len(encoding) > 0:
#                 for name, stored_encoding in stored_encodings.items():
#                     # Comparing the new encoding with each stored encoding
#                     result = face_recognition.compare_faces([stored_encoding], encoding, tolerance=recognition_threshold)

#                     if result[0]:  # If a match is found
#                         recognized_name = name
#                         break

#                 if recognized_name:
#                     recognized_names.append(recognized_name)
#                 else:
#                     recognized_names.append("Unknown person")  # Label as "Unknown person" if no match

#         # Draw rectangles around detected faces and display names
#         for (top, right, bottom, left), name in zip(face_locations, recognized_names):
#             rect_color = (255, 0, 0)  # Blue color
#             rect_thickness = 2
#             cv2.rectangle(frame, (left, top), (right, bottom), rect_color, rect_thickness)

#             font = cv2.FONT_ITALIC
#             label_color = (0, 0, 255)  # Red color for labels
#             cv2.putText(frame,  name, (left, bottom + 20), font, 0.6, label_color, 1)
    
#     # Display the video frame
#     cv2.imshow('Face Recognition', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()