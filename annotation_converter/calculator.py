def calculate_coordinates(extreme_points):
    center_x = (extreme_points[0][0] + extreme_points[2][0]) / 2
    center_y = (extreme_points[1][1] + extreme_points[3][1]) / 2
    width = extreme_points[0][0] - extreme_points[2][0]
    height = extreme_points[1][1] - extreme_points[3][1]

    return [center_x, center_y, width, height]
