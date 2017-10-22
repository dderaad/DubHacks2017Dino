import cv2
import numpy as np

def vid2path(video, file_name):
    k = .35 # decay factor
    cap = cv2.VideoCapture(video)

    ret, frame1 = cap.read()
    prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    total = np.zeros_like(prvs)
    no_frame = 1

    while (cap.isOpened()):
        ret, frame2 = cap.read()
        if frame2 is not None:
            next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

            flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

            mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])

            mag_no_infs = mag
            mag_no_infs[mag_no_infs == np.inf] = np.max(mag_no_infs[np.isfinite(mag_no_infs)]) * 5

            total = mag_no_infs + total * k
            no_frame += 1
        else:
            break

    path = total * 255.0 / total.max()
    #path = total

    cv2.imwrite(file_name, path)
    cv2.imshow('', path)
    cv2.waitKey(0)

url_test = "http://csr.bu.edu/ftp/asl/asllvd/demos/verify_start_end_handshape_annotations//test_auto_move//signs_mov_separ_signers/Liz_2921.mov"

gloss_file = "gloss_urls_short"

#read dict from file
with open(gloss_file) as f:
    html_dict = {}
    for line in f:
        line = line.split(";")
        html_dict[line[0].rstrip()] = set(eval("set(" + line[1] + ")"))

for gloss in html_dict:
    i = 0
    for video_link in html_dict[gloss]:
        i += 1
        vid2path(video_link, '{}{}.jpg'.format(gloss, i))
