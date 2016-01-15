#building a better administrator - we can do this in python 2.x

admininput = raw_input('What did the bad student do?  ')

rulebroken = raw_input('What level rule did they break? (enter an integer from 1 to 292000000) ')

corporalpunishment = raw_input('does your state allow corporal punishment? (y/n) ')

punishment = 'unknown'

try:
    rulebroken = int(rulebroken)
except:
   print  'rules are rules, you didn\'t enter an integer so you\'re fired'


def rules():
    if rulebroken == 1:
        print 'detention for eternity because you committed the grave infraction of: ' + admininput
    elif rulebroken == 2:
        print 'suspenion for a week because you you committed the grave infraction of: ' + admininput
    elif rulebroken  >= 2:
        print 'expulsion because you you committed the grave infraction of: ' + admininput
    else:
        print 'I need time to consider this carefully' 


rules()
