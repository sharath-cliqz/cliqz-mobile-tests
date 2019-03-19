from selenium.webdriver import Safari


def getWebpageList():
    driver = Safari()
    try:
        driver.get("https://www.alexa.com/topsites/countries/DE")
        cells = driver.find_elements_by_class_name("td DescriptionCell")
        with open("weblist.txt", "w") as fp:
            for cell in cells:
                webpage = cell.find_element_by_tag_name("a").text
                fp.write("http://{}\n".format(webpage))
    except Exception as e:
        print(e)
    finally:
        driver.quit()

def getLinksFromFile():
    list = []
    with open("weblist.txt", "r") as fp:
        for line in fp.readlines():
            list.append(line.strip("\n"))
    return list


if __name__ == "__main__":
    getWebpageList()