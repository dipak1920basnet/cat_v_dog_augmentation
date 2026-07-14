from Data_Preprocessing.instan import instantiate_data
import tensorflow as tf 


train_dataset_final, validation_dataset_final = instantiate_data()

def train(model):
    EPOCHS = 20

    # Setup the training parameters
    model.compile(loss='binary_crossentropy',
                optimizer=tf.keras.optimizers.RMSprop(learning_rate=1e-4),
                metrics=['accuracy'])

    # Train the model
    history = model.fit(
        train_dataset_final,
        epochs=EPOCHS,
        validation_data=validation_dataset_final,
        verbose=2)
    
    return history