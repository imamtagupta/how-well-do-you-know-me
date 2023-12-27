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
user_answers = parsed_json["user_answers"]
friend_answers = parsed_json["friend_answers"]

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

class UserAnswers(BaseModel):
    uid: int
    qid: int
    oid: int
    
class FriendAnswers(BaseModel):
    id: int
    qid: int
    oid: int
    uid: int
    fid: int 

    
    
# Define a basic route
@app.get('/')
def read_root():
    return {
        'success': True,
        'data': 'Hello World'
        }
    
@app.post('/questions')
def create_questions(req_data: Questions):
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
    questions_options.append(req_data)
    return req_data

@app.get('/question_options')
def get_question_options_ass():
    return {
        'success': True,
        'data': questions_options
        }
    
    
@app.post('/user_answers')
def post_user_answers(req_data: UserAnswers):
    user_answers.append(req_data)
    return {
        'success': True,
        'data': req_data
        }

@app.get('/user_answers')
def get_user_answers():
    data: UserAnswers = user_answers
    return {
        'success': True,
        'data': data
        }

@app.post('/friend_answers')
def post_friend_answers(req_data: FriendAnswers):
    friend_answers.append(req_data)
    return {
        'success': True,
        'data': req_data
        }

@app.get('/friend_answers')
def get_friend_answers():
    data: FriendAnswers = friend_answers
    return {
        'success': True,
        'data': data
        }


# Run the application using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
