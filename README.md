# Shines School Supplies

Shines School Suplies is a full stack e-commerce website built using Django, Python, HTML, CSS and JavaScript. The website utilises Stripe as the payment processor.

This version has been built for project 5 of the Code Institute Diploma in Software Development and therefore doesn't accept real payments and any orders made won't be fulfilled.

If you would like to test the payment functionality please feel free to do so by entering the card details below when prompted:

Card number: 4242 4242 4242 4242  Exp: any future date eg. 11/26 CVC: any 3 digits eg 123

Live Site: [Shines School Supplies](https://shine-school-supplies.herokuapp.com/)

## Table Of Contents

* [User Experience (UX)](#user-expeienceux)
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
* Features
  * General
  * Home Page
  * Products Page
  * Product Details Page
  * Products Admin
  * Shopping Bag Page
  * Checkout Page
  * Checkout Success Page
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
* Testing
* Credits
  * Code Used
  * Content
  * Media
  * Acknowledgments
  
## User Expeience(UX)

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

  #### User Story
   
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

   ![facebook mockup page](/documentation/readme/fb-mock-img1.png)

   ![facebook mockup page](/documentation/readme/fb-mock-img2.png)

   ![facebook mockup page](/documentation/readme/fb-mock-img3.png)

## Testing

   The testing documentation can be found [here](TESTING.md)
