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
  * Profile Page
  * Reviews Page
  * Contact Page
  * Newsletter
  * Accounts Pages
  * Privacy Page
  * Terms Page
  * Delivery Page
  * 404 Error Page
* Technologies Used
  * Languages Used
  * Libraries and Frameworks
  * Packages / Dependencies Installed
  * Database Management
  * Payment Service
  * Cloud Storage
  * Tools and Programs
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

## Testing

   The testing documentation can be found [here](TESTING.md)
