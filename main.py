# stdlib
import logging

from time import sleep

# third party
import click

from tqdm import tqdm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S"
)


@click.command()
@click.option(
    "--path",
    default="https://google.com",
    prompt="A path to a given page",
    help="Url to the page to work on",
)
@click.option("--wait", default=5, help="How long to wait before each refresh")
@click.option(
    "--hold",
    default=20,
    help="How long you have to interact after changes in DOM are found in minutes",
)
def interact(path, wait, hold):
    driver = webdriver.Firefox()
    driver.get(path)
    driver.implicitly_wait(20)
    original = driver.page_source
    while driver.page_source == original:
        sleep(wait)
        driver.refresh()

    logging.info("Page change found!")
    logging.info(f"You have {hold} minutes to do what you need to before shutdown")
    for s in tqdm(range(hold), desc="Minutes spent", unit="min", postfix={}):
        sleep(60)

    driver.quit()


if __name__ == "__main__":
    interact()
