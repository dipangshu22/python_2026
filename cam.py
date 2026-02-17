import cv2

camera = cv2.VideoCapture(0)

# Allow camera to warm up
cv2.waitKey(2000)

first_frame = None

while True:
    ret, frame = camera.read()

    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur to remove noise
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    # Initialize first frame
    if first_frame is None:
        first_frame = gray
        continue

    # Compute difference
    diff = cv2.absdiff(first_frame, gray)

    thresh = cv2.threshold(diff, 25, 255,
                           cv2.THRESH_BINARY)[1]

    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:

        # Ignore small movements
        if cv2.contourArea(contour) < 1500:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(frame,
                      (x,y),
                      (x+w, y+h),
                      (0,255,0),
                      2)

        cv2.putText(frame,
                    "Motion Detected",
                    (10,20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0,0,255),
                    2)

    cv2.imshow("Motion Detector", frame)
    cv2.imshow("Threshold", thresh)

    key = cv2.waitKey(1)

    if key == 27:  # ESC key
        break

camera.release()
cv2.destroyAllWindows()
