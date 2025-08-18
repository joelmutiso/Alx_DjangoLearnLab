# Permissions and Groups

## Custom Permissions
Defined in `Book` model (bookshelf/models.py):
- can_view
- can_create
- can_edit
- can_delete

## Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## Enforcement
Views in `bookshelf/views.py` are protected using @permission_required.
