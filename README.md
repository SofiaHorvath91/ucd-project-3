# Hogwarts Sorting App (UCD Project 3)
Get sorted & let the magic begin!

Ready to enter the Wizarding World and start your journey in Hogwarts School of Witchcraft and Wizardry?
There are four Houses in Hogwarts to host students with different personalities, founded by the four greatest witches and wizards of their time who built Hogwarts a thousand years ago. Students are sorted in their house by the Sorting Hat, the magical and sentient piece of headwear, which can see the hearth and mind of a person.
In the Hogwarts Sorting App, you have the possibility to discover all the four houses with the latest student numbers, see the popularity of the houses among students and get sorted in one or more of them in frame of the Sorting Ceremony by answering honestly the questions of the Sorting Hat.
If you are ready, meet the most magical Hat of all, participate in the Sorting Ceremony and find your own Hogwarts House!

![Responsive Layouts](/static/readme/responsive-design.PNG)

Deployed site (Heroku) : https://cryptic-citadel-55296.herokuapp.com/ \
Technologies : Python + Django + HTML + CSS \
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