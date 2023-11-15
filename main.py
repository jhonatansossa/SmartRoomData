import cv2
import torch
from PIL import Image

def predict(model, img):
    '''

    :param model: person detection model
    :param img: img in RGB format
    :return: drawn image and person count
    '''
    out_img = img.copy()
    # Inference
    results = model([img], size=800)  # batch of images
    # Results
    results.save()  # or .show()
    person_count = 0
    for det in results.xyxy[0]:
        x1, y1, x2, y2, conf, cls = det
        if cls == 0 and conf > 0.7:
            out_img = cv2.rectangle(out_img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            person_count  = person_count + 1
    return out_img, person_count

if __name__ == '__main__':

    # Model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5l')
    # Image loading
    img = cv2.imread(r'inputs/test_img.png')[..., ::-1]  # OpenCV image (BGR to RGB)
    out_img , person_count = predict(model,img)
    print('Persons detected :',person_count)
    cv2.imshow('results',out_img)
    cv2.waitKey(2000)

