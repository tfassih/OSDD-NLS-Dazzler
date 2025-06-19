import cv2
import random
import numpy as np
import serial

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
serial_connection_g: serial.Serial = None
port_var = 'COM6'

def send_servo_command(x, y):
    serial_connection = serial_connection_g
    # formula for the multiplier is field_of_view_in_degrees/(resolution_x^2 + resolution_y^2); the default assumes a 1080p resolution with a 45 degree fov. We then calculate the distance from the center of the image to determine the angle.
    angle = (int(.0153994 * x) + int(.0153994 * y))
    if y < 0:
        command = f"A{angle}"
    else:
        command = f"B{angle}"
    print(command + '\n')

    try:
        serial_connection.write(command.encode())
        response = serial_connection.readline().decode().strip()
        print(f"Arduino response: {response}")
    except serial.SerialException as e:
        serial_connection = None


def main():
    serial_connection = serial_connection_g
    if serial_connection is None:
        try:
            port = port_var
            serial_connection = serial.Serial(port, 9600, timeout=1)
            print("connected to port: " + str(port) + '\n')
        except serial.SerialException as e:
            print("ERROR")
        else:
            serial_connection.close()
            serial_connection = None
    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
            roi_gray = gray[y:y+w, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
                if eyes.all():
                    print("Eyes detected")
                    send_servo_command(ex, ey)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
