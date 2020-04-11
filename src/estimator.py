from math import floor, ceil, trunc


def requestedDays(data):
    if data['periodType'] == 'days':
        requestedTimeD = data['timeToElapse']
        return requestedTimeD
    if data['periodType'] == 'weeks':
        requestedTimeW = data['timeToElapse'] * 7
        return requestedTimeW
    if data['periodType'] == 'months':
        requestedTimeM = data['timeToElapse'] * 30
        return requestedTimeM


def truncate(n):
    return n // 1


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

    casesForICUByRequestedTimeC = int(.05 * infectionsByRequestedTimeC)
    casesForICUByRequestedTimeS = int(.05 * infectionsByRequestedTimeS)
    casesForVentilatorsByRequestedTimeC = int( .02 * infectionsByRequestedTimeC)
    casesForVentilatorsByRequestedTimeS = int( .02 * infectionsByRequestedTimeS)

    avgDailyIncomeInUSD = data['region']['avgDailyIncomeInUSD']
    avgDailyIncomePopulation = data['region']['avgDailyIncomePopulation']
    dollarsInFlightC = infectionsByRequestedTimeC * avgDailyIncomePopulation * avgDailyIncomeInUSD * days
    dollarsInFlightS = infectionsByRequestedTimeS * avgDailyIncomePopulation * avgDailyIncomeInUSD * days

    #     def round_down(n, decimals=0):
    #         #   multiplier = 10 ** decimals
    #         #   return floor(n * multiplier) / multiplier
    #         return n // 1

    #     def truncate(n, decimals=0):
    #         multiplier = 10 ** decimals
    #         x = floor(n * multiplier) / multiplier
    #         return round_down(x)

    #     def truncate(num, digits=0):
    #         sp = str(num).split('.')
    #         x = '.'.join([sp[0], sp[1][:digits]])
    #         #   return float(x)
    #         return x

    #     def truncate(n):
    #         return n // 1

    data = {
        'data': data,
        'impact': {
            'currentlyInfected': currentlyInfected,
            'infectionsByRequestedTime': infectionsByRequestedTimeC,
            'severeCasesByRequestedTime': severeCasesByRequestedTimeC,
            'hospitalBedsByRequestedTime': hospitalBedsByRequestedTimeC,
            'casesForICUByRequestedTime': truncate(casesForICUByRequestedTimeC),
            'casesForVentilatorsByRequestedTime': truncate(casesForVentilatorsByRequestedTimeC),
            'dollarsInFlight': truncate(dollarsInFlightC)
            },
        'severeImpact': {
            'currentlyInfected': severeImpact,
            'infectionsByRequestedTime': infectionsByRequestedTimeS,
            'severeCasesByRequestedTime': severeCasesByRequestedTimeS,
            'hospitalBedsByRequestedTime': hospitalBedsByRequestedTimeS,
            'casesForICUByRequestedTime': truncate(casesForICUByRequestedTimeS),
            'casesForVentilatorsByRequestedTime': truncate(casesForVentilatorsByRequestedTimeS),
            'dollarsInFlight': truncate(dollarsInFlightS)
            }
      }

    return data
