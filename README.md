# Shines School Supplies

 ![main image](/documentation/readme/main-image.png)

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
    * [Database Schema](#database-schema)
  * Skeleton
    * Wireframes
  * [Surface](#surface)
    * [Color Schema](#color-schema)
    * [Typography](#typography)
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
* [Deployment](#deployment)
  * [How To Use This Project](#how-to-use-this-project)
  * [Deployment to Heroku](#deployment-to-heroku)
  * [AWS Bucket Creation](#aws-bucket-creation)
  * [Connect Django to AWS Bucket](#connect-django-to-aws-bucket)
* [Testing](#testing)
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)
  
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

### Structure

#### Database Schema

  The database model has been designed using [dbdiagram.io](https://dbdiagram.io/home).

  ![er diagram](/documentation/readme/erd-img.png) 

### Surface

### Color Schema
 
  * Mostly white and black colour was used in this website.
  * #00827F was used for delivery banner
  * #706563 was used when links hovered.
  * red and green are used for edit and delete link

   ![colour palette](/documentation/readme/color-palette.png)
   
### Typography 

  The font used across the site is Oswald an Lato. It was used in different weights.

  After some research on popular ecommerce business fonts. We decided to go with Oswald and Lato for its simplicity, which makes it easy to read but at the same time being attention-grabbing.


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

## Deployment

  The project was developed using [GitPod](https://gitpod.io/workspaces) workspace. The code was commited to [Git](https://git-scm.com/) and pushed to [GitHub](https://github.com/) using the terminal. The web application is deployed on Heroku as Github Pages is not able to host a Python project. Static and media files are being stored in AWS S3. The repository is hosted on Github.

### How To Use This Project

  To use and further develop this project you can either fork or clone the repository.

#### Fork GitHub Repository

  By forking the GitHub repository you can make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original repository, by using the following steps:

  1. Log in to GitHub.
  2. Navigate to the main page of the GitHub Repository that you want to fork.
  3. At the top right of the Repository just below your profile picture, locate the "Fork" button.
  4. You should now have a copy of the original repository in your GitHub account.
  5. Changes made to the forked repository can be merged with the original repository via a pull request.

#### Clone Github Repository

  By cloning a GitHub repository you can create a local copy on your computer of the remote repository. The developer who clones a repository can synchronize their copy of the codebase with any updates made by fellow developers with push or pull request. Cloning is done by using the following steps:

  1. Log in to GitHub.
  2. Navigate to the main page of the GitHub Repository that you want to clone.
  3. Above the list of files, click the dropdown called "Code".
  4. o clone the repository using HTTPS, under "HTTPS", copy the link.
  5. Open Git Bash.
  6. Change the current working directory to the location where you want the cloned directory to be made.
  7. Type git clone, and then paste the URL you copied in Step 4.
      $ git clone https://github.com/YOUR-USERNAME/YOUR-
  8. Press Enter. Your local clone will be created.

      $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
      > Cloning into `CI-Clone`...
      > remote: Counting objects: 10, done.
      > remote: Compressing objects: 100% (8/8), done.
      > remove: Total 10 (delta 1), reused 10 (delta 1)
      > Unpacking objects: 100% (10/10), done.   

    Changes made on the local machine (cloned repository) can be pushed to the upstream repository directly if you have a write access for the repository. Otherwise, the changes made in the cloned repository are first pushed to the forked repository, and then a pull request is created.

#### Project Set Up After Forking or Cloning

  1. Install all dependencies by typing in the CLI pip3 install -r requirements.txt

  2. Create a .gitignore file and env.py file in the project's root directory. Add the env.py file to .gitignore.

  3. Inside the env.py file, enter the project's environment variables:

    import os

    os.environ.setdefault("SECRET_KEY", <your_secret_key>)
    os.environ.setdefault("DEVELOPMENT", '1')
    os.environ.setdefault("STRIPE_PUBLIC_KEY", <your_key>)
    os.environ.setdefault("STRIPE_SECRET_KEY", <your_key>)
    os.environ.setdefault("STRIPE_WH_SECRET", <your_key>)
   
    You can get the keys from:

    * "SECRET_KEY" can be generated using Django Secret Key Generator.

    * "STRIPE_PUBLIC_KEY" and "STRIPE_SECRET_KEY" can be generated by creating a stripe account. The keys are found in 'Developers' Section, under 'API Keys'.
    
    * In the Developer Section, under 'Webhooks', add a new endpoint. "STRIPE_WH_SECRET". On Endpoint  
      URL, enter:
       https://<your_host_url>/checkout/wh/
      Select to listen to all events, and create endpoint, and you can view your "STRIPE_WH_SECRET".
    
    * We can now adjust the DEBUG variable to only set DEBUG as true if in development:

        DEBUG = 'DEVELOPMENT' in os.environ

  4. Make migrations to setup the inital database operations.

     python3 manage.py makemigrations 
     python3 manage.py migrate

  5. Load data for the database or create data manually.

     python3 manage.py loaddata <app_name>

  6. Create a super user.

     python3 manage.py create superuser

  7. Save, add, commit and push these changes.

  The project should now complete to run and can now be used for development. To run the project, type in the CLI terminal: python3 manage.py runserver 

### Deployment to Heroku

  This project is deployed on Heroku for production, with all static and media files stored on AWS S3. These are steps to deploy on Heroku:

  1. Navigate to Heroku.com, create a new account or login if you already have an account. On the dashboard page, click "Create New App" button. Give the app a name, the name must be unique with hypens between words. Set the region closest to you, and click "Create App".

  2. On the resources tab, provision a new Heroku Postgres database.

  3. Configure variables on Heroku by navigating to Settings, and click on Reveal Config Vars. You may not have all the values yet. Add the others as you progress through the steps.

  | Variables | Keys |
  | --- | --- |
  | AWS_ACCESS_KEY_ID | your_access_key_id_from_AWS |
  | AWS_SECRET_ACCESS_KEY | your_secret_access_key_from_AWS |
  | DATABASE_URL | your_database_url |
  | EMAIL_HOST_PASS | your_app_password_from_your_email |
  | EMAIL_HOST_USER | your_email_address |
  | SECRET_KEY | your_secret_key |
  | STRIPE_PUBLIC_KEY | your_stripe_public_key |
  | STRIPE_SECRET_KEY | your_stripe_secret_key |
  | USE_AWS | True |

  4. If you haven't install it, install dj_database_url and psycopg2.

       pip3 install dj_database_url==0.5.0 psycopg2

    Note: you don't have to do this if you've installed all dependencies in the requirements.txt file.

  5. In settings.py underneath import os, add import dj_database_url

  6. Find the section for DATABASES and comment out the code. Add the following code below the commented out database block, and use the URL copied from elephantSQL for the value:

   (NOTE! don't delete the original section, as this is a temporary step whilst we connect the external database. Make sure you don't push this value to GitHub - this value should not be saved to GitHub, it will be added to the Heroku config vars in a later step, this is temporary to allow us to migrate our models to the external database)

       DATABASES = {
         'default': dj_database_url.parse('paste-elephantsql-db-url-here')
       }

  7. In the terminal, run the show migrations command to confirm connection to the external database:

      python3 manage.py runserver
   
  8. Run migrations

     python3 manage.py migrate

  9. You should now be able to go to the browser tab on the left of the page in elephantsql, click the table queries button and see the user you've just created by selecting the auth_user table.

  10. We can now add an if/else statement for the databases in settings.py, so we use the development database while in development (the code we commented out) - and the external database on the live site (note the change where the db URL was is now a variable we will use in Heroku):

     if 'DATABASE_URL' in os.environ:
        DATABASES = {
           'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
     else:
        DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.sqlite3',
               'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
            }
        }

  11. Install gunicorn which will act as our webserver and freeze this to the requirements.txt file:

   pip3 install gunicorn
   pip3 freeze > requirements.txt

  12. Create a Procfile in the root directory. This tells Heroku to create a web dyno which runs gunicorn and serves our django app. Add the following to the file (making sure not to leave any blank lines underneath):

       web: gunicorn seaside_sewing.wsgi:application

  13. Log into the Heroku CLI in the terminal and then run the following command to disable
  collectstatic. This command tells Heroku not to collect static files when we deploy:

       heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name-here

  14. We will also need to add the Heroku app and localhost (which will allow GitPod to still work) to ALLOWED_HOSTS = [] in settings.py:

     ALLOWED_HOSTS = ['{heroku deployed site URL here}', 'localhost' ]

  15. Save, add, commit and push the changes to GitHub. You can then also initialize the Heroku git remote in the terminal and push to Heroku with:

  heroku git:remote -a {app name here}
  git push heroku master

  16. You should now be able to see the deployed site (without any static files as we haven't set these up yet).

  17. To enable automatic deploys on Heroku, go to the deploy tab and click the connect to GitHub button in the deployment method section. Search for the projects repository and then click connect. Click enable automatic deploys at the bottom of the page.

### AWS Bucket Creation

   All static and media files in this project are stored in Amazon Web Services S3 bucket which is a cloud based storage service. You can create your own bucket by following these steps:

   1. Go to Amazon Web Service website and click on Create An AWS Account, or login if you already have an account.
   2. Login to your new account, go to AWS Management Console and find service S3. Click on Create Bucket.

       * Give it a name (I recommend naming your bucket to match the Heroku app name), and choose region 
         closest to you.
     
       * In Object Ownership section, choose ACLS enabled. and Bucket Owner Preffered.
     
       * Uncheck box 'Block All Public Access'.
       
       * Check box 'I acknowledge that the current settings might result in this bucket and the objects 
         within becoming public.'
     
       * Click on Create Bucket, and your bucket is created.
   
   3. Click on your newly created bucket, and navigate to the Properties tab. Scroll down to the bottom until you find Static Website Hosting. Click on Edit, then enable.
      
       * Hosting type: choose Host a Static Website
       * Index document: index.html
       * Error document: error.html
       * Click on Save Changes.
   
   4. Navigate to the Permissions tab. Scroll down to the bottom until you find Cross-origin resource sharing (CORS). Click on Edit, and paste in this Cors Configuration below, which is going to set up the required access between the Heroku app and this S3 bucket. Click on Save Changes.

    [
      {
        "AllowedHeaders": [
        "Authorization"
        ],
        "AllowedMethods": [
           "GET"
        ],
        "AllowedOrigins": [
           "*"
        ],
        "ExposeHeaders": []
      }
    ]

      Still on the Permissions tab, find Bucket policy, click on Edit, and then go to Policy Generator.

       * Select Type of Policy: choose S3 Bucket Policy
   
       * Effect: choose Allow
     
       * Principal: *
     
       * Actions: select GetObject
     
       * Fill in the Amazon Resource Name (ARN), from the Bucket ARN back in the Bucket Policy
     
       * Click on the Add Statement and then Generate Policy. Copy the policy and paste in the bucket policy editor.
     
       * Add a slash star on to the end of the resource key (because we want to allow access to all    resources in this bucket). Click Save. The resource key should look like this 

         "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*", 

     Still on Permissions tab, go to Access Control List (ACL) section, click Edit and enable List for Everyone (public access), and accept the warning box.

  5. With the bucket ready, now we need to create a user to access it through another service called IAM which stands for Identity and Access Management. Go back to the service menu and open IAM.

     a. Create a group for our user to live in.
         Click User Groups, and then create a new group with a name you want. I gave the group the name: manage-shoes-and-more. Scroll down to the bottom and click on Create Group. 

     b. Create an access policy giving the group access to the S3 bucket that has been created.
      
      * Click on Policy, and then Create Policy. Go to the JSON tab, and then select import managed policy, which will let us import one that AWS has pre-built for full access to S3. Search for S3, then import the AmazonS3FullAccess policy.
      
      * Because we only want to allow full access to our new bucket and everything within it, paste the bucket ARN (from the bucket policy page in s3) in the JSON editor.
       
      "Resource": [
         "arn:aws:s3:::YOUR_BUCKET_NAME",
          "arn:aws:s3:::YOUR_BUCKET_NAME/*"
      ]

       Now click on Next:Tags, then click Next:Review.

      * Give the review policy a name and a description, then click Create Policy. The policy has now been created.

     c. Finally, assign the user to the group so it can use the policy to access all our files.

       * Go to User Groups, and select the group. Go to the Permissions tab, open the Add Permissions dropdown, and click Attach Policies.

       * Select the policy and click Add permissions at the bottom.
       
       * Create a user to put in the group, by going to the Users page, and clicking Add Users.
       
       * Set a user name, give them access type: Programmatic access, and then click Next: Permissions.
       
       * Check on the group that has the policy attached. Click Next: Tags, then click Next: Review, and lastly Create User.
       
       * Download the csv file and save it.     

### Connect Django to AWS Bucket

   Note: If you've forked the repository, all of these steps are already done/ written on the files. Make sure you've installed all dependencies in the requirements.txt file, add all the AWS-related Config Vars to Heroku, and remove the DISABLE_COLLECTSTATIC variable from Heroku.

   Here are the steps I took to connect Django to AWS:

   1. Install two new packages: boto3 and django-storages. Freeze them into requirements.txt.
      pip3 install boto3
      pip3 install django-storages 
      pip3 freeze > requirements.txt

   2. Add storages to the Installed Apps in settings.py.

   3. In settings.py, we need to set cache control, set bucket configurations, set static and media files location, and override static and media URLs in production. We'll only want to do this on Heroku, so add an if statement as well.
   
     if 'USE_AWS' in os.environ:
         # Cache control
         AWS_S3_OBJECT_PARAMETERS = {
             'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
             'CacheControl': 'max-age=94608000',
         }

         # Bucket Config
         AWS_STORAGE_BUCKET_NAME = 'YOUR_BUCKET_NAME'
         AWS_S3_REGION_NAME = 'YOUR_REGION'
         AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
         AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
         AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

         # Static and media files
         STATICFILES_STORAGE = 'custom_storages.StaticStorage'
         STATICFILES_LOCATION = 'static'
         DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
         MEDIAFILES_LOCATION = 'media' 

         # Override static and media URLs in production
         STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
         MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

   Set the Config Vars on Heroku. On your app's dashboard on Heroku, go to Settings and click Reveal Config Vars. Set this variables:

  | Variables | Keys |
  | --- | --- |
  | AWS_ACCESS_KEY_ID | your access key id from the csv file that you've downloaded before |
  | AWS_SECRET_ACCESS_KEY | your secret access key from the csv file that you've downloaded before |
  | USE_AWS | True |

  Also remove the COLLECTSTATIC variable from the Config Vars.
 
  4. We then want to tell Django that in production we want to use S3 to store our static files whenever someone runs collectstatic, and that we sent any uploaded images to go there as well.
  Create a custom_storages.py file in your project's root directory, and inside it, include the Static and Media Storage locations:

    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage

  
    class StaticStorage(S3Boto3Storage):
       location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
       location = settings.MEDIAFILES_LOCATION

  5. Finally, push these changes on Github.

    git add .
    git commit -m "Your commit message"
    git push

## Testing

   The testing documentation can be found [here](TESTING.md)

## Credits

### Code Used

  The code in Code Institute's video on the Boutique Ado project was used as the main reference point to set up an e-commerce / online store project using HTML, CSS, JS, Python+Django, ElephantSQL database, Stripe, and AWS S3 as storage.

### Content

  The content for this project is taken from

   * [ABC School Supplies](https://www.abcschoolsupplies.ie/?gclid=Cj0KCQjw7PCjBhDwARIsANo7CglAGDpgxipgGP4vQhznS5fJmmvWQO3lgKysP8uecmONKUUevo0AQx4aAn2xEALw_wcB)
   * [Eason](https://www.easons.com/?gclid=Cj0KCQjw7PCjBhDwARIsANo7CgmTR5Eo5h_35IJIcsUwndJb-WElKtQP1eJPuv0NyhHpghPuLXG5EPgaAkcPEALw_wcB)

### Media

  Photos used in this project taken from [Pexels](https://www.pexels.com/) and [unsplash](https://unsplash.com/)

### Acknowledgments

  The Shines School Supplies was created as my fifth portfolio project. I would like to thank my mentor Marcel Mulders for his helpful feedback and encouragement throughout the development process. I would also like to thank tutor of code institute for their support. I'd like to thank fellow Code Institute students in May 2022 class at code institute.

  Dania Khanam
