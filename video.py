import argparse
from cv2 import *

arg=argparse.ArgumentParser()
arg.add_argument("--input",help="enter video path")
args=vars(arg.parse_args())
cap=VideoCapture(0)

while True:
    reg,frame=cap.read()

    cv2.imshow("OUPUT IMAGE",frame)
    if cv2.waitKey(100) & 0xFF==ord('q'):
        break
cap.release()
destroyAllWindows()