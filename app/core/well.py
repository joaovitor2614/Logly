import lasio
import pandas as pd
from app.models.well.well import WellLog, Well
from typing import List


class WellHandler:
    def __init__(self, las_file_path: str, user_id: str):
        self.las_file_path = las_file_path
        self.lasio_object = None
        self.user_id = user_id

    def get_well_db_obj_from_las_file(self):
        
        self.lasio_object = lasio.read(self.las_file_path)
        

        welllogs = self._create_well_logs_instances_from_curves_section()

        well = self._create_well_instance(welllogs)

        return well
        
    def _create_well_instance(self, welllogs: List[WellLog]):
        well_name = self.lasio_object.sections["Well"]["WELL"].value
        print('well_namewell_name', well_name)
        return Well(name=well_name, welllogs=welllogs, user_id=self.user_id)
       
       

    def _create_well_logs_instances_from_curves_section(self):
        curves_section = self.lasio_object.sections["Curves"]
        welllogs = [
            WellLog(
                mnemonic =curve_item.mnemonic,
                unit=curve_item.unit,
                descr=curve_item.descr
            ) for curve_item in curves_section
        ]
        self._populate_well_logs_instances_data(welllogs)
        return welllogs
            

    def _populate_well_logs_instances_data(self, welllogs: List[WellLog]):
        well_logs_amount = self.lasio_object.data.shape[1]
        for i in range(well_logs_amount):
            well_log_data_jsonfied = pd.Series(self.lasio_object.data[:, i]).to_json(orient='values')
            welllogs[i].data = well_log_data_jsonfied
 
    

