import lasio
from typing import List
import io

LASIO_WELL_SECTION_INFO_MNEMONICS_BY_MODEL_ATTR = {
    "name": "WELL",
    "start": "STRT",
    "stop": "STOP",
    "company": "COMP"
}

class WellHandler:
    def __init__(self):
        self.lasio_object: lasio.LASFile = None

    def get_depth_info_from_lasio_obj(self):
        las_depth_info = {"min": 0, "max": 0}

    def get_lasio_object_from_las_file_object(self, las_file_object):
        las_file_text_stream = io.TextIOWrapper(las_file_object.file, encoding="utf-8", errors="ignore")
        return lasio.read(las_file_text_stream)
    def get_well_info_from_las_file(self, las_file_object) -> dict:
 
        self.lasio_object = self.get_lasio_object_from_las_file_object(las_file_object)
        well_info = self._extract_well_info_lasio_obj()

        well_logs_info = self._extract_well_logs_info_from_lasio_obj()
        

        well_info = self._create_well_info(well_logs_info, well_info)
  
        return well_info
    def _extract_well_info_lasio_obj(self) -> dict:
        well_info = {}
        for well_model_attr, lasio_well_attr_mnemonic in LASIO_WELL_SECTION_INFO_MNEMONICS_BY_MODEL_ATTR.items():
            well_attr_lasio_header_item = self.lasio_object.sections["Well"].get(lasio_well_attr_mnemonic, None)
            if well_attr_lasio_header_item is not None:
           
                well_attr_value = well_attr_lasio_header_item.value
                well_info[well_model_attr] = well_attr_value
        return well_info

    def _create_well_info(self, well_logs_info: List[dict], well_attrs_info: dict):
        well_info = {"well_logs": well_logs_info}
        for well_info_key, well_info_value in well_attrs_info.items():
            well_info[well_info_key] = well_info_value
        return well_info


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