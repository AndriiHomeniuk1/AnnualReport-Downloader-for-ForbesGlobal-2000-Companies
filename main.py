import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)


def download_pdf(company_name: str, rank: str, year: int = 2023) -> None:
    name_for_url = company_name.replace(" ", "+")
    browser.get(
        f"https://www.google.com/search?q={name_for_url}+annual+report"
        f"+{year}+filetype:pdf+&start=0"
    )

    first_result_link = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.g:nth-child(1) a')
        )
    )

    first_result_link.click()

    # To get the current URL of the window with the PDF file
    pdf_link = browser.current_url

    response = requests.get(pdf_link)
    if response.status_code == 200:
        with open(f'reports/{rank}. {company_name}_{year}.pdf', 'wb') as pdf_file:
            pdf_file.write(response.content)
        print("The PDF file has been successfully downloaded.")
    else:
        print("Error downloading the PDF file.")


def download_multiple_pdfs(file_name: str, year: int = 2023) -> None:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        for element in data:
            try:
                download_pdf(element['name'], element['rank'], year=year)
                print(f"Downloaded {element['rank']}. {element['name']}")
            except Exception as e:
                with open("errors.txt", "a") as errors_file:
                    errors_file.write(f"{element['rank']}. {element['name']}: {str(e)}\n")
                print(f"Error downloading {element['rank']}. {element['name']}: {str(e)}")

    browser.quit()

if __name__ == "__main__":
    download_multiple_pdfs("for_download_forbes.json", year=2023)
