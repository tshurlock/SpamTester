# Overview

SpamTester allows you to test your websites defence against spamming of user input such as contact forms. It uses lists of random names and location details and a `random_person` class to generate a random person, these details can the be entered into form at target URL. 

# Disclaimer

You should only use SpamTester for testing your own website, or those that you have explicit permission to conduct spam testing on.

## Main

Searches for a defined list of elements, therefore needs to be tailored to target URL

## localVariables

Not in repo (gitignore), you will need a local file localVaraibles.py that contains
`target` = *your target URL*
`chromedriverPath` = *path to chromedriver*

## detailsVar

detailsVar.py contains a number of lists that can be used to generate random people.

## personClass

personClass.py contains `random_person` class, that generates a random person based on the available options stored in detailsVar.py

## proxies

18/06/2024- to be updated

# TODO
Write out to local csv file each time.
Configure attack- add variables for volume and frequency of entries






12/06/2024 Add more UK locations to detailsVar.py [locations]
12/06/2024 Add proxies
