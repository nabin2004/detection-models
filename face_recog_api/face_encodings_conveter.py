import face_recognition

img_path = ["Anushna chaulagain.jpg","Nabin oli.jpg","Pradeep raj basnet.jpg","Pramod giri.jpg","Roshan shrestha.jpg","sudip majkoti.jpg","Sailesh aryal.jpg"]

with open('encodings.csv', 'a') as file:
    for i in img_path:
        picture_of_me = face_recognition.load_image_file(f"./photos/{i}")
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
        
        # Converting the list to a comma-separated string and write it to the file
        encoded_str = ','.join(map(str, my_face_encoding))
        file.write(encoded_str + '\n')
