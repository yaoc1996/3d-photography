class PointCloud:
    def __init__(self):
        self.ncols = 0
        self.nrows = 0
        self.pos = None
        self.axis = None
        self.transform = None
        self.points = None
    
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
            
            self.points = np.zeros(shape=(self.nrows, self.ncols, 3))
            
            for c in range(self.ncols):
                for r in range(self.nrows):
                    self.points[r][c] += list(map(float, f.readline().split()))[:3]