import cv2

# Initialize video capture
video_path = 'D:/Internship Assignments/Auriga Tech Solutions Private Limited/Traffic/traffic_vid.mp4'
cap = cv2.VideoCapture(video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    # Read the first frame from the video
    ret, frame = cap.read()
    if ret:
        # Resize the frame to a smaller size
        frame_resized = cv2.resize(frame, (640, 480))  # Resize to 640x480 or any size you prefer

        # Display the resized frame
        cv2.imshow('Frame (Resized)', frame_resized)
        
        # Wait for a key press indefinitely or for a given amount of time in milliseconds
        key = cv2.waitKey(0)
        
        # Optionally print the key pressed (for debugging)
        print(f"Key pressed: {key}")
        
        # Destroy the window
        cv2.destroyAllWindows()
    else:
        print("Error: Could not read frame from video.")

cap.release()
