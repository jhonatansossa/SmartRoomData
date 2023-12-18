from mmdet.apis import DetInferencer
import cv2

def predict_with_mmdetection(model, img):
    result = model(img, out_dir='./outputs', pred_score_thr=0.4)
    all_labels = result['predictions'][0]['labels']
    all_scores = result['predictions'][0]['scores']
    person_count = 0
    for i in range(len(all_scores)):
        if all_scores[i] >= 0.5 and all_labels[i] == 0:
            person_count = person_count + 1
    return person_count
if __name__ == '__main__':
    # Choose to use a config
    model_name = 'rtmdet_l_8xb32-300e_coco'
    # Setup a checkpoint file to load
    checkpoint = './checkpoints/rtmdet_l_8xb32-300e_coco_20220719_112030-5a0be7c4.pth'
    # Set the device to be used for evaluation
    device = 'cpu'
    # Initialize the DetInferencer
    inferencer = DetInferencer(model_name, checkpoint, device)
    # Use the detector to do inference
    img_path = './inputs/test_img_1.png'
    img = cv2.imread(img_path)
    person_count = predict_with_mmdetection(inferencer,img)
    print(person_count)
