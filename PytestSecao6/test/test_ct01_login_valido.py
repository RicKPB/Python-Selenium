# --------- IMPORTS -------------
import pytest

from selenium.webdriver.common.by import By

import conftest


# -----------------------------


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_login_valido(self):
        driver = conftest.driver
        # -------- MAPEAMENTO DE ELEMENTOS -----------------
        username = driver.find_element(By.XPATH, '//input[@id="user-name"]')
        password = driver.find_element(By.XPATH, '//input[@id="password"]')
        buttonLogin = driver.find_element(By.XPATH, '//input[@id="login-button"]')
        # --------------------------------------------------

        # -------- REALIZACAO DE LOGIN ---------------------
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        buttonLogin.click()
        # --------------------------------------------------

        # -------- VERIFICACAO DE LOGIN --------------------
        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
        # --------------------------------------------------
