from accessibility_practice.accessibility_practice_dto import AirlineOperatorDto

class AccessibilityPracticeProcessor:
    def __init__(self, accessibility_practices):
        self.accessibility_practices = accessibility_practices

    def get_scope(self, accessibility_practice):
        length_scopes = len(accessibility_practice['accessibilityPracticeTypeScopes'])

        if length_scopes > 1:
            return "BOTH_OPERATORS"
        return accessibility_practice['accessibilityPracticeTypeScopes'][0]['operatorType']

    def get_level(self, desired_level, accessibility_practice_levels):
        for current_level in accessibility_practice_levels:
            if current_level['level'] == desired_level:
                return current_level['description']
        return None

    def convert_response_to_dto(self, accessibility_practice):
        practice_code = accessibility_practice['practiceCode']
        dimension = accessibility_practice['dimensionGroup']['dimension']['name']
        group = accessibility_practice['dimensionGroup']['name']
        scope = self.get_scope(accessibility_practice)
        coverage = accessibility_practice['accessibilityPracticeTypeScopes'][0]['operatorScope']
        show_to_passenger = accessibility_practice['showToPassenger']
        alias_name_to_passenger = accessibility_practice['aliasNameToPassenger']
        name = accessibility_practice['name']
        description = accessibility_practice['description']
        dispensable_by = accessibility_practice['dispensableBy']
        prescriptive = accessibility_practice['prescriptive']
        level1 = self.get_level(1, accessibility_practice['accessibilityPracticeLevels'])
        level2 = self.get_level(2, accessibility_practice['accessibilityPracticeLevels'])
        level3 = self.get_level(3, accessibility_practice['accessibilityPracticeLevels'])
        level4 = self.get_level(4, accessibility_practice['accessibilityPracticeLevels'])
        level5 = self.get_level(5, accessibility_practice['accessibilityPracticeLevels'])
        guidance = accessibility_practice['requireLegalGuidanceExternalAgency']
        references = accessibility_practice['legalPrescriptiveReferences']

        return AirlineOperatorDto(practice_code, dimension, group, scope, coverage, show_to_passenger, alias_name_to_passenger, name, description, dispensable_by, prescriptive, level1, level2, level3, level4, level5, guidance, references)

    def pre_processor(self):
        accessibility_practices_modified = []

        for accessibility_practice in self.accessibility_practices['data']['accessibilityPractices']:
            accessibility_practice_dto = self.convert_response_to_dto(accessibility_practice)
            accessibility_practices_modified.append(accessibility_practice_dto.__dict__)

        return accessibility_practices_modified