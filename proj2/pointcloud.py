class PointCloud:
    def __init__(self):
        self.ncols = 0
        self.nrows = 0
        self.pos = None
        self.axis = None
        self.transform = None
        self.points = None
        self.homogeneous_points = None
        self.intensities = None
    
    def read_from_file(self, fn):
        import numpy as np
        with open(fn, 'r') as f:
            self.ncols = int(f.readline().strip())
            self.nrows = int(f.readline().strip())

            self.pos = list(map(int, f.readline().split()))
            self.axis = [
                list(map(int, f.readline().split())),
                list(map(int, f.readline().split())),
                list(map(int, f.readline().split())),
            ]
            self.transform = [
                list(map(int, f.readline().split())),
                list(map(int, f.readline().split())),
                list(map(int, f.readline().split())),
                list(map(int, f.readline().split())),
            ]
            
            self.homogeneous_points = np.ones(shape=(self.nrows, self.ncols, 4))
            self.intensities = np.zeros(shape=(self.nrows, self.ncols, 1))
            
            for c in range(self.ncols):
                for r in range(self.nrows):
                    p = list(map(float, f.readline().split()))
                    self.homogeneous_points[r][c][:3] = p[:3]
                    self.intensities[r][c] += p[3]
                    
            self.points = self.homogeneous_points[:, :, :3]
                    
    def write_to_file(self, fn):
        import numpy as np
        with open(fn, 'w') as f:
            f.write('{}\n'.format(self.ncols))
            f.write('{}\n'.format(self.nrows))
            f.write('{}\n'.format(' '.join(map(str, self.pos))))
            f.write('{}\n'.format(' '.join(map(str, self.axis[0]))))
            f.write('{}\n'.format(' '.join(map(str, self.axis[1]))))
            f.write('{}\n'.format(' '.join(map(str, self.axis[2]))))
            f.write('{}\n'.format(' '.join(map(str, self.transform[0]))))
            f.write('{}\n'.format(' '.join(map(str, self.transform[1]))))
            f.write('{}\n'.format(' '.join(map(str, self.transform[2]))))
            f.write('{}\n'.format(' '.join(map(str, self.transform[3]))))
            
            for c in range(self.ncols):
                for r in range(self.nrows):
                    f.write('{} {}\n'.format(' '.join(map(str, self.points[r][c])), str(self.intensities[r][c][0])))
                    
    def apply_transform(self, transform):
        import numpy as np
        points = self.homogeneous_points.reshape((self.nrows*self.ncols, 4))
        points = np.matmul(transform, points.transpose()).transpose()
        
        self.homogeneous_points = points.reshape((self.nrows, self.ncols, 4))
        self.points = self.homogeneous_points[:, :, :3]
