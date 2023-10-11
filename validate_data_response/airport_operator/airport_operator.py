from airport_operator.airport_operator_dto import AirportOperatorDto

class AirportOperatorProcessor:
    def __init__(self, airport_operators):
        self.airport_operators = airport_operators

    def convert_response_to_dto(self, airport_operator):
        name = airport_operator['name']
        cnpj = airport_operator['cnpj']
        focalName = airport_operator['focalName']
        phoneNumber = airport_operator['phoneNumber']
        email = airport_operator['email']

        return AirportOperatorDto(name, cnpj, focalName, phoneNumber, email)

    def pre_processor(self):
        airport_operators_modified = []

        for airport_operator in self.airport_operators['data']['operatorsCompanies']['data']:
            airport_operator_dto = self.convert_response_to_dto(airport_operator)
            airport_operators_modified.append(airport_operator_dto.__dict__)

        return airport_operators_modified