import tensorflow as tf

def main():
    ...

def create_model():
    model = tf.keras.models.Sequential([
        # input shape 
        tf.keras.Input(shape=(150, 150, 3)),
        # rescale the data 
        tf.keras.layers.Rescaling(1./255),

        # use convolutional layers 
        tf.keras.layers.Conv2D(32, (3,3), activation="relu"),
        # use poolin layers 
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, (3,3), activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(128, (3,3), activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(128, (3,3), activation="relu"),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid")
        ]
    )

    return model

if __name__ == "__main__":
    main()