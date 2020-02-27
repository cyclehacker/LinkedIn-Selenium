# Skeleton LinkedIn crawler

Build using Python 3.6.9, Selenium 3.141.0 and Parsel 1.5.2

This script uses Selenium to first login to LinkedIn, then search LinkedIn using a search query and Google.

Add your LinkedIn Username/Password in parameters.py and change the Google search query as required.

Currently configured to loop through the Google results and return:

- Name
- Job Title
- Location
- Schools
- LinkedIn Profile Url

Outputs to CSV.

# Future updates:

- Expand range of data crawled to include all available data.
- Write tests to Travis
- Add user input to customise google search query to be crawled.

