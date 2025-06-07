import lasio
from app.models.well import WellLog



class WellHandler:
    def __init__(self, las_file_path: str):
        self.las_file_path = las_file_path
        self.lasio_object = None


    def read_las(self):
        self.lasio_object = lasio.read(self.las_file_path)

        welllogs = self.create_well_logs_instances_from_curves_section()
        
        print(welllogs)

    def create_well_logs_instances_from_curves_section(self, curves_section):
        curves_section = self.lasio_object.sections["Curves"]
        return [
            WellLog(
                mnemonic =curve_item.mnemonic,
                unit=curve_item.unit,
                descr=curve_item.descr
            ) for curve_item in curves_section
        ]





well_handler = WellHandler('../tests/data/well1.las')
well_handler.read_las()