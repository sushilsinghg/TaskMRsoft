
# event_finder_app/views.py
from django.shortcuts import render
from .forms import EventSearchForm
from .models import UserPreferences
import requests

def event_search(request):
    if request.method == 'POST':
        form = EventSearchForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            interests = form.cleaned_data['interests']

            # Save user preferences to the database
            UserPreferences.objects.create(location=location, interests=interests)

            # Call a function to retrieve events based on user input
            events = get_events(location, interests)

            return render(request, 'event_finder_app/results.html', {'events': events})

    else:
        form = EventSearchForm()

    return render(request, 'event_finder_app/search.html', {'form': form})


def get_events(location, interests):
    # Use Eventbrite API to get events based on location and interests
    # Update the URL and parameters based on Eventbrite API documentation
    eventbrite_url = 'https://www.eventbriteapi.com/v3/events/search/'
    eventbrite_api_key = 'RFERLDODOWLN3FH4L4WA'

    params = {
        'location.address': location,
        'q': interests,
        'token': eventbrite_api_key,
    }

    response = requests.get(eventbrite_url, params=params)
    data = response.json()

    # Extract and return relevant event information
    events = []
    for event in data.get('events', []):
        events.append({
            'name': event['name']['text'],
            'url': event['url'],
            'start_time': event['start']['local'],
        })

    return events
# event_finder_app/views.py
# ... (previous code)

def get_events(location, interests):
    # Use Eventbrite API to get events based on location and interests
    # Update the URL and parameters based on Eventbrite API documentation
    eventbrite_url = 'https://www.eventbriteapi.com/v3/events/search/'
    eventbrite_api_key = 'RFERLDODOWLN3FH4L4WA'

    params = {
        'location.address': location,
        'q': interests,
        'token': eventbrite_api_key,
    }

    response = requests.get(eventbrite_url, params=params)
    data = response.json()

    # Extract and return relevant event information
    events = []
    for event in data.get('events', []):
        events.append({
            'name': event['name']['text'],
            'url': event['url'],
            'start_time': event['start']['local'],
        })

    return events
