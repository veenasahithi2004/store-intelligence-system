from ultralytics import YOLO

print("Loading model...")

model = YOLO("yolov8n.pt")

video_path = "data/videos/CAM 1.mp4"

results = model.predict(
    source=video_path,
    classes=[0],      # person class only
    save=True,
    conf=0.4
)

print("Processing complete!")