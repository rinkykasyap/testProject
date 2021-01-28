import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ZestMoney.Pages.TripAdvisor import TripAdvisor
from ZestMoney.Locators.locators import Locators
from selenium.webdriver.support.ui import  Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TripAdvisorReview(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="E:/testProject/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.get("https://www.tripadvisor.in/")
        cls.driver.set_page_load_timeout(10)

    def test_review(self):
        driver = self.driver
        driver_page = TripAdvisor(driver)
        actual_name = driver_page.club_search("Club Mahindra")
        print(actual_name)

        #Switch window by selecting the clubname
        driver.window_handles[0]
        driver.find_element_by_xpath(Locators.result_selection).click()
        window_after = driver.window_handles[1]
        driver.switch_to_window(window_after)
        expected_name = driver.find_element_by_xpath(Locators.result_expected).text
        self.assertEqual(actual_name,expected_name, "Review is not for the correct hotel")
        driver.implicitly_wait(10)

        ##Switch window to write review
        driver.find_element_by_xpath(Locators.review_page).click()
        window_review = driver.window_handles[2]
        driver.switch_to_window(window_review)
        review_head = driver.find_element_by_xpath(Locators.review_head_verify).text
        self.assertEqual(actual_name, review_head, "Review heading is not for the correct hotel")

        #Select 5 rating and write reviews
        driver_page.bubble_rating()
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_DOWN)

        driver.find_element_by_xpath(Locators.review_type)
        sel = Select(driver.find_element_by_id(Locators.review_date))
        sel.select_by_index(2)

        html.send_keys(Keys.END)
        driver.implicitly_wait(10)
        driver_page.question_bubbles()

        html.send_keys(Keys.END)
        driver.find_element_by_id("noFraud").click()

        driver.find_element_by_id(Locators.submit)

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.close()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="E:/SeleniumPrac/reports"))




