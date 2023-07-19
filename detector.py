import onnxruntime as onnxrt
import numpy as np
import cv2
import random

class Detector:
    def __init__(self, model_name, shape):
        self.labels = self.load_labels("./model/"+ model_name + "/labels.txt")
        self.model = self.load_model("./model/" + model_name + "/best.onnx")
        self.colors = [tuple(random.choices(range(256), k=3)) for i in range(len(self.labels))]
        self.shape = shape

    def load_labels(self, path):
        with open(path, 'r') as f:
            return f.read().splitlines()

    def load_model(self, model_path):
        providers = ['CUDAExecutionProvider', 'CPUExecutionProvider'] if onnxrt.get_device()=='GPU' else ['CPUExecutionProvider']
        onnx_session= onnxrt.InferenceSession(model_path, providers=providers)
        return onnx_session

    def letterbox(self, im, color=(114, 114, 114), auto=True, scaleup=True, stride=32):
        # Resize and pad image while meeting stride-multiple constraints
        shape = im.shape[:2]  # current shape [height, width]
        if isinstance(self.shape, int):
            self.shape = (self.shape, self.shape)

        # Scale ratio (new / old)
        r = min(self.shape[0] / shape[0], self.shape[1] / shape[1])
        if not scaleup:  # only scale down, do not scale up (for better val mAP)
            r = min(r, 1.0)

        # Compute padding
        new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
        dw, dh = self.shape[1] - new_unpad[0], self.shape[0] - new_unpad[1]  # wh padding

        if auto:  # minimum rectangle
            dw, dh = np.mod(dw, stride), np.mod(dh, stride)  # wh padding

        dw /= 2  # divide padding into 2 sides
        dh /= 2

        if shape[::-1] != new_unpad:  # resize
            im = cv2.resize(im, new_unpad, interpolation=cv2.INTER_LINEAR)
        top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
        left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
        im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
        return im, r, (dw, dh)

    def preprocess_image(self, image):
        image, ratio, dwdh = self.letterbox(image, auto=False)
        image = image.transpose((2, 0, 1))
        image = np.expand_dims(image, 0)
        image = np.ascontiguousarray(image)
        im = image.astype(np.float32)
        im /= 255
        return im, ratio, dwdh

    def process_output(self, model_outputs, ratio, dwdh, confidence_threshold, iou_threshold):
        boxes = []
        confidences = []
        classes = []
        batch_ids = []

        for i,(batch_id,x0,y0,x1,y1,cls_id,score) in enumerate(model_outputs):
            box = np.array([x0,y0,x1,y1])
            box -= np.array(dwdh*2)
            box /= ratio
            box = box.round().astype(np.int32).tolist()
            classes.append(cls_id)
            boxes.append(box)
            confidences.append(score)
            batch_ids.append(batch_id)

        best_indexes = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, iou_threshold)

        boxes = [boxes[i] for i in best_indexes]
        confidences = [confidences[i] for i in best_indexes]
        classes = [classes[i] for i in best_indexes]
        batch_ids = [batch_ids[i] for i in best_indexes]

        return boxes, confidences, classes, batch_ids

    def debug_image(self, image, boxes, confidences, classes, batch_ids):
        original_images = [image.copy()]

        for i, _ in enumerate(boxes):
            image = original_images[int(batch_ids[i])]
            cls_id = int(classes[i])
            score = round(float(confidences[i]),3)
            name = self.labels[cls_id]
            color = self.colors[cls_id]
            name += ' '+ str(score)
            cv2.rectangle(image, boxes[i][:2], boxes[i][2:], color, 2)

            middle_x = boxes[i][0] + int((boxes[i][2] - boxes[i][0]) / 2)
            middle_y = boxes[i][3] - 10

            cv2.rectangle(image, [middle_x, middle_y], [middle_x, middle_y + 10], color, 2)
            cv2.putText(image, name,(boxes[i][0], boxes[i][1] - 2),cv2.FONT_HERSHEY_SIMPLEX,0.75,[225, 255, 255],thickness=2)

        return cv2.cvtColor(original_images[0], cv2.COLOR_RGB2BGR) 

    def detect(self, image, confidence_threshold=0.7, iou_threshold=0.7):
        im, ratio, dwdh = self.preprocess_image(image)
        model_outputs = self.model.run(None, { 'images': im })[0]
        return self.process_output(model_outputs, ratio, dwdh, confidence_threshold, iou_threshold)
