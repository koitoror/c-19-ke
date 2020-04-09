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

    #     population = data['population']
    totalHospitalBeds = data['totalHospitalBeds']
    severeCasesByRequestedTime = float(.15 * infectionsByRequestedTimeS)
    expectedHospitalBeds = float(.35 * totalHospitalBeds)
    hospitalBedsByRequestedTime = int(expectedHospitalBeds - severeCasesByRequestedTime)

    data = {
        'data' : data,
        'impact': {
          'currentlyInfected': currentlyInfected,
          'infectionsByRequestedTime': infectionsByRequestedTimeC
        },
        'severeImpact': {
          'currentlyInfected': severeImpact,
          'infectionsByRequestedTime' : infectionsByRequestedTimeS,
          'severeCasesByRequestedTime' : severeCasesByRequestedTime,
          'hospitalBedsByRequestedTime' : hospitalBedsByRequestedTime
        }
    }

    return data
