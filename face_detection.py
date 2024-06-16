import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/Aditya/Desktop/Projects/Facial Expression Recognition/Project-Face Detection-2/Harr_Cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/Aditya/Desktop/Projects/Facial Expression Recognition/Project-Face Detection-2/Harr_Cascades/haarcascade_eye.xml')

web_cam = 1

# Start Video Camera
cap = cv2.VideoCapture(0)
# Error Message if Video Camera not shown
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


def video_camera():
    print("\nOpening Web Cam.....")

    # Start Video Camera
    cap = cv2.VideoCapture(0)
    # Error Message if Video Camera not shown
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    print("Processing Image...")

    print("\nPress 'q' to exit\n")
    
    while (web_cam):
        ret, img = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        def_boundaries(gray, faces, img)

        if cv2.waitKey(30) & 0xff == ord('q'):
            break

        cv2.imshow('Face and Eye Detection',img)

    choose()

    cap.release()
    cv2.destroyAllWindows()
    

def image():
    image_path = input("Enter the path to the image: ")
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not load the image.")
        image()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    def_boundaries(gray, faces, img)
    cv2.imshow('Face and Eye Detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    choose()


def def_boundaries(gray_img, face_data, img_data):
    # For face Data
    for (x,y,w,h) in face_data:
        cv2.rectangle(img_data,(x,y),(x+w,y+h),(255,0,0),2) #Blue box for Face
        roi_gray = gray_img[y:y+h, x:x+w] #Returns the Region of Face, on which eyes will be matched
        roi_color = img_data[y:y+h, x:x+w]

        eye_data = eye_cascade.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eye_data:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) #Green Box for eyes


def choose():
    print("There are 2 features:")
    print("\t 1. Detect Image from LIVE Video [Press 1]")
    print("\t 2. Detect Image from a picture [Press 2]\n")
    print("\t Exit [Press 0] \n")

    opt_1 = input("Press 1 or 2 or 0(For exit): ")

    if (opt_1 == '1'):
        video_camera()

    elif (opt_1 == '2'):
        image()

    elif (opt_1 == '0'):
        return
    
    else:
        print("\nPress either 1 or 2. Pressing any other key will not work! \n")
        choose()
    return


def main():
    print("\nPROJECT - FACIAL DETECTION\n")

    print("This project is capable of detecting and labeling the faces and eyes of that face in an image\n")

    choose()
    return


main()
