import ICP_Solver
import numpy as np
import scipy.spatial.kdtree as kdTree
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# vertex in row
def readPointCloud(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    vertex = []
    for line in lines:
        xyz_str_list = line.split(' ')
        xyz_list = [float(i) for i in xyz_str_list]
        vertex.append(xyz_list)
    vertex = np.array(vertex)
    return vertex

bunny1_vertex = readPointCloud('./ICPs/bunny_part1.xyz.txt')
bunny2_vertex = readPointCloud('./ICPs/bunny_part2.xyz.txt')
print(bunny1_vertex.shape)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.scatter3D(bunny2_vertex[:,0], bunny2_vertex[:,1], bunny2_vertex[:,2])
# plt.show()