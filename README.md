# NegarKhodro

This is an assignment task for NegarKhodro company.

## Installation

- install dependencies: `pip install -r requirements.txt`
- make migrations: `python manage.py makemigrations`
- migrate: `python manage.py migrate`
- run: `python manage.py runserver`
- now you can access in `localhost:8000/tree`

## User-interface

### Show tree

- open path `/tree/api/tree/<root_node_id>/` (use `root_id` that usually is `1`)
- here you can see tree that rooted by node `root_id`

### Add & List node

- open path `/tree/api/nodes/` that show you all nodes
- in bottom of page you can define your node name and assign parent to it (or you can ignore parent for root nodes)
- click on `POST` bottom to add your new node

### Edit & Delete node

- open path `/tree/api/nodes/<node_id>/` to  your node
- you can press `DELETE` red button to delete your node
- you can edit your node in bottom of page, then click `PUT` to update your node

## API

- Create node:
  - method: `POST`
  - path: `/tree/api/nodes/`
  - data:

    ```jsonc
            {
                "name": <nodeName>,
                "parent": <parentId> // can be null for root nodes
            }
    ```

- Update node:
  - method: `PUT`
  - path: `/tree/api/nodes/<node_id>/`
  - data:

    ```jsonc
    {
        "name": <editedName>,
        "parent": <editedParentID>
    }
    ```

- Delete node:
  - method: `DELETE`
  - path: `/tree/api/nodes/<node_id>/`

- Get node:
  - method: `GET`
  - path: `/tree/api/nodes/<node_id>/`

- List nodes:
  - method: `GET`
  - path: `/tree/api/nodes/`

- Get tree:
  - method: `GET`
  - path: `/tree/api/tree/<root_node_id>/`