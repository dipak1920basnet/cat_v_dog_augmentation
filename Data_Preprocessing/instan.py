from data_load import DataLoader
import tensorflow as tf 

def instantiate_data():
    
    train_dataset = tf.keras.utils.image_dataset_from_directory(
        DataLoader.train_dir,
        image_size = (150,150),
        batch_size = 20,
        label_mode = "binary"
    )

    validation_dataset = tf.keras.utils.image_dataset_from_directory(
        DataLoader.validation_dir,
        image_size = (150,150),
        batch_size = 20,
        label_mode = "binary"
    )

    SHUFFLE_BUFFER_SIZE = 1000
    PREFETCH_BUFFER_SIZE = tf.data.AUTOTUNE

    train_dataset_final = (train_dataset
                           .cache()
                           .shuffle(SHUFFLE_BUFFER_SIZE)
                           .prefetch(PREFETCH_BUFFER_SIZE)
                           )
    
    validation_dataset_final = (validation_dataset
                                .cache()
                                .prefetch(PREFETCH_BUFFER_SIZE)
                                )
    
    return train_dataset_final, validation_dataset_final
