import os
import pandas as pd

# Header mapping for CSV types
CSV_HEADERS = {
    "activities.csv": ["ID", "ACTIVITY", "PARENT_ID"],
    "countries.csv": ["CONTINENT", "COUNTRY_NAME", "ISO2_CODE"],
    "employees.csv": ["EMPLOYEE_NAME", "EMPLOYEE_EMAIL", "JOB_NAME", "JOB_TYPE", "COMPANY_NAME", "TAX_ID",
                      "ACTIVITY", "ACTIVITY_PARENT", "ACTIVITY_GRAND_PARENT", "LAT", "LNG", "CONTINENT", "COUNTRY_NAME", "ISO2_CODE"],
    "jobs.csv": ["ID", "JOB", "JOB_TYPE_ID"],
    "job_types.csv": ["ID", "JOB_TYPE"],
    "companies.csv": ["ID", "COMPANY_NAME", "ACTIVITY_ID", "LAT", "LNG", "COUNTRY_ID"]
}

ACTIVITIES_CSV = "Activities.csv"
EMPLOYEE_CSV = "Employee.csv"
COUNTRIES_CSV = "Countries.csv"
JOBS_CSV = "Jobs.csv"
JOB_TYPES_CSV = "Job_types.csv"
COMPANIES_CSV = "Companies.csv"
    
def normalize_employee_data(employees_file, output_path):
    """
    Normalize the employee data into structured tables: Employee, Job, Job Type, Company, Activities, Countries.
    Args:
        employees_file (str): Path to the CSV file containing processed employee data.
        output_path (str): Path to the directory where reports will be saved.
    """
    # Read the employees CSV file into a DataFrame
    df = pd.read_csv(employees_file, sep=",")

    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Extract relevant columns for each normalized table

    if os.path.exists(os.path.join(output_path, EMPLOYEE_CSV)):
        print(f"File {EMPLOYEE_CSV} already exists. Skipping.")
    else:
        # 1. Employee Table
        employee_df = df[['EMPLOYEE_NAME', 'EMPLOYEE_EMAIL', 'COMPANY_NAME', 'JOB_NAME']].drop_duplicates().reset_index(drop=True)
        employee_df['ID'] = employee_df.index + 1  # Generate unique IDs starting from 1
        employee_df = employee_df.rename(columns={
            'EMPLOYEE_NAME': 'EMPLOYEE_NAME',
            'EMPLOYEE_EMAIL': 'EMPLOYEE_EMAIL',
            'COMPANY_NAME': 'COMPANY_ID',
            'JOB_NAME': 'JOB_ID'
        })
        employee_df = employee_df[['ID', 'EMPLOYEE_NAME', 'EMPLOYEE_EMAIL', 'COMPANY_ID', 'JOB_ID']]
        employee_df.to_csv(os.path.join(output_path, 'Employee.csv'), index=False)


    if os.path.exists(os.path.join(output_path, JOBS_CSV)):
        print(f"File {JOBS_CSV} already exists. Skipping.")
    else:
        # 2. Job Table
        job_df = df[['JOB_NAME', 'JOB_TYPE']].drop_duplicates().reset_index(drop=True)
        job_df['ID'] = job_df.index + 1  # Generate unique IDs starting from 1
        job_df = job_df.rename(columns={
            'JOB_NAME': 'JOB',
            'JOB_TYPE': 'JOB_TYPE_ID'
        })
        job_df = job_df[['ID', 'JOB', 'JOB_TYPE_ID']]
        job_df.to_csv(os.path.join(output_path, 'Job.csv'), index=False)



    if os.path.exists(os.path.join(output_path, JOB_TYPES_CSV)):
        print(f"File {JOB_TYPES_CSV} already exists. Skipping.")
    else:
        # 3. Job Type Table
        job_type_df = df[['JOB_TYPE']].drop_duplicates().reset_index(drop=True)
        job_type_df['ID'] = job_type_df.index + 1  # Generate unique IDs starting from 1
        job_type_df = job_type_df.rename(columns={'JOB_TYPE': 'JOB_TYPE'})
        job_type_df = job_type_df[['ID', 'JOB_TYPE']]
        job_type_df.to_csv(os.path.join(output_path, 'Job_Type.csv'), index=False)


    if os.path.exists(os.path.join(output_path, COMPANIES_CSV)):
        print(f"File {COMPANIES_CSV} already exists. Skipping.")
    else:
        # 4. Company Table
        company_df = df[['COMPANY_NAME', 'LAT', 'LNG', 'COUNTRY_NAME']].drop_duplicates().reset_index(drop=True)
        company_df['ID'] = company_df.index + 1  # Generate unique IDs starting from 1
        company_df = company_df.rename(columns={
            'COMPANY_NAME': 'COMPANY_NAME',
            'LAT': 'LAT',
            'LNG': 'LNG',
            'COUNTRY_NAME': 'COUNTRY_ID'
        })
        company_df = company_df[['ID', 'COMPANY_NAME', 'LAT', 'LNG', 'COUNTRY_ID']]
        company_df.to_csv(os.path.join(output_path, 'Company.csv'), index=False)

    if os.path.exists(os.path.join(output_path, ACTIVITIES_CSV)):
        print(f"File {ACTIVITIES_CSV} already exists. Skipping.")
    else:
        # 5. Activities Table
        activities_df = df[['ACTIVITY', 'ACTIVITY_PARENT']].drop_duplicates().reset_index(drop=True)
        activities_df['ID'] = activities_df.index + 1  # Generate unique IDs starting from 1
        activities_df = activities_df.rename(columns={
            'ACTIVITY': 'ACTIVITY',
            'ACTIVITY_PARENT': 'PARENT_ID'
        })
        activities_df = activities_df[['ID', 'ACTIVITY', 'PARENT_ID']]
        activities_df.to_csv(os.path.join(output_path, 'Activities.csv'), index=False)



    if os.path.exists(os.path.join(output_path, COUNTRIES_CSV)):
        print(f"File {COUNTRIES_CSV} already exists. Skipping.")
    else:
        # 6. Countries Table
        countries_df = df[['COUNTRY_NAME', 'CONTINENT']].drop_duplicates().reset_index(drop=True)
        countries_df['ID'] = countries_df.index + 1  # Generate unique IDs starting from 1
        countries_df = countries_df.rename(columns={
            'COUNTRY_NAME': 'COUNTRY_NAME',
            'CONTINENT': 'CONTINENT_ID'
        })
        countries_df = countries_df[['ID', 'COUNTRY_NAME', 'CONTINENT_ID']]
        countries_df.to_csv(os.path.join(output_path, 'Countries.csv'), index=False)

    print("Data has been successfully normalized and saved.")

def generate_reports(employees_file, output_path):
    """
    Generates reports based on the processed data.

    Args:
        employees_file (str): Path to the CSV file containing processed employee data.
        output_path (str): Path to the directory where reports will be saved.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    df = pd.read_csv(employees_file, sep=",")
    
    # **Report 1**: Amount of employees by country, company (Ordered by country and company)
    employees_by_country_company = df.groupby(['COUNTRY_NAME', 'COMPANY_NAME']).size().reset_index(name='EMPLOYEES_COUNT')
    employees_by_country_company = employees_by_country_company.sort_values(by=['COUNTRY_NAME', 'COMPANY_NAME'])
    
    # Write to CSV
    employees_by_country_company.to_csv(os.path.join(output_path, 'AMOUNT_EMPLOYEES_BY_COMPANY_COUNTRY.csv'), index=False, sep=";")
    
    # **Report 2**: Amount of companies by activities (Ordered by grand parent activity, parent activity, and activity)
    # Assuming we have company information in the 'COMPANY_NAME' and activities info in 'ACTIVITY_GRAND_PARENT', 'ACTIVITY_PARENT', 'ACTIVITY'
    companies_by_activity = df.groupby(['ACTIVITY_GRAND_PARENT', 'ACTIVITY_PARENT', 'ACTIVITY']).size().reset_index(name='COMPANIES_COUNT')
    
    # Add a row for the parent activities sum (grand parent activity + parent activity without specific activity)
    parent_activity_sum = df.groupby(['ACTIVITY_GRAND_PARENT', 'ACTIVITY_PARENT']).size().reset_index(name='COMPANIES_COUNT')
    parent_activity_sum['ACTIVITY'] = '-'
    parent_activity_sum = parent_activity_sum[['ACTIVITY_GRAND_PARENT', 'ACTIVITY_PARENT', 'ACTIVITY', 'COMPANIES_COUNT']]
    
    # Combine both results (companies by activity and parent activity sum)
    final_activity_report = pd.concat([companies_by_activity, parent_activity_sum], ignore_index=True)
    final_activity_report = final_activity_report.sort_values(by=['ACTIVITY_GRAND_PARENT', 'ACTIVITY_PARENT', 'ACTIVITY'])
    
    # Write to CSV
    final_activity_report.to_csv(os.path.join(output_path, 'AMOUNT_COMPANIES_BY_ACTIVITIES.csv'), index=False, sep=";")

    print("Reports generated successfully.")





