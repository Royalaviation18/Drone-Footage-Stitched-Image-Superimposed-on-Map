import cv2
import os

folder_path = 'frames'
images = []

# Load and verify images
for file in sorted(os.listdir(folder_path)):
    if file.endswith('.png'):
        img_path = os.path.join(folder_path, file)
        img = cv2.imread(img_path)
        if img is not None:
            images.append(img)
        else:
            print(f"Warning: Could not read image {file}")

print(f"Total images loaded: {len(images)}")

# Sanity check
if len(images) < 2:
    print("Need at least 2 images to stitch.")
    exit()

# Optional: Resize all to same size (useful if resolution differs)
# base_height, base_width = images[0].shape[:2]
# images = [cv2.resize(img, (base_width, base_height)) for img in images]

# Create stitcher in SCANS mode if it's top-down drone view
stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)

(status, stitched) = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    cv2.imwrite("stitched_output.png", stitched)
    print("✅ Stitching completed successfully. Saved as stitched_output.png")
else:
    print(f"❌ Stitching failed with status code: {status}")
