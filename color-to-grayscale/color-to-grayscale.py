def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    re = []
    for i in range(len(image)):
        row = []
        for j in range(len(image[i])):
            y = 0.299 * image[i][j][0] + 0.587*image[i][j][1] + 0.114*image[i][j][2]
            row.append(y)
        re.append(row)
    return re