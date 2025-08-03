import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()  # Load environment variables from .env file for api keys

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))  # Initialize Apify client with the API token


# Function to fetch jobs from LinkedIn using the Apify client
def fetch_linkedin_jobs(search_query,location="India", rows=60):
    """
    Function to fetch jobs from LinkedIn using the Apify client.

    Args:
        search_query (str): The job search query.
        location (str): The location to search for jobs.
        rows (int): The number of job listings to return.

    Returns:
        list: A list of job listings.
    """
    run_input = {
        "searchQuery": search_query,
        "location": location,
        "rows": rows,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"],
        }
    }
    
    run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs  # Return the list of job listings


# Function to fetch jobs from Naukri using the Apify client
def fetch_naukri_jobs(search_query, location="India", rows=60):
    """
    Function to fetch jobs from Naukri using the Apify client.

    Args:
        search_query (str): The job search query.
        location (str): The location to search for jobs.
        rows (int): The number of job listings to return.

    Returns:
        list: A list of job listings.
    """
    run_input = {
        "keywords": search_query,
        "maxJobs": rows,
        "freshness": "all",
        "sortedBy": "relevance",
        "experience": "all",
        "location": location,
    }
    
    run = apify_client.actor("wsrn5gy5C4EDeYCcD").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs  # Return the list of job listings