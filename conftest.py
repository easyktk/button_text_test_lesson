import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print(f"\nstart chrome browser for test...lang:{user_language}")
        if user_language:
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            browser = webdriver.Chrome(options=options)
        else:
            browser = webdriver.Chrome()

    elif browser_name == "firefox":
        if user_language:
            options_firefox = OptionsFirefox()
            options_firefox.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def get_language(request):
    user_language = request.config.getoption("language")
    return user_language
