Permissions and Groups Setup:

Permissions defined in Book model:
- can_view
- can_create
- can_edit
- can_delete

Groups and Permissions:
- Viewers: can_view
- Editors: can_create, can_edit
- Admins: All permissions

Views are protected using @permission_required decorators.
