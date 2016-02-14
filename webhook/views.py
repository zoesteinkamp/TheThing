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
    GREETINGS = ['Hello', 'Hi', 'Hi im travis', 'hi', 'hey']
    GO_TO = ['I want to go to seattle', 'id like to go to seattle', 'Seattle', 'seattle']
    FROM_LOCATION = ['Denver', 'from denver', 'denver']
    DATES = ['I want to go March 13 to March 16', 'March 13 to March 16', 'march 13 to march 16']
    BUDGET_TICKETS = ['500', '500 dollars', '$500']
    FLIGHT_SELECTION = ['I want the first', 'one', 'first flight']
    ROOM = ['my own place', 'my own', 'private room']
    ROOM_BUDGET = ['200 a night', '200', '200 dollars']
    ROOM_SELECTION = ['the first', 'number one', 'first place']
    if request.GET.get('message') in GREETINGS:
        response = "Hi I'm Watson. Im here to help your family or buisness plan their vacation fast! Where would you like to go?"
    elif request.GET.get('message') in GO_TO:
        response = "I will gladly book you a trip for Seattle. Where are you flying from?"
    elif request.GET.get('message') in FROM_LOCATION:
        response = "What dates would you like to go?"
    elif request.GET.get('message') in DATES:
        response = "Alright, what is your budget for round trip tickets?"
    elif request.GET.get('message') in BUDGET_TICKETS:
        response = " Alright I found these flights Which one would you like me to book?"
    elif request.GET.get('message') in FLIGHT_SELECTION:
        response = "Fantastic! Lets get you a airbnb place as well! Would you like to have your own place or private room?"
    elif request.GET.get('message') in ROOM:
        response = "Okay what is your budget a night for that private place?"
    elif request.GET.get('message') in ROOM_BUDGET:
        response = "Great, here are the top two rated airbnb private rentals in Seattle for 200 dollars a night for those dates. Please pick your prefered one. "
    elif request.GET.get('message') in ROOM_SELECTION:
        response = "Alright I have your flight and place booked. Would you like some reservations for resturaunts in the area?"
    # elif request.GET.get('message') == "I would":
    #     pass
    # elif request.GET.get('message') in LOCATIONS:
    #     results = IterateMainPage(request.GET.get('message'), NUMBER_OF_AIRBNB_PAGES_TO_SCRAPE)
    #     detailed_results = iterateDetail(results)
    #     parsed_results = parse_airbnb_detialed_results(detailed_results)
    #     response = generate_location_response(parsed_results)
    else:
        response = "Sorry, I don't understand."
    return HttpResponse(response)
