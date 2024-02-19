# Geocoding ETL Project

## Overview
This project encompasses a comprehensive ETL (Extract, Transform, Load) pipeline designed for the enhancement and optimization of Boston crime incident data (https://data.boston.gov/dataset/crime-incident-reports-august-2015-to-date-source-new-system). The primary objective is to extract data from CSV files, transform it by filling in missing geocodes (latitude and longitude) using an external geocoding API, and finally load the enriched data into a SQL database for further analysis and querying.

## Process Flow
1. **Extract**: Data is extracted from multiple CSV files, each containing details of crime incidents, including location, date, and nature of the crime.
2. **Transform**:
    - Missing geocode information (latitude and longitude) for some incidents is identified.
    - The OpenCage Geocoder API is utilized to retrieve geocodes for addresses lacking this information.
    - Data cleansing operations are performed to ensure data quality, including the removal of duplicates and correction of anomalies.
3. **Load**: The cleaned and enriched data is loaded into an SQL database, making it readily available for reporting, analysis, and visualization.

![DALL·E 2024-02-19 18 19 31](https://github.com/hanush14/Geocode-ETL/assets/4678423/4a87b3e9-9c13-4860-a24a-414d990adbae)

## Technologies Used
- **Python**: The primary programming language for scripting the ETL process.
- **Pandas**: A Python library used for data manipulation and analysis.
- **SQLite**: A lightweight, disk-based database for testing the ETL process.
- **OpenCage Geocoder API**: An external API used for forward and reverse geocoding.

## Getting Started
To run this project on your local machine, follow these steps:
1. Clone the repository to your local machine.
2. Ensure Python and the required libraries (`pandas`, `requests`, `sqlalchemy`) are installed.
3. Place your CSV files in the designated directory.
4. Update the script with your OpenCage API key.
5. Execute the script to run the ETL process.

## Contributions
Contributions to this project are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
