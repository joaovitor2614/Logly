import lasio

class WellHandler:
    def __init__(self, las_file_path: str):
        self.las_file_path = las_file_path


    def read_las(self):
        las = lasio.read(self.las_file_path)