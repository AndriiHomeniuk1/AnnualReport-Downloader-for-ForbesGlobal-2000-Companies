from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time


# topic_search = "JPMorgan Chase"
# year_search = "2023"
# topic_search = topic_search.replace(" ", "+")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)



# elements = browser.get(
#         f"https://www.google.com/search?q={company_name}+annual+report+{year}+filetype:pdf+&start=0"
#     )


def download_pdf(company_name: str, rank: int, year: int = 2023) -> None:
    name_for_url = company_name.replace(" ", "+")

    elements = browser.get(
        f"https://www.google.com/search?q={name_for_url}+annual+report+{year}+filetype:pdf+&start=0"
    )

    # Очікування появи посилання
    first_result_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g:nth-child(1) a'))
    )

    # Клік на посилання
    first_result_link.click()

    # Перехід на нову вкладку
    time.sleep(10)
    browser.switch_to.window(browser.window_handles[-1])

    pdf_link = browser.current_url  # Отримати поточну URL-адресу вікна з PDF-файлом


    response = requests.get(pdf_link)
    if response.status_code == 200:
        with open(f"reports\\{rank}. {company_name}_{year}.pdf", "wb") as pdf_file:
            pdf_file.write(response.content)
        print("PDF-файл завантажено успішно.")
    else:
        print("Помилка завантаження PDF-файлу.")


if __name__ == "__main__":
    download_pdf("JPMorgan Chase", 1)











