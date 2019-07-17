import os
import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier


class BottlePredictor:

    _training_path = None
    _clf = None
    _X = []
    _y = []

    def __init__(self):
        print("Initiated")
        
    def train():
        _clf = RandomForestClassifier(random_state=0).fit(self._X, self._y)

    def load_data(folder_path):
        X = []
        y = []

        for sub_dir in os.listdir(folder_path):
            for f in os.listdir(os.path.join(folder_path, sub_dir)):
                _img = cv2.imread(os.path.join(folder_path, sub_dir, f)) 
                _np_array = np.asarray(_img)    
                l,b,c = _np_array.shape
                _np_array = _np_array.reshape(l * b * c,) 
                X.append(_np_array)
                y.append(sub_dir)

        self._X = X
        self._y = y

    def predict(self, img):
        return self._clf.predict(img)


classifier = BottlePredictor()
