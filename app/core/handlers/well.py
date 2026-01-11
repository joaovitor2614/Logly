import lasio
from typing import List
import io
import numpy as np

LASIO_WELL_SECTION_INFO_MNEMONICS_BY_MODEL_ATTR = {
    "name": "WELL",
    "start": "STRT",
    "stop": "STOP",
    "company": "COMP"
}

REF_DEPTH_MNEMONICS = ["DEPTH", "MD"]

class WellHandler:
    def __init__(self):
        self.lasio_object: lasio.LASFile = None
    def _extract_well_info_from_las_file(self, las_file, is_pre_import: bool = False):  
        self.lasio_object = self.get_lasio_object_from_las_file_object(las_file)
        well_info = self._extract_well_info_lasio_obj()

        exclude_data = True if is_pre_import else False

        well_logs_info = self._extract_well_logs_info_from_lasio_obj(exclude_data)
        ref_depth_info = self._extract_ref_depth_info() if is_pre_import else None
        well_info = self._create_well_info(well_logs_info, well_info, ref_depth_info)
        return well_info




    def get_lasio_object_from_las_file_object(self, las_file_object):
        las_file_text_stream = io.TextIOWrapper(las_file_object.file, encoding="utf-8", errors="ignore")
        return lasio.read(las_file_text_stream)
    def get_well_info_from_las_file(self, las_file_object) -> dict:
        well_info = well_info = self._extract_well_info_from_las_file(las_file_object, is_pre_import=False)
  
        return well_info
    def get_pre_import_well_info_from_las_file_object(self, las_file_object):

        well_info = self._extract_well_info_from_las_file(las_file_object, is_pre_import=True)
        return well_info
    def _extract_well_info_lasio_obj(self) -> dict:
        """
        Extract well information from the LAS file object.

        Returns a dictionary containing well information.
        """
        well_info = {}
        for well_model_attr, lasio_well_attr_mnemonic in LASIO_WELL_SECTION_INFO_MNEMONICS_BY_MODEL_ATTR.items():
            well_attr_lasio_header_item = self.lasio_object.sections["Well"].get(lasio_well_attr_mnemonic, None)
            if well_attr_lasio_header_item is not None:
           
                well_attr_value = well_attr_lasio_header_item.value
                well_info[well_model_attr] = well_attr_value
        return well_info

    def _create_well_info(self, well_logs_info: List[dict], well_attrs_info: dict, *args):
        """
        Create a dictionary containing well information from the given well logs and well attributes information.

        Args:
            well_logs_info (List[dict]): A list of dictionaries containing well log information.
            well_attrs_info (dict): A dictionary containing well attributes information.
            *args: Additional dictionaries containing well information to be added to the returned dictionary.

        Returns:
            dict: A dictionary containing well information.
        """
        well_info = {"well_logs": well_logs_info}
        for well_info_key, well_info_value in well_attrs_info.items():
            well_info[well_info_key] = well_info_value

        for arg in args:
            if isinstance(arg, dict):
                well_info.update(arg)
        return well_info
    def _create_well_info_dict(self, curve_info, curve_data, exclude_data: bool):

        return {
            "name": curve_info.mnemonic,
            "unit": curve_info.unit,
            "descr": curve_info.descr,
            "min": np.nanmin(curve_data),
            "max": np.nanmax(curve_data),
            "data": [] if exclude_data else curve_data
        }
       


    def _extract_well_logs_info_from_lasio_obj(self, exclude_data: bool = False):
        curves_section = self.lasio_object.sections["Curves"]
        well_logs_info = []
        for i in range(len(curves_section)):
            curve_info = curves_section[i]
            curve_data = self.lasio_object.data[:, i]
            well_logs_info.append(self._create_well_info_dict(curve_info, curve_data, exclude_data))
        print('well_logs_info', well_logs_info)
        return well_logs_info
    
    def _extract_ref_depth_info(self):
        curves_section = self.lasio_object.sections["Curves"]
        ref_depth_info = {"name": "", "min_value": 0.00, "max_value": 0.00}
        for i in range(len(curves_section)):
            curve_info = curves_section[i]
     
            if curve_info.mnemonic.strip().upper() in REF_DEPTH_MNEMONICS:
                ref_depth_info["name"] = curve_info.mnemonic
                ref_depth_info["min_value"] = self.lasio_object.data[:, i].min()
                ref_depth_info["max_value"] = self.lasio_object.data[:, i].max()
                break

        return ref_depth_info

        
well_handler = WellHandler()