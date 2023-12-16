from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a basic route
@app.get('/')
def read_root():
    return {
        'success': True,
        'message': 'Hello World'
        }

# Run the application using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
