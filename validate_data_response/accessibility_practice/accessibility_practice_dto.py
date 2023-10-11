
class AirlineOperatorDto:
    def __init__(self, practice_code, dimension, group, scope, coverage, name, description, dispensable_by, prescriptive, level1, level2, level3, level4, level5, guidance, references):
        self.practice_code = practice_code
        self.dimension = dimension
        self.group = group
        self.scope = scope
        self.coverage = coverage
        self.name = name
        self.description = description
        self.dispensable_by = dispensable_by
        self.prescriptive = prescriptive
        self.level1 = level1
        self.level2 = level2
        self.level3 = level3
        self.level4 = level4
        self.level5 = level5
        self.guidance = guidance
        self.references = references