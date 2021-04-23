# Testing

- Testing was carried out on all screen ratios from 2560 x 1440 to 320 x 568.
- Any errors found where corrected using Media queries which can be found [here](https://github.com/Bar-Dev/star-wars-fandom/blob/master/static/css/style.css) at the bottom of the css page

# Testing each Feature

- [Home-Page](/readme/img/features/about.PNG)
    - Appears as intended across all devices. Main image of the iconic Millennium Falcon resizes to each device size along with the text quote on the image.
    - On larger screens two images under the "Coming Soon..." title sit side by side but on smaller devices become stacked on top of each other.

**Prior to Login/Register**

- [Navbar]()
    - On larger screens the Navbar displays all the tab wordings.
    - On smaller resolutions the different tabs disappear and are replaced with a menu button that drops down the tab list.

- [Reviews](/readme/img/features/about.PNG)
    - Appears centered on screen as supposed to with a little room allowed for at the edges for the popout fuction of the dropdown lists.
    - On smaller resolutions, under 600px wide the Subtitle disappears and is moved to within the dropdown of each Review. 

- [Login](/readme/img/features/express.PNG)
    - Appears centered on screen as supposed to.
    - Resizes accordingly on smaller resolutions.  

- [Register](/readme/img/features/tasting.PNG)
    - Appears centered on screen as supposed to.
    - Resizes accordingly on smaller resolutions.
    - Gives the user 3 inputs to carry out, upon registration they are directed to their Profile page where they can choose an image.

**After Login**

- [Add Review](/readme/img/features/index_reviews.PNG)
    - Appears centered on screen as supposed to.
    - Resizes accordingly on smaller resolutions.
    - Gives the user 3 inputs to carry out while the "Film Subtitle" is automatically populated based on Film Selection.
    - Icon list displays the icons as well as the name.

- [Profile](/readme/img/features/map.PNG)
    - Appears centered on screen as supposed to.
    - On larger resolutions the Profile Image is displayed next to the Users name. 
    - On smaller screens the Profile Image stacks above the name
    - Users name is after a defined "sides" wording based on users selection.
    - Upon entering Users own profile a soundclip is played. The "Pause Audio" button functions properly.
    - From Profile Page Users can edit their Profile through the "Edit" button

- [Log Out](/readme/img/features/navbar.PNG)
    - Redirects to Login Page.
    - Appears centered on screen as supposed to.
    - Resizes accordingly on smaller resolutions.
    - After Logout, flash message is shown to confirm Logout.

**Editing Reviews**

- [Edit](/readme/img/features/navbar_mobile.PNG)
    - Only users that made reviews can Edit/Delete their own reviews via the three dots that are displayed on their reviews when logged in.
    - Appears centered on screen as supposed to.
    - Resizes accordingly on smaller resolutions.
    - Gives the user 2 inputs to carry out, Film Name and Subtitle cannot be altered while editing.

- [Footer](/readme/img/features/footer.PNG)
    - Sticky Footer appears as it should on all pages and devices, at the bottom of page.
    - Social Links all link to required web pages.
    - Social Links change colour when hovered over for identification. 

- [Delete-Review](/readme/img/features/reservation_cancel.PNG)
    - Only users that made reviews can Edit/Delete their own reviews via the three dots that are displayed on their reviews when logged in.
    - Re-directs to "Reviews" page.
    - Review is removed.

<!--

# Testing the User-stories

- As a user, I want to see what site navigation options are available.

  - [On the index page, either through clicking the menu in navbar, or scrolling down](/readme/img/features/express.PNG)
  - [At the same point, but having selected Sample Tasting Menu](/readme/img/features/tasting.PNG)

- As a user, I want to have anchors to different parts of the page, so that I do not have to keep scrolling.

  - [In the header, there is the navbar which jumps to all appropriate anchors](/readme/img/features/navbar.PNG)
  - [Or on mobile, having selected the three bars icon](/readme/img/features/navbar_mobile.PNG)

- As a user, I want to see information on the chef, so I know if it is a chef I am interested in.

  - [On the index page, either selected "about" in the navbar, or having scrolled](/readme/img/features/about.PNG)

- As a user, I want to see reviews of the restaurant, so that others' experiences may influence my decision.

  - [On the index page, either selected "Reviews" in the navbar, or having scrolled](/readme/img/features/index_reviews.PNG)

- As a user, I want to see contact information for the restaurant, so that I may call with a special request.

  - [On any page, at the bottom in the footer, or in the Maps section](/readme/img/features/footer.PNG)

- As a user, I wish to see an address and a map, so I can ensure I am heading to the right place.

  - [On the index page, either selected "Find Us" in the navbar, or having scrolled](/readme/img/features/map.PNG)

- As a user, I want to be able to create an account, so that I may manage my bookings and reviews.

  - [Having selected Login, the user will be presented with the Okta login screen](/readme/img/features/okta.PNG)

- As a user, I want to be able to make a reservation, so that I may visit the restaurant for a meal.

  - [Once logged in, the user may create a reservation from the dashboard after pressing the make a reservation button](/readme/img/features/reservation.PNG)

- As a user, I want to be able to leave a review, so that I may let other people know my opinion of my meal.

  - [Once logged in, the user may create a review from the dashboard after pressing the leave a review button](/readme/img/features/review.PNG)

- As a user, I want to be able to edit my reservation, in case circumstances change.

  - [Once logged in, the user may edit a reservation from the dashboard after pressing the Edit this Booking button on the appropriate card.](/readme/img/features/reservation_edit.PNG)

- As a user, I want to be able to cancel my reservation, in case I am no longer able to, or wanting, to attend.

  - [Once logged in, the user may cancel a reservation from the dashboard after pressing the Cancel this Booking button on the appropriate card. A modal will appear to ensure they want to do this.](/readme/img/features/reservation_cancel.PNG)

- As a user, I want to be able to edit my review, in case I have changed my opinion of the restaurant.

  - [Once logged in, the user may edit a reservation from the dashboard after pressing the Edit this Booking button on the appropriate card.](/readme/img/features/review_edit.PNG)

- As a user, I want to be able to cancel my review, in case I have changed my opinion of the restaurant.

  - [Once logged in, the user may delete a review from the dashboard after pressing the Delete this Review button on the appropriate card. A modal will appear to ensure they want to do this.](/readme/img/features/review_delete.PNG)

- As a site owner, I wish to see all the reservations that have been made, so that I know which bookings to prepare for.

  - [Once logged in, on the admin account, the admin may see all the reservations that have been made.](/readme/img/features/dashboard_admin.PNG)

- As a site owner, I wish to see all the reviews that have been made, so that I know what people think of my restaurant.

  - [Once logged in, on the admin account, the admin may see all the reviews that have been made.](/readme/img/features/dashboard_admin.PNG)

- As a site owner, I want the reservations that would have occurred deleted, so that I do not have clutter from expired reservations.

  - [Whenever the index page is called, the mongodb collection checks today's date versus the date of each reservation, and if it is less than today, it is deleted from the collection.](/readme/img/features/reservation_expired.PNG)

# Validation Testing

- HTML has been validated using [W3C HTML Validator](https://validator.w3.org/nu/) 

- CSS has been validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) 

- JS has been validated using [JSHint](https://jshint.com)
    - The line /*jshint esversion: 6 */ was added to the start each file for testing purposes. 

- Python has been checked for PEP8 compliance using [PEP8](http://pep8online.com)

## Validation Testing Results 

![HTML validation](/readme/img/validation/html.png)

- [Messages filtered were ones to do with UiKit](/readme/img/validation/message_filtering.png)

![CSS validation](/readme/img/validation/css.png)


![JS validation](/readme/img/validation/js.png)


![PEP8 validation](/readme/img/validation/pep8.png)

-->