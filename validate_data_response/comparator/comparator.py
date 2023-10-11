class Comparator:
    def __init__(self, json_df, csv_data, key_comparator):
        self.json_df = json_df
        self.csv_data = csv_data
        self.key_comparator = key_comparator
        return
    
    def check_existence_row_in_json(self, csv_row):
        # Criar uma lista de chaves do JSON
        json_keys = list(self.json_df[self.key_comparator])

        csv_key = csv_row[0]
        if csv_key not in json_keys:
            print(f"[ERROR 404]: The key '{csv_key}' from JSON was not found in CSV.\n")
            return False
        
        return True
    
    def check_existence_row_in_csv(self, json_row):
        # Criar uma lista de chaves do JSON
        csv_keys = list(self.csv_data[self.key_comparator])

        json_key = json_row[0]
        if json_key not in csv_keys:
            print(f"[ERROR 404]: The key '{json_key}' from CSV was not found in JSON.\n")
            return False
        
        return True

    def check_existence_of_lines(self):
        number_of_entities_not_found = 0

        for idx, (json_row, csv_row) in enumerate(zip(self.json_df.itertuples(index=False), self.csv_data.itertuples(index=False))):
            line_json_exists = self.check_existence_row_in_json(csv_row)
            line_csv_exists = self.check_existence_row_in_csv(json_row)

            if line_json_exists == False:
                self.csv_data.drop(idx, inplace=True)
                number_of_entities_not_found += 1

            if line_csv_exists == False:
                self.json_df.drop(idx, inplace=True)
                number_of_entities_not_found += 1

        return number_of_entities_not_found

    
    def compare_data(self):
        number_of_entities_not_found = self.check_existence_of_lines()
        number_of_failures = 0

        for idx, (json_row, csv_row) in enumerate(zip(self.json_df.itertuples(index=False), self.csv_data.itertuples(index=False))):
            for col, (json_value, csv_value) in enumerate(zip(json_row, csv_row)):            
                # Check if both values are not None
                if json_value is not None and csv_value is not None:
                    json_normalized_value = str(json_value).lower().strip().replace('\n', '').replace('\r', '')
                    csv_normalized_value = str(csv_value).lower().strip().replace('\n', '').replace('\r', '')

                    if json_normalized_value != csv_normalized_value:
                        print(f"[ERROR 400]: Row {idx + 2} | Key = {json_row[0]} | Column '{self.json_df.columns[col]}'. \n\nJSON = {json_normalized_value}\nCSVV = {csv_normalized_value}\n")
                        number_of_failures += 1

                # If both values are None, they are considered equal
                elif json_value is None and csv_value is None:
                    continue
                
                # If one of the values is None, it is considered a failure
                else:
                    print(f"[ERROR 400]: Row {idx + 2} | Key = {json_row[0]} | Column '{self.json_df.columns[col]}'. \n\nJSON = {json_value}\nCSVV = {csv_value}\n")
                    number_of_failures += 1

        print(f"\nAnalysis completed with {number_of_entities_not_found} entities not found and {number_of_failures} failures.\n")
