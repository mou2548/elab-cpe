manchesterResult = input("What's the result of Manchester city's match? ")
liverpoolResult = input("What's the result of Liverpool's match? ")

if manchesterResult == liverpoolResult:
    manchesterMargin = input("What is the margin that Manchester city won by? ")
    liverpoolMargin = input("What is the margin that Liverpool won by? ")
    if manchesterMargin == liverpoolMargin:
        playoff = input("Which team won the play-off match?(Manchester city/Liverpool) ")
        if playoff == "Manchester city":
            result = 'manchester'
        else:
            result = 'liverpool'
    elif manchesterMargin > liverpoolMargin:
        result = 'manchester'
    else:
        result = 'liverpool'
elif manchesterResult == 'won':
    result = 'manchester'
else:
    result = 'liverpool'

if result == 'manchester':
    print("Manchester city is the champion of Premier League.")
else:
    print("Liverpool is the champion of Premier League.")
