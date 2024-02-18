from selenium import webdriver

def main():
    driver = webdriver.Chrome()
    driver.get("https://proghub.ru/")
    btn_element = driver.find_element_by_class_name("btn-cyan")
    print(btn_element)
if __name__=="__main__":
    main()