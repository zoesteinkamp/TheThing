from scrapper import IterateMainPage, iterateDetail, writeToCSV

NUMBER_OF_PAGES = 1
results_for_san_francisco = IterateMainPage('San Francisco--CA', NUMBER_OF_PAGES)
detailed_results = iterateDetail(results_for_san_francisco)
print detailed_results
# writeToCSV(detailed_results, 'san_francisco.csv')
