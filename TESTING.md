# Testing

## Table of Contents

* [Testing user stories](#testing-user-stories)
* [Manual Testing](#manual-testing)
* [Validator Testing](#validator-testing)
  * [W3C HTML Validator](#w3c-html-validator)
  * [W3C CSS Validator](#w3c-css-validator)
  * [JSHint JavaScript validator](#jshint-javascript-validator)
  * [Python Validation](#python-validation)
* [Lighthouse Testing](#lighthouse-testing)
* [Browser Compatibility Testing](#browser-compatibility-testing)
* [Tools Testing](#tool-testing)
* [Bugs](#bugs)
  * [Resolved Bugs](#resolved-bugs)
  * [Unresolved Bugs](#unresolved-bugs)

## Testing User Stories

### Epic 1 - Shopping Experience

#### As a shopper, I want to easily find the products and their details

* Products page is available, displaying the products and their main details.

#### As a shopper, I want to view products on a specific category

* Links to each product category are provided in the home page.
* A product navigation bar is present in the products page, allowing the shopper to filter products per category.

#### As a shopper, I want to be able to sort the products depending on their price, rating or category
  
* A sorting functionality is provided in the products page, allowing the shopper to sort products by price, name, rating and category.

#### As a shopper, I want to be able to search for products using specific keywords

* A search bar is available on the website header, allowing the shopper to find a product by keyword across the whole website.

#### As a shopper, I want to easily select the quantity of products to be purchased

* Quantity field is available in the product details page, allowing the shopper to select the desired product quantity before adding the product to the shopping bag.

#### As a shopper, I want to easily view the current purchase amount

* The current purchase amount is available under the shopping cart icon in the header, making the information available across the whole website.
  
### Epic 2 - Shopping Bag and Checkout

#### As a shopper, I want to view all items currently on my shopping bag and be able to update them

* Products added to the shopping bag are displayed in the shopping bag page.
* A quantity form is available in the shopping bag page for the shopper to update the product quantity.

#### As a shopper, I want to easily provide my shipping and payment information during the checkout

* A form is available at the checkout for the shopper to provide the necessary information to complete the purchase.

#### As a shopper, I want to feel my personal and payment data is being handled securely

* Stripe payments has been implemented as a payment method for the website in order to provide secure and easy transactions for the shoppers.

#### As a shopper, I want to receive an order confirmation once I have finished my purchase

* A checkout success page is displayed to the shopper after completing the purchase.

#### As a shopper, I want to receive an order confirmation email for my records

* An email is being sent to the email address provided by the shopper during the checkout.  

### Epic 3 - shopper Accounts

#### As a frequent shopper, I want to be able to register an account using my email address to be able to keep my records and interact with the website

* All-auth has been implemented to handle user authentication, allowing the user to register an account.

#### As a frequent shopper, I want to receive a confirmation once my account has been registered to make sure the information entered was correctly

* A confirmation is sent to the registered email address in order to validate it.

#### As a registered shopper, I want to easily log in and out from my account

* All-auth has been implemented to handle user authentication, allowing the user to easily login and logout from their account.

#### As a registered shopper, I want to have a personalized profile page where I can keep my contact information updated and see my past orders

* A profile page is available for the shopper to keep their contact information updated as well as access their past orders.

### Epic 4 - Product Reviews

#### As a shopper, I want to be able to read product reviews left by other shoppers

* Product reviews are available in the product details page for each product.

#### As a registered shopper, I want to be able to leave product reviews and rate the products

* Forms are available for registered shoppers if to review and rate products.

* Registered shoppers are also able to update or delete their existing reviews.

### Epic 5 - Product Admin

#### As a site admin, I want to be able to add and update products

* Full CRUD functionality has been implemented for site admins to manage the website products.
* As a site admin, I want to be able to remove product no longer available.
Full CRUD functionality has been implemented for site admins to manage the website products.

### Epic 6 - Newsletter Subscription

#### As a site admin, I want shoppers to be able to provide their contact information to be able to reach out to them with information and offers

* A newsletter subscription form had been added to the website footer, making it available for the shoppers across the whole website.
  
### Epic 7 - Contact

#### As a Shopper, I can see an option to contact the owner of the site for inquiries

* The shopper can see the option to fill out a contact form so that I can get in touch with the site owner directly.

## Manual Testing

### General

  | Element | Expected Outcome |Pass/Fail |
  | --- | --- | --- |
  | Main Logo Link | Clicking the link redirects to the home page | Pass |
  | Shop Link | Clicking the link redirects to the products page | Pass |
  | Search Bar | Clicking the link redirects to the products page and display the matching products | Pass |
  | My Account Icon - Register Link | Clicking the link redirects to the account sign up page | Pass |
  | My Account Icon - Login Link | Clicking the link redirects to the account sign in page | Pass |
  | My Account Icon - Logout link | Clicking the link redirects to the account sign out page. | Pass |
  | My Account Icon - Product Management Link | Clicking the link redirects superuser/admin to the add product page | Pass |
  | My Account Icon - My Profile Link | Clicking the link redirects to the profile page | Pass |
  | Shopping Cart Icon | Clicking the link redirects to the shopping cart | Pass |
  | Facebook Icon | Clicking the link open the business Facebook page on a separate tab | Pass |
  | Privacy Policy Link | Clicking the link opens the privacy policy page | Pass |
  | Terms & Condition Link | Clicking the link opens the terms & condition page | Pass |
  | Delivery Policy Link  | Clicking the link opens the delivery policy page | Pass |
  | Newsletter Form | Email address gets registered to the database when submitting the form | Pass |

### Navbar 

| Element | Expected Outcome |Pass/Fail |
| Home Link | Clicking on home link opens the homepage | Pass |
| View a category of products/filter products  | When a user clicks on a category, they are then provided a dropdown with a breakdown of items within the chosen category. If a user choses the view all link, the page will display all items but the user will also be given the choice to refine the products shown via links to the sub-categories at the top of the page | Pass |
| Sort the list of available products | Users may view products bases on their price, rating or category from the navbar by selecting all products and then the option they want from the dropdown | Pass |


## Validator Testing

* ### W3C HTML Validator

  #### Home Page

  ![home Page](/documentation/testing/html-validator-home.png)

  #### Privacy Page
   
  ![privacy page](/documentation/testing/html-validator-privacy.png)

  #### Delivery Page

  ![delivery page](/documentation/testing/html-validator-delivery.png)

  #### Terms Page

  ![terms page](/documentation/testing/html-validator-term.png)

  #### Product Page

  ![product page](/documentation/testing/html-validator-products.png)

  #### Product Detail Page

  ![product detail page](/documentation/testing/html-validator-product-detail.png)

  #### Add Product Page

  ![add product page](/documentation/testing/html-validator-add-product.png)

  #### Edit Product Page

  ![edit product page](/documentation/testing/html-validator-edit-product.png)

  * The add and edit product page shows two errors. These are because the image upload widget and changing this code breaks the field.

  #### Bag Page

  ![bag page](/documentation/testing/html-validator-bag.png)

  #### Checkout Success Page

  ![checkout success Page](/documentation/testing/html-validator-checkout-success.png)

  #### Contact Page

  ![contact page](/documentation/testing/html-validator-contact.png)

  #### Contact Success Page

  ![contact success Page](/documentation/testing/html-validator-contact-success.png)

  #### Profile Page

  ![Profile Page](/documentation/testing/html-validator-profile.png)

  #### 404 page

  ![404 Page](/documentation/testing/html-validator-404.png)

* ### W3C CSS Validator

  [W3C](https://jigsaw.w3.org/css-validator/) was used to validate the CSS. All pages now pass with no errors.

   * static/base.css
   * checkout/static/checkout/css/checkout.css
   * profiles/static/profiles/css/profile.css

   ![css validator](/documentation/testing/css-validator.png)

* ### JSHint JavaScript validator

  JS Hint was used to validate the JavaScript. It found a total of 6 warnings concerning missing or unnecessary semicolons. These warnings were corrected.

  * #### Products

   ![product page](/documentation/testing/jshint-products.png)

  * #### Profiles

   ![country field](/documentation/testing/jshint-profiles.png)

  * #### Bag

    ![update quantity & remove item](/documentation/testing/jshint-bag.png)

  * #### Checkout

    ![stripe](/documentation/testing/jshint-checkout.png)   

* ### Python Validation

  [Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python, returned a number of whitespace and indentation errors which were rectified where possible.

  * custom_storages.py
  * shines_schoolsuplies/settings.py
  * shines_schoolsupplies/urls.py
  * shines_schoolsupplies/views.py
  * home/urls.py
  * home/views.py
  * products/admin.py
  * products/forms.py
  * products/models.py
  * products/urls.py
  * products/views.py
  * products/widgets.py
  * bag/contexts.py
  * bag/urls.py
  * bag/views.py
  * bag/templatetags/bag_tools.py
  * checkout/admin.py
  * checkout/apps.py
  * checkout/forms.py
  * checkout/models.py
  * checkout/signals.py
  * checkout/urls.py
  * checkout/views.py
  * checkout/webhook_handler.py
  * checkout/webhooks.py
  * profiles/forms.py
  * profiles/models.py
  * profiles/urls.py
  * profiles/views.py
  * reviews/admin.py
  * reviews/forms.py
  * reviews/models.py
  * reviews/urls.py
  * reviews/views.py
  * contact/admin.py
  * contact/forms.py
  * contact/models.py
  * contact/urls.py
  * contact/views.py
  * newsletter/admin.py
  * newsletter/contexts.py
  * newsletter/forms.py
  * newsletter/models.py
  * newsletter/urls.py
  * newsletter/views.py

## Lighthouse Testing

I have used Googles Lighthouse testing to test the performance, accessibility, best practices and SEO of the site.

### Home page

  ![Home Page](/documentation/testing/lighthouse-desktop-home.png)

### Product page

  ![Product Page](/documentation/testing/lighthouse-desktop-products.png)

### Product Detail page

  ![product Detail Page](/documentation/testing/lighthouse-desktop-product-detail.png)

### Checkout page

  ![Checkout Page](/documentation/testing/lighthouse-desktop-checkout.png)


### Checkout Success Page

  ![Checkout Success Page](/documentation/testing/lighthouse-desktop-checkout-success.png)

### Shopping Bag Page

  ![Shopping bag Page](/documentation/testing/lighthouse-desktop-home.png)

### Add Product Page

  ![Add product page](/documentation/testing/lighthouse-desktop-add-product.png)

### Edit Product Page

  ![Edit Product Page](/documentation/testing/lighthouse-desktop-edit-product.png)

### Profil Page

  ![Profile Page](/documentation/testing/lighthouse-desktop-profile.png)

### Contact Page

  ![Contact Page](/documentation/testing/lighthouse-desktop-contact.png)

### Contact Success Page

  ![Contact Success Page](/documentation/testing/lighthouse-desktop-contact-success.png)

### Privacy Page

  ![Privacy Page](/documentation/testing/lighthouse-desktop-privacy.png)

### Delivery Page

  ![Delivery Page](/documentation/testing/lighthouse-desktop-delivery.png)

## Browser Compatibility Testing

## Tool Testing

## Bugs

* ### Resolved Bugs

* ### Unresolved Bugs