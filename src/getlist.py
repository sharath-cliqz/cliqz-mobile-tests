from selenium.webdriver import Safari


def getList():
    list = []
    driver = Safari()
    try:
        driver.get("https://www.alexa.com/topsites/countries/DE")
        cells = driver.find_elements_by_class_name("td DescriptionCell")
        for cell in cells:
            webpage = cell.find_element_by_tag_name("a").text
            list.append(webpage)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
    return list
