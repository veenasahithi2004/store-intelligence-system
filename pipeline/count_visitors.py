from ultralytics import YOLO

print("Loading YOLO...")

model = YOLO("yolov8n.pt")

print("Starting tracking...")

results = model.track(
    source="data/videos/CAM 1.mp4",
    tracker="botsort.yaml",
    classes=[0],      # person only
    conf=0.4,
    save=True,
    persist=True
)

print("Tracking completed!")