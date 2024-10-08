import csv
from jobspy import scrape_jobs

search_terms = ["AS400", "RPGLE", "IBMi"]

unique_companies = {}

for term in search_terms:
    jobs = scrape_jobs(
        site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
        search_term=term,
        results_wanted=100,
        country_indeed='USA',
    )
    
    jobs_dict = jobs.to_dict(orient='records')

    for job in jobs_dict:
        company = job.get('company')
        date_posted = job.get('date_posted')
        company_url = job.get('company_url')
        
        if company not in unique_companies:
            unique_companies[company] = (date_posted, company_url)

csv_file_path = "IBMi_Companies.csv"

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['COMPANY', 'DATE POSTED', 'WEBSITE'])  # Header row

    for company, (date_posted, company_url) in unique_companies.items():
        writer.writerow([company, date_posted, company_url])  # Write job details
