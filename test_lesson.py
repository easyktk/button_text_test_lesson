from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_buy_button(browser, get_language):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")))
    if language := get_language:
        lang_dict = {"es": "Añadir al carrito", "en": "Add to basket", "fr": "Ajouter au panier"}
        if language in lang_dict:
            assert lang_dict[language] == button.text, "Incorrect buy button text"
        else:
            assert button.text, "No buy button text"


