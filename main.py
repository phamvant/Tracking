import cv2
import tracking_init as track
import imutils
import toExl
import glob

img_array = []
array_name = []

for filename in glob.glob('D:\\Python\\LAB\\Tracking\\data\\*.jpg'):
    array_name.append(filename)

frame = cv2.imread(array_name[0])
# cv2.imshow("a", frame)
# cap = cv2.VideoCapture("D:\\Python\\LAB\\IMAGE_CALIBRATION_V2\\video\\Tracking.avi")
# cap = cv2.VideoCapture("D:\\Python\\LAB\\Tracking\\project1.avi")

# success, frame = cap.read()
# bboxes = [(442, 542, 110, 106), (1124, 570, 116, 108), (270, 804, 98, 106), (1176, 854, 130, 106)]

check = False

if(check):
  bboxes = []
  while True:
    # draw bounding boxes over objects

    bbox = list(cv2.selectROI('MultiTracker', imutils.resize(frame, width = 960)))
    bboxes.append(tuple(map(lambda x: x * 2, bbox)))

    # colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))
    print("Press q to quit selecting boxes and start tracking")
    print("Press any other key to select next object")
    k = cv2.waitKey(0) & 0xFF
    if (k == 113):
      cv2.waitKey()
else:
  # bboxes = [(442, 542, 110, 106), (1124, 570, 116, 108), (270, 804, 98, 106), (1176, 854, 130, 106)]
  # bboxes = [(586, 432, 142, 128), (1194, 424, 146, 116), (562, 748, 166, 148), (1208, 750, 176, 158)]
  # bboxes = [(502, 514, 106, 104), (1262, 520, 58, 68), (280, 784, 118, 108), (1290, 836, 122, 108)]
  bboxes = [(503, 513, 100, 100), (1250, 520, 100, 100), (280, 790, 100, 100), (1303, 842, 100, 100)]

print('Selected bounding boxes {}'.format(bboxes))

multiTrack = track.multi_create(bboxes, frame)

wb, sheet = toExl.newWB()
  
for filename in array_name:
  centroid, lost_yellow, multiTrack, dist2 = track.track(frame, multiTrack, bboxes)
  # sheet = toExl.process(sheet, centroid, lost_yellow)
  sheet = toExl.process2(sheet, dist2)
  try:
    frame = cv2.imread(filename)
  except:
    break
  # success, frame = cap.read()
  # if(not success):
  #   break
  # if(not success):
  #   cap = cv2.VideoCapture("D:\\Python\\LAB\\project.avi")
  #   success, frame = cap.read()

# wb.save('D:\Python\LAB\Tracking\CompareN3.xlsx')