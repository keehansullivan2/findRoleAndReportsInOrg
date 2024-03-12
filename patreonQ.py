ORG_CHART: dict = {
    'mark': {
        'jason': None,
        'jenny': {
            'tom': None,
            'rachel': {
                'peter': None,
                'jeff': {
                    'annie': None,
                    'andy': None,
                }
            }
        }
    },
    'john': None,
}
#example, for jenny, you should return ('manager', 2, 6)
#example: for johm, return ('IC', 0, 0)

####^^^^^^^^ this is the only thing you are given ^^^^^^^^####
#
#
#### Below is my solution / what i think they expected. Yes I believe they expected test cases.

def findPerson(person, root): ##returns [person, {} = reports]
	stck = []
	for i in root.keys():
		stck.append([i, root[i]])

	while len(stck) > 0:
		personAndReports = stck.pop()
		employee = personAndReports[0]
		reports = personAndReports[1]
		if employee == person:
			return [employee, reports]
		if reports:
			for report in reports.keys():
				stck.append([report, reports[report]])
		
def finddirectReports(person, org):
	if (findPerson(person, org)[1] == None):
		return 0
	return len(findPerson(person, ORG_CHART)[1])

def findTotalReports(person, org):
	total = 0
	total += finddirectReports(person, org)
	reports = findPerson(person, org)[1]
	if reports:
		for i in reports.keys():
			total+= findTotalReports(i, org)
	return total

def returnPerson(person, org):
	try: ## When asked about how to handle non-existing person, he said "how would you handle it"
		if finddirectReports(person, org) == 0:
			return ("IC", 0, 0)
		else:
			return ("manager", finddirectReports(person, org), findTotalReports(person, org))
	except:
		return "Person not in org"

test_findPerson_pass = findPerson('mark', ORG_CHART) == ['mark', {
        'jason': None,
        'jenny': {
            'tom': None,
            'rachel': {
                'peter': None,
                'jeff': {
                    'annie': None,
                    'andy': None,
                }
            }
        }
    }]
test_returnPerson_pass = returnPerson("jenny", ORG_CHART) == ("manager", 2, 6)
test_findDirectReports_pass = finddirectReports("rachel", ORG_CHART) == 2

print("test findPerson pass?: " + str(test_findPerson_pass))
print("test returnPerson pass?: " + str(test_returnPerson_pass))
print("test findDirectReports pass?: " + str(test_findDirectReports_pass))

