from accessibility_practice.accessibility_practice import AccessibilityPracticeProcessor
from airline_operator.airline_operator import AirlineOperatorProcessor
from airport_operator.airport_operator import AirportOperatorProcessor
from comparator.comparator import Comparator

import pandas as pd
import json

CURRENT_ENTITY = 'airport_operator'
RELATIVE_PATH = CURRENT_ENTITY + '/data/'
CSV_PATH = RELATIVE_PATH + CURRENT_ENTITY + '.csv'
JSON_PATH = RELATIVE_PATH + CURRENT_ENTITY + '.json'

def main():
    # Read a CSV file
    csv_data = pd.read_csv(CSV_PATH)

    # Read a JSON file
    with open(JSON_PATH, encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    # Normalize data
    csv_data = normalize_csv_data(csv_data)
    json_data = normalize_json_data(json_data)

    Comparator(json_data, csv_data, KEY_COMPARATOR).compare_data()

    return


def normalize_csv_data(csv_data):
    # Converting all NaN values to None
    csv_data = csv_data.where(pd.notna(csv_data), None)

    # Converting all '-' values to None
    csv_data.replace('-', None, inplace=True)

    return csv_data

def normalize_json_data(json_data):
    json_data_processed = processor_json_based_entity(json_data, CURRENT_ENTITY)

    # Write the Acessibility Practices Dto in a new file
    with open(RELATIVE_PATH + 'response_api_modified.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data_processed, json_file, ensure_ascii=False, indent=2)

    # Converting JSON to a DataFrame
    json_df = pd.DataFrame(json_data_processed)

    return json_df

def processor_json_based_entity(json_data, entity):
    global KEY_COMPARATOR

    if entity == 'airline_operator':
        KEY_COMPARATOR = 'name'
        return AirlineOperatorProcessor(json_data).pre_processor()
    
    elif entity == 'airport_operator':
        KEY_COMPARATOR = 'name'
        return AirportOperatorProcessor(json_data).pre_processor()
    
    elif entity == 'accessibility_practice':
        KEY_COMPARATOR = 'practice_code'
        return AccessibilityPracticeProcessor(json_data).pre_processor()
    else:
        raise Exception("[ERROR 400] Invalid entity name")

main()