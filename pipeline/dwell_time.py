from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("data/videos/CAM 2.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)

first_seen = {}
last_seen = {}

frame_number = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1

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

            if track_id not in first_seen:
                first_seen[track_id] = frame_number

            last_seen[track_id] = frame_number

cap.release()

dwell_times = []

for track_id in first_seen:

    duration = (
        last_seen[track_id] - first_seen[track_id]
    ) / fps

    if duration >= 3:
        dwell_times.append(duration)

if len(dwell_times) > 0:

    avg_dwell = sum(dwell_times) / len(dwell_times)

    print("\nValid Visitors:", len(dwell_times))
    print("Average Dwell Time:", round(avg_dwell, 2), "seconds")
    print("Longest Stay:", round(max(dwell_times), 2), "seconds")
    print("Shortest Stay:", round(min(dwell_times), 2), "seconds")