# Shines School Supplies

Shines School Suplies is a full stack e-commerce website built using Django, Python, HTML, CSS and JavaScript. The website utilises Stripe as the payment processor.

This version has been built for project 5 of the Code Institute Diploma in Software Development and therefore doesn't accept real payments and any orders made won't be fulfilled.

If you would like to test the payment functionality please feel free to do so by entering the card details below when prompted:

Card number: 4242 4242 4242 4242  Exp: any future date eg. 11/26 CVC: any 3 digits eg 123

Live Site: [Shines School Supplies](https://shine-school-supplies.herokuapp.com/)

## Table Of Contents

* [User Experience (UX)](#user-experienceux)
  * [Strategy](#strategy)
    * [Project Goals](#project-goals)
    * [User Goals](#user-goals)
  * [Scope](#scope)
    * [User Stories](#user-stories)
  * [Structure](#structure)
    * Database Schema
  * Skeleton
    * Wireframes
  * Surface
    * Color Schema
    * Typography
* [Marketing](#marketing)
  * [Search Engine Optimisation](#search-engine-optimisation)
  * [xml-sitemap](#xml-sitemap)
  * [Business Model](#business-model)
* [Features](#features)
  * [General Features](#general-features)
  * [Home Page](#home-page)
  * [Products Page](#products-page)
  * [Product Details Page](#product-details-page)
  * [Product Admin](#product-admin)
  * [Shopping Bag Page](#shopping-bag-page)
  * [Checkout Page](#checkout-page)
  * [Checkout Success Page](#checkout-success-page)
  * [Profile Page](#profile-page)
  * [Reviews Page](#reviews-page)
  * [Contact Page](#contact-page)
  * [Accounts Pages](#accounts)
  * [Privacy Page](#privacy-page)
  * [Terms Page](#terms-page)
  * [Delivery Page](#delivery-page)
  * [404 Error Page](#404-page)
* [Technologies Used](#technologies-used)
  * [Languages Used](#technologies-used)
  * [Libraries and Frameworks](#libraries-and-frameworks)
  * [Packages / Dependencies Installed](#packages--dependencies-installed)
  * [Database Management](#database-management)
  * [Payment Service](#payment-service)
  * [Cloud Storage](#cloud-storage)
  * [Tools and Programs](#tools-and-programs)
* Deployment
  * How To Use This Project
  * Deployment to Heroku
  * AWS Bucket Creation
  * Connect Django to AWS Bucket
* [Testing](#testing)
* Credits
  * Code Used
  * Content
  * Media
  * Acknowledgments
  
## User Experience(UX)

### Strategy

  * #### Project goals

    * Shines School Supplies is a Business to Consumer (B2C) e-commerce site.

    * The sites primary audience will be student and people who love art and craft. It will cater to a range of supplies and selling a range of items over different price points.

    * Structure is easy to understand and navigates effortlessly for an easy shopping experience.

    * Customers are offered the opportunity to register an account.

    * Easy shopping process to create a pleaseant experince for the customer.

  * #### User Goals

    ##### Epic 1 - Shopping Experience  

     * As a shopper, I want to view products on a specific category.
     * As a shopper, I want to be able to sort the products depending on their price, rating or category.
     * As a shopper, I want to be able to search for products using specific keywords.
     * As a shopper, I want to easily find the products and their details.
     * As a shopper, I want to easily select the quantity of products to be purchased.
     * As a shopper, I want to easily view the current purchase amount.
    
    ##### Epic 2 - User Accounts

    * As a shopper, I want to be able to register an account to keep my records and interact with the website.
    * As a shopper, I want to receive a confirmation once my account has been registered to make sure the information entered was correctly.
    * As a registered shopper, I want to easily log in and out from my account.
    * As a registered shopper, I want to have a personalized profile page where I can keep my contact information updated and see my past orders.

    ##### Epic 3 - Shopping Bag and Checkout

     * As a shopper, I want to view all items currently on my shopping bag and be able to update them.
     * As a shopper, I want to feel my personal and payment data is being handled securely.
     * As a shopper, I want to easily provide my shipping and payment information during the checkout.
     * As a shopper, I want to receive an order confirmation once I have finished my purchase.
     * As a shopper, I want to receive an order confirmation email for my records.

    ##### Epic 4 - Product Admin

     * As a site admin, I want to be able to add and update products.
     * As a site admin, I want to be able to remove product no longer available.

    ##### Epic 5 - Product Reviews

     * As a shopper, I want to be able to read product reviews left by other shoppers.
     * As a registered shopper, I want to be able to leave product reviews and rate the products.
     * As a registered shopper, I want to update my review.
     * As a registered shopper, I want to delete my review.

    ##### Epic 6 - Newsletter Subscription
   
     * As a site admin, I want shoppers to be able to provide their contact information to be able to reach out to them with information and offers.

    ##### Epic 7 - Contact

     * As a shopper, I can see an option to contact the owner of the site for inquiries.
       
### Scope

The plan for this project was carried out using the Agile Methodology in Github. User Stories were created using issues on git hub. Each user story explicitly explains the purpose of the issues. Each user story is segmented into acceptance criteria and tasks. It was prioritised using GitHub labels with different colors.

7 Epics were created which were then further developed into 30 User Stories. Each story was assigned a classification of Must-Have, Should-Have or Could-Have. Each story was also assigned user story points, based on my best estimation for the time/difficulty of completing each story.

#### User Stories
   
  Using a Kanban board helped to focus on specific tasks and track the project progress.

  ![user story](/documentation/readme/kanban-board-image.png)

  ![user story](/documentation/readme/user-story.png)

## Marketing

  ### Search Engine Optimisation

  To improve the search index rating on Google, research was carried out using a number of tools, such as [Wordtracker](https://www.wordtracker.com/) to search for relevant keywords to use in meta tags in the project head element.

  Search terms such as school supplies and art & craft were used to return popular keywords. A number of short and long tail keywords were then selected and inputted into the head element of base.html.

  The selected keywords are:

  * art
  * craft
  * art & craft
  * stationary
  * school
  * school supplies
  * back to school
  * classroom
  * activity
  * educational
  * coloring

  These keywords remain a work in progress however. As is normal practise, in production these keywords would be monitored via, for example, Google Analytics, to determine which terms are driving traffic to the site.

  These terms could then be added to, or removed as deemed necessary, and with continual improvement and refinement of these over time should utlimately assist in the site ranking higher on Google.

  ### XML Sitemap

   Additionally to help the search engines crawl the website, I've added an XML sitemap file to the main root directory. The file was created using the free service through XML-Sitemaps.com. A sitemap is a way of organizing a website, identifying the URLs and the data under each section. Previously, the sitemaps were primarily geared for the users of the website. However, Google's XML format was designed for the search engines, allowing them to find the data faster and more efficiently.

   A robots.txt file has also be included in the build to tell the search engine crawlers which URLs the crawler can access on this site. This is used mainly to avoid overloading the site with requests.

  ### Business Model

   Shines School Suuplies is a B2C company that offer our school supplies products. Selling directly to consumers means that the site is designed to sell quickly, on impulse, and in smaller quantities aswell as cater to people who may wish to commission a piece. While wholesale is a possible future goal, the website was not yet intended to sell to other businesses. For this reason, a large amount of the functionality is focused on the user experience and the ability to purchase products quickly and effectively.

   Our thought consumers are school students and people who love art & craft.

  #### Marketing Strategy

  Due to our small marketing budget, we have decided to start a Facebook Business page and interact with our customers and bigger organizations. For our buying customers we have made it easy to sign up for our newsletter, in order to make them even more loyal and facilitate for them to share tips and products with their friends and family. There is an image of the Facebook page below and a link to the page [here](https://www.facebook.com/profile.php?id=100092700921305).
  
  The use of paid ads allows the business to target specific demographics and increase brand awareness. 

  Influencers are a great way to increase brand awareness. Free samples could be sent to popular influencers on youtube in exchange for a mention/hashtag/ link in the description. This further helps raise brand awareness because the video could be posted on Facebook and the influencer tagged in the post, which with the help of the Facebook algorithm, would help bring an organic audience to the Facebook page and, hopefully, the store.

  #### Facebook Business page

   ![facebook mockup page](/documentation/readme/fb-img1.png)

   ![facebook mockup page](/documentation/readme/fb-img2.png)

## Features

### General Features

  The website has been designed from a mobile first perspective. Each page of the site shares the following:

  * #### Navbar

   The navbar on the site is split into two sections, the first section contains the main logo, search bar, an account icon and the bag icon. The second section contains the sites products categories. The navbar is fully responsive, and utilises a hamburger menu toggle on smaller screens.

   The Categories links in the navbar when hovered over to give the user feedback that they are selecting that category. A dropdown menu will then show with further options. The account icon also contains a dropdown menu which displays different options depending on whether a user is logged in, and whether the user has a superuser account.


   ![navbar](/documentation/readme/navbar-image.png)

  * #### Footer

    The footer is broken into 4 distinct sections - a section that contains section contains contact information for the site, such as a link to the contact form, and social media links. The second information about the site, such as terms and conditions and policies. The third section contains a newsletter registration form for shopper to subscribe across the whole website. The final section is a disclaimer to let users know this site was created as an educational product and to remind users that no orders will be processed. The footer is fully responsive, and on small screens stacks the sections.

   ![footer](/documentation/readme/footer.png)

### Home Page

  The home page contains background image, a mesage and shop now button. The button for "Shop now" brings the user to the product page.

  ![home page](/documentation/readme/home-page.png)

### Products Page

  The Products page displays the products showing an image (if one is not available a default no image filler image is inserted), the products name, sku, description, price, category and rating. If the user is a superuser there will also be an update and delete link on the right of the product information for ease of editing and deleting products.
  
  At the top left of the products page you will be able to see the number of items on the page, and if you are viewing a category, there will be a link to allow you to easily view all products. If you have performed a search, you will also be shown the search term used here.

  On the top right hand side of the page is a sort by dropdown. This enables the user to sort price and rating in ascending/descending order, and name and category in alphabetical order A-Z or Z-A.

  ![products page](/documentation/readme/products-page.png)

### Product Details Page

  The product detail page gives more details about the chosen item. An image of the product is displayed on the left of medium and large screens, and at the top of small screens.

  To the right on medium and large screens (underneath the image on small screens) is the Product information. The name is displayed followed by the price, category and rating. The description for the product follows and underneath the rating, if the user is a superuser, they will find a set of edit and delete buttons for the product for ease of admin.

  A quantity selector comes next, with plus and minus buttons and a quantity input which allows the user to input their value. The minus quantity button is disabled when the value is 1, and is enabled above this. The plus button is enabled until it reaches 99, and then becomes disabled.

  Users are shown two buttons underneath the quantity selector, one to add the product to the bag cart, and one to go back to the product page. If the user selects the add to cart button, they will be shown a success toast letting them know the product was added to the bag, and then they will be given a quick overview of the items in their bag together with their quantities, the total price excluding delivery, if they have not reached the free delivery threshold they will be given an amount they need to spend to get the free delivery and a button to go to the checkout.

  All reviews the product has received are being displayed on the reviews section at the bottom of the page. A link to leave a review is available at the bottom of the reviews, provide edit and delete link for the logged in user's own reviews.

  ![product detail page](/documentation/readme/product-detail-page.png)

  ![product detail page](/documentation/readme/product-detail-page2.png)

### Product Admin

#### Add Product

  Superusers are also able to add a product directly from the site via the product management link in the account icon dropdown menu. This will provide them with a form to complete for all the various information required to create a product. If a required field is not filled in, the superuser will be shown a tooltip asking them to fill in the required fields. The superuser is shown two buttons at the bottom of the form, one to cancel, which if selected returns the superuser to the products page and an add product button. Once a superuser creates a new item and clicks the add product button they will be shown a success toast letting them know that the product was successfully created, and they will be shown that products product detail page.

  If a regular user tries to view the add product page, defensive programming is in place so that they will be shown an error toast that informs them only administrators have the permissions to perform that activity.

  ![add product page](/documentation/readme/add-product.png)

  ![add product page](/documentation/readme/add-product-img.png)

#### Edit Product

  Superusers are able to edit products directly from the site by clicking the edit button on the products page, or on the product detail page. This will open up the edit product page which will be pre-populated with the products current information. The superuser is given buttons to go back or to update the product. Upon update, they will be shown the product detail page for that product, and a success toast will show letting them know the product they updated was successful.

  If a regular user tries to view the edit product page, defensive programming is in place so that they will be shown an error toast that informs them only administrators have the permissions to perform the activity.

  ![edit product page](/documentation/readme/edit-product.png)

  ![edit product page](/documentation/readme/edit-product-img.png)

#### Delete Product

  If a superuser clicks the delete link, either on the product page or from the product detail page that product gets deleted from the database and the superuser redirected to the products page.

  Regular users trying to manually access the url for product deletion will be shown an error toast informing them that only an administrator has the permissions to perform the task. Users that are not logged into an account will be redirected to the sign in page.

### Shopping Bag page

  The bag page lists all items the user has added to their bag. It displays an image of the item, the product name & sku, the price of the item and the quantity selected and the subtotal for that item. Users are able to adjust the quantity of the item in the bag here, as well as delete the item from their bag.

  At the bottom the user is shown their bag total, the delivery fee and then a grand total. If the user hasn't reached the free delivery threshold, a small piece of text will highlight to the user that they only need to spend the amount shown to get free delivery. Underneath the totals are a keep shopping button and a secure checkout button.

  ![shopping bag](/documentation/readme/shopping-bag.png)

  ![shopping bag](/documentation/readme/shopping-bag-img.png)

### Checkout Page

  The checkout page is broken into two sections, a delivery information section and an order summary section.The delivery information section provides inputs for the user to enter their name, email and phone number, a delivery section contains inputs for the address and a dropdown to select their country. If the user is logged in and has filled out their profile, information from the profile will be pre-populated in this form, for a faster checkout experience. The user is also given a checkbox at the bottom of the delivery information which allows them to save the information they have input in their profile for future use.

  If a user is not signed during checkout, instead of the checkbox, they will be given the options to either create an account or login if they already have one. This is optional - as users can checkout as a guest, however this means that they will not be able to view their previous orders on the site.

  The last section is the payment information section. Payments are processed by Stripe and to facilitate payment, a user needs to input their card details into the payment box. If the details are invalid a warning will be displayed under the payment box giving the user feedback on what the error was.

  Beneath the payment section are an adjust bag button which takes the user back to their bag and a complete order button which processes their payment. Underneath the buttons the user is reminded that their card will be charged the grand total amount.

  The order summary section contains an image, name, quantity and subtotal for each item in the bag, along with an order total, delivery fee and the grand total.

  ![checkout](/documentation/readme/checkout.png)

  ![checkout](/documentation/readme/checkout-img.png)

  When a user clicks the complete order button, a checkout payment overlay is displayed which shows a loading spinner which gives the user feedback that their payment is being processed.

  If there is an error with the delivery information form the user will be taken back to the checkout page and they will be shown an error toast informing them there was a problem with their information and to try again.

### Checkout Success Page

 If the payment is successful the user will then be shown the checkout success page. This lists a summary of their order and lets the user know that an email confirmation has also been sent to the email address shown on the page.

 A button at the bottom of the page allows the user to continue shopping. Users are also show a success toast to let them know that their order has been placed successfully, giving them their order number and confirming an email will be sent to their email address.

 ![checkout success page](/documentation/readme/checkout-success.png)

 ![checkout success page](/documentation/readme/checkout-success-img.png)

#### Order Confirmation Email

  ![order confirmation email](/documentation/readme/order-confirmation-email.png)

### Profile Page

 The profile page is broken into two sections, one for the default delivery information and the second for the order history.

 The default delivery information comprises of the name, address & phone number for the user. The user can update their profile by clicking the update information button and the page will reload with the new information pre-populated in the relevant fields together with a success toast that gives the user feedback that their information has been saved successfully. This saved information will then be used in the checkout to pre-populate the payment form to speed up the checkout process for registered users.

 The order history section contains all the previous orders created by the user. These list the first part of the order number, the date the order was made, the items purchased and the order total. If a user would like to look at an order in more detail they can click on the order number and they will be taken to the checkout success page that lists their order summary, together with an alert toast which informs the user they are looking at a previous order.

 ![profile page](/documentation/readme/profile.png)

 ![profile page](/documentation/readme/profile-img.png)

### Reviews Page

#### Add Review Page

  The add review page provide a form for the registered user to be able to add review to the product. This page has two buttons, one is cancel button and the other is add product button.

  ![add review page](/documentation/readme/add-review.png)

  ![add review page](/documentation/readme/add-review-img.png)

  ![profile page](/documentation/readme/profile-img.png)

#### Edit Review Page

  The edit review page provide a prefilled form for the registered user to be able to update their existing reviews.

  ![edit review page](/documentation/readme/edit-review.png)

  ![edit review page](/documentation/readme/edit-review-img.png)

  ![profile page](/documentation/readme/profile-img.png)

#### Delete Review  

  If a registered user clicks the delete link, on the product detail page that review gets deleted from the database and the user redirected to the product detail page.

### Contact Page

  The contact page gives users an easy way to communicate with the shop, without leaving the site. The form has required fields of name, email and message and an optional field of phone number. Underneath the form the user is given 2 buttons, a back button and a submit form button. The back to shop button takes the user to the products page. If a user is signed in to their account, the contact form will pre-populate the name, email and phone number fields from the users profile if they have been filled in. This prevents a user having to fill out a form that where we already hold the information, which speeds up the process for the user and is good practice.

  ![contact page](/documentation/readme/contact.png)

  ![profile page](/documentation/readme/profile-img.png)

### Accounts

#### Signup Page

  Allow the user to sign up an account for the website.

  ![signup page](/documentation/readme/signup-page.png)

  After signing up verfication email send to their email address.

  ![confirmation email](/documentation/readme/email-verification.png)

#### SignIn Page

  Allow the registered user to sign in with their account.

  ![signin page](/documentation/readme/login.png)

#### Signout Page

  Allow the registered user to sign out from their account.
  
  ![signout page](/documentation/readme/logout.png)	

### Privacy Page 

  The privacy policy page contains a privacy policy created for an e-commerce shop created on the rocket lawyer site. As this project is purely for educational purposes, the privacy policy is not legally binding as Shines School Supplies is not a real shop.

### Terms Page

  The terms and conditions page lists a set of terms and conditions created on the rocket lawyer site for an e-commerce store. As this project is purely for educational purposes, no terms or conditions are legally binding as Shines School Supplies is not a real shop.

### Delivery Page

  The delivery policy sets out information for a delivery policy for the shop.

### 404 Page

   The 404 error page is shown if the page a user is trying to access cannot be found (for example the user enters an incorrect product id in the product url.) Users are asked to use the navigation menu to try again.

   ![404 page](/documentation/readme/404.png)

## Technologies Used

### Languages Used

    HTML, CSS, JavaScript, Python

### Libraries and Frameworks

  * [Django](https://www.djangoproject.com/) was used as web framework.
  * [Django Template](https://jinja.palletsprojects.com/en/3.1.x/) was used as a templating language for Django to display backend data to HTML.
  * [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) was used throughout the website to help with styling and responsiveness.
  * [Google Fonts](https://fonts.google.com/) was used to import the font into the html file, and were used on all parts of the site.
  * [Font Awesome](https://fontawesome.com/) was used throughout the website to add icons for aesthetic and UX purposes.
  * [jQuery](https://jquery.com/) Version 3.6.2 A JavaScript Framework

### Packages / Dependencies Installed

  * [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication, registration, and account management.
  * [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/) was used to control the rendering of the forms.
  * [Django Countries](https://pypi.org/project/django-countries/) was used to provide country choices for use with forms and a country field for models.
  * [Pillow](https://pypi.org/project/Pillow/) was used to add image processing capabilities.
  * [Gunicorn](https://gunicorn.org/) was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.
  * [dj_databsae_url](https://pypi.org/project/dj-database-url/) allows us to utilise the DATABASE_URL variable.
  * [psycopg2](https://pypi.org/project/psycopg2/) - a postgres database adapter which allow us to connect with a postgres database.
  * [Django-storages](https://django-storages.readthedocs.io/en/latest/) - a storage backend library
  * [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Allows connection to AWS S3 bucket.
    
### Database Management

  * sqlite3 for development.
  * [ElephantSQL](https://www.elephantsql.com/) for deployment.

### Payment Service

  [Stripe](https://stripe.com/en-ie) was used to process all online payments transactions.

### Cloud Storage

  [Amazon Web Service S3](https://aws.amazon.com/s3/) was used to store all static and media files in production.

### Tools and Programs

  * [Git](https://git-scm.com/) - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
  * [GitPod](https://gitpod.io/workspaces) - GitPod was used for writing code, committing, and then pushing to GitHub.
  * [GitHub](https://github.com/) - GitHub was used to store the projects code after being pushed from Git.
  * [Heroku](https://id.heroku.com/login) - Heroku was used to deploy the website.
  * [Favicon.io](https://favicon.io/) - To create the favicon.
  * [Balsamiq](https://balsamiq.com/) - Used to create wireframes.
  * [dbdiagram.io](https://dbdiagram.io/home) - Used to create the database schema.
  * [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Chrome DevTools was used during development process for code review and to test responsiveness.
  * [Tiny PNG](https://tinypng.com/) - To compress images 

## Testing

   The testing documentation can be found [here](TESTING.md)
