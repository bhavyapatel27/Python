class Office:
    def __init__(self, name, technology, sallery, aggrement):
        self.name = name
        self.technology = technology
        self.sallery = sallery
        self.aggrement = aggrement

    def details(self):
        print(
            f"{self.name} is working on {self.technology} technology with the gross sallery of {self.sallery} thousand and working till {self.aggrement} year")


techrover = Office("Bhavya", "Python", 25, 2)
techrover.details()

meditab_name = input("Enter the name of employee:\n")
meditab_technology = input("Enter your work technology:\n")
meditab_sallery = input("Enter your gross sallery:\n")
meditab_aggrement = input("Enter the year of aggrement:\n")
meditab = Office(meditab_name, meditab_technology, meditab_sallery, meditab_aggrement)

meditab.details()
