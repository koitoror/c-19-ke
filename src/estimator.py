def estimator(data):
    # print(data)
    reportedCases = data['reportedCases']
    currentlyInfected = reportedCases * 10
    severeImpact = reportedCases * 50
    # severeImpact = currentlyInfected * 5
    requestedTime = data['timeToElapse']//3


    data1 = {
        'data' : data,
        'impact': {
          'currentlyInfected': currentlyInfected,
          'infectionsByRequestedTime': currentlyInfected * int(2 ** requestedTime)
        },
        'severeImpact': {
          'currentlyInfected': severeImpact,
          'infectionsByRequestedTime' : severeImpact * int(2 ** requestedTime)
        }
    }

    print(data1)
    return data1
