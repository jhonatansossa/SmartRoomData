import cv2
import torch
from PIL import Image

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def predict(model, img):

    out_img = img.copy()
    results = model([img], size=800) 
    results.save()
    person_count = 0
    for det in results.xyxy[0]:
        x1, y1, x2, y2, conf, cls = det
        if cls == 0 and conf > 0.7:
            out_img = cv2.rectangle(out_img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            person_count  = person_count + 1
    return out_img, person_count


class DetectPerson(Resource):

    # Sample request: http://127.0.0.1:5100/detect_person -> Upload image through postman (form-data)
    def post(self):
        if 'file' not in request.files:
            return {'message': 'No file part'}, 400

        file = request.files['file']

        if file.filename == '':
            return {'message': 'No selected file'}, 400
        
        try:
            uploaded_image_path = 'inputs/upload_image_1.png'
            file.save(uploaded_image_path)
        except:
            return {'message': 'File Saving Error'}, 400
        
        try:
            model = torch.hub.load('ultralytics/yolov5', 'yolov5l')
    
            img = cv2.imread(uploaded_image_path)[..., ::-1]
            out_img , person_count = predict(model,img)

            print('Persons detected :', person_count)
        except:
            return {'message': 'Model Error !!'}, 400

        return {'person_count': person_count}, 200


api.add_resource(DetectPerson, '/detect_person')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)
