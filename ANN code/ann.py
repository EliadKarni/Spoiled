from keras.applications import ResNet50
from keras.layers import Dense, Flatten
from keras.models import Model
from PIL import Image
import numpy as np
import glob
import os
from keras.utils import to_categorical

num_classes = 2


def extract_label_from_filename(filename):
    label_map = {'avatar': 0, 'TheGoodPlace': 1}
    label = filename.split("\\")[1]
    return label_map[label]


def get_training_data():
    # Set the path to the directory containing your images
    img_dir = "fullImages"

    # Create empty arrays to hold your training data
    x_train = []
    y_train = []

    img_files = glob.glob(img_dir + "/**/*.jpg", recursive=True)

    # Loop through the images in the directory
    for img_path in glob.glob(img_dir + "/**/*.jpg", recursive=True):
        # Open the image using PIL
        img = Image.open(img_path)

        # Resize the image to the desired size
        img = img.resize((224, 224))

        # Convert the image to a numpy array
        img_array = np.array(img)

        # Normalize the pixel values of the image
        img_array = img_array / 255.0

        # Add the image to the x_train list
        x_train.append(img_array)

        # Get the label of the image
        # You can extract the label from the filename or the path
        label = extract_label_from_filename(img_path)

        # One-hot encode the label and add it to the y_train list
        y_train.append(to_categorical(label, num_classes=num_classes))

    # Convert the x_train and y_train lists to numpy arrays
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    return x_train, y_train


# Load the ResNet50 model, excluding the final fully-connected layer
model = ResNet50(include_top=False, weights='imagenet', input_shape=(224, 224, 3))

x_train, y_train = get_training_data()
# Add a new Flatten layer
x = model.output
x = Flatten()(x)

# Add a dense layer with softmax activation for multi-class classification
predictions = Dense(num_classes, activation='softmax')(x)

# Create a new model with the added layers
model = Model(inputs=model.input, outputs=predictions)

# Freeze the base ResNet50 layers
for layer in model.layers[:-1]:
    layer.trainable = False

# Compile the model with an optimizer, loss function and metrics
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'], run_eagerly=True)

# Train the model on your dataset
model.fit(x_train, y_train, epochs=15, batch_size=32)

model.save('my_full_test_model.h5')
