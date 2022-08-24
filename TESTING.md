# Testing

## Manual Testing

In addition to the other tests, I have conducted a manual check list for myself to carry out to make sure that everything is working as intended.

| Status | **Navigation Bar - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the navbar logo loads the home page
| &check; | That the navbar shows the tabs Home, Bookshelf, Login, Signup and Contact if the user is logged out
| &check; | Clicking the Home tab on the navbar loads the home page
| &check; | Clicking the Bookshelf tab on the navbar loads the bookshelf page
| &check; | Clicking the Login tab on the navbar loads the login Page
| &check; | Clicking the Signup tab on the navbar loads the signup page
| &check; | Clicking the Contact tab on the navbar loads the contact page

| Status | **Navigation Bar - User Logged In**
|:-------:|:--------|
| &check; | Clicking the navbar logo loads the home page
| &check; | That the navbar shows the tabs Home, Bookshelf, My Books, Logout and Contact if the user is logged in
| &check; | That the navbar shows the username of the logged in user and that clicking this leads to the user My Books page
| &check; | Clicking the Home tab on the navbar loads the home page
| &check; | Clicking the Bookshelf tab on the navbar loads the bookshelf page
| &check; | Clicking the My Books tab on the navbar loads the user's my books Page
| &check; | Clicking the Logout tab on the navbar loads the logout page
| &check; | Clicking the Contact tab on the navbar loads the contact page
| &check; | Clicking user's username in the navbar loads the user's my books page


| Status | **Navigation Bar - Admin (superuser) User Logged In**
|:-------:|:--------|
| &check; | Clicking the navbar logo loads the home page
| &check; | That the navbar shows the tabs Home, Bookshelf, My Books, Logout, Admin Only and Contact if the user is logged in
| &check; | That the navbar shows the username of the logged in user and that clicking this leads to the user My Books page
| &check; | Clicking the Home tab on the navbar loads the home page
| &check; | Clicking the Bookshelf tab on the navbar loads the bookshelf page
| &check; | Clicking the My Books tab on the navbar loads the user's my books Page
| &check; | Clicking the Logout tab on the navbar loads the logout page
| &check; | Clicking the Admin Only tab on the navbar loads the admin only page
| &check; | Clicking the Contact tab on the navbar loads the contact page
| &check; | Clicking user's username in the navbar loads the user's my books page

| Status | **Footer - User Logged Out/In**
|:-------:|:--------|
| &check; | Clicking email icon loads the contact page in the wesbite
| &check; | Clicking the instagram icon loads the instagram home page in a new tab
| &check; | Clicking the facebook icon loads the facebook home page in a new tab
| &check; | Clicking the twitter icon loads the twitter home page in a new tab

| Status | **Home Page - User Logged Out**
|:-------:|:--------|
| &check; | That a Login and Signup button appear in the hero section
| &check; | Clicking the Login button in the hero section of the home page loads the login page
| &check; | Clicking the Signup button in the hero section of the home page loads the signup page
| &check; | That a random selection of books from the approved list only and with a book cover image can be seen in a carousel effect
| &check; | Clicking on a book in the Discover list will bring the user to the book's detail page
| &check; | That a list of genre's from the genre list can be seen in a carousel efect under the Discover List
| &check; | Clicking on a genre in the Genre list will bring the user to the Genre page
| &check; | Typing in a incorrect URL will load the 404 error page

| Status | **Home Page - User Logged In**
|:-------:|:--------|
| &check; | That a Welcome text appears with the user's username in the hero section
| &check; | That a My Books button appears below the welcome text
| &check; | That the My Books button loads the user's my books page
| &check; | That a random selection of books from the approved list only and with a book cover image can be seen in a carousel effect
| &check; | Clicking on a book in the Discover list will bring the user to the book's detail page
| &check; | That a list of genre's from the genre list can be seen in a carousel efect under the Discover List
| &check; | Clicking on a genre in the Genre list will bring the user to the Genre page
| &check; | Typing in a incorrect URL will load the 404 error page


| Status | **Genre Page - User Logged Out**
|:-------:|:--------|
| &check; | That the page heading reflects the genre chosen
| &check; | That the books listed on the page are listed by the category chosen and that they are approved
| &check; | Clicking on a book listing will bring the user to the book's detail page
| &check; | That the book listing card shows a heading with the book title and author and book rating
| &check; | That the book rating can not be clicked by the user if they are not logged in
| &check; | That the book rating shows the average rating of the specific book
| &check; | That the book listing card shows the book image and an excerpt of the book blurb
| &check; | That below the book list the genre list is generated again, the same as the home page
| &check; | Clicking on a genre in the Genre list will bring the user to the Genre page 


| Status | **Genre Page - User Logged In**
|:-------:|:--------|
| &check; | That the page heading reflects the genre chosen
| &check; | That the books listed on the page are listed by the category chosen and that they are approved
| &check; | Clicking on a book listing will bring the user to the book's detail page
| &check; | That the book listing card shows a heading with the book title and author and book rating
| &check; | That the book rating can be clicked by the user to rate that book
| &check; | That the book rating can be changed by the user if they decide to change their rating 
| &check; | That the book rating shows the average rating of the specific book
| &check; | That the average book rating is reflected accurately according to how the user rates/changes their rate
| &check; | That the book listing card shows the book image and an excerpt of the book blurb
| &check; | That below the book list the genre list is generated again, the same as the home page
| &check; | Clicking on a genre in the Genre list will bring the user to the Genre page 

| Status | **Log In Page - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the sign up link above the user input loads the sign up page
| &check; | That the username input field is required
| &check; | That the password input field is required
| &check; | That if the username does not match the password the user cannot log in and user feedback is provided
| &check; | That if the correct credentials are given the user is logged in when the log in button is clicked
| &check; | That when the user is logged in they are redirected to the the home page and an alert message informs the user that they logged in successfully
| &check; |That when the user is logged in successfully their username will appear in the navbar indicating their logged in status

| Status | **Log In Page - User Logged In**
|:-------:|:--------|
| &check; | That the user cannot access the login tab from the navbar if they have logged in
| &check; | That if the user tries to type in the url of the Login page, when they are logged in they are redirected to the home page

| Status | **Sign Up Page - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the log in link above the user input loads the log in page
| &check; | That the username input field is required
| &check; | That both password input fields is a required field
| &check; | That if you provide a username and password that is too similiar that the user cannot sign up and user feedback is provided
| &check; | That if your password doesn't match in both password fields, the user cannot sign up and user feedback is provided
| &check; | That if the user provides a password less that 8 character, the user cannot sign up and user feedback is provided
| &check; | That if you provide a good username and password but the email field does not contain a proper email address, the user cannot sign up and user feedback is given
| &check; | That the email input field is optional
| &check; | Clicking the Sign Up button signs the user up and logs the user in if the correct user information was provided for sign up
| &check; |That when the user signs up, they are redirected to the home page and an alert message informs the user that they sisgned up successfully
| &check; |That when the user signs up and is logged in successfully their username will appear in the navbar indicating their logged in status

| Status | **Sign Up Page - User Logged In**
|:-------:|:--------|
| &check; | That the user cannot access the signup tab from the navbar if they have logged in
| &check; | That if the user tries to type in the url of the sign up page, when they are logged in they are redirected to the home page

| Status | **Log Out Page - User Logged Out**
|:-------:|:--------|
| &check; | That the user cannot access the log out tab from the navbar if they have logged out
| &check; | That if the user tries to type in the url of the log out page, when they are logged out they are redirected to the home page


| Status | **Log Out Page - User Logged In**
|:-------:|:--------|
| &check; | Clicking the logout button logs the user out
| &check; | When the user logs out they are redirected to the home page and a message alerts the user that they have logged out
| &check; | Once the user logs out the username in the navbar is removed


| Status | **Bookshelf page - User Logged Out**
|:-------:|:--------|
| &check; | That a searchbar appears at the top of the page underneath the page heading
| &check; | That the search bar filters through the entire approved books in the database and searches via title, author and book blurb of each book
| &check; | Clicking the magnifier button triggers the search
| &check; | Clicking the magnifier button without typing anything in the search bar redirects to the same page (Bookshelf)
| &check; | If a match is made the books that match are loaded
| &check; | If a user clicks on a book that has been pulled up from the search, the user is brought to that book'sdetail page
| &check; | If a match is not found, user feedback tells the user
| &check; | Clicking the X button cancels the search and redirects back to the bookshelf page
| &check; | Clicking the X button without typing anything in the search bar redirects to the same page (Bookshelf)
| &check; | That the user can see a list of Books in the books section, ordered by the date they are added and pulling from the database of all books that are approved
| &check; | The book list is paginated once 8 book listings are reached on screen
| &check; | Clicking the next button of the pagination brings the user to the next lot of books
| &check; | Clicking the prev button of the pagination brings the user to the previous lot of books
| &check; | Clicking on a book listing will bring the user to the book's detail page
| &check; | That the book listing card shows a heading with the book title and author and book rating
| &check; | That the book rating can not be clicked by the user if they are not logged in
| &check; | That the book rating shows the average rating of the specific book
| &check; | That the book listing card shows the book image and an excerpt of the book blurb


| Status | **Bookshelf page - User Logged In**
|:-------:|:--------|
| &check; | That a searchbar appears at the top of the page underneath the page heading
| &check; | That the search bar filters through the entire approved books in the database and searches via title, author and book blurb of each book
| &check; | Clicking the magnifier button triggers the search
| &check; | Clicking the magnifier button without typing anything in the search bar redirects to the same page (Bookshelf)
| &check; | If a match is made the books that match are loaded
| &check; | If a user clicks on a book that has been pulled up from the search, the user is brought to that book'sdetail page
| &check; | If a match is not found, user feedback tells the user
| &check; | Clicking the X button cancels the search and redirects back to the bookshelf page
| &check; | Clicking the X button without typing anything in the search bar redirects to the same page (Bookshelf)
| &check; | That an Add Book button can only be viewed if the user is logged in
| &check; | Clicking the Add Book button loads the add book page
| &check; | That the user can see a list of books in the Books section, ordered by the date they are added and pulling from the database of all books that are approved
| &check; | The book list is paginated once 8 book listings are reached on screen
| &check; | Clicking the next button of the pagination brings the user to the next lot of books
| &check; | Clicking the prev button of the pagination brings the user to the previous lot of books
| &check; | Clicking on a book listing will bring the user to the book's detail page
| &check; | That the book listing card shows a heading with the book title and author and book rating
| &check; | That the book rating can be clicked by the user to rate that book
| &check; | That the book rating can be changed by the user if they decide to change their rating 
| &check; | That the book rating shows the average rating of the specific book
| &check; | That the average book rating is reflected accurately according to how the user rates/changes their rating
| &check; | That the book listing card shows the book image and an excerpt of the book blurb


| Status | **Add Book Page - User Logged Out**
|:-------:|:--------|
| &check; | That the user cannot access the Add Book button from the Booshelf page if they have logged out
| &check; | That if the user tries to type in the url of the Add Book page, when they are logged out they are redirected to the log in page

| Status | **Add Book Page - User Logged In**
|:-------:|:--------|
| &check; | That the Title input field is required
| &check; | That the Book Author field is required
| &check; | That Book Image field is optional
| &check; | That the Book Blurb field is required
| &check; | That the Book Genre field is required
| &check; | That the form cannot be submitted without all the required fields and user feedback is given if a user forgets a  required field
| &check; | That none of the input fields accept empty fields
| &check; | That none of the fields accept just spaces in an input field
| &check; | That when the form is submitted a book slug is automatically created from the title and book author input fields in the form
| &check; | That when the form is submitted that if the user added an image, this is uploaded correctly and linked to the book added
| &check; | That when the book is added, the user is redirected back to the Bookshelf page and a message alert informs the user that they successfully added a book and it's waiting for approval
| &check; | That when a book is added it is automatically set as unapproved (False) until changed otherwise (to True) by an admin


| Status | **Book Page - User Logged Out**
|:-------:|:--------|
| &check; | That the page url is specific to that book
| &check; | That the website page pulls all the correct information on that specific book; book image, title, author, blurb.
| &check; | That the star rating for this book is not clickable by the user
| &check; | That the star rating displays the average star rating for this book, how many users have rated it and what rating you gave it.
| &check; | That the star rating displays the message to the user to log in to rate
| &check; | Clicking the review button will bring the user to the bottom of the page to the reviews and will ask them to log in or sign up to review.
| &check; | That the log in and sign up links in the in this text link to the appropriate log in and sign up pages
| &check; | That the bookmark displays the number of users who have bookmarked this book
| &check; | That the bookmark icon is not clickable by the user
| &check; | That the bookmark displays that the user needs to log in or signup to bookmark this book
| &check; | That the bookmark message log in and sign up links load the appropriate log in and sign up pages when clicked.
| &check; | That at the bottom of the page, all the approved reviews for that particular book are displayed correctly in order of the newest created.
| &check; | That the reviews shown show the name of the user who made the review, the date and time it was created and the review text itself.
| &check; | That if there are no reviews for this book, that No Reviews made yet is shown to the user


| Status | **Book Page - User Logged In**
|:-------:|:--------|
| &check; | That the page url is specific to that book
| &check; | That the website page pulls all the correct information on that specific book; book image, title, author, blurb.
| &check; | That the star rating for this book is clickable by the user to rate the book
| &check; | That the star rating displays the average star rating for this book, how many users have rated it and what rating you gave it.
| &check; | Clicking the review button will bring the user to the bottom of the page to the review form to create a review.
| &check; | That the bookmark displays the number of users who have bookmarked this book
| &check; | That the bookmark icon is clickable by the user
| &check; | That the bookmark turns a solid color if the user bookmarks (clicks) the icon
| &check; | That the bookmark turns back to an outline if the user clicks the icon again removing the bookmark
| &check; | In the review section the review form displays correctly
| &check; | That the text above the input field informs the user of who they are posting as (their username)
| &check; | That the review input field is required
| &check; | That clicking the review button will submit the review if all the criteria are correct
| &check; | That the newly created review is automatically set as unapproved (False) until changed otherwise (to True) by an admin
| &check; | That upon submitting the review, an alert message notifies the user of their success and that while the review needs to be approved, the unapproved review can be viewed in their My Books page
| &check; | Clicking the link in the alert message brings the user to their specific My Books page
| &check; | That at the bottom of the page, all the approved reviews for that particular book are displayed correctly in order of the newest created.
| &check; | That the reviews shown show the name of the user who made the review, the date and time it was created and the review text itself.
| &check; | That if there are no reviews for this book, that No Reviews made yet is shown to the users


| Status | **My Books Page - User Logged Out**
|:-------:|:--------|
| &check; | That the My Books tab in the navbar cannot be accessed
| &check; | That if the user tries to access the My Books url that they are redirected to the login page

| Status | **My Books Page - User Logged In**
|:-------:|:--------|
| &check; | That the username is in fact the username of the user currently logged in
| &check; | That the Bookmarked Books section correspond to the books that the user has bookmarked
| &check; | That the bookmarked list removes a book listing if the user removes the bookmark
| &check; | Clicking a book in the bookmarked list loads the books detail page
| &check; | That the book listing card shows the book title, author, rating, book image and blurb of the bookmarked book
| &check; | That the book rating can be clicked by the user to rate that book
| &check; | That the book rating can be changed by the user if they decide to change their rating 
| &check; | That the book rating shows the average rating of the specific book
| &check; | That the average book rating is reflected accurately according to how the user rates/changes their rating
| &check; | That if the user has no books bookmarked, the user sees the text: To bookmark books, go to the book page and click the bookmark icon to bookmark the book. Click it again to remove the bookmark
| &check; | That the user can see a list of all reviews they have created in order of the newest one created
| &check; | That if the user has made no reviews yet, the user can see the text: No reviews made yet
| &check; | That any reviews the user has made that are still awaiting approval have the tag Waiting for Approval on
| &check; | That the waiting for approval tag is removed once the review is approved
| &check; | That the each review in the reviews list shows the title of the book reviewd, the date reviewed, the review text itself and the buttons Update and Delete
| &check; | Clicking the book title in the review loads that book's page
| &check; | Clicking the Update button loads the edit review page
| &check; | Clicking the Delete button loads the delete review page


| Status | **User Edit Review Page - User Logged Out**
|:-------:|:--------|
| &check; | That if the user tries to access the edit review url that they are redirected to the login page

| Status | **User Edit Review Page - User Logged In**
|:-------:|:--------|
| &check; | That the user can see the book title of the review they are updating
| &check; | That the user can see their username name in the posting as section
| &check; | That the user can see the review input field is already prepoulated with the review as it currently is
| &check; | That review input field is required and cannot be submitted empty or with just spaces
| &check; | Clicking Update Review, updates the review, changes the status of the approval to False again, and redirects the user back to the My Books page
| &check; | That the an alert message informs the user that their review has been updated and is flagged for approval
| &check; | That the review has been updated with the Waiting on Approval tag in the My Books page
| &check; | That the review has been removed from the related Books page until it has been approved again


| Status | **User Delete Review Page - User Logged Out**
|:-------:|:--------|
| &check; | That if the user tries to access the delete review url that they are redirected to the login page

| Status | **User Delete Review Page - User Logged In**
|:-------:|:--------|
| &check; | That the user can see the book title and review details of the the review they would like to delete
| &check; | Clicking the Delete button redirects back to the My Books page
| &check; | That an alert message informs the user that they successfully deleted their review
| &check; | That the review is completely deleted and doesnt show up in the database or subsequently any place on the website


| Status | **Contact Page- User Logged Out/In**
|:-------:|:--------|
| &check; | That First Name input field is required
| &check; | That Last Name input field is required
| &check; | That Email input field is required
| &check; | That Message input field is required
| &check; | That none of the fields can be submitted blank
| &check; | That the email field only accepts proper email syntax (@ symbol has to be present)
| &check; | That none of the fields can accept just blank spaces
| &check; | That user feedback is provided if none of the required criteria to sub,it the form are met
| &check; | Clicking the Send button sends the email to the Dummy Email account set up via EmailJS, that the user is redirected to the contact page.
| &#88; | That an alert message informs the user that their message was sent successfully upon the user sending the message


| Status | **Admin Only Page - User Logged Out**
|:-------:|:--------|
| &check; | That the user cannot access the Admin Only tab in the navbar
| &check; | That if the user tries to access the Admin Only url that they are redirected to the login page

| Status | **Admin Only Page - User Logged In**
|:-------:|:--------|
| &check; | That the user cannot access the Admin Only tab in the navbar
| &check; | That if the user tries to access the Admin Only url that they are redirected to a 403 forbidden page


| Status | **Admin Only Page - Admin User Logged In**
|:-------:|:--------|
| &check; | That the Admin Only Page is accessible from the navbar
| &check; | That the admin user sees two sections, Books for Approval and Review for Approval
| &check; | That the list of books in the books for approval are only books with an approved status of False.
| &check; | That the books are listed in order of newest book added with the approved status of False
| &check; | That the Book listing itself shows the correct title, author, book image, when it was created, the book genre and book blurb, with two buttons at the end, Approve and Delete
| &check; | Clicking the Approve button loads the approve book page
| &check; | Clicking the Delete button loads the appropriate delete view and immediately deletes the book
| &check; | Upon deleting the book, the user is redirected to the Admin Only page, that they are informed via alert message that the book has been deleted and the book is removed from the database and completely from the website
| &check; | That the list of reviews in the reviews for approval section are only reviews with the approved status of False
| &check; | That the reviews are listed in order of the newest view created with the approved status of False
| &check; | That the review listing itself shows the correct user who listed the review, when it was created, the text detail of the review and two buttons at the end, Approve and Delete
| &check; | Clicking the Approve button will immediately change the approved status of the review to True, subsequently removing it from the reviews for approval list, redirecting the user to the Admin Only page and informing the user that they approved the review via alert message
| &check; | That any approved review shows up correctly as part of the book that was reviewed once approved
| &check; | Clicking the Delete button will immediately delete the users review, subsequently removing it from the database and website entirely, redirecting the user to the Admin Only page and informing the user that they deleted the review via alert message


| Status | **Approve Book Page - User Logged Out**
|:-------:|:--------|
| &check; | That if the user tries to access the approve book url that they are redirected to the login page


| Status | **Approve Book Page - User Logged In**
|:-------:|:--------|
| &check; | That if the user tries to access the approve book url that they are redirected to the 403 forbidden page

| Status | **Approve Book Page - Admin User Logged In**
|:-------:|:--------|
| &check; | That the book title, author, blurb and genre fields are visible to the admin
| &check; | That the all the fields are pre filled with the information that was originally added
| &check; | That none of the fields can be submitted empty or with just blank spaces if the admin deletes the information
| &check; | That all the fields are required fields
| &check; | Clicking the Approve Book Listing button, changes the approved status of the book to True and if any changes were made to the book, updates the database with the changes made
| &check; | That if the book is approved, the user is redirected to the Admin Only page and an alert message informs the admin that the book was approved successfully, and that the book is successfully added to the approved book lists across the website and removed from the Book Approvals list on the Admin Only page
