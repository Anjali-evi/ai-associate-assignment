import pandas as pd

quadrant = pd.read_csv('/content/drive/MyDrive/ColabNotebooks/ball-detection/bbox_quadrant.csv')
quad_1 = [df['x_min'][0], df['y_min'][0], df['x_max'][0], df['y_max'][0]]
quad_2 = [df['x_min'][1], df['y_min'][1], df['x_max'][1], df['y_max'][1]]
quad_3 = [df['x_min'][2], df['y_min'][2], df['x_max'][2], df['y_max'][2]]
quad_4 = [df['x_min'][3], df['y_min'][3], df['x_max'][3], df['y_max'][3]]

# dictionary for the bbox of quadrants
quad_dic = {'quad_1': [quad_1[0], quad_1[1], quad_1[2], quad_1[3]],
            'quad_2': [quad_2[0], quad_2[1], quad_2[2], quad_2[3]],
            'quad_3': [quad_3[0], quad_3[1], quad_3[2], quad_3[3]],
            'quad_4': [quad_4[0], quad_4[1], quad_4[2], quad_4[3]]}

# counters for quadrants
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0

# active status for the quadrants
act_q1 = 0
act_q2 = 0
act_q3 = 0
act_q4 = 0



import glob
  
  
vidcap = cv2.VideoCapture('AI Assignment video.mp4')
  
# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(vidcap.get(3))
frame_height = int(vidcap.get(4))
   
size = (frame_width, frame_height)

result = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'avc1'),20.0, size)

if (vidcap.isOpened()== False):
    print("Error opening video file")
success,image = vidcap.read()
while(vidcap.isOpened()):
      success,imageFrame = vidcap.read()
      if success == True:
        # imageFrame = image.copy()
        gray = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 3)
        edge = cv2.Canny(gray, 20, 100)
        #cv2_imshow(edge)

        ret, thresh = cv2.threshold(edge, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(gray, contours, -1, (0,255,0), 4)
        # cv2_imshow(gray)
              
              
        rows = gray.shape[0]
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                        param1=100, param2=30,
                                        minRadius=10, maxRadius= 100)
        # for j in (4):      
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]: 
                center = (i[0], i[1])
                # circle center
                cv2.circle(imageFrame, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = i[2]
                cv2.circle(imageFrame, center, radius, (255, 0, 255), 3)
                for keys,values in quad_dic.items():
                    if collision(values[0],values[1],values[2],values[3], i[0], i[1], i[2]) and keys == 'quad_1':
                        cnt1 +=1 
                        cv2.rectangle(imageFrame, (values[0],values[1]),(values[2],values[3]), (255,0,0), 3)
                        cv2.putText(imageFrame, "Occupied", (values[0],values[1]),cv2.FONT_HERSHEY_SIMPLEX,1.0, (255,0,0))
                        print("Intersected with quadrant 1")

                    elif collision(values[0],values[1],values[2],values[3], i[0], i[1], i[2]) and keys == 'quad_2':
                        cnt2 +=1
                        cv2.rectangle(imageFrame, (values[0],values[1]),(values[2],values[3]), (255,0,0), 3)
                        cv2.putText(imageFrame, "Occupied", (values[0],values[1]),cv2.FONT_HERSHEY_SIMPLEX,1.0, (255,0,0))
                        print("Intersected with quadrant 2")

                    elif collision(values[0],values[1],values[2],values[3], i[0], i[1], i[2]) and keys == 'quad_3':
                        cnt3 +=1
                        cv2.rectangle(imageFrame, (values[0],values[1]), (values[2],values[3]), (255,0,0), 3)
                        cv2.putText(imageFrame, "Occupied", (values[0],values[1]),cv2.FONT_HERSHEY_SIMPLEX,1.0, (255,0,0))
                        print("Intersected with quadrant 3")

                    elif collision(values[0],values[1],values[2],values[3], i[0], i[1], i[2]) and keys == 'quad_4':
                        cnt4 +=1
                        cv2.rectangle(imageFrame, (values[0],values[1]),(values[2],values[3]), (255,0,0), 3)
                        cv2.putText(imageFrame, "Occupied", (values[0],values[1]),cv2.FONT_HERSHEY_SIMPLEX,1.0, (255,0,0))
                        print("Intersected with quadrant 4")

        result.write(imageFrame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

      else:
        break


# print(cnt1, cnt2, cnt3, cnt4)
vidcap.release()
result.release()
cv2.destroyAllWindows()
