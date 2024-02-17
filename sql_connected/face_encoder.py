import face_recognition
import pickle
import os

# Specify the directory containing the image files
image_directory = "./photos"

# # List all files in the directory
all_files = os.listdir(image_directory)


img_path = [filename for filename in all_files if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.gif', '.bmp'))]

face_encodings = []
face_name = []

for i in img_path:
    picture_of_me = face_recognition.load_image_file(f"./photos/{i}")
    face_encodings.append(face_recognition.face_encodings(picture_of_me)[0])
    face_name.append(i.split('.')[0].strip())

###########################################################################################

with open('face_encodings', 'wb') as file:
    pickle.dump(face_encodings, file)

with open('people', 'wb') as file:
    pickle.dump(face_name, file)

with open('face_encodings', 'rb') as file:
    face = pickle.load(file)
 
with open('people', 'rb') as file:
    names = pickle.load(file)
    
##########################################################################################


