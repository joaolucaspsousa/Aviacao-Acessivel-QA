from airport_unit.airport_unit_dto import AirportUnitDto

class AirportUnitProcessor:
    def __init__(self, airport_units):
        self.airport_units = airport_units

    def get_airport_operator(self, operatorCompanies):
        for operator in operatorCompanies:
            if operator['type'] == 'AIRPORT_OPERATOR':
                return operator['name']
            
        return False

    def convert_response_to_dto(self, airport_unit):
        name = airport_unit['name']
        airport_operator = self.get_airport_operator(airport_unit['operatorCompanies'])
        city = airport_unit['city']['name']
        uf = airport_unit['city']['state']['acronym']
        internationalCivilAviationOrganization = airport_unit['internationalCivilAviationOrganization']
        internationalAirTransportAssociation = airport_unit['internationalAirTransportAssociation']
        totalArea = airport_unit['totalArea']
        capacity = airport_unit['capacity']
        amountOfDomesticTerminals = airport_unit['amountOfDomesticTerminals']
        amountOfInternationalTerminals = airport_unit['amountOfInternationalTerminals']
        focalName = airport_unit['focalName']
        phoneNumber = airport_unit['phoneNumber']
        email = airport_unit['email']

        return AirportUnitDto(name, airport_operator, city, uf, internationalCivilAviationOrganization, internationalAirTransportAssociation, totalArea, capacity, amountOfDomesticTerminals, amountOfInternationalTerminals, focalName, phoneNumber, email)

       
    def pre_processor(self):
        airport_units_modified = []

        for airport_unit in self.airport_units['data']['airports']['data']:
            airport_unit_dto = self.convert_response_to_dto(airport_unit)
            airport_units_modified.append(airport_unit_dto.__dict__)

        return airport_units_modified