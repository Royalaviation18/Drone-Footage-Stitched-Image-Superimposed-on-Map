
# 🛰️ Georeferenced Drone Footage to Stitched Map Overlay

🎯 Objective

The goal of this project is to simulate drone-based geospatial data processing by:

- Extracting frames from a georeferenced video.

- Stitching the frames into a seamless composite image.

- Overlaying the stitched image on an interactive map using Python’s Folium library.

- Creating a visual tool for use in AI training datasets or GIS analysis.


📁 Project Structure
 
├── framExt.py                # Frame extraction script

├── imageStich.py             # Image stitching script

├── geroReferencing.py        # Folium overlay script

├── frames/                   # Extracted PNG frames

├── stitched_output.png       # Final stitched panoramic image

├── map_with_overlay.html     # Interactive Folium map



📽️ Source Video

Source: Google Earth Pro (Simulated drone flyover)

Coordinates: 30.1158° N, 78.2853° E

Format: .m4v georeferenced video

Reason: Urban flyover view with good stitching potential


🧩 Step-by-Step Process

1. 🎞️ Frame Extraction (framExt.py)
    
    - Library Used: OpenCV

    - Strategy: Extracted 1 frame per second for clarity and efficiency.

    - Output: PNG frames stored in frames/ directory

       ```bash
       if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % int(cap.get(cv2.CAP_PROP_FPS)) == 0
       ```

2. 🧵 Image Stitching (imageStich.py)

 #### Library Used: OpenCV (Stitcher_SCANS)

- Why SCANS mode?: Optimized for top-down stitching like drone or satellite maps

- Result: Single large image stitched_output.png

- Images were sorted and verified for integrity before stitching

3. 🌍 Geo-Referencing (geroReferencing.py)

- Library Used: Folium

- Bounds Used: [30.1140, 78.2825] (SW) to [30.1170, 78.2880] (NE)

- Output: Interactive map map_with_overlay.html with overlay opacity 0.7

    ```bash
       ImageOverlay(image='stitched_output.png', bounds=bounds, opacity=0.7)
     ```

📌 Manual Estimation

- Since the stitched image does not contain GPS metadata, bounding coordinates were estimated manually based on:

- Video origin coordinates

- Visual landmarks in stitched image

- Map alignment trial and error


🔧 Tools & Technologies

| Tool/Library           | Use|
| ----------------- | ------------------------------------------------------------------ |
| OpenCV  | 	Frame extraction, image stitching |
| Folium  |	Map rendering and overlay |
| PIL / Pillow| 	Image format support |
| Google Earth Pro	 | Video generation and simulation |
| Python 3.10+ | 	Programming language |



🧪 Challenges Faced

- Aligning stitched image with real-world bounds manually

- Avoiding ghosting due to overlapping motion

- Ensuring consistent image size and quality before stitching


🎥 Walkthrough Video

[![Watch the Demo]]([https://www.loom.com/share/d99d8c8b58c349098e818ed3888e995b?sid=2a83a575-7c0a-43bb-8729-c7a5db6587bc](https://www.loom.com/share/df9434941d5844efb56821b688db5cb9?sid=04ca5a87-fb51-409b-9645-aa4d1dc38947https://www.loom.com/share/df9434941d5844efb56821b688db5cb9?sid=04ca5a87-fb51-409b-9645-aa4d1dc38947))

✅ Final Outputs

| Deliverable           | 	Status|
| ----------------- | ------------------------------------------------------------------ |
| Stitched Image  | 	stitched_output.png |
| Frame Extractor  |	framExt.py |
| Image Stitcher| imageStich.py |
| Map Overlay	 | map_with_overlay.html |
| Video Demo | 	Programming language |



🧭 Coordinate System

- WGS84 (EPSG:4326) — used for bounding boxes in Folium


👤 Author

- Name: Rohit Priyadarshi

- GitHub: https://github.com/royalaviation18

- Email: rohitp2203@gmail.com

