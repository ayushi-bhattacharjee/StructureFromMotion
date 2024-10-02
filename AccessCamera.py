#!/usr/bin/env python3

import cv2 
import os

# make a output directory for photos
# possibly add a command line argument to change this directory from a default
# output format should be <outdir>/<iso-8601 date>.{png,mp4}
#chmod +x

def main():
    # Define paths
    save_path = '/Users/ayla/Desktop/Research/'
    photo_filename = os.path.join(save_path, 'photo.png')
    video_filename = os.path.join(save_path, 'output.mp4')  # Change extension to .mp4

    # Open a connection to the default camera // make output directory for photos 
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Error: Could not open video source.")
        exit()

    # Define codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' codec for .mp4 format
    out = None
    recording = False

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Display the resulting frame
        cv2.imshow('Camera Feed', frame)

        # Check for key presses
        key = cv2.waitKey(1) & 0xFF

        # Start recording when 's' is pressed
        if key == ord('s'):
            if out is None:
                # Get frame width and height
                frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                # Create VideoWriter object
                out = cv2.VideoWriter(video_filename, fourcc, 20.0, (frame_width, frame_height))
                recording = True
                print("Recording started...")

        # Stop recording when 'q' is pressed
        elif key == ord('q'):
            if out is not None:
                out.release()
                out = None
                recording = False
                print("Recording stopped.")

        # Take a photo when 'p' is pressed
        elif key == ord('p'):
            cv2.imwrite(photo_filename, frame)
            print(f"Photo saved as {photo_filename}")

        # Exit the loop and close everything when 'x' is pressed
        elif key == ord('x'):
            break

        # Write the frame to the video file if recording
        if recording and out is not None:
            out.write(frame)

    # Release the camera and close all OpenCV windows
    cap.release()
    if out is not None:
        out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()