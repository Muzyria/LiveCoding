import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver = webdriver.Chrome(options=options)
    # request.cls.driver = driver
    request.cls.it_is_my_test = "ITS MY TEST"
    yield driver
    driver.quit()
