from ultralytics import YOLO
import cv2

# Load YOLO model once
model = YOLO("yolov8n.pt")

videos = [
    "CAM 1.mp4",
    "CAM 2.mp4",
    "CAM 3.mp4",
    "CAM 4.mp4",
    "CAM 5.mp4"
]

camera_results = {}

for video in videos:

    print("\n" + "=" * 50)
    print(f"Processing {video}")
    print("=" * 50)

    cap = cv2.VideoCapture(f"data/videos/{video}")

    visitor_ids = set()
    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        # Progress update every 500 frames
        if frame_count % 500 == 0:
            print(f"{video}: Processed {frame_count} frames")

        results = model.track(
            frame,
            persist=True,
            classes=[0],            # Person class only
            tracker="botsort.yaml",
            verbose=False
        )

        boxes = results[0].boxes

        if boxes.id is not None:

            ids = boxes.id.cpu().numpy().astype(int)

            for track_id in ids:
                visitor_ids.add(track_id)

    cap.release()

    camera_results[video] = len(visitor_ids)

    print(f"\n{video} Visitor Count: {len(visitor_ids)}")

print("\n")
print("=" * 50)
print("FINAL STORE TRAFFIC REPORT")
print("=" * 50)

total_visitors = 0

for camera, count in camera_results.items():
    print(f"{camera}: {count} visitors")
    total_visitors += count

print("\nTotal Visitors Across All Cameras:", total_visitors)

highest_camera = max(camera_results, key=camera_results.get)

print(
    f"Most Active Camera: {highest_camera} "
    f"({camera_results[highest_camera]} visitors)"
)