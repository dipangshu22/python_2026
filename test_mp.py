import cv2
import numpy as np

KNOWN_MARKER_SIZE = 5  # cm

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(
    aruco.DICT_4X4_50
)

detector = aruco.ArucoDetector(dictionary)

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    corners, ids, _ = detector.detectMarkers(frame)

    if ids is not None:

        # Draw marker
        cv2.aruco.drawDetectedMarkers(frame, corners)

        marker_corners = corners[0][0]

        # Compute marker height in pixels
        pixel_height = np.linalg.norm(
            marker_corners[0] - marker_corners[3]
        )

        cm_per_pixel = KNOWN_MARKER_SIZE / pixel_height

        # Example: measure something vertically
        height_pixels = frame.shape[0]

        estimated_height = height_pixels * cm_per_pixel

        cv2.putText(frame,
                    f"Estimated Height Scale Ready",
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,(0,255,0),2)

    cv2.imshow("Measurement Scanner", frame)

    if cv2.waitKey(1)==27:
        break

camera.release()
cv2.destroyAllWindows()
