def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    x1_a,y1_a,x2_a,y2_a=box_a
    x1_b,y1_b,x2_b,y2_b=box_b

    x_left=max(x1_a,x1_b)
    y_top=max(y1_a,y1_b)
    x_right=min(x2_a,x2_b)
    y_bottom=min(y2_a,y2_b)

    if x_right<=x_left or y_bottom<=y_top:
        inter = 0
    else:
        inter = (x_right - x_left) * (y_bottom - y_top)

    area_a=(x2_a-x1_a)*(y2_a-y1_a)
    area_b=(x2_b-x1_b)*(y2_b-y1_b)

    union = area_a+area_b-inter 

    if union<=0:
        return 0.0

    return inter/union