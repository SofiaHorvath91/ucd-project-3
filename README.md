# Hogwarts Sorting App (UCD Project 3)
Get sorted & let the magic begin!

Ready to enter the Wizarding World and start your journey in Hogwarts School of Witchcraft and Wizardry?
There are four Houses in Hogwarts to host students with different personalities, founded by the four greatest witches and wizards of their time who built Hogwarts a thousand years ago. Students are sorted in their house by the Sorting Hat, the magical and sentient piece of headwear, which can see the hearth and mind of a person.
In the Hogwarts Sorting App, you have the possibility to discover all the four houses with the latest student numbers, see the popularity of the houses among students and get sorted in one or more of them in frame of the Sorting Ceremony by answering honestly the questions of the Sorting Hat.
If you are ready, meet the most magical Hat of all, participate in the Sorting Ceremony and find your own Hogwarts House!

![Responsive Layouts](/static/readme/responsive-design.PNG)

Deployed app on [Heroku](https://heroku.com) : https://cryptic-citadel-55296.herokuapp.com/ \
Technologies : Python with [Django](https://www.djangoproject.com/) + HTML + CSS \
Software : [PyCharm](https://www.jetbrains.com/pycharm/)

## UX
### 1. User stories
* Expectations as a user :
  * be able to navigate through the site easily through any device.
  * be able to go through the Sorting Ceremony and find their own Hogwarts house.
  * be able to export their Sorting Ceremony result to save it for themselves.
  * be able to get introduced to and to learn a little about all the Hogwarts houses.
  * be able to see the latest student statistics for all houses (number of students, popularity, selected vs sorted house rate etc.).
* Expectations as a site owner :
  * the site to be tastefully and creatively designed.
  * the visual content to be appealing and relevant.
  * the site to be clearly structured for easy navigation.
  * the Sorting Ceremony quiz works as intended and handle empty user inputs.
  * the users enjoy spending time with Sorting Quiz and learn about the Hogwarts Houses.
### 2. Strategy
* Purpose of Project
  * To promote the Wizarding World and it's hearth and center, the Hogwarts School.
  * To allow users having some fun and know themselves a bit better with the Sorting Ceremony.
  * To have users discover their own Hogwarts house and the other school houses.
  * To ecourage the deeper discovery of the J. K. Rowling's magical world.
### 3. Scope
* I wanted a simple, evident and user-friendly UX experience.
* I wanted clear and informative content.
* I wanted a visually appealing and creative design.
* I wanted interesting and thought-provoking questions for the Sorting Ceremony.
* I wanted smooth and interactive quiz game experience.
* I wanted detailed result / house statistics and house descriptions for full insight.
### 4. Structure
* The layout is simple and clear to ensure the easy navigation through site content by users
* The navigation bar is clear, fixed, visible and responsive with matching site logo and dropdown list for houses' pages. 
* The content is easy to read and quiz experience is smooth with self-explanatory steps.
* The Home page displays clearly the site’s main subject, allows to explore site content, and appeal visitors to stay and try Sorting Ceremony.
* The Sorting Ceremony page allows users to answer questions related to their personality to dicover their Hogwarts house(s) 
* The Sorting Result page allows users to see their detailed Sorting Ceremony results for their main house(s) and for other houses too,and to export their result in csv format.
* The Results page allows users to see the detailed sorting statistics for all houses in an organized structure and export the current total house results in csv format.
* The House page allows users to discover house statistics and house-specific detais of all Hogwarts houses one by one, here included personnalized, random, inspirational house quotes
* In the Footer, users can find copyrights and navigate to external sites to discover the Wizarding World and it's creators, as well as icon buttons to share site on different social media platforms.
### 5. Skeleton
The very basic skeleton of the site was modelled by Wireframes via Balsamiq, and during site development, additional design elements was added for better UX.
* [Home Page Wireframe](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/balsamiq-home.png)
* [Sorting Ceremony Page Wireframe](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/balsamiq-sorting.png)
* [Sorting Result Page Wireframe](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/balsamiq-sorting-result.png)
* [Results Page Wireframe](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/balsamiq-results.png)
* [House Page Wireframe](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/balsamiq-house.png)
### 6. Style
* Design & Colours
  * When planning the project, I wanted the four primary colors of the four houses (red/yellow/blue/green) to dominate on the site in order to emphasize house-related statistics and details. Therefore as a basic, I chose a simple black-white design along with a greyish, minimalist background of Hogwarts castle, and for the house-specific elements, I combined standard Bootstrap color values to represent houses' primary/secondary colors and to fit well with Bootstrap-styled buttons : 
Red (#dc3545) with Gold (#ffc107) / Yellow (gold: #ffc107) with Black (#000000) / Blue (#0d6efd) with Bronze (custom color: #ff7c02) / Green (#198754) with Silver (white: #FFFFFF)
* Font Selection
  * The main font type was chosen with [Google Fonts](https://fonts.google.com/) and is used across the whole of the website: [Yuji Syuku](https://fonts.google.com/specimen/Yuji+Syuku?category=Serif,Display,Handwriting,Monospace). This is a well readable font type which yet gives a floating, handwriting-like, tastefully assymetric feeling which I found suitable for the magical word where they use quill and ink for writing.
## Features
### 1. Existing Features
* __Navigation Bar__
  * Featured on all pages, the navigation bar includes links to all subpages and is identical on each page for smooth navigation. The navbar is fixed and fully responsive on all screen sizes: for smaller devices, a hamburger navbar view is included with the help of Bootstrap for better UX and easier navigation.

Navbar on Desktop\
![Navbar desktop](/static/readme/navbar-desktop.png)
Navbar on Mobile\
![Navbar mobile](/static/readme/navbar-mobile.png)

* __Home page__
  * Presenting Hogwarts and Sorting Ceremony, the home page clearly and briefly indicates site objective and also offers entry point to the Sorting Ceremony which allow users to immediately dive into the app. However for users who wish to know more about the houses before the sorting, the home page also presents their short description and quick links to respective house pages.

Home Page - Site Title\
![Home Page](/static/readme/page-home1.png)
Home Page - About the Sorting Ceremony\
![Home Page](/static/readme/page-home2.png)
Home Page - Quick glance at Hogwarts Houses\
![Home Page](/static/readme/page-home3.png)

* __Sorting Ceremony page__
  * Either by clicking on the Sorting Ceremony button on Home page, either by using navigation bar link, when arriving to Sorting Ceremony pase, the user is prompted to start the sorting quiz which is a series of personlity-based questions.

Sorting Ceremony Page - About the Ceremony\
![Sorting Ceremony Page](/static/readme/page-sorting1.png)
Sorting Ceremony Page - A question about you\
![Sorting Ceremony Page](/static/readme/page-sorting2.png)
Sorting Ceremony Page - Ready for the result?\
![Sorting Ceremony Page](/static/readme/page-sorting3.png)

* __Sorting Result page__
  * At the end of the Sorting Ceremony, the user is navigated to the page presenting the full result of sorting, here included main house(s), description in keywords and the associated result in %, as well as the sub-results for all other houses. The page also offers quick links to house pages and the overall result page, a quick way to play again, the option to provide feedback about the sorting result, and the possibility to export the sorting result in csv format.

Sorting Result Page - Main House(s)\
![Sorting Result Page](/static/readme/page-sorting-result1.png)
Sorting Result Page - Other House(s)\
![Sorting Result Page](/static/readme/page-sorting-result2.png)
Sorting Result Page - Feedback and Quick Links\
![Sorting Result Page](/static/readme/page-sorting-result3.png)

* __Results page__
  * This page allows user to see the actual sorting statistics for all houses at a glance, here included number of students, average satisfaction rate with sorting results, the rate of those who selected a house and also got sorted in it and the rate of those whose selected the house but got sorted in another, and also the average % of influence of other houses for students sorted in a house. Quick links to house pages and the possibility to export current total results in a csv file is also possible.

Results Page - Page title\
![Results Page](/static/readme/page-results1.png)
Results Page - In-House Statistics\
![Results Page](/static/readme/page-results2.png)
Results Page - Influence of other Houses\
![Results Page](/static/readme/page-results3.png)

* __House Page__
  * This page allows user to discover a Hogwarts House in details, here included the detailed house statistics and also many interesting house-specific information like house personality traits, brief history of the house founder, the house common room and more. The lyrical house description of the Sorting Hat, as well as the randomly chosen, house-specific quote help to understand and embrace better the spirit of the given house.

House Page - Sorting Hat's Poem\
![House Page](/static/readme/page-house1.png)
House Page - House Statistics\
![House Page](/static/readme/page-house2.png)
House Page - House Information\
![House Page](/static/readme/page-house3.png)
House Page - Collapsible Section\
![House Page](/static/readme/page-house4.png)

* __Footer__
  * The footer section includes copyrights of Wizarding World books/films, allowing user to navigate to external sites to discover Harry Potter books/films and their creators. The footer also allows to share this website with other people through social media sites and email via social share buttons. 

Footer\
![Footer](/static/readme/page-footer.png)

### 2. Future Features
* Setup of analysis per question
* Extend user feedback collection part
* Include sub-quiz based on sorting result to discover which specific house traits are the strongest among students
## Code validation
### 1. Automated tests
* HTML\
Passing the HTML of all pages through the [W3C Markup Validator](https://validator.w3.org/) and errors are only related to special format of input calculated by Python logic and passed to html page via Django.
  * [Home Page Validation](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/w3validator-html-home.pdf)
  * [Sorting Ceremony Page Validation](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/w3validator-html-sorting.pdf)
  * [Sorting Result Page Validation](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/w3validator-html-sorting-result.pdf)
  * [Results Page Validation](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/w3validator-html-results.pdf)
  * [House Validation](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/w3validator-html-house.pdf)
* CSS\
Passing the global CSS file through the [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/) and no errors have been found.\
Warnings are coming from dynamic CSS variables and imported style sheets which are out of scope of validator. Also warning appears concerning -webkit/-moz effects, as these elements are out of scope for validator.
  * [CSS Style Validation](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/w3validator-css-style.pdf)
* Python Code\
Passing the python logic file (hogwarts_quiz/views.py) through the [PEP8 Validator](http://pep8online.com/) and no errors have been found.\
  * [PEP8 Validation - Image](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/pep8-validation.PNG)
  * [PEP8 Validation - Text file](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/pep8-result_20211122_224907.txt)
### 2. Manual tests
* Desktop\
Mozilla Firefox, Google Chrome, Microsoft Edge: pages are working fine and have the corresponding style.
* Mobile\
Tested with Samsung A5, Galaxy Fold, iPhone 5, and iPad, and webpage works well, responsive as intended and no style deformations.
* Mozilla Developer Tools\
Tested for available devices, webpage works well, responsive as intended, no style deformations and no error messages in Pycharm debug tool.
### 3. Accessibility tests
The entire website was verified about accessibility using [Wave](https://wave.webaim.org/). Only few stylistic errors found (low contrast errors for color), alerts related to heading elements hierarchy.
* [Home Page Wave Result](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/wave-home.PNG) | [Home Page Wave Errors](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/wave-home-errors.PNG)
* [Sorting Ceremony Page Wave Result](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/wave-sorting.PNG) (No errors)
* [Sorting Result Page Wave Result](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/wave-sorting-result.PNG) | [Sorting Result Page Wave Errors](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/wave-sorting-result-errors.PNG)
* [Results Page Wave Result](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/wave-results.PNG) | [Results Page Wave Errors](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/wave-results-errors.PNG)
* [House Page Wave Result](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/wave-house.PNG) | [House Page Wave Errors](https://github.com/SofiaHorvath91/ucd-project-3/blob/master/static/readme/wave-house-errors.PNG)
### 4. Bugs and Solution
While building the application, I often encountered with zero value error while communicating between html page and python logic via Django, so each time an input is received directly / indirectly from user via UI, I set up validations for zero values in Python logic. I also wished to implement a more detailed feedback form, but due to little time, I had to find a workaround to still collect user feedback, thus I extended Result object to store the satisfaction value.
## Deployment
The site was deployed to [Heroku](https://heroku.com) (find it [here](https://cryptic-citadel-55296.herokuapp.com/)) while building it with [PyCharm](https://www.jetbrains.com/pycharm/) and pushing it to GitHub Repository and Heroku via [Git Bash](https://git-scm.com/downloads) and [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
### 1. Forking Repository
By forking the GitHub Repository, the user can copy the original repository in his/her own GitHub account, allowing the user to view and/or make changes without affecting the original repository.
1.	Open GitHub => GitHub Repository
2.	Top of Repository => Fork option
3.	Copy of the original repository appears in your GitHub account
### 2. Local Clone
1.	Open GitHub => GitHub Repository
2.	Under Repository name => Clone or download option
3.	Clone Repository using HTTPS => Clone with HTTPS => Copy URL
4.	Open Git Bash
5.	Current working directory => Choose location where you want the directory to be cloned
6.	Type git clone, and then paste the URL copied in Step 3.\
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
7.	Press Enter
## Credits
* The ['Harry Potter' books](https://en.wikipedia.org/wiki/Harry_Potter) and [Wizarding World](https://en.wikipedia.org/wiki/Wizarding_World) belong to [J. K. Rowling](https://en.wikipedia.org/wiki/J._K._Rowling).
* The ['Harry Potter' film series](https://en.wikipedia.org/wiki/Harry_Potter_(film_series)) belong to [J. K. Rowling](https://en.wikipedia.org/wiki/J._K._Rowling) / [Warner Bros](https://en.wikipedia.org/wiki/Warner_Bros.)
### 1. Content
* Informations / descriptions about the story of 'Harry Potter' books and about Wizarding World provided by [Harry Potter Wiki](https://harrypotter.fandom.com/)
* House-specific quotes : [GoodReads](https://www.goodreads.com/quotes)
### 2. Media
Pictures were treated with [Photoshop](http://www.apsportable.com/photoshop-cs6-portable-download-4/) and [tinyPNG](https://tinypng.com/) to have a better size for online presentation.
* Site Logo : [Vectorified](https://vectorified.com/download-image#hogwarts-icon-35.png)
* Background image : [WallpaperDog](https://wallpaper.dog/harry-potter-hogwarts-castle-wallpapers)
* Common sources :
  * Hogwarts Crest : Won game image from [DecalsCity](https://decalscity.com/products/game-of-thrones-crown-die-cut-vinyl-decal-sticker)
  * Gryffindor / Hufflepuff / Ravenclaw / Slytherin crests : [Wizarding Studies](https://wizardingstudies.wordpress.com/2016/03/18/hogwarts-houses-in-real-life/)
  * Gryffindor / Hufflepuff / Ravenclaw / Slytherin sorting hat badges: [KindPNG](https://www.kindpng.com/) & [NicePNG](https://www.nicepng.com/) & [SeekPNG](https://www.seekpng.com/)
* Media Source(s) used exclusively for Sorting Page :
  * Sorting Hat image : [CustomCursor](https://custom-cursor.com/en/collection/harry-potter/hp-sortinghat-gryffindor-sword)
  * Sorting Hat black icon : [Clipart-Library](http://clipart-library.com/clip-art/hogwarts-silhouette-clipart-3.htm)
* Media Source(s) used exclusively for House Page :
  * Gryffindor / Hufflepuff / Ravenclaw / Slytherin alternative crests : [Rhynn Collins (DeviantArt)](https://www.deviantart.com/rhynncollins/art/Hogwarts-House-crests-274881289)
  * Gryffindor / Hufflepuff / Ravenclaw / Slytherin traits: [Emily Corene (DeviantArt](https://www.deviantart.com/emily-corene)
  * Gryffindor / Hufflepuff / Ravenclaw / Slytherin founders: [AkaMaiden (Tumblr](https://akamaiden.tumblr.com/post/168842476569/godric-gryffindor-helga-hufflepuff-rowena)
  * Gryffindor / Hufflepuff / Ravenclaw / Slytherin symbols: [Harry Potter Wiki] (https://harrypotter.fandom.com/)
  * Gryffindor / Hufflepuff / Ravenclaw / Slytherin elements: [SubPNG] (https://www.subpng.com/png-g60lu5/)
  * Gryffindor / Hufflepuff / Ravenclaw / Slytherin common rooms: [Wizarding World (https://www.wizardingworld.com/)
  * Gryffindor / Hufflepuff / Ravenclaw / Slytherin common ghosts: [Wizarding World (https://www.wizardingworld.com/)
### 3. External Codes used as source / inspiration
* Sticky Menu (Navigation Bar) : [W3Schools](https://www.w3schools.com/howto/howto_js_navbar_sticky.asp)
* Responsive Menu (Navigation Bar) : [Bootstrap](https://getbootstrap.com/docs/4.4/components/navbar/) (also used for general styling like margins, rows)
* Sticky Footer (Footer) : [CSS Tricks](https://css-tricks.com/couple-takes-sticky-footer/)
* Social Media Sharing Buttons (Footer) : [SharingButtons](https://sharingbuttons.io/)
### 4. Acknowledgements
* To the Code Institute for the great course material
* To the [Stack Overflow](https://stackoverflow.com/) & [W3Schools](https://www.w3schools.com/) as a valuable resource for solving issues.
* To John Elder (Founder of Codemy)(https://www.udemy.com/user/johnelder3/) for his valuable [tutorial](https://www.udemy.com/course/push-django-python-apps-to-heroku/) about how to deploy Python with Django to Heroku
* To all the wonderful artists, organizations and programmers who provided great source materials 
* To J. K. Rowling for creating the most wonderful fantasy world of all time
### 5. Special Thanks
* My mentor Rahul Lakhanpal for his time, kind words and support.
* My previous private mentor Samu Gábor Tamás who taught me all I know in the last two years
* My Mother who is always there for me and who bought me the first Harry Potter book a long time ago for Christmas