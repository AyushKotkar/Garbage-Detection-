import os
import cv2
vidcap = cv2.VideoCapture('video.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 1.0 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

folder_path = 'C:/Users/ayush/Desktop/Sift'
image_files = os.listdir(folder_path)
image_files = [file for file in image_files if file.endswith('.jpg')]

sift = cv2.SIFT_create()

for file in image_files:
    image_path = os.path.join(folder_path, file)
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kp, des = sift.detectAndCompute(gray_img, None)
    

    print('Keypoints for image', file, ':', len(kp))
    # print('Descriptors for image', file, ':', des.shape)
    # if len(kp) > 100:
    #    print("Garbage is Not Collected")
    # else:
    #    print("Garbage is Collected")

if len(kp) > 100:
    print("Garbage is Not Collected")
else:
    print("Garbage is Collected")


