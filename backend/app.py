from fastapi import FastAPI
from pydantic import BaseModel, Field
import json

# Create an instance of the FastAPI class
app = FastAPI()


with open("data.json") as json_file:
    file_contents = json_file.read()

print(file_contents)

parsed_json = json.loads(file_contents)

questions = parsed_json["sample_question"]
options = parsed_json["sample_options"]
questions_options = parsed_json["sample_question_options_association"]


class Questions(BaseModel):
    id: int
    title: str
    descriptions: str


# Define a basic route
@app.get('/')
def read_root():
    return {
        'success': True,
        'data': 'Hello World'
        }
    
@app.post('/questions')
def create_questions(req_data: Questions):
    print(req_data)
    questions.append(req_data)
    return req_data
    
    
@app.get('/questions')
def get_questions():
    return {
        'success': True,
        'data': questions
        }

# @app.post('/options')
# def post_options():
    
    
@app.get('/options')
def get_options():
    return {
        'success': True,
        'data': options
        }


@app.get('/question_options')
def get_question_options_ass():
    return {
        'success': True,
        'data': questions_options
        }



# Run the application using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
