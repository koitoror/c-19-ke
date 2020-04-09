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
    severeImpact = currentlyInfected * 5
    requestedTimeSet = requestedDays(data) // 3
    infectionsByRequestedTimeC = float(currentlyInfected * 2 ** requestedTimeSet)
    infectionsByRequestedTimeS = float(severeImpact * 2 ** requestedTimeSet)
    totalHospitalBeds = data['totalHospitalBeds']
#     population = data['population']
    severeCasesByRequestedTime = .15 * infectionsByRequestedTimeS
    expectedHospitalBeds = .35 * totalHospitalBeds
    hospitalBedsByRequestedTime = expectedHospitalBeds - totalHospitalBeds

    data = {
        'data' : data,
        'impact': {
          'currentlyInfected': currentlyInfected,
          'infectionsByRequestedTime': infectionsByRequestedTimeC
        },
        'severeImpact': {
          'currentlyInfected': severeImpact,
          'infectionsByRequestedTime' : infectionsByRequestedTimeS,
          'severeCasesByRequestedTime' : .15 * infectionsByRequestedTimeS,
          'hospitalBedsByRequestedTime' : hospitalBedsByRequestedTime
        }
    }

    return data
