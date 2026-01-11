import uuid
import ast
from ..controllers.well import WellController
from ..controllers.welldata import WellDataController
import numpy as np
from typing import Dict
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
    def __init__(self, well_id: uuid.UUID, formula: str):
        self.well_id = well_id
        self.formula = formula
        self.well_log_data_name_mapping: Dict[str, np.array]
        self.well_controller = WellController()
        self.well_data_controller = WellDataController()
        self.build_logs_data_mapping()


    def get_well_calculator_formula_well_logs_names(self):
        tree = ast.parse(self.formula, mode="eval")
        extractor = NameExtractor()
        extractor.visit(tree)
        return extractor.names


    def build_logs_data_mapping(self):
        formula_well_logs_names = self.get_well_calculator_formula_well_logs_names()
        for well_log_name in formula_well_logs_names:
         well_log_db_obj = self.well_controller.get_well_by_name("WELL1")
         well_log_data = self.well_data_controller.get_well_log_data_by_id(
             self.well_id, well_log_db_obj["_id"]
         )
         self.well_log_data_name_mapping[well_log_name] = well_log_data


