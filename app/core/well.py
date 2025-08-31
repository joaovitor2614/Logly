import lasio
from typing import List

class WellHandler:
    def __init__(self):
        self.lasio_object: lasio.LASFile = None

    def get_well_info_from_las_file(self, las_file) -> dict:
        
        well_name = self._extract_well_name_from_lasio_obj()
        well_logs_info = self._extract_well_logs_info_from_lasio_obj()
        

        well_info = self._create_well_info(well_logs_info, well_name)

        return well_info
    def _extract_well_name_from_lasio_obj(self) -> str:
        return self.lasio_object.sections["Well"]["WELL"].value
    def _create_well_info(self, well_logs_info: List[dict], well_name: str):
        return {
            "name": well_name,
            "well_logs": well_logs_info,

        }

    def _extract_well_logs_info_from_lasio_obj(self):
        curves_section = self.lasio_object.sections["Curves"]
    
        return [
            {
       
                "mnemonic": curves_section[i].mnemonic,
                "unit": curves_section[i].unit,
                "descr": curves_section[i].descr,
                "data": self.lasio_object.data[:, i]
            }
            for i in range(len(curves_section))
        ]

        
well_handler = WellHandler()