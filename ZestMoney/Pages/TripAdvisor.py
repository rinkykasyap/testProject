from ZestMoney.Locators.locators import Locators
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

#Add every action & objects
class TripAdvisor():

    def __init__(self,driver):
        self.driver = driver

        self.search_textbox = Locators.search_text
        self.result_text = Locators.result_text
        self.result_selection = Locators.result_selection
        self.review_page =  Locators.review_page
        self.review_head_verify = Locators.review_head_verify
        self.select_bubble = Locators.select_bubble
        self.review_title = Locators.review_title
        self.review_text = Locators.review_text

    def club_search(self, club_name):
        driver = self.driver
        driver.find_element_by_xpath(self.search_textbox).send_keys(club_name)
        driver.find_element_by_xpath(self.search_textbox).send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        actual_name = driver.find_element_by_xpath(self.result_text).text
        print(actual_name)
        return actual_name

    def bubble_rating(self):
        driver = self.driver
        driver.find_element_by_id("bubble_rating").click()
        driver.execute_script(
            'document.querySelector("#bubble_rating").setAttribute("class", "ui_bubble_rating fl bubble_50");')
        driver.find_element_by_xpath(self.review_title).send_keys("Very Nice Assignments")
        driver.find_element_by_xpath(self.review_text).send_keys("VeryGood"*200)

    def question_bubbles(self):
        driver = self.driver
        driver.execute_script(
            'document.querySelector("#qid12_bubbles").setAttribute("class", "answersBubbles ui_bubble_rating fl qid12 bubble_50");')
        driver.implicitly_wait(10)
        driver.execute_script(
            'document.querySelector("#qid13_bubbles").setAttribute("class", "answersBubbles ui_bubble_rating fl qid13 bubble_50");')
        driver.implicitly_wait(10)
        driver.execute_script(
            'document.querySelector("#qid14_bubbles").setAttribute("class", "answersBubbles ui_bubble_rating fl qid14 bubble_50");')
