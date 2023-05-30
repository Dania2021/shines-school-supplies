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

#### As a shopper, I want to easily find the products and their details.
  * Products page is available, displaying the products and their main details.

#### As a shopper, I want to view products on a specific category.
  * Links to each product category are provided in the home page.
  * A product navigation bar is present in the products page, allowing the shopper to filter products per category.

#### As a shopper, I want to be able to sort the products depending on their price, rating or category.
  * A sorting functionality is provided in the products page, allowing the shopper to sort products by price, name, rating and category.

#### As a shopper, I want to be able to search for products using specific keywords.
  * A search bar is available on the website header, allowing the shopper to find a product by keyword across the whole website.

#### As a shopper, I want to easily select the quantity of products to be purchased.
  * Quantity field is available in the product details page, allowing the shopper to select the desired product quantity before adding the product to the shopping bag.

#### As a shopper, I want to easily view the current purchase amount.
  * The current purchase amount is available under the shopping cart icon in the header, making the information available across the whole website.
  
### Epic 2 - Shopping Bag and Checkout

#### As a shopper, I want to view all items currently on my shopping bag and be able to update them.
  * Products added to the shopping bag are displayed in the shopping bag page.

  * A quantity form is available in the shopping bag page for the shopper to update the product quantity.

#### As a shopper, I want to easily provide my shipping and payment information during the checkout.
  * A form is available at the checkout for the shopper to provide the necessary information to complete the purchase.

#### As a shopper, I want to feel my personal and payment data is being handled securely.
  * Stripe payments has been implemented as a payment method for the website in order to provide secure and easy transactions for the shoppers.

#### As a shopper, I want to receive an order confirmation once I have finished my purchase.
  * A checkout success page is displayed to the shopper after completing the purchase.

#### As a shopper, I want to receive an order confirmation email for my records.
  * An email is being sent to the email address provided by the shopper during the checkout.  
