from face import find_faces
from encode import encoding_pictures

def main():
    encoding_pictures('Photos/')
    registration_id = find_faces('Videos/Video5.mp4')
    return registration_id

print(main())
