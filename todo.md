# todo

* create a Django form for creating and updating characters.
This will allow you to easily render a form in your template that users can use to input character data. 
You can do this by defining your form in a Django app's forms.py file.

* create a Django view and template for the character list page.
This view should handle the logic for querying the database for a list of the user's characters, 
and render a template that displays this list.
You can do this by defining your view in a Django app's views.py file,
and creating a corresponding template in your app's templates directory.

* create a Django view and template for the character detail page. 
This view should handle the logic for querying the database for a specific character, 
and render a template that displays the character's data. 
You can do this by defining your view in a Django app's views.py file, 
and creating a corresponding template in your app's templates directory.

* create the spell tables. You can use a library like django-tables2 to do this. 
You'll need to create a Django view and template for each of the spell tables, 
and use django-tables2 to render the table in the template.

* add some logic for handling AJAX requests for adding, preparing, and using spell slots.
You can do this by defining some Django views that handle these requests and update the database accordingly.

## tests

Here are some tests that you might consider writing for each piece of functionality:

    For the character list page:
        Test that the view returns a list of the user's characters
        Test that the template correctly displays the list of characters
    For the character detail page:
        Test that the view returns the correct character data
        Test that the template correctly displays the character data
    For the spell tables:
        Test that the table correctly displays the relevant spells
        Test that the table can be filtered, sorted, and searched as expected
    For the AJAX functionality:
        Test that adding, preparing, and using spell slots updates the database correctly
        Test that the page is correctly updated when a spell is added, prepared, or used


