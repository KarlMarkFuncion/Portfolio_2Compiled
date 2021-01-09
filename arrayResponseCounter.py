# PROGRAM That counts responses from the given arrays

response01 = ('Articles for the lesson from google search results',
              'Knowledge and Educational websites (e.g. Brilliant, Khan Academy, etc.)',
              'Knowledge and Educational websites (e.g. Brilliant, Khan Academy, etc.)',
              'Knowledge and Educational websites (e.g. Brilliant, Khan Academy, etc.)',
              'Knowledge and Educational websites (e.g. Brilliant, Khan Academy, etc.)',
              'Asychronous learning and recorded lectures',
              'Asychronous learning and recorded lectures',
              'Synchronized learning sessions.',
              'Knowledge and Educational websites (e.g. Brilliant, Khan Academy, etc.)',
              'Synchronized learning sessions.',
              'Asychronous learning and recorded lectures',
              'Written lessons in hand-out modules (online and hardcopy)',
              'Knowledge and Educational websites (e.g. Brilliant, Khan Academy, etc.)',
              'Written lessons in hand-out modules (online and hardcopy)',
              'Knowledge and Educational websites (e.g. Brilliant, Khan Academy, etc.)',
              'Asychronous learning and recorded lectures',
              'Knowledge and Educational websites (e.g. Brilliant, Khan Academy, etc.)',
              'Articles for the lesson from google search results',
              'Articles for the lesson from google search results',
              'Asychronous learning and recorded lectures',
              'Knowledge and Educational websites (e.g. Brilliant, Khan Academy, etc.)',
              'Knowledge and Educational websites (e.g. Brilliant, Khan Academy, etc.)',
              'Knowledge and Educational websites (e.g. Brilliant, Khan Academy, etc.)',
              'Synchronized learning sessions.',)
response02 = (
    'Digital to-do lists ( MinimaList, etc. );Dedicated productivity applications (notion, evernote, etc.);Traditional notebooks and physical notes;Calendar apps ( Google Calendars )',
    'Digital to-do lists ( MinimaList, etc. )',
    'Digital to-do lists ( MinimaList, etc. );Dedicated productivity applications (notion, evernote, etc.);Traditional notebooks and physical notes;Calendar apps ( Google Calendars )',
    'Digital to-do lists ( MinimaList, etc. );Dedicated productivity applications (notion, evernote, etc.);Traditional notebooks and physical notes;Calendar apps ( Google Calendars )',
    'Traditional notebooks and physical notes',
    'Traditional notebooks and physical notes',
    'Calendar apps ( Google Calendars )',
    'Digital to-do lists ( MinimaList, etc. )',
    'Digital to-do lists ( MinimaList, etc. );Dedicated productivity applications (notion, evernote, etc.);Traditional notebooks and physical notes;Calendar apps ( Google Calendars )',
    'Digital to-do lists ( MinimaList, etc. )',
    'Digital to-do lists ( MinimaList, etc. );Calendar apps ( Google Calendars )',
    'Digital to-do lists ( MinimaList, etc. )',
    'Digital to-do lists ( MinimaList, etc. );Traditional notebooks and physical notes;Calendar apps ( Google Calendars )',
    'Digital to-do lists ( MinimaList, etc. )',
    'Dedicated productivity applications (notion, evernote, etc.)',
    'Digital to-do lists ( MinimaList, etc. )',
    'Dedicated productivity applications (notion, evernote, etc.)',
    'Digital to-do lists ( MinimaList, etc. )',
    'none',
    'Traditional notebooks and physical notes',
    'Digital to-do lists ( MinimaList, etc. );Traditional notebooks and physical notes',
    'Digital to-do lists ( MinimaList, etc. )',
    'Digital to-do lists ( MinimaList, etc. );Dedicated productivity applications (notion, evernote, etc.);Traditional notebooks and physical notes;Calendar apps ( Google Calendars )',
    'Digital to-do lists ( MinimaList, etc. );Traditional notebooks and physical notes;Calendar apps ( Google Calendars )')
response04 = ("Blended Learning",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "Continue Online Classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes",
              "If Possible, I'd Like to return to normal classes")
responses03 = ('Possibly asking for less work to the teachers',
               'Improving discipline through willpower',
               'Improving discipline through willpower',
               'Improving discipline through routinizations',
               'Improving discipline through willpower',
               'Improving discipline through routinizations',
               'Improving discipline through willpower',
               'Improving discipline through willpower',
               'Improving discipline through routinizations',
               'Improving discipline through willpower',
               'Possibly asking for less work to the teachers',
               'Organizing my schedule more',
               'Improving discipline through willpower',
               'Possibly asking for less work to the teachers',
               'Organizing my schedule more',
               'Possibly asking for less work to the teachers',
               'Improving discipline through routinizations',
               'Organizing my schedule more',
               'Improving discipline through willpower',
               'Improving discipline through willpower',
               'Improving discipline through willpower',
               'Asking help from others to alleviate the burdens of school',
               'Improving discipline through willpower',
               'Improving discipline through willpower')


def responseSorter01(responses):
    # Responses for 2nd set of questions
    arts = 0
    webs = 0
    asyncL = 0
    syncL = 0
    modls = 0

    for responses in responses:
        if responses.startswith('As'):
            asyncL = asyncL + 1
        elif responses.startswith('K'):
            webs = webs + 1
        elif responses.startswith('Ar'):
            arts = arts + 1
        elif responses.startswith("Wr"):
            modls = modls + 1
        elif responses.startswith("Sy"):
            syncL = modls + 1

    print('Articles from google: ', arts, '\n Knowledge websites: ', webs, '\nAsyncronous learning: ',
          asyncL, '\nSyncronous Learning: ', syncL, '\nWritten module lessons: ', modls)


def responseSorter02(responses):
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0
    res5 = 0

    for responses in responses:
        if responses:
            if 'willpower' in responses:
                res1 = res1 + 1
            elif 'routinizations' in responses:
                res2 = res2 + 1
        elif responses.startswith('Or'):
            res3 = res3 + 1
        elif responses.startswith('As'):
            res4 = res4 + 1
        elif responses.startswith('Po'):
            res5 = res5 + 1

    print("ImprWill / ImprRout / Organize / Asking / Possibly")
    print(res1, ' / ', res2, ' / ', res3, ' / ', res4, ' / ', res5)


def responseSorter03(responses):
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0
    res5 = 0

    for responses in responses:
        if responses.startswith('I'):
            if 'willpower' in responses:
                res1 = res1 + 1
            elif 'routinizations' in responses:
                res2 = res2 + 1
        elif responses.startswith('Or'):
            res3 = res3 + 1
        elif responses.startswith('As'):
            res4 = res4 + 1
        elif responses.startswith('Po'):
            res5 = res5 + 1

    print("ImprWill / ImprRout / Organize / Asking / Possibly")
    print(res1, ' / ', res2, ' / ', res3, ' / ', res4, ' / ', res5)


def responseSorter04(responses):
    # Variables for counting the responses
    blenLearn = 0
    ifPossible = 0
    contOnline = 0
    for items in responses:
        if items == "If Possible, I'd Like to return to normal classes":
            ifPossible = ifPossible + 1
        elif items == "Continue Online Classes":
            contOnline = contOnline + 1
        elif items == "Blended Learning":
            blenLearn = blenLearn + 1
    print("If Possible, I'd Like to return to normal classes: ", ifPossible, "\n", "Continue Online Classes: ",
          contOnline, "\n",
          "Blended Learning: ", blenLearn)


print('|||SORTED 1|||')
responseSorter01(response01)
print("")
print("")
print('|||SORTED 3|||')
responseSorter03(responses03)
print("")
print("")
print('|||SORTED 4|||')
responseSorter04(response04)
