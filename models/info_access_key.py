class InfoAccessKey:
    
    def __init__(
            self,
            dayEmission: str,
            monthEmission: str,
            yearEmission: str,
            codDoc: str,
            rucBusiness: str,
            environment: str,
            establishment: str,
            pointEmission: str,
            sequential: str,
            randomNumber: str,
    ):
        self.dayEmission = dayEmission
        self.monthEmission = monthEmission
        self.yearEmission = yearEmission
        self.codDoc = codDoc
        self.rucBusiness = rucBusiness
        self.environment = environment
        self.establishment = establishment
        self.pointEmission = pointEmission
        self.sequential = sequential
        self.randomNumber = randomNumber

    def getDateComplete(self):
        return self.dayEmission + self.monthEmission + self.yearEmission

        