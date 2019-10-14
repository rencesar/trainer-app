# Kickstart


1. Start dev server without building it

    ```
    $ make start-dev
    ```

1. Start production server without building it

    ```
    $ make start-prod
    ```

1. Stop server
    ```
    $ make stop
    ```

1. Access the nginx container (while running it)
    ```
    $ make ssh-nginx
    ```

1. Access the backend container (while running it)
    ```
    $ make ssh-backend
    ```

1. Access the frontend container (while running it)
    ```
    $ make ssh-frontend
    ```

1. Access the database container (while running it)
    ```
    $ make ssh-db
    ```

1. Build production
    ```
    $ make build-prod
    ```

1. Build dev
    ```
    $ make build-dev
    ```