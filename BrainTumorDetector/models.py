import pandas as pd
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator as Imgen
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D, Activation
from keras.metrics import categorical_crossentropy
from keras.optimizers import Adam

#Augmenting the training dataset
traingen = Imgen(
                 rescale=1./255,
                 shear_range= 0.2,
                 zoom_range = 0.3,
                 width_shift_range = 0.2,
                 height_shift_range  =0.2,
                 fill_mode = "nearest",
                 validation_split=0.2)

#Augmenting the testing dataset
testgen = Imgen(# rescale the images to 1./255 
                rescale = 1./255
                )

trainds = traingen.flow_from_directory("F:\Main Project\Multiple-Diseases-Predictor-2\BrainTumorDetector\BrainTumuorExecutors\Training",
                                       target_size = (224,224),
                                       seed=123,
                                       batch_size  = 16,
                                       subset="training"
                                      )
valds = traingen.flow_from_directory("F:\Main Project\Multiple-Diseases-Predictor-2\BrainTumorDetector\BrainTumuorExecutors\Training",
                                     target_size = (224,224),
                                     seed=123,
                                     batch_size  = 16,
                                     subset="validation"
                                      )
testds = testgen.flow_from_directory("F:\Main Project\Multiple-Diseases-Predictor-2\BrainTumorDetector\BrainTumuorExecutors\Testing",
                                     target_size = (224,224),
                                     seed=123,
                                     batch_size  = 16,
                                     shuffle=False)

c = trainds.class_indices
classes = list(c.keys())
#print(classes)

x,y = next(trainds)                             #function returns the next item in an iterator.
def plotImages(x,y):
    plt.figure(figsize=[15,11])                 #size of the plot
    for i in range(16):                         #16 images
        plt.subplot(4,4,i+1)                    #4 by 4 plot    
        plt.imshow(x[i])                        #Imshow() is a function of matplotlib displays the image
        plt.title(classes[np.argmax(y[i])])     # Class of the image will be it's title
        plt.axis("off")
    plt.show()   

#plotImages(x,y)

cnn = Sequential([
    # first Layer
    Conv2D(filters=16, kernel_size=(3, 3), padding = 'same', activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D((2, 2)),
    # second layer
    Conv2D(filters=32, kernel_size=(3, 3), padding = 'same', activation='relu'),
    MaxPooling2D((2, 2)),
    # third layer
    Conv2D(filters=64, kernel_size=(3, 3), padding = 'same', activation='relu'),
    MaxPooling2D((2, 2)),
    # fourth layer
    Conv2D(filters=128, kernel_size=(3, 3), padding = 'same', activation='relu'),
    Dropout(0.20),
    Flatten(),
    Dense(128, activation='relu', activity_regularizer=keras.regularizers.l2(0.01)),
    Dense(64, activation='relu', activity_regularizer=keras.regularizers.l2(0.01)),
    Dense(10, activation='relu', activity_regularizer=keras.regularizers.l2(0.01)),
    Dense(4, activation='softmax')
])

print(cnn.summary())

cnn.compile(loss="categorical_crossentropy",optimizer = "Adam",metrics=["accuracy"])

history = cnn.fit(trainds,validation_data=valds,epochs=20, batch_size=16)
cnn.save("BrainTumorModel.h5","label.txt")
#print(history)
test_loss, test_acc = cnn.evaluate(testds)
print('Test accuracy:', test_acc)

