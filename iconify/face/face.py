from PIL import Image
import face_recognition


def face(image_name):
    original_image = Image.open(image_name)
    image = face_recognition.load_image_file(image_name)
    face_locations = face_recognition.face_locations(image)
    for i in range(len(face_locations)):
        face_location = face_locations[i]
        output = original_image.crop((face_location[3], face_location[0],
                                      face_location[1], face_location[2]))
        output.save(f"face_{i}.jpg", "JPEG")
