import requests

from pytest_bdd import scenario, scenarios, parsers, given, when, then

EXTRA_TYPES = {
  'Number': int,
}

CONVERTERS = {
  'phrase': str
}

# Shared variables
DUCKDUCKGO_API = 'https://api.duckduckgo.com'

# Scenarios
scenarios('../features/service.feature', example_converters = CONVERTERS)


@given('the DuckDuckGo API is queried with "<phrase>"')
def ddg_response(phrase):
  params = {'q': phrase, 'format': 'json'}
  response = requests.get(DUCKDUCKGO_API, params=params)
  return response


@then('the response contains the results for "<phrase>"')
def ddg_response_contents(ddg_response, phrase):
  assert phrase.lower() == ddg_response.json()['Heading'].lower()


@then(parsers.parse('the response status code is "{code:d}"'))
def basket_has_total(ddg_response, code):
  assert ddg_response.status_code == code