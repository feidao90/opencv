import cv2
from os.path import dirname, abspath

if __name__=='__main__':
    cap = cv2.VideoCapture(0)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    path = dirname(dirname(abspath(__file__)))
    out = cv2.VideoWriter(path+'/video/output.avi', fourcc, 20.0, (640, 360))
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 0)
            # write the flipped frame
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
