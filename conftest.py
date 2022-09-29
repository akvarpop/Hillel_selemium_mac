import pytest
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
#options.add_argument(f"user-agent={useragent.cache}")
#options.add_argument(f"user-agent={useragent.random}")


@pytest.fixture(scope='session', autouse=True)
def driver():
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )
    driver.maximize_window()
    yield driver
    driver.quit()


#command_executor = 'http://localhost:4444/wd/hub

""" Код для запуска с ПК  """

# @pytest.fixture(scope='session', autouse=True)
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     driver.quit()

"""
docker run --rm -it -p 4444:4444 -p 7900:7900 --shm-size 2g selenium/standalone-chrome:beta
Перед запуском docker pull selenium/standalone-chrome-debug:3.141
docker run -d --name selenium_hillel -p 4444:4444 -p 5900:5900 selenium/standalone-chrome-debug
docker rm selenium_chrome
docker stop selenium_chrome
docker rm --force selenium_chrome
--platform linux/amd64
pull selenium/standalone-chrome-debug:3.141
docker run --platform=arm64 -it drone/drone-runner-docker:1.8-linux-arm64
docker run --rm -it -p 4444:4444 -p 7900:7900 --shm-size 2g selenium/standalone-chrome:beta
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" --platform=linux/amd64 selenium/standalone-chrome:4.1.0-20211209
docker pull selenium/standalone-chrome-debug
docker run -d -p 4444:4444 -p 5900:5900 --platform=linux/amd64 selenium/standalone-chrome-debug:3.141.59-mercury

"""
