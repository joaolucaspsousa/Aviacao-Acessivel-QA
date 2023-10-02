from accessibility_practice.accessibility_practice import AccessibilityPracticeProcessor
import pandas as pd
import json

def compare_data(data_compair, json_df):
    number_of_failures = 0

    for idx, (json_row, csv_row) in enumerate(zip(json_df.itertuples(index=False), data_compair.itertuples(index=False))):
        for col, (json_value, csv_value) in enumerate(zip(json_row, csv_row)):            
            # Check if both values are not None
            if json_value is not None and csv_value is not None:
                json_normalized_value = str(json_value).lower().strip().replace('\n', '').replace('\r', '')
                csv_normalized_value = str(csv_value).lower().strip().replace('\n', '').replace('\r', '')

                if json_normalized_value != csv_normalized_value:
                    print(f"1: Row {idx + 1} | Code Practice = {json_row[0]} | Column '{json_df.columns[col]}'. \n\nJSON = {json_normalized_value}\nCSVV = {csv_normalized_value}\n")
                    number_of_failures += 1

            # If both values are None, they are considered equal
            elif json_value is None and csv_value is None:
                continue
            
            # If one of the values is None, it is considered a failure
            else:
                print(f"2: Row {idx + 1} | Code Practice = {json_row[0]} | Column '{json_df.columns[col]}'. \n\nJSON = {json_value}\nCSVV = {csv_value}\n")
                number_of_failures += 1

    return number_of_failures


def validate_data():
    csv_path = 'data/data_compair.csv'
    json_path = 'data/response_api.json'

    data_compair = pd.read_csv(csv_path)

    # Converting all NaN values to None
    data_compair = data_compair.where(pd.notna(data_compair), None)

    with open(json_path, encoding='utf-8') as json_file:
        accessibility_practices = json.load(json_file)

    accessibility_practices_processed = AccessibilityPracticeProcessor(accessibility_practices).pre_processor()

    # Write the Acessibility Practices Dto in a new file
    with open('data/response_api_modified.json', 'w', encoding='utf-8') as json_file:
        json.dump(accessibility_practices_processed, json_file, ensure_ascii=False, indent=2)

    # Converting JSON to a DataFrame
    json_df = pd.DataFrame(accessibility_practices_processed)   

    # Comparing data
    number_of_failures = compare_data(data_compair, json_df)
    print(f"\nAnalysis completed with {number_of_failures} failures.")

validate_data()