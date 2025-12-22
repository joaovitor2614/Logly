import uuid



class WellCalculatorHandler:
    def __init__(self, well_id: uuid.UUID, formula: str):
        self.well_id = well_id
        self.formula = formula