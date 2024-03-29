# Backend boilerplate

- one folder named backend to maintain everything at one place
- using fastapi for creating apis
- utilised poetry to manager effiecienty venv, so installed it globally as `pip install poetry`
- we can check the version also through `poetry --version`
- once that is done setup version manager for fastAPI app with `poetry init`
- now all python libraries can be managed easily by poetry for example `poetry add fastapi uvicorn`
- after that just created app.py file with basic architecture something like this - 

    ```python
    from fastapi import FastAPI

    # Create an instance of the FastAPI class
    app = FastAPI()

    # Define a basic route
    @app.get('/')
    def read_root():
        return {
            'success': True,
            'data': 'Hello World'
            }

    # Run the application using Uvicorn
    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)


    ```
- run fastAPI app using `uvicorn app:app --reload` which will result into stating few prints that `app is running on port 8000`
- redirect yourself to hit the link http://localhost:8000. and which will show the response content being designed in root route.
- once you see everything working fine you can go to link http://localhost:8000/doc and for detailed description on rest endpoints we can utilise http://localhost:8000/redoc
- login endpoints will help to receive to authorized token and which will help to update the authorization tab to enable the authentication of all endpoints.




- create models.py to update stuff in there
- do alembic init and update sqlalchemy.url
- above command will also generate alembic folder having env.py file
inside that import the Base from model file
also update the  target_metadata = None to target_metadata = Base.metadata