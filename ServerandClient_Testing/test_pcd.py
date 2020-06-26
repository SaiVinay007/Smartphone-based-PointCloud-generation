import numpy as np
from open3d import *    
import open3d as o3d

def main():
    pcd = o3d.io.read_point_cloud("../code/socket_programming/pcd.ply") # Read the point cloud
    o3d.visualization.draw_geometries([pcd]) # Visualize the point cloud     
    # print(pcd)
    # help(o3d)
    # help(o3d.geometry.PointCloud)
    # help(o3d.io.read_point_cloud)
if __name__ == "__main__":
    main()