# autotrade-sales-api
## Local testing instructions
In order to start the application, follow these steps in the root directory of
your local repository with an active virtual environment:
- Rename ```.env.template``` to ```.env``` in root directory.
- Run the commands:
    ```
    docker-compose up -d db
    ```

    ```
    pip3 install -r requirements.txt
    ```

    ```
    uvicorn src.interface_adapters.fastapi.main:app --host 0.0.0.0 --port 8001 --reload
    ```

Then the documentation should be available at http://localhost:8001/docs
