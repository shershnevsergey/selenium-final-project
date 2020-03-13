import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    selected_language = request.config.getoption('language')

    options = Options()
    # options.add_argument("--headless")
    options.add_experimental_option('prefs', {'intl.accept_languages': selected_language})

    print("\nstart chrome browser with {} language for test..".format(selected_language))
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
