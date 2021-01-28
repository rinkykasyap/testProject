class Locators():

    #TripAdvisor page objects

    search_text = "//input[@type='search' and @placeholder='Where to?']"
    result_text = "(//div[@class='result-title'])[1]"
    result_selection = "(//div[@class='rating-review-count'])[1]"
    result_expected = "//div[@class='_3e22blA6']/span"
    review_page = "//*[@id='COMMUNITYCONTENT']//a"
    review_head_verify = "//div[@class='locationInfo wrap']//h2"
    select_bubble = "//span[@id='bubble_rating']"
    review_title = "//*[@id='ReviewTitle']"
    review_text = "//*[@id='ReviewText']"
    review_type = "//*[@id='trip_type_table']/div[1]"
    review_date = "trip_date_month_year"
    submit = "SUBMIT"

