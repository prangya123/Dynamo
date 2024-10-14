import csv

csv_file_path = "test.csv"
line_seperator = ','


def create_cognito_user(user_name, email):
    print("*************************************************************************************************")
    print("user_name is:", user_name)
    print("email is:", email)

    # Construct the AWS CLI command to create the Cognito user
    command = f"""
aws cognito-idp admin-create-user --user-pool-id us-west-2_e8cq1XOGY --username {user_name} --user-attributes Name=email,Value={email} --desired-delivery-mediums "EMAIL" --message-action SUPPRESS  
    """
    print(command)
    print(f"Created Item: {user_name}")
    print("*************************************************************************************************")


# Read the CSV file and process it
with open(csv_file_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)  # Automatically maps the CSV columns to a dictionary
    print("Column Names:", reader.fieldnames)  # Print column names for reference

    # Process each subsequent row
    for row in reader:
        user_name = row['user_name']
        email = row['email']

        # Call the function to create a Cognito user
        create_cognito_user(user_name, email)
