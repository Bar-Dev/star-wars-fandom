# Star Wars Fandom (https://star-wars-fandom.herokuapp.com/)

- [Introduction](#introduction)
- [UX](#ux)
  - [Wireframes](#wireframes)
  - [The Design](#the-design)
  - [User-stories](#user-stories)
  - [Developer-stories](#developer-stories)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [MongoDB](#mongodb)
  - [Materialize](#materialize)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Inspiration](#inspiration)
  - [Acknowledgements](#acknowledgements)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Introduction
 
The live website can be found here at [https://star-wars-fandom.herokuapp.com/](https://star-wars-fandom.herokuapp.com/)

If you do not wish to make an account, feel free to use existing account below made for reviewing: 

User account:
username - Timmy
password - testone 

# UX

With the latest Star Wars films released over the last few years it has grabbed the attention of newer audiences wanting to know what the whole Star Wars Saga is about. The Star Wars Fandom website was designed for that purpose, to give new audiences an unbiased look over the entire Star Wars series from the eyes of other people. 
The UX was laid out with the specific goal to be about the reviews of other people, generate a friendly community and to cover:

1. What Films have been covered by the reviews. 
2. What did people who reviewed them think of the films?
3. The ability to be able to add their own reviews. 

The website is designed to give the user the aim of been able to view others reviews, create their own reviews, edit only their own work and delete their own reviews should they wish. In addition they have the ability to crete their own user profile, select/change a profile image and select/change what side of the "Force" they chose to be on.

## Wireframes

With the help of [figma](https://www.figma.com/) I produced mockups of the proposed website starting with a mobile first approach.

Links to the mockups can be found [here](https://www.figma.com/file/gk8v8WA3ndCOmjdplOmE7x/Star-Wars-Fandom?node-id=0%3A1) where you will find the full design 
proposal for each page. 

If you cannot access the mockups via the link above you can view them [here](https://github.com/Bar-Dev/star-wars-fandom/tree/master/documentation/wireframes)

## The Design

As you can see from the Wireframes there was a few other elements I wanted to add to the website however due to their complexity I've decided to leave these for further updates and add-ons in the future.
For now I toned things back and went for a more minimalistic approach to give the user a good feel of what the website is about and keeping it specifically to film reviews. By generating a fan base and followers now to the website I believe the additional items such as the Chat-Room and Memorabilia displays will be more welcome in the future and keep peoples attention to an ever evolving site.


<!---
### Colors 

The following colors have formed the main design of the website:

<img src="./assets/images/reilly-colours.png" style="margin: 0;">

**List of colors used are:**
* #F7D165 Orange Yellow Crayola
* #555F7B Independence
* #FFFFFF White
* #777777 Sonic Silver
* #2F0147 Russian Violet

The predominant color used for this website was Independence apart from the mainbackground colour of white. 
This was chosen to provide a nice contrast with the various images used and maintain a dominant look and feel.

### Fonts

The main font used for this website was **Roboto** with **Sans Serif** as a backup font. Apart from the main logo text which was **Roboto Slab** to give
the title matching style to the font style on the main image of the Home page.

Font weights used were:
* 300
* 400
* 600
--->


## User-stories

- As a user, I want to see what site navigation options are available.

- As a user, I want to be able to immediately grasp what the website is about.

- As a user, I want to see a list of Star Wars films available that have been reviewed.

- As a user, I want to be able see who reviewed each film.

- As a user, I want to see the profile pages of individuals that reviewed certain films.

- As a user, I want to be able to create my own profile page.

- As a user, I want to see what profile images are available to me.

- As a user, I want to be able to edit my profile details should i wish to.

- As a user, I want to be able to add a review of my own.

- As a user, I want to be able to edit my review should I change my mind.

- As a user, I want to be able to delete my review should I chose to.

- As a user, I want to be able to search for different reviews by using keywords.

- As a user, I want to be able to log out of my profile when I'm done.


## Developer-stories

- As a site developer, I want to see all the users that have created accounts

- As a site developer, I want to see all the reviews that users have left.

- As a site developer, I want to see reviews remain organised in an appropiate way.

- As a site developer, I want to see reviews are left in a friendly manner. 

- As a site developer, I want to see who wrote which reviews.

# Features

### Existing Features

#### Home Page

* **Layout and Style**
    * I want the user to immediately know where they are and what the site is about as soon as they arrive. This was done with the use of the image of the iconic Millenium Falcon along with a popular quote from Han Solo from the initial Star Wars movie.
    * Upon reading the quote this then directs the users eyeline down to the reviews button where they would naturally proceed to next.
    * Careful detail was applied to the responsiveness of the site to further ensure all retail space sized correctly and not leaving any blank areas. A lot 
    of attention was put into this through the use of media queries.

#### Reviews Page
    * Materialize was used to allow for the dropdown popout function of the reviews list. This ensures the user gets a good understanding of the review they have clicked on.
    * The review bar consists of teh review Film Title, the Film Subtitle, who wrote the review and should the user be logged in then at the end of the review bar they will see the commom three vertical dots that would be familiar to users as a more options button. This gives the user the option to edit or delete their own reviews only.
    * One issue I could not overcome was due to using Materialize I could not over ride the function to stop the review popout from happening when clicking on "edit" or "delete". This is something that I may be able to over come in the future by possibly reverting to Bootstrap instead of Materialize.

#### Profile Page
    * The Profile Page consists of a profile image the user can change, their name, and the side of the Force they chose. 
    * In addition if the user is viewing their own page they will see an edit button to enable them to edit their Profile, which is not visible if viewing a different users page.
    * Upon entering their own Profile page a theme tune lasting approx 16 seconds will play based on the side of the Force they have chosen. Should they edit the side of the Force in their Profile the alternative theme tune will play. The tune is set to auto-play but a Pause/Play Button has been added to allow the user to toggle it on or off.

#### Materialize

[Materialize](https://materializecss.com/getting-started.html) was used on this site for items such as Navbar, Footer, Dropdown lists and some general alignment and layout.

* **Navigation Bar**
    * The navigation bar has a fixed position and rendered on all pages using the base.html file. 
    * On small screen widths the navbar items reduce to a menu item with a sidebar dropdown.
    * The ----- color was used on the navbar and footer to keep it unioen throughout.
    * While not logged in the navbar allows users to view the reviews, register or log in. Once registered and logged in more options appear to give the user further control during their visit to the site.

* **Footer**
    * Social Links:
    For now the soical links have been kept simple and straight forward and just link to the social networks main pages. In the future, there will be plans to extend these to futher relevant network pages.
    Upon hovering over the icons the color will change from ------- to -------, this allows the user to identify what icon they are on.


## MongoDB

My [MongoDB Database](/readme/images/swf-database.png) is titled star-wars-fandom. It is composed of 4 collections: Films, Icons, Reviews and Users. 

[Films](/readme/images/films.png) is a pre-compiled list of Star Wars Films which form a list that the user can pick from once they decide to post a review. Also in this is the pre-defined film-subtitle. The subtitle gets automatically inputted to the relevant fields based on the film that is selected.

[Icons](/readme/images/icons.png) is a pre-comiled list of various memorabil icons from throughout the Star Wars Series. The data inputed for this list was taken as a string from the [FontAwesome](https://fontawesome.com/) website and once the string is inputted to the code the logo is generated. There was issues however trying to show these images on the Materialize dropdown list so as a workaround for this the "data-icon" of the icon was needed which required the icons to be saved and displayed as images in the dropdown list. More details on this available from this thread: [Icons on Materialize Dropdown](https://github.com/Dogfalo/materialize/issues/4056). This formed an additional entry into the Database as icon_image.

[Reviews](/readme/images/reviews.png) takes all the relevant inputs into the database, based on the users selection and their own input under the headings of icons, film, subtitle and description. It also assigns the user the title of "reviewed_by" with their name added to the review. In addition there is also a further input using JavaScript which is assigned to the review based on film selection, this is "film_order" and allows for proper assortment of the reviews when they are displayed on the review page. I opted not to have the newest review first but instead maintain the films in their order of the storyline and additional film reviews of the same name will be entered below that film title.

[Users](/readme/images/users.png) takes the initial input from the user of their username, password, and the side of the Force they chose to be on. While in addition the profile image of a standard placeholder image is also entered to the database using JavaScript. The user can then change this image in their own Profile Page. While not used elsewhere on the site as of yet, the idea is that it will form part of their identity for different features to the site at a later date. 
The password is coded into a hash address with the use of Werkzeug making it un-readable even from the MongoDB database and is pulled from the Database and decoded upon login.


# Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

  - Semantic markup language as the shell of the site.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

  - Cascading Style Sheets as the design of the site.

- [JS](https://en.wikipedia.org/wiki/JavaScripts)

  - JavaScript used to enable interactivity of the webpages.

- [jQuery-ui](https://jqueryui.com)

  - Used for a number of Materialize functions.

- [Font Awesome 5](https://fontawesome.com)

  - Used for all the Star Wars based icons.

- [Materialize](https://materializecss.com/getting-started.html)

  - Used for the basis behind the site layout and functions.

- [Git](https://git-scm.com)

  - Git was used for version-control and for pushing through to my Github Repo.

- [Heroku](https://www.heroku.com/)

  - Heroku was used for deployment of my live website.

- [MongoDB](https://www.mongodb.com)

  - NoSQL database management used for management of reservations and reviews.

- [Photoshop](https://www.adobe.com/uk/products/photoshop.html)
  - Used to edit the images.

