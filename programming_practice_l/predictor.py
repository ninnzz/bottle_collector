import cv2
import numpy as np
from os import listdir
# from sklearn.linear_model import LassoCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

class BottleClassifier:

    # Bottle image data
    x_train = []
    # Bottle lable, depending on how many
    y_train = []

    classifier = None

    def train(self):
        # Delete old classifier if needed
        # if self.classifier is not None:
            # del self.classifier
        print(self.x_train.shape)
        # self.classifier = RandomForestClassifier(n_estimators=100, random_state=1).fit(self.x_train, self.y_train)
        self.classifier = KNeighborsClassifier(n_neighbors=5).fit(self.x_train, self.y_train)

    def set_training_data(self, x_train, y_train):
        if x_train is None or y_train is None:
            raise ValueError('X and Y train should not be empty')

        self.x_train = np.asarray(x_train)
        self.x_train = self.x_train.reshape(self.x_train.shape[0], self.x_train.shape[1] * self.x_train.shape[2])      
        self.y_train = y_train

    def predict(self, x_test):
        
        return self.classifier.predict(x_test)

        
def convert_images(location):
    result = listdir(location)
    transformed_image = []
    for item in result:
        # print(location + '/' + item)
        img = cv2.imread(location + '/' + item)
        # You can put image tuning up here
        # reshape numpy
        img = cv2.resize(img, (0,0), fx = 0.4, fy = 0.4)
        img = img.reshape(img.shape[0], img.shape[1] * img.shape[2])
        transformed_image.append(img)

    return transformed_image
        
def load_data():

    coke = '/Users/ninz/dev/leaf_detector/data/test_shapes/test_data/bottles/coke'
    c2 = '/Users/ninz/dev/leaf_detector/data/test_shapes/test_data/bottles/c2'
    local = '/Users/ninz/dev/leaf_detector/data/test_shapes/test_data/bottles/local'
    refresh = '/Users/ninz/dev/leaf_detector/data/test_shapes/test_data/bottles/refresh'
    royal = '/Users/ninz/dev/leaf_detector/data/test_shapes/test_data/bottles/royal'
    wilkins = '/Users/ninz/dev/leaf_detector/data/test_shapes/test_data/bottles/wilkins'

    # _coke = convert_images(coke)
    _c2 = convert_images(c2)
    _local = convert_images(local)
    _refresh = convert_images(refresh)
    _royal = convert_images(royal)
    _wilkins = convert_images(wilkins)

    

    # _coke_l = len(_coke) * ['coke']
    _c2_l = len(_c2) * ['c2']
    _local_l = len(_local) * ['local']
    _refresh_l = len(_refresh) * ['refresh']
    _royal_l = len(_royal) * ['royal']
    _wilkins_l = len(_wilkins) * ['wilkins']

    x_train = _c2 + _local + _refresh + _royal + _wilkins
    y_train = _c2_l + _local_l + _refresh_l + _royal_l + _wilkins_l
    
    return x_train, y_train

def load_test_data(data_dir):
    img = cv2.imread(data_dir)
    img = cv2.resize(img, (0,0), fx = 0.4, fy = 0.4)
    img = img.reshape(img.shape[0], img.shape[1] * img.shape[2])
    img = np.asarray(img)
    img = img.reshape(1, img.shape[0] * img.shape[1])
    
    return img


testing_data = [
    '/Users/ninz/dev/leaf_detector/data/test_shapes/test_data/bottles/testing_data/c2.jpg',
    '/Users/ninz/dev/leaf_detector/data/test_shapes/test_data/bottles/testing_data/coke.jpg',
    '/Users/ninz/dev/leaf_detector/data/test_shapes/test_data/bottles/testing_data/coke2.jpg',
    '/Users/ninz/dev/leaf_detector/data/test_shapes/test_data/bottles/testing_data/local.jpg',
    '/Users/ninz/dev/leaf_detector/data/test_shapes/test_data/bottles/testing_data/refresh.jpg',
    '/Users/ninz/dev/leaf_detector/data/test_shapes/test_data/bottles/testing_data/royal.jpg',
    '/Users/ninz/dev/leaf_detector/data/test_shapes/test_data/bottles/testing_data/wilkins.jpg'
]

x, y = load_data()
print('Finished loading data')
l_cls = BottleClassifier()
l_cls.set_training_data(x, y)
l_cls.train()
print('Finished setting training data')

for val in testing_data:
    data = load_test_data(val)
    prediction = l_cls.predict(data)
    print(val)
    print(prediction)