# NegarKhodro

This is an assignment task for NegarKhodro company.

## Installation

- install dependencies: `pip install -r requirements.txt`
- make migrations: `python manage.py makemigrations`
- migrate: `python manage.py migrate`
- run: `python manage.py runserver`
- now you can access in `localhost:8000/tree`

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