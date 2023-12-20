from fastapi import FastAPI
from pydantic import BaseModel
import json

# Create an instance of the FastAPI class
app = FastAPI()


with open("data.json") as json_file:
    file_contents = json_file.read()

parsed_json = json.loads(file_contents)

questions = parsed_json["sample_question"]
options = parsed_json["sample_options"]
questions_options = parsed_json["sample_question_options_association"]


class Questions(BaseModel):
    id: int
    title: str
    descriptions: str

class Options(BaseModel):
    id: int
    type: str
    value: str

class QuestionOptionsAssociation(BaseModel):
    id: int
    qid: int
    oid: int

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

@app.post('/options')
def post_options(req_data: Options):
    print(req_data)
    options.append(req_data)
    return req_data
    
@app.get('/options')
def get_options():
    return {
        'success': True,
        'data': options
        }


@app.post('/question_options')
def post_question_options_ass(req_data: QuestionOptionsAssociation):
    print(req_data)
    questions_options.append(req_data)
    return req_data

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
