import argparse

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging

class FlatexBrowser:

    def __init__(self, port: int):
        self.logger = self.get_logger()
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
        self.logger.info(f"Verbinde zu Chrome-Browser auf Port {port} ...")
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_logger(self):
        log_format = (
            '[%(asctime)s] %(levelname)s\t%(name)s\t%(message)s')
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            handlers=[logging.StreamHandler()]
        )
        logger = logging.getLogger('flatex')
        return logger

    def download_documents(self):
        document_rows = self.driver.find_elements_by_xpath('//tr[starts-with(@id, "TID")]')
        self.logger.info(f"{len(document_rows)} Dokumente in der Liste gefunden. Starte Download ...")

        document_ids = []
        for document_row in document_rows:
            document_ids.append(document_row.get_property('id'))

        document_counter = 0
        for document_id in document_ids:
            document_counter += 1
            document_row = self.driver.find_element_by_xpath(f'//tr[@id="{document_id}"]')
            document_title = self.driver.find_element_by_xpath(f'//tr[@id="{document_id}"]//td[@class="C3 "]').text
            ActionChains(self.driver).move_to_element(document_row).perform()
            document_row.click()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            bt_download =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@id="download"]')))
            bt_download.click()
            self.logger.info(f"[{document_counter}/{len(document_ids)}]\t{document_title} - {self.driver.title}")
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(prog='flatex_documents_download_helper',
                                        description='Das Skript erlaubt es mittels per Selenium gesteuerten '
                                                    'Chrome-Browser PDF-Dokumente aus dem Dokumentenarchiv von '
                                                    'Flatex herunterzuladen.')
    my_parser.add_argument('Port',
                           metavar='port',
                           type=int,
                           help='Der Debugging-Port des Chrome-Browsers.')

    args = my_parser.parse_args()

    flatex_browser = FlatexBrowser(port=args.Port)
    flatex_browser.download_documents()