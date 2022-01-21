

# neural network tools
import tensorflow as tf
from tensorflow.keras import (
    regularizers,
    models,
    optimizers
)
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import (
    Dense,
    Conv2D,
    Flatten,
    MaxPooling2D,
    Dropout,
    Activation,
    BatchNormalization
)
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import ModelCheckpoint

# other utilities
import pickle
import sys
import os
from typing import (
    Tuple,
    Any
)


class Net:

    def __init__(self,
                 train_path: str,
                 test_path: str,
                 valid_path: str):

        self.train_path = train_path
        self.test_path = test_path
        self.valid_path = valid_path
        try:
            # self.weights = "app/Net/.bacteria_trained.hdf5"
            self.weights = "lib/neural_weights_test.hdf5"
        except:
            pass

    def load_image_set(self) -> Tuple[Any, Any, Any]:

        train_gen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            horizontal_flip=True
        )

        test_gen = ImageDataGenerator(
            rescale=1./255
        )

        valid_gen = ImageDataGenerator(
            rescale=1./255
        )

        train_generator = train_gen.flow_from_directory(
            self.train_path,
            target_size=(64, 64),
            batch_size=32,
            class_mode="categorical"
        )

        test_generator = train_gen.flow_from_directory(
            self.test_path,
            target_size=(64, 64),
            batch_size=32,
            class_mode="categorical"
        )

        valid_generator = train_gen.flow_from_directory(
            self.valid_path,
            target_size=(64, 64),
            batch_size=32,
            class_mode="categorical"
        )

        return train_generator, test_generator, valid_generator

    def save_history_values(self, history: Any) -> None:
        with open("app/Net/.history_dict", "wb") as file:
            pickle.dump(file)

    def neural_model(self, train_generator: Any, valid_generator: Any) -> Any:

        model = Sequential()

        """
            NEURAL ARCHITECTURE
        """
        # first convolution
        model.add(Conv2D(
            32,
            kernel_size=(2, 2),
            padding="same",
            kernel_regularizer=regularizers.l2(1e-4),
            input_shape=(64, 64, 3)
        ))
        model.add(Activation("relu"))
        model.add(BatchNormalization())

        # second convolution
        model.add(Conv2D(
            32,
            kernel_size=(2, 2),
            padding="same",
            kernel_regularizer=regularizers.l2(1e-4)
        ))
        model.add(Activation("relu"))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.2))

        # third convolution, more deep
        model.add(Conv2D(
            64,
            kernel_size=(2, 2),
            padding="same",
            kernel_regularizer=regularizers.l2(1e-4)
        ))
        model.add(Activation("relu"))
        model.add(BatchNormalization())
        model.add(Dropout(0.2))

        # fourth convolution
        model.add(Conv2D(
            64,
            kernel_size=(2, 2),
            padding="same",
            kernel_regularizer=regularizers.l2(1e-4)
        ))
        model.add(Activation("relu"))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.3))

        # fifth convolution
        model.add(Conv2D(
            64,
            kernel_size=(2, 2),
            padding="same",
            kernel_regularizer=regularizers.l2(1e-4)
        ))
        model.add(Activation("relu"))
        model.add(BatchNormalization())

        # sixth convolution
        model.add(Conv2D(
            64,
            kernel_size=(2, 2),
            padding="same",
            kernel_regularizer=regularizers.l2(1e-4)
        ))
        model.add(Activation("relu"))
        model.add(BatchNormalization())
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.4))

        # classification flatten
        model.add(Flatten())
        model.add(Dense(3, activation="softmax"))

        # compiling

        model.compile(loss="categorical_crossentropy",
                      optimizer=optimizers.Adam(),
                      metrics=["accuracy"])

        checkpoint = ModelCheckpoint("lib/.bacteria_trained_new_model.hdf5", monitor="accuracy",
                                     verbose=1, save_best_only=True)
        if os.path.exists(self.weights):
            model.load_weights(self.weights)
        else:

            model.fit(train_generator,
                      steps_per_epoch=531//32,
                      epochs=500,
                      validation_data=valid_generator,
                      validation_steps=76//32,
                      callbacks=[checkpoint])
        return model
