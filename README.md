# Creation and editing of posts.
Yatube project extension (hw02_community):
Added static pages / about / author / and / about / tech /.
A paginator is connected, dividing the list of posts by ten per page:
*On the home page.
* On the profile page.
* On the group page.
User page created / <username> /
Created a separate post page / <username> / <post_id> /

Registered Yatube users now have the ability to independently publish posts.
The link "New record" has been added to the header of the site, it is visible only to authorized users and leads to the page / new /
A form for adding a new publication appears on the page / new /
After validating the form and creating a new post, the author is redirected to the main page of the project.

# Added edit post page.
Only the author of this post has the rights to edit a post. The rest of the users are redirected to the post view page.

To generate the edit page, the same HTML template was used as for the new post creation page.

This template has been extended: when editing a post, the title "Add post" is replaced with "Edit post". The inscription on the button for submitting the form depends on the operation: "Add" for a new record and "Save" - ​​for editing.
In the HTML templates for the list of posts and for a single post, the "Edit" link is configured so that it leads to the post edit page.
