import cv2
import os

video_path = 'DehradunPath.m4v'
output_dir = 'frames'
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
fps = 1  # 1 frame per second
count = 0
success, frame = cap.read()
while success:
    if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % int(cap.get(cv2.CAP_PROP_FPS) * fps) == 0:
        cv2.imwrite(f"{output_dir}/frame_{count:04d}.png", frame)
        count += 1
    success, frame = cap.read()
cap.release()
