# Convolutional Neural Network

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential  # creating sequence of layers of the CNN 
from keras.layers import Conv2D  # 2D convolution to deal with images
from keras.layers import MaxPooling2D  # to add pooling layers
from keras.layers import Flatten  
from keras.layers import Dense  

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Conv2D(32, # feature detectors
                      (3, 3),  # 3x3 dimensions of each feature detector
                      input_shape = (64, 64, # Dimensions of 2D array
                                     3), #  number of channels
                      activation = 'relu'))

# Step 2 - Pooling 
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                    target_size=(64, 64),
                                                    batch_size=32,
                                                    class_mode='binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                                        target_size=(64, 64),
                                                        batch_size=32,
                                                        class_mode='binary')

classifier.fit_generator(training_set,
                        steps_per_epoch = 8000,
                        epochs=8,
                        validation_data=test_set,
                        validation_steps = 2000)


# Making single image prediction

import numpy as np 
from keras.preprocessing import image as image_utils 
test_image = image_utils.load_img('dataset/single_prediction/cat_and_dog.jpg', target_size = (64, 64))
test_image = image_utils.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict_on_batch(test_image)
training_set.class_indices 

if result[0][0] == 1:
    prediction = 'Dog'
else:
    prediction = 'Cat'

print("Uploaded image is of", prediction)

# Saving the model
classifier.save('DogVSCatModel.h5')

from keras.models import load_model 
newMod = load_model('DogVSCatModel.h5')

newMod.fit_generator(training_set,
                        steps_per_epoch = 8000,
                        epochs=8,
                        validation_data=test_set,
                        validation_steps = 2000)