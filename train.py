import tensorflow as tf
import os
num_skipped = 0
for folder_name in ("Cat", "Dog"):
    folder_path = f"cat-dog-image-classifier-cnn/dataset/PetImages/{folder_name}"
    for fname in os.listdir(folder_path):
        fpath = os.path.join(folder_path, fname)
        try:
            with open(fpath, "rb") as fobj:
                is_jfif = b"JFIF" in fobj.peek(10)
            if not is_jfif:
                num_skipped += 1
                os.remove(fpath)
        except:
            num_skipped += 1
            os.remove(fpath)
print("Deleted", num_skipped, "corrupted images")


train_dataset = tf.keras.utils.image_dataset_from_directory(
    "cat-dog-image-classifier-cnn/dataset/PetImages",
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=(128,128),
    batch_size=32
)
print(train_dataset.class_names)

val_dataset = tf.keras.utils.image_dataset_from_directory(
    "cat-dog-image-classifier-cnn/dataset/PetImages",
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=(128,128),
    batch_size=32
)

print(train_dataset)
print(val_dataset)

# normalization_layer = tf.keras.layers.Rescaling(1./255)
# train_dataset = train_dataset.map(
#     lambda x,y:(normalization_layer(x),y)
# )
# val_dataset = val_dataset.map(
#     lambda x, y:(normalization_layer(x),y)
# )

# model = tf.keras.Sequential([
#     tf.keras.layers.Conv2D(
#         32,
#         (3,3),
#         activation="relu",
#         input_shape=(128,128,3)
#     ),

#     tf.keras.layers.MaxPooling2D((2,2)),
#     tf.keras.layers.Conv2D(
#         64,
#         (3,3),
#         activation="relu"
#     ),
#     tf.keras.layers.MaxPooling2D((2,2)),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(
#         64,
#         activation="relu",
#     ),
#     tf.keras.layers.Dropout(0.5),
    
#     tf.keras.layers.Dense(
#         1,
#         activation="sigmoid"
#     )
# ])

# model.compile(
#     optimizer = "adam",
#     loss="binary_crossentropy",
#     metrics = ["accuracy"]
# )

# model.summary()
# history = model.fit(
#     train_dataset,
#     validation_data = val_dataset,
#     epochs = 10
# )
# model.save("cat_dog_model.keras")