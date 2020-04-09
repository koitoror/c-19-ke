def estimator(data):
    # print(data)
    reportedCases = data['reportedCases']
    currentlyInfected = reportedCases * 10
    severeImpact = reportedCases * 50
    # severeImpact = currentlyInfected * 5
    # severeImpact.currentlyInfected = currentlyInfected
    requestedTime = (data['timeToElapse'])/3
    # # infectionsByRequestedTime = currentlyInfected * (2 ** requestedTime),
    # infectionsByRequestedTimeC : currentlyInfected * (2 ** requestedTime)
    # infectionsByRequestedTimeS : severeImpact * (2 ** requestedTime)
    infectionsByRequestedTime = {}

    
    impact = {
        currentlyInfected,
    }

    data1 = {
        data : data,
        impact: {
          currentlyInfected: currentlyInfected,
          infectionsByRequestedTime: currentlyInfected * (2 ** requestedTime)
        },
        severeImpact: {
          severeImpact: severeImpact,
          currentlyInfected: currentlyInfected,
          infectionsByRequestedTime : severeImpact * (2 ** requestedTime)
        }
    }

    return data1
