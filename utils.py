


# overlap function part-2
import math

def collision(xmin, ymin, xmax, ymax, center_x, center_y, radius):

    # bounding box of the circle
    cxmin, cymin = center_x-radius, center_y-radius
    cxmax, cymax = center_x+radius, center_y+radius

    # reject if bounding boxes do not intersect
    if xmax < cxmin or xmin > cxmax or ymax < cymin or ymin > cymax:
        return False  # no collision possible

    # check whether any point of rectangle is inside circle's radius
    for x in (xmin, xmax):
        for y in (ymin, ymax):
            # compare distance between circle's center point and each point of
            # the rectangle with the circle's radius
            if math.hypot(x-center_x, y-center_y) <= radius:
                return True  # collision detected

    # check if center of circle is inside rectangle
    if xmin <= center_x <= xmax and ymin <= center_y <= ymax:
        return True  # # collision overlaid
    

