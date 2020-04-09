def estimator(data):
    print(data)
    reportedCases = data['reportedCases']
    currentlyInfected = reportedCases * 10
    severeImpact = reportedCases * 50
    # severeImpact = currentlyInfected * 5
    requestedTime = data['timeToElapse']/3


    data1 = {
        'data' : data,
        'impact': {
          'currentlyInfected': currentlyInfected,
          'infectionsByRequestedTime': currentlyInfected * (2 ** requestedTime)
        },
        'severeImpact': {
          'severeImpact': severeImpact,
          'currentlyInfected': currentlyInfected,
          'infectionsByRequestedTime' : severeImpact * (2 ** requestedTime)
        }
    }

    print(data1)
    return data1
