import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def fill_form_and_submit(self, link):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, """//label[text() = "First name*"]/following-sibling::input""").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, """[placeholder="Input your last name"]""").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("Smole@n.sk")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # ожидание, что в <h1> появится нужный текст
        WebDriverWait(self.browser, 5).until(
            EC.text_to_be_present_in_element(
                (By.TAG_NAME, "h1"),
                "Congratulations! You have successfully registered!"
            )
        )
        return self.browser.find_element(By.TAG_NAME, "h1").text

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.fill_form_and_submit(link)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.fill_form_and_submit(link)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()