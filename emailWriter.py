#variables below

#functions below
def questionEmail(yourName, otherName, assignmentName, issue):
    print('Dear ' + otherName)
    print("I have a question regarding the assignment called " + assignmentName + ". The thing is that this assignment " + issue + " and I would like inform you about that. " + "Thank you!")
    print("-" + yourName)

questionEmail('Alex','Mr. Smith', "Math practice 2", "still has a 5/10 score")