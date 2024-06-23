# Annual Report Downloader for Forbes Global 2000 Companies

This Python script automates the download of annual reports for companies listed in the Forbes Global 2000. It utilizes Selenium for web scraping to find and download PDF reports from Google search results.

## Features

- **Download Automation**: Downloads annual reports for Forbes Global 2000 companies for a specified year.
- **Error Handling**: Logs errors encountered during download to `errors.txt` for review.
- **Browser Management**: Manages browser sessions and closes them after downloads are complete.

## Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver

## Dependencies

- `requests`
- `selenium`
- `argparse`
- `json`
## Usage

1. **Setup Environment**:
   - Install Python 3.x from [python.org](https://www.python.org/downloads/)
   - Install required dependencies:
     ```bash
     pip install requests selenium
     ```

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `main.py`.
   - Run the script with optional arguments:
     ```bash
     python main.py --year 2023
     ```
     Replace `2023` with the desired year for the annual reports.

3. **Output**:
   - PDF reports will be downloaded into the `reports` directory with filenames formatted as `rank. company_name_year.pdf`.

## Existing Reports

- The `reports` directory contains a demonstration of 20 downloaded reports for companies in the Forbes Global 2000 list.

## Files

- `main.py`: Main script to download annual reports.
- `forbes_global_2000.json`: JSON file containing the list of Forbes Global 2000 companies.
- `custom_companies.json`: Custom JSON file where you can specify specific companies to download reports for.
- `errors.txt`: Log file for error messages encountered during downloads.
- `reports/`: Directory where downloaded PDF reports are saved.

## Notes

- Ensure you have a stable internet connection as the script relies on web scraping to fetch report links.
- Adjust timeout settings in `main.py` if needed (`WebDriverWait` duration).
