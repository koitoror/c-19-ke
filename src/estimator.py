from math import floor

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
    days = requestedDays(data)
    requestedTimeSet = days // 3
    infectionsByRequestedTimeC = float(currentlyInfected * 2 ** requestedTimeSet)
    infectionsByRequestedTimeS = float(severeImpact * 2 ** requestedTimeSet)

    #     population = data['population']
    totalHospitalBeds = data['totalHospitalBeds']
    severeCasesByRequestedTimeC = float(.15 * infectionsByRequestedTimeC)
    severeCasesByRequestedTimeS = float(.15 * infectionsByRequestedTimeS)
    expectedHospitalBeds = float(.35 * totalHospitalBeds)
    hospitalBedsByRequestedTimeC = int(expectedHospitalBeds - severeCasesByRequestedTimeC)
    hospitalBedsByRequestedTimeS = int(expectedHospitalBeds - severeCasesByRequestedTimeS)

    casesForICUByRequestedTimeC = float(.05 * infectionsByRequestedTimeC)
    casesForICUByRequestedTimeS = float(.05 * infectionsByRequestedTimeS)
    casesForVentilatorsByRequestedTimeC = float(.02 * infectionsByRequestedTimeC)
    casesForVentilatorsByRequestedTimeS = float(.02 * infectionsByRequestedTimeS)

    avgDailyIncomeInUSD = data['region']['avgDailyIncomeInUSD']
    avgDailyIncomePopulation = data['region']['avgDailyIncomePopulation']
    dollarsInFlightC = infectionsByRequestedTimeC * avgDailyIncomePopulation * avgDailyIncomeInUSD * days
    dollarsInFlightS = infectionsByRequestedTimeS * avgDailyIncomePopulation * avgDailyIncomeInUSD * days

    def round_up(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier
    
    def truncate(n, decimals=1):
        multiplier = 10 ** decimals
        x = floor(n * multiplier) / multiplier
        return round_up(x)

    data = {
        'data' : data,
        'impact': {
          'currentlyInfected': currentlyInfected,
          'infectionsByRequestedTime': infectionsByRequestedTimeC,
          'severeCasesByRequestedTime' : severeCasesByRequestedTimeC,
          'hospitalBedsByRequestedTime' : hospitalBedsByRequestedTimeC,
          'casesForICUByRequestedTime' : casesForICUByRequestedTimeC,
          'casesForVentilatorsByRequestedTime' : casesForVentilatorsByRequestedTimeC,
          'dollarsInFlight' : truncate(dollarsInFlightC)
        },
        'severeImpact': {
          'currentlyInfected': severeImpact,
          'infectionsByRequestedTime' : infectionsByRequestedTimeS,
          'severeCasesByRequestedTime' : severeCasesByRequestedTimeS,
          'hospitalBedsByRequestedTime' : hospitalBedsByRequestedTimeS,
          'casesForICUByRequestedTime' : casesForICUByRequestedTimeS,
          'casesForVentilatorsByRequestedTime' : casesForVentilatorsByRequestedTimeS,
          'dollarsInFlight' : truncate(dollarsInFlightS)
        }
    }

    return data
