from fnmatch import translate
import numpy as np
import math
class ICP_Solver:
    # column vector is a point
    def _get_avg_point(self, point):
        avg_point = np.array([0.0, 0.0, 0.0])
        for i in range(len(point[0])):
            avg_point[0] += point[0][i]
            avg_point[1] += point[1][i]
            avg_point[2] += point[2][i]
        avg_point/=len(point[0])
        return avg_point

    def _get_Cross_Covariance(self, point_a, point_b, point_a_avg, point_b_avg):

            H = np.array([[0.0, 0, 0],[0, 0, 0],[0, 0, 0]])
            for i in range(len(point_b[0])):
                diff_b = point_b[:,i]-point_b_avg
                diff_a = point_a[:,i]-point_a_avg
                tempH = np.outer(diff_a, diff_b)
                H += tempH
            return H

    # column vector
    def get_estimate_transform(self, point_source, point_target):
        point_a = point_source
        point_b = point_target
        point_a_avg = self._get_avg_point(point_a)
        point_b_avg = self._get_avg_point(point_b)

        H = self._get_Cross_Covariance(point_a, point_b, point_a_avg, point_b_avg)

        u, s, v = np.linalg.svd(H, full_matrices=True)
        rotation = v.transpose().dot(u.transpose())
        translation = point_b_avg - rotation.dot(point_a_avg)
        return rotation, translation

# point_a = np.array([[0, 0, 0], [5, 0, 0], [0, 5, 0]])
# point_a_noise = np.array([[0.1, -0.9, -0.1],[3.95, 0, 0.1],[0, 5.2, 0]])
# theta = math.pi/4
# rotation = np.array([[math.cos(theta), -math.sin(theta), 0], 
#                       [math.sin(theta), math.cos(theta), 0],
#                       [0, 0, 1]])
# translate = np.array([[5],[10],[4]])
# point_b = np.dot(rotation, point_a.transpose())
# point_b = translate + point_b

# solv = ICP_Solver()
# rot, trans = solv.get_estimate_transform(point_a.transpose(), point_b)
# print(rot)
# print(trans)
# print(rotation)

