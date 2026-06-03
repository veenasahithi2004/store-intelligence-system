from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("data/videos/CAM 1.mp4")

visitor_ids = set()
frame_number = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1
    
    if frame_number % 2!= 0:
        continue

    if frame_number % 500 == 0:
        print("Processed", frame_number, "frames")
    frame = cv2.resize(frame, (640, 360))
    results = model.track(
        frame,
        persist=True,
        classes=[0],
        tracker="bytetrack.yaml",
        verbose=False
    )

    boxes = results[0].boxes

    if boxes.id is not None:
        ids = boxes.id.cpu().numpy().astype(int)

        for track_id in ids:
            visitor_ids.add(track_id)

cap.release()

print("\nVisitor Count:", len(visitor_ids))