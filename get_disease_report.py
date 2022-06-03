from pyexpat import model
import cv2
import numpy as np
from object_detector import object_detector
from load_model import load_model

def get_disease_report():
    model = load_model()
    camera = cv2.VideoCapture(1)

    for i in range(100):
        result, image = camera.read()

        if not result:
            print ("Cannot open camera")
            return

        # TODO - EXCEPTION HANDLING CAMERA OPEN CV
        cv2.waitKey(10)
        image = image[::, 80:560]
        image = cv2.resize(image, (256,256))
        #show image
        cv2.imwrite("image.jpg", image)
        cv2.imshow("image", image)


        prediction = object_detector(model, image)
        print(prediction)
    camera.release()
    cv2.destroyAllWindows()

    clarified_prediction = clarify_prediction_data(prediction)
    return clarified_prediction

def clarify_prediction_data(prediction):
    # TODO - Clarify the prediction data- compleate this functuion 
    return prediction


if __name__ == "__main__":
    print("program started")
    report  = get_disease_report()
    print("program ended")
    print(report)
    
