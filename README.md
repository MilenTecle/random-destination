# The Random Destination Generator

The Random Destination Generator is an interactive text-based application,
that will let the user travel plan in fun a creative way. The application
provides the user with a randomized city based on continent preference.

The live link can be found here - [The Random Destination Generator](https://random-destination-generator-3e9ef050a262.herokuapp.com/)


## Contents


- [Site Owner Goals](#site-owner-goals)
- [User Stories](#user-stories)
  - [First time user](#first-time-user)

- [Design](#design)
  - [Images](#images)
  - [Colours](#colours)
  - [Fonts](#fonts)
  - [Flowchart](#flowchart)

- [Features](#features)
  - [Features left to implement](#features-left-to-implement)

- [Technologies used](#technologies-used)

- [Languages](#languages)
- [Frameworks, Libraries and Programs](#frameworks-libraries-programs)
- [Modules](#modules)
- [Known bugs](#know-bugs)
- [Testing](#testing)

- [Validator Testing](#validator-testing)
  - [Accessibility](#accessibility)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [User Stories Testing](#user-stories-testing)
- [Friends and Family](#friends-and-family)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [Github](#github)
- [Credits](#credits)
  - [Code](#code)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)



 ## Site Owner Goals

The Random Destination Generator is an application designed to simplify travel
planning. To discover new travel destinations and to inspire spontaneus solo
adventures or with a group of friends.



## User Stories
- ### First time user
  - As a first time user I want to understand the purpose of the application
  easily.
  - As a first time user I want a simple and intuitive interface for my travel
  inputs.
  - As a first time user I want clear instructions and guidance should I enter
  a wrongful input.
  - As a first time user I want the application to provide me with a random
  destination based on my preference.
  - As a first time user I want the option to add accommodation and
  transportation to help me plan my entire trip.
  - As a first time user I want the option to re-choose a city if that is not
  what I expected.
  - As a first time user I want the option to see the travel details
  displayed in a summary after I have made all my choices.
  - As a first time user I want the option to restart the application to make
  other choices, or to the exit the program.



- ### Returning User
  - As a returning user I can quickly make another choice so I can get another
   random destination generated wihout delay.
  - As a returning user I want to see my previous inputs so I can reuse input
  or avoid making the same input.


## Design

### Images
ASCII images are used to further enhance the purpose and to make the first
look appealing to the user.

### Colours
The colours are imported from termcolor. Red colour is used when input is
invalid for clarity to the user. The travel details summary is in yellow to
add a contrast.


## Flowchart
The flowchart was produced via Lucid charts.

[Random Destination Flowchart](images/flowchart/random-destination-generator.png)


## Features



- ### The Start Page
  -


- ### The Application
  -


### Features left to implement
  - Export the travel details to a pdf for the user to keep.
  - Extend the options for accommodation to actual names of hotels and hostels
  stored in the google spreadsheet.
  - Extend the options for transportation to car rental companies and
  different types of bus transfer stored in the google spreadsheet.


## Technologies used

## Languages
  - Python


  ## Frameworks, Libraries and Programs
   - [Am I Responsive](https://ui.dev/amiresponsive) - Was used to ensure that
    the website is responsive on diffrerent devices.
   - [Gitpod](https://gitpod.io/) - Was the Codespace used for this project.
   - [Git](https://git-scm.com/) - Git was used for version control by using
   the Gitpod terminal to commit and then push to Github.
   - [Github](https://github.com/) - Is where the projects code is stored
   after being pushed.
   - [Heroku]
   - [Responsinator](http://www.responsinator.com/) - Was also used to ensure
   that the website is responsive on diffrerent devices.

  ## Modules
  - Gspread was installed to open the spreadsheet that holds the random
  destination data.
  - Google.oauth2 module was installed to provide credentials.
  - Datetime module was installed to handle the date input from the user.
  - Termcolor was installed to change the text and image colour.
  - Tabulate module was installed to display the travel details in a table.
  - Random module was imported to randomize a city.
  - Time module was installed to add delay before printing text.
  - from PIL import Image

## Known bugs
No known bugs.

## Testing

### Validator Testing

 - ### Python
  - No errors were returned when running the Javascript code through [Python](https://jshint.com/)
    - [Python result]()

 - ### Accessibility
  - The site achieved a Lighthouse accessibility score of 100%, a confirmation
  that the fonts and colours chosen are accessible and easy to read.
    - [Lighthouse result](assets/test-results/lighthouse-result.png)


### Application Testing



### Links Testing
 - All navigation links on the site has been tested manually to ensure that
 they are working, and takes the user to the right page.
 - All the buttons were tested to ensure that the the links are working
 correctly.
 - The social media links were tested separately to make sure they function,
 and opens in a new tab.


### Browser Testing
 - The Website was tested on Microsoft Edge, Google Chrome, Firefox and Safari browsers and no issues were noted.

### Device Testing
  - The website was tested and on different devices such as: Iphone 8, Iphone mini 12 and Pro, Samsung Galaxy S21, Samsung Galaxy Tab S6 lite, Ipad Mini, Laptop and Desktop to see that the website is responsive on different devices. Chrome developer tools was used to test and to check the responsivness on multiple devices.
  - I also used the following websites to test the responsivness:
  - [Responsinator](http://www.responsinator.com/?url=https%3A%2F%2Fmilentecle.github.io%2Fhuman-body-quiz%2F)
  - [Am I responsive](https://ui.dev/amiresponsive?url=https://milentecle.github.io/human-body-quiz/)

### User Stories Testing
   #### First time user
 1. As a first time user I understand the purpose of the application
  easily with the clear introductury messages and image.
 2. As a first time user the interface for my travel inputs are intuitive with
 clear labeld input fields.
 3. As a first time user I get clear instructions and guidance should I enter
  a wrongful input.
 4. As a first time user I recieve a random destination along with the price,
 based on my continent input.
 5. As a first time user I can choose to add accommodation and transportation,
 and to choose different accommodations and
 transportation options.
 6. As a first time user I can re-choose a city if that is not
  what I expected or wanted.
 7. As a first time user I can see the travel details
  displayed in a summary after I have made all my choices.
 8. As a first time user I want the option to restart the application to make
  other choices, or to he exit the program.



   #### Returning user
 1. As a returning user I can make another choice quickly so I can get another
  random destination generated wihout delay.
 2. As a returning user I can see my previous inputs so I can reuse input
  or avoid making the same input.



  ## Friends and Family
   - Family members and friends were asked to test the website for bugs and overall experience.

## Deployment

## Heroku

## Github
The project was deployed using Github pages with the following steps:
1. Go to the repository on Github.com.
2. Select 'Settings' towards the top of the page.
3. Select 'Pages' from the left menu bar.
4. Under 'Source', choose the preselected 'Branch' from the dropdown menu and then select the main branch.
5. Deployment is confirmed after a couple of minutes by the following message "Your site is published at" and there is a link to the web address.

The live link can be found here - [The Random Destination Generator](https://random-destination-generator-3e9ef050a262.herokuapp.com/)

## Credits

### Code



### Content
The content were written by the developer.

### Media
Images were taken from:
 - [Shutterstock](https://www.shutterstock.com/)


### Acknowledgements
- Antonio, my mentor, for guiding med throughout the project with important suggestions to improve the quiz and funcionality.
- To my husband and family, for all the support and patience throughout this project.

