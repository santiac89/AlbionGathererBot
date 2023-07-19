import cv2
from detector import Detector
from window_capture import WindowCapture

models = {
    "1024": {
        "model_name": "1024_v7",
        "width": 1024,
        "height": 576,
        "shape": 1024
    },
    "640": {
        "model_name": "640_v2",
        "width": 1138,
        "height": 640,
        "shape": 640
    }
}

model = models["1024"]

window = WindowCapture("Albion Online Client")
detector = Detector(model["model_name"], model["shape"])

while True:    
    screenshot = window.get_screenshot()

    if screenshot is None:
        continue

    boxes, confidences, classes, batch_ids = detector.detect(screenshot)

    result = detector.debug_image(screenshot, boxes, confidences, classes, batch_ids)

    cv2.imshow("Computer Vision", cv2.resize(result, (model["width"], model["height"])))

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        exit(0)