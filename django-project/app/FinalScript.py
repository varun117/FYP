import cv2
import numpy as np
from tensorflow.keras.models import load_model
#from keras import backend as K
from collections import Counter
import os
#from django.conf import settings

labels = ["Infected", "Normal"]

def testForImage(imgPath):
    #imgPath = '..'+imgPath
    imgPath = imgPath[1:]
    ans = []
    data = []
    models = ["initial-Model-extraData.h5", "vggPretrainedModel-extraData.h5", "vaibhavModel-Final.h5"]
    #models = ["MODEL_1", "MODEL_2", "MODEL_3"]
    #print("opening: ", imgPath)
    image = cv2.imread(imgPath)
    #print(image)
    #print(os.listdir(os.curdir))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    data.append(image)
    data = np.array(data)/255
    print("The shape of the test image is:", data.shape)
    
    for modelPath in models:
        #K.clear_session()
        print("\nLoading ", modelPath[:-3], "...")
        loadedModel = load_model(modelPath)
        #loadedModel = getattr(settings, modelPath, 'the_default_value')
        print(type(loadedModel))
        pred = loadedModel.predict(data)
        print(modelPath[:-3], " predicted value:", pred)
        print("Predicted Label:", labels[np.argmax(pred)], "\n")
        ans.append(labels[np.argmax(pred)])
        if modelPath == "vggPretrainedModel-extraData.h5":
            ans.append(labels[np.argmax(pred)])
    
    print("Answers: ", ans)
    ensemble = Counter(ans)
    print("\nEnsembled Prediction:", ensemble.most_common()[0][0])
    return ensemble.most_common()[0][0]
    