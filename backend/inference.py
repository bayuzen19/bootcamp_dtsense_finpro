from ultralytics import YOLO
import numpy as np

def inference(image):
    model = YOLO('best.pt')
    results = model(image, conf=0.3)
    infer = np.zeros(image.shape, dtype=np.uint8)
    classes = dict()
    namesInfer = []

    for r in results:
        infer = r.plot()
        classes = r.names
        namesInfer = r.boxes.cls.tolist()
    
    return infer, classes, namesInfer
