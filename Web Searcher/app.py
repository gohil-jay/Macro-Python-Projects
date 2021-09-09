from selenium import webdriver

search_string = input("Enter the URL or string : ")
search_string = search_string.replace(' ', '+')
n = int(input("Enter the number : "))

browser = webdriver.Chrome('chromedriver')

for i in range(n):
	matched_elements = browser.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))
  print(matched_elements)
