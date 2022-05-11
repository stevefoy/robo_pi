import cv2
import time
import sys
import argparse
import os

def create_folder(folder_path):
    try:
        if not os.path.exists(path_save):
            os.makedirs(path_save)
            
            path_save = os.path.dirname(path_save)
            try:
                os.stat(path_save)
            except:
                os.mkdir(path_save)
    except :
        print("excetpion failed to make folder")


def capture(width=0, height=0):

    #os.system('sudo modprobe bcm2835-v4l2')

    frame_raw = cv2.VideoCapture(0)
    if width>0 and height>0:
        print("Setting the custom Width and Height")
        #frame_raw.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        #frame_raw.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    name_prefix="capture"
    folder = os.path.join(os.getcwd(), "raw_captures")
    print("Data save to :", folder)
    create_folder(folder)

    capture_count   = 0



    
    while frame_raw.get(cv2.CAP_PROP_FRAME_WIDTH) and frame_raw.get(cv2.CAP_PROP_FRAME_HEIGHT):
        

        ret, frame = frame_raw.read()

        cv2.imshow('camera', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord('s'):
            fileName    = "%s/%s_%d_%d_" %(folder, name_prefix, frame_raw.get(cv2.CAP_PROP_FRAME_WIDTH), frame_raw.get(cv2.CAP_PROP_FRAME_HEIGHT))
            cv2.imwrite("%s%d.jpg"%(fileName, capture_count), frame)
            print("Captured image ", capture_count)
            capture_count += 1

    frame_raw.release()
    cv2.destroyAllWindows()

def main():


    parser = argparse.ArgumentParser(description="Capture images pi, press s to save current image ")

    parser.add_argument("--width", default=0, type=int, help="width px ")
    parser.add_argument("--height", default=0, type=int, help="height px ")

    args = parser.parse_args()

    capture(width=args.width, height=args.height)






if __name__ == "__main__":
    main()