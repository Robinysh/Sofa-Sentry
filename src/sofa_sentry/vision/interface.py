from picamera2 import Picamera2

from ultralytics import YOLO


class Vision:
    def __init__(self):
        # Initialize the Picamera2
        self.picam2 = Picamera2()
        # config = self.picam2.create_video_configuration(
        #    main={"size": (640, 480)},
        #    transform=Transform(vflip=True)  # vertical flip
        # )
        # self.picam2.configure(config)
        self.picam2.preview_configuration.main.size = (1280, 720)
        self.picam2.preview_configuration.main.format = "RGB888"
        self.picam2.preview_configuration.align()
        # self.picam2.configure("preview")
        self.picam2.start()

        # Load the YOLO11 model
        self.yolo_model = YOLO("models/yolo11n.onnx")
        self.seg_model = YOLO("models/yolo11n-seg.onnx")
        self.count = 0

    def detected(self):
        # Capture frame-by-frame
        frame = self.picam2.capture_array()

        # Run YOLO11 inference on the frame
        result = self.yolo_model(frame)[0]
        # result = self.yolo_model('./tests/cat.jpg')[0]

        result.save(result.path)

        summary = result.summary()
        if "human" in [item["name"] for item in summary]:
            print("Human on sofa detected, skipping...")
            return False

        for i, item in enumerate(summary):
            print(item)
            if item["name"] != "cat":
                continue
            print("Cat detected:", item)
            result.save(f"./logs/cat_{self.count}.jpg")
            self.count += 1

            # seg_result = self.seg_model(frame)[0]

            box = item["box"]
            center = (box["x1"] + box["x2"]) / 2, (box["y1"] + box["y2"]) / 2
            return center
        return False
