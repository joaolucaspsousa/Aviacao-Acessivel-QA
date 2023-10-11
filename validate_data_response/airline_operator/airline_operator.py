from airline_operator.airline_operator_dto import AirlineOperatorDto

class AirlineOperatorProcessor:
    def __init__(self, airline_operators):
        self.airline_operators = airline_operators

    def convert_response_to_dto(self, airline_operator):
        name = airline_operator['name']
        cnpj = airline_operator['cnpj']
        internationalCivilAviationOrganization = airline_operator['internationalCivilAviationOrganization']
        internationalAirTransportAssociation = airline_operator['internationalAirTransportAssociation']
        country = airline_operator['country']['name']
        focalName = airline_operator['focalName']
        phoneNumber = airline_operator['phoneNumber']
        email = airline_operator['email']

        return AirlineOperatorDto(name, cnpj, internationalCivilAviationOrganization, internationalAirTransportAssociation, country, focalName, phoneNumber, email)

    def pre_processor(self):
        airline_operators_modified = []

        for airline_operator in self.airline_operators['data']['operatorsCompanies']['data']:
            airline_operator_dto = self.convert_response_to_dto(airline_operator)
            airline_operators_modified.append(airline_operator_dto.__dict__)

        return airline_operators_modified