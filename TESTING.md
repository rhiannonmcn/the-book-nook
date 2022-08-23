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
| &check; | That the average book rating is reflected accurately according to how the user rates/changes their rate
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
| &check; | That when a book is added it is automatically classified as unapproved(False) until changed to otherwise (True) by an admin