# Testing

- Testing was carried out on all screen ratios from 2560 x 1440 to 320 x 568.
- Any errors found where corrected using Media queries which can be found [here](https://github.com/Bar-Dev/star-wars-fandom/blob/master/static/css/style.css) at the bottom of the css page

# Testing each Feature

- [Home-Page](/readme/images/sw-testing20.png)
    - Appears as intended across all devices. Main image of the iconic Millennium Falcon resizes to each device size along with the text quote on the image.
    - On larger screens two images under the "Coming Soon..." title sit side by side but on smaller devices become stacked on top of each other.

**Prior to Login/Register**

- [Navbar](/readme/images/sw-testing3.png)
    - On larger screens the Navbar displays all the tab wordings.
    - On smaller resolutions the different tabs disappear and are replaced with a menu button that drops down the tab list.

- [Reviews](/readme/images/sw-testing21.png)
    - Appears centered on screen as supposed to with a little room allowed for at the edges for the popout fuction of the dropdown lists.
    - On smaller resolutions, under 600px wide the Subtitle disappears and is moved to within the dropdown of each Review. 

- [Login](/readme/images/sw-testing22.png)
    - Appears centered on screen as supposed to.
    - Resizes accordingly on smaller resolutions.  

- [Register](/readme/images/sw-testing23.png)
    - Appears centered on screen as supposed to.
    - Resizes accordingly on smaller resolutions.
    - Gives the user 3 inputs to carry out, upon registration they are directed to their Profile page where they can choose an image.

**After Login**

- [Add Review](/readme/images/sw-testing24.png)
    - Appears centered on screen as supposed to.
    - Resizes accordingly on smaller resolutions.
    - Gives the user 3 inputs to carry out while the "Film Subtitle" is automatically populated based on Film Selection.
    - Icon list displays the icons as well as the name.

- [Profile](/readme/images/sw-testing25.png)
    - Appears centered on screen as supposed to.
    - On larger resolutions the Profile Image is displayed next to the Users name. 
    - On smaller screens the Profile Image stacks above the name
    - Users name is after a defined "sides" wording based on users selection.
    - Upon entering Users own profile a soundclip is played. The "Pause Audio" button functions properly.
    - From Profile Page Users can edit their Profile through the "Edit" button

- [Log Out](/readme/images/sw-testing16.png)
    - Redirects to Login Page.
    - Appears centered on screen as supposed to.
    - Resizes accordingly on smaller resolutions.
    - After Logout, flash message is shown to confirm Logout.

**Editing Reviews**

- [Edit](/readme/images/sw-testing26.png)
    - Only users that made reviews can Edit/Delete their own reviews via the three dots that are displayed on their reviews when logged in.
    - Appears centered on screen as supposed to.
    - Resizes accordingly on smaller resolutions.
    - Gives the user 2 inputs to carry out, Film Name and Subtitle cannot be altered while editing.

- [Footer](/readme/images/sw-testing27.png)
    - Sticky Footer appears as it should on all pages and devices, at the bottom of page.
    - Social Links all link to required web pages.
    - Social Links change colour when hovered over for identification. 

- [Delete-Review](/readme/images/sw-testing28.png)
    - Only users that made reviews can Edit/Delete their own reviews via the three dots that are displayed on their reviews when logged in.
    - Re-directs to "Reviews" page.
    - Review is removed.


# Testing the User-stories

- As a user, I want to see what site navigation options are available.

  - [On the Home Page, options are visible on main Navbar](/readme/images/sw-testing1.png)
  - [On smaller screens by clicking the "menu" button a dropdown of options appear](/readme/images/sw-testing2.png)
  - [When logged in additional navigation items appear](/readme/images/sw-testing3.png)

- As a user, I want to be able to immediately grasp what the website is about.

  - [In the header, the Logo immediately tells me it is a Star Wars related site](/readme/images/sw-testing4.png)
  - [The hero image of the Millennium Falcon combined with a quote from Han-Solo tells me it is a Star Wars related site](/readme/images/sw-testing5.png)
  - [In the header and on the main image the link to "Reviews" tells me what the site is about](/readme/images/sw-testing6.png)

- As a user, I want to see a list of Star Wars films available that have been reviewed.

  - [On the Home page, either selected "Reviews" in the navbar, or "View Star Wars Reviews" on the main image](/readme/images/sw-testing6.png)

- As a user, I want to be able see who reviewed each film.

  - [On the Reviews page, scroll down through the reviews and the reviewer can be seen highlighted in blue](/readme/images/sw-testing7.png)

- As a user, I want to see the profile pages of individuals that reviewed certain films.

  - [On the reviews page once I hover over the reviewers name it prompts me to view profile, by clicking it leads me to reviewers profile](/readme/images/sw-testing8.png)

- As a user, I want to be able to create my own profile page.

  - [In the header, by clicking "Register" it leads me to a registration page to input my details](/readme/images/sw-testing9.png)

- As a user, I want to see what profile images are available to me.

  - [Once registered the user is lead to their Profile page where they have the choice to "edit" their profile, this then brings up a number of different Profile image options](/readme/images/sw-testing10.png)

- As a user, I want to be able to edit my profile details should I wish to.

  - [On their Profile page where they have the choice to "edit" their profile, this then brings up a number of different options](/readme/images/sw-testing11.png)

- As a user, I want to be able to add a review of my own.

  - [Once logged in, the user will have the "Add Review" tab in the navbar which brings them to the "Add Review" page](/readme/images/sw-testing12.png)

- As a user, I want to be able to edit my review should I change my mind.

  - [On the reviews page, if the user created the review they will see three dots menu on the review they created, upon hovering over the dots they will see a dropdown menu to edit or delete the review](/readme/images/sw-testing13.png)

- As a user, I want to be able to delete my review should I chose to.

  - [On the reviews page, if the user created the review they will see three dots menu on the review they created, upon hovering over the dots they will see a dropdown menu to edit or delete the review. A modal will appear to ensure they want to do this.](/readme/images/sw-testing14.png)

- As a user, I want to be able to search for different reviews by using keywords.

  - [On the reviews page, user can enter search words into the search box at the top of page, minimum of 3 letters required](/readme/images/sw-testing15.png)

- As a user, I want to be able to log out of my profile when I'm done.

  - [In the navbar, once logged in the user will have a "Logout" tab available, once pressed they will redirect to Login page with a confirmation they are logged out](/readme/images/sw-testing16.png)

- As a site developer, I want to see all the users that have created accounts

  - [From the MongoDB Database used to store all the data I can view all users and details provided](/readme/images/sw-testing17.png)

- As a site developer, I want to see all the reviews that users have left.

  - [I can review or edit each user review from the MongoDB Database](/readme/images/sw-testing18.png)

- As a site developer, I want to see reviews remain organised in an appropiate way.

  - [When created the Film Title is assigned an order number, this organises all the same film reviews next to each other in the reviews page.](/readme/images/sw-testing19.png)


# Validation Testing

- HTML has been validated using [W3C HTML Validator](https://validator.w3.org/nu/) 

- CSS has been validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) 

- JS has been validated using [JSHint](https://jshint.com)

- Python has been checked for PEP8 compliance using [PEP8](http://pep8online.com)

