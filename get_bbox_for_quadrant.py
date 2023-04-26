import pandas as pd
import cv2
import numpy as np

image= cv2.imread('/content/first_frame.jpg')
original_image= image

gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges= cv2.Canny(gray, 50,200)

contours, hierarchy= cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


cv2.destroyAllWindows()


# def get_contour_areas(contours):

#     all_areas= []

#     for cnt in contours:
#         area= cv2.contourArea(cnt)
#         all_areas.append(area)

#     return all_areas


sorted_contours= sorted(contours, key=cv2.contourArea, reverse= True)


largest_item1= sorted_contours[0]
cv2.drawContours(original_image, largest_item1, -1, (255,0,0),10)
x1,y1,w1,h1 = cv2.boundingRect(largest_item1)
image = cv2.rectangle(image, (x1, y1), (x1 + w1, y1 + h1), (36,255,12), 1)
cv2.putText(image, 'Top-One', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

largest_item2= sorted_contours[1]
cv2.drawContours(original_image, largest_item2, -1, (255,0,0),10)
x2,y2,w2,h2 = cv2.boundingRect(largest_item2)
image = cv2.rectangle(image, (x2, y2), (x2 + w2, y2 + h2), (36,255,12), 1)
cv2.putText(image, 'Top-Two', (x2, y2-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

largest_item3= sorted_contours[2]
cv2.drawContours(original_image, largest_item3, -1, (255,0,0),10)
x3,y3,w3,h3 = cv2.boundingRect(largest_item3)
image = cv2.rectangle(image, (x3, y3), (x3 + w3, y3 + h3), (36,255,12), 1)
cv2.putText(image, 'Top-Three', (x3, y3-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

largest_item4= sorted_contours[3]
cv2.drawContours(original_image, largest_item4, -1, (255,0,0),10)
x4,y4,w4,h4 = cv2.boundingRect(largest_item4)
image = cv2.rectangle(image, (x4, y4), (x4 + w4, y4 + h4), (36,255,12), 1)
cv2.putText(image, 'Top-Four', (x4, y4-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

xmin = [x2, x4 , x3, x1]
ymin = [y2, y4, y3, y1]
xmax = [x2+w2, x4+w4, x3+w3, x1+w1]
ymax = [y2+h2, y4+h4, y3+h3, y1+h1]

d = {'Squares':['1st_quadrant','2nd_quadrant','3rd_quadrant','4th_quadrant'], 'x_min':xmin ,'y_min': ymin, 'x_max':xmax, 'y_max': ymax}
df = pd.DataFrame(d)

cv2.waitKey(0)
cv2.imshow("Original Image",original_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
