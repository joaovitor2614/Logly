import uuid
import ast
import json
from app.controllers.well import WellController
from app.controllers.welldata import WellDataController
import numpy as np
from typing import Dict
import numexpr as ne

class NameExtractor(ast.NodeVisitor):
    def __init__(self):
        self.names = set()

    def visit_Name(self, node):
        self.names.add(node.id)

    def visit_Call(self, node):
        # Do not treat function names as variables
        for arg in node.args:
            self.visit(arg)


class WellCalculatorHandler:
    def __init__(self, request, well_id: str, formula: str):
        self.well_id = well_id
        self.formula = formula
        self.well_log_data_name_mapping: Dict[str, np.array] = {}
        self.well_controller = WellController(request)
        self.well_data_controller = WellDataController(request)
        self.build_logs_data_mapping()

    

    def get_well_calculator_formula_well_logs_names(self):
        tree = ast.parse(self.formula, mode="eval")
        extractor = NameExtractor()
        extractor.visit(tree)
        return extractor.names


    def build_logs_data_mapping(self):
        formula_well_logs_names = self.get_well_calculator_formula_well_logs_names()
        well_db_obj = self.well_controller.get_well_by_id(self.well_id)
    
        for well_log_name in formula_well_logs_names:
    
            well_log_db_obj = next(
                (
                    wl
                    for wl in well_db_obj["welllogs"]
                    if wl["name"] == well_log_name
                ),
                None,
            )
            well_log_data = self.well_data_controller.get_well_log_data_by_id(
                self.well_id, well_log_db_obj["_id"], destringyfy=True
            )
            self.well_log_data_name_mapping[well_log_name] = well_log_data

    def run(self):
        calculated_well_log_data = ne.evaluate(self.formula, local_dict=self.well_log_data_name_mapping)
        return calculated_well_log_data
      



