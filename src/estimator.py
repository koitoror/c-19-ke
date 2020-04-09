from math import ceil

def requestedDays(data):
    if data['periodType'] == 'days':
          requestedTime = data['timeToElapse']
          return requestedTime
    elif data['periodType'] == 'weeks':
          requestedTime = data['timeToElapse'] * 7
          return requestedTime
    elif data['periodType'] == 'months':
          requestedTime = data['timeToElapse'] * 30
          return requestedTime

def estimator(data):
    reportedCases = data['reportedCases']
    currentlyInfected = reportedCases * 10
    # severeImpact = reportedCases * 50
    severeImpact = currentlyInfected * 5
    requestedTimeSet = ceil(requestedDays(data) / 3)

    data = {
        'data' : data,
        'impact': {
          'currentlyInfected': currentlyInfected,
          'infectionsByRequestedTime': float(currentlyInfected * 2 ** requestedTimeSet)
        },
        'severeImpact': {
          'currentlyInfected': severeImpact,
          'infectionsByRequestedTime' : float(severeImpact * 2 ** requestedTimeSet)
        }
    }

    return data
