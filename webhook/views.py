from django.http import HttpResponse
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from app.scrapper import IterateMainPage, iterateDetail


def parse_airbnb_detialed_results(results):
    parsed_response = []
    for result in results:
        parsed_response.append({
            'link': 'https://www.airbnb.com/rooms/%s' % result.get('ListingID'),
            'price': result.get('Price', 'Unknown')
        })
    return parsed_response


def generate_location_response(parsed_results):
    EXTRA_CHARS = 2
    response = ['Here are the results for airbnb:']
    for result in parsed_results:
        response.append('%s for $%s a night, ' % (result['link'], result['price']))
    response = ' '.join(response)
    return response[:len(response) - EXTRA_CHARS]


@parser_classes((JSONParser,))
def webhook(request, format=None):
    NUMBER_OF_AIRBNB_PAGES_TO_SCRAPE = 1
    LOCATIONS = ['San Francisco--CA', 'Gainesville--FL', 'Denver--CO']
    if request.GET.get('message') == 'Hello':
        response = "Hi I'm Watson"
    elif request.GET.get('message') in LOCATIONS:
        results = IterateMainPage(request.GET.get('message'), NUMBER_OF_AIRBNB_PAGES_TO_SCRAPE)
        detailed_results = iterateDetail(results)
        parsed_results = parse_airbnb_detialed_results(detailed_results)
        response = generate_location_response(parsed_results)
    else:
        response = "Sorry, I don't understand."
    return HttpResponse(response)
