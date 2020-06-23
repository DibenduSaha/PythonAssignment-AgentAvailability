# Taking start_time, answer_time, resolved_time into consideration
class Issue: 
    def __init__(self, startTime, answerTime, resolvedTime):
        self.startTime = round(startTime, 2)
        self.answerTime = round(answerTime, 2)
        self.resolvedTime = round(resolvedTime, 2)
        self.timeToSolve = round(self.resolvedTime - self.answerTime, 2)
    def __repr__(self):
        return '{startTime: ' + str(self.startTime) + ', answerTime: ' + str(self.answerTime) + ', resolvedTime: ' + str(self.resolvedTime) + ', timeToSolve: '+str(self.timeToSolve) + '}' 


# Issues till date are stored here
listOfIssues = []

# Dummy Data
issue1 = Issue(1.0, 2.4, 2.5) # Issue requested at 1hr, solve time 0.5hr, wait time 1.3hr
listOfIssues.append(issue1) 
issue2 = Issue(1.5, 2.5, 3.1) # Issue requested at 1.5hr, solve time 0.4hr, wait time 1.1hr
listOfIssues.append(issue2)



def agentAvailability(newIssueStartTime, listOfIssues):
    agentBusyUpto = listOfIssues[-1].resolvedTime
    
    totalTime = 0
    for issue in listOfIssues:
        totalTime += issue.timeToSolve
    meanTimeToSolve = totalTime/len(listOfIssues)
    
    if newIssueStartTime < agentBusyUpto:
        endTime = agentBusyUpto + meanTimeToSolve
        listOfIssues.append(Issue(newIssueStartTime, agentBusyUpto, endTime))
        agentBusyUpto = endTime

    else:
        endTime = newIssueStartTime + meanTimeToSolve
        listOfIssues.append(Issue(newIssueStartTime, newIssueStartTime, endTime))
        agentBusyUpto = endTime
    print('Agent available at ',listOfIssues[-1].answerTime, 'hr', sep='')


# New Issue Generation
agentAvailability(1.6, listOfIssues)# Issue requested at 1.6hr (NEW REQUEST) O/P: 3.1hr(Time agent will be assigned)
agentAvailability(1.7, listOfIssues)
agentAvailability(20.1, listOfIssues)
agentAvailability(20.2, listOfIssues)
# for issue in listOfIssues:
#     print(issue.__repr__())




        
