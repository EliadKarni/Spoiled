from keras.models import load_model
import numpy as np
from keras.preprocessing import image
from PIL import Image
from keras.utils import load_img, img_to_array

# load your model
loaded_model = load_model('my_test_model.h5')

# load an example image
img_path = 'testData/Avatar/ep1frame174.jpg'
img = load_img(img_path, target_size=(224, 224))

# preprocess the image to match the input format expected by your model
img_array = img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0

# use the loaded model to make predictions on the image
predictions = loaded_model.predict(img_array)

# print the predictions
print(predictions)

