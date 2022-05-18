import numpy as np
import math
point_a = np.array([[0, 0, 0, 1], [5, 0, 0, 1], [0, 5, 0, 1]])
point_a_noise = np.array([[0.1, -0.9, -0.1, 1],[3.95, 0, 0.1, 1],[0, 5.2, 0, 1]])
theta = math.pi/4
transform = np.array([[math.cos(theta), -math.sin(theta), 0, 5], 
                      [math.sin(theta), math.cos(theta), 0, 10],
                      [0, 0, 1, 4],
                      [0, 0, 0, 1]])

point_b = np.dot(transform, point_a.transpose())
# column vector is a point
def get_avg_point(point):
    avg_point = np.array([0.0, 0.0, 0.0])
    for i in range(len(point[0])):
        avg_point[0] += point[0][i]
        avg_point[1] += point[1][i]
        avg_point[2] += point[2][i]
    avg_point/=len(point[0])
    return avg_point


point_b_avg = get_avg_point(point_b)
point_a_avg = get_avg_point(point_a.transpose())
H = np.array([[0.0, 0, 0],[0, 0, 0],[0, 0, 0]])
for i in range(len(point_b[0])):
    diff_b = point_b[0:-1,i]-point_b_avg
    diff_a = point_a.transpose()[0:-1,i]-point_a_avg
    tempH = np.outer(diff_a, diff_b)
    H += tempH
u, s, v = np.linalg.svd(H, full_matrices=True)
rotation = v.transpose().dot(u.transpose())
translation = point_b_avg - rotation.dot(point_a_avg)

print(rotation)
print(translation)
print(transform)
