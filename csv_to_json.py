import pandas as pd

# # Convert csv file to JSON file
# # Load the csv file
# # Define a list of tuples. Each tuple contains the dataframe name and the corresponding file path
# dataframes = [
#     ("df_industries", "Data\maps\industries.csv"),
#     ("df_skills", "Data\maps\skills.csv"),
#     ("df_benefits", "Data\job_details\benefits.csv"),
#     ("df_job_skills", "Data\job_details\job_skills.csv"),
#     ("df_salaries", "Data\job_details\salaries.csv"),
#     ("df_companies", "Data\company_details\companies.csv"),
#     ("df_company_industries", "Data\company_details\company_industries.csv"),
#     ("df_company_specialties", "Data\company_details\company_specialties.csv"),
#     ("df_employee_counts", "Data\company_details\employee_coutns.csv"),
# ]

# # Use a for loop to load each csv file and convert it to a json file
# for df_name, file_path in dataframes:
#     # Load the csv file
#     df = pd.read_csv(file_path)

#     # Convert the dataframe to json format
#     json_data = df.to_json(orient="records")

#     # Write the json data to a file
#     with open(f"\json_versions\{df_name}.json", "w") as json_file:
#         json_file.write(json_data)

# Convert the csv file to a json file
# Load the csv file

# dataframes = (["df_company_industries", "Data\company_details\company_industries.csv"],
#              ["df_company_specialties", "Data\company_details\company_specialties.csv"],
#              ["df_employee_counts", "Data\company_details\employee_counts.csv"],)

# # Load CSV file
# for df_name, file_path in dataframes:
#     df = pd.read_csv(file_path)
#     json_data = df.to_json(orient="records")
#     with open(f"Data\json_versions\{df_name}.json", "w") as json_file:
#         json_file.write(json_data)


df = pd.read_csv("Data\maps\industries.csv")

# Convert the dataframe to json format
json_data = df.to_json(orient="records")

# Write the json data to a file
with open("Data/json_versions/industries.json", "w") as json_file:
    json_file.write(json_data)