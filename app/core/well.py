import lasio
import pandas as pd

from typing import List


class WellHandler:
    def __init__(self, las_file_path: str):
        self.las_file_path = las_file_path
        self.lasio_object = None


    def get_well_info_from_las_file(self) -> dict:
        
        self.lasio_object = lasio.read(self.las_file_path)
        

        well_logs_info = self._extract_well_logs_info_from_curves_section()

        well_info = self._create_well_info(well_logs_info)

        return well_info
        
    def _create_well_info(self, well_logs_info: List[dct]):
        well_name = self.lasio_object.sections["Well"]["WELL"].value

        return {
            "name": well_name,
            "well_logs": well_logs_info,

        }
 
   
       
       

    def _extract_well_logs_info_from_curves_section(self):
        curves_section = self.lasio_object.sections["Curves"]
        
    
        welllogs_info = [
            {
       
                "mnemonic": curve_item.mnemonic,
                "unit": curve_item.unit,
                "descr": curve_item.descr,
                "data": []
            }
            for curve_item in curves_section
        ]
        self._populate_well_logs_info_data(welllogs_info)
        return welllogs_info
            

    def _populate_well_logs_info_data(self, welllogs_info: List[dict]):
        well_logs_amount = self.lasio_object.data.shape[1]
        for i in range(well_logs_amount):

            welllogs_info[i]["data"] = self.lasio_object.data[:, i]
 
    

