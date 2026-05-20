import cv2

def preprocess_image(image_path):

    image = cv2.imread(image_path)

    resized = cv2.resize(
        image,
        (224, 224)
    )

    return resized
