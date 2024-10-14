import boto3
import csv

csv_file_path = "test.csv"
table_name = "test-UserProducts"
db_table = boto3.resource('dynamodb',region_name='us-west-2').Table(table_name)
line_seperator = ','
#Print the table name to confirm access
print("**************************************Table Name*************************************************")
print("Table Name:", db_table)


def save_to_dynamodb(column_names, values):
    print("*************************************************************************************************")
    print("Column Names:",column_names)
    print("Record values:",values)
    print("*************************************************************************************************")
    # Create a dictionary to store the item with column names as keys
    #item = dict()
    item = {}
    for idx, column_name in enumerate(column_names):
        item[column_name] = values[idx]
        print(f"Index: {idx}, Column: {column_name}, Value: {values[idx]}")
          
    return db_table.put_item(
            Item=item
    )
    


# Read the CSV file and process it
with open(csv_file_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=line_seperator)
   # print ("reader.line_num",reader.line_num)
    # Get the header (first row)
    column_names = next(reader)
   # print("Column Names:", column_names)
   # print("reader.line_num",reader.line_num)

    # Process each subsequent row
    for values in reader:
        #print("reader.line_num",reader.line_num)
        #print("Record Values:", values)
        response = save_to_dynamodb(column_names, values)
        print("*************************************************************************************************")
        print("Saved Item:", response)

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("Item added successfully!")
            #print("*************************************************************************************************")
        else:
            print("Error adding item.")
            print("*********ERROOR*********ERROR*******************ERROR****************************ERROR***********")
