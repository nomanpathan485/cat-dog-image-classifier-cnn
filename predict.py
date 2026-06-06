import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model(
    "cat-dog-image-classifier-cnn/cat_dog_model.keras"
)

img_path = "cat-dog-image-classifier-cnn/dataset/PetImages/Cat/1.jpg"

img = image.load_img(img_path, target_size=(128,128))

img_array = image.img_to_array(img)

img_array = img_array / 255.0

img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)

print("Raw Prediction:", prediction)

if prediction[0][0] > 0.5:
    print("Dog")
    print("Confidence:", prediction[0][0] * 100)
else:
    print("Cat")
    print("Confidence:", (1 - prediction[0][0]) * 100)
    