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
| &check; | That if you provide just the username field the user cannot log in and user feedback is provided
| &check; | That if you provide just the password field the user cannot log in and user feedback is provided
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
| &check; | That if you provide just the username field the user cannot sign up and user feedback is provided
| &check; | That if ypu provide just the password field the user cannot sign up and user feedback is provided
| &check; | That if you provide the username and one password field the user cannot sign up and user feedback is provided
| &check; | That if you provide a username and password that is too similiar that the user cannot sign up and user feedback is provided
| &check; | That if you rpassword doesn't match in both password fields, the user cannot sign up and user feedback is provided
| &check; | That if the user provides a password less that 8 character, the user cannot sign up and user feedback is provided
| &check; | That if you provide a good username and password but the email field does not contain a proper email address, the user cannot sign up and user feedback is given
| &check; | That if the user a good username and a good password but leaves the email field empty, the user can sign up
| &check; | That if the user provides a good username, a good password and a good email address, the user can sign up
| &check; | Clicking the Sign Up button signs the user up and logs the user in if the correct user information was provided for sign up
| &check; |That when the user signs up, they are redirevted to the home page and an alert message informs the user that they sisgned up successfully
| &check; |That when the user signs up and is logged in successfully their username will appear in the navbar indicating their logged in status

| Status | **Sign Up Page - User Logged In**
|:-------:|:--------|
| &check; | That the user cannot access the signup tab from the navbar if they have logged in
| &check; | That if the user tries to type in the url of the sign up page, when they are logged in they are redirected to the home page
