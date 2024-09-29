import cv2

# Open a connection to the camera (0 is the default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press 'q' to quit and save the image as 'Camera Test Image.jpg'.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break  # Exit loop if there's an error capturing the frame

    # Display the resulting frame
    cv2.imshow('Camera Feed', frame)

    # Break the loop and save the image if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Save the captured frame when 'q' is pressed
        cv2.imwrite("Camera Test Image.jpg", frame)
        print("Image saved as 'Camera Test Image.jpg'")
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

