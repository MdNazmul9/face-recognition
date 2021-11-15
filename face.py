

import face_biometric_recognition
image = face_biometric_recognition.load_image_file("your_file.jpg")
face_locations = face_biometric_recognition.face_locations(image)

# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# img = mpimg.imread('your_image.png')
# imgplot = plt.imshow(img)
# plt.show()



import face_biometric_recognition
known_image = face_biometric_recognition.load_image_file("nazmul.jpg")
unknown_image = face_biometric_recognition.load_image_file("your_file.jpg")

biden_encoding = face_biometric_recognition.face_encodings(known_image)[0]
unknown_encoding = face_biometric_recognition.face_encodings(unknown_image)[0]

results = face_biometric_recognition.compare_faces([biden_encoding], unknown_encoding)
print(results)