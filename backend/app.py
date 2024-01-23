from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import jwt

app = FastAPI()

questions = [] 
options = [] 
questions_options = [] 
user_answers = [] 
friend_answers = []

class QuestionRequest(BaseModel):
    title: str
    descriptions: str
    
class Questions(BaseModel):
    id: int
    title: str
    descriptions: str

class Options(BaseModel):
    id: int
    type: str
    value: str
    
class OptionsRequest(BaseModel):
    type: str
    value: str

class QuestionOptionsAssociation(BaseModel):
    id: int
    qid: int
    oid: int
    
class QuestionOptionsAssociationRequest(BaseModel):
    qid: int
    oid: int

class UserAnswers(BaseModel):
    id: int
    uid: int
    qid: int
    oid: int

class UserAnswersRequest(BaseModel):
    uid: int
    qid: int
    oid: int
    
class FriendAnswers(BaseModel):
    id: int
    qid: int
    oid: int
    uid: int
    fid: int 
    
class FriendAnswersRequest(BaseModel):
    qid: int
    oid: int
    uid: int
    fid: int 

SECRET_KEY = 'do?you?know?me!'
bearer_scheme = HTTPBearer()

def create_jwt_token(username):
    payload = {
        'username': username,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token
    

def verify_jwt_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded_token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get('/login')
def login(username: str):
    token = create_jwt_token(username)
    return {
        'success': True,
        'data': {
            'username': username,
            'token': token
            }
        }

@app.get('/')
def read_root(current_user = Depends(verify_jwt_token)):
    return {
        'success': True,
        'data': 'Hello World'
        }


@app.post('/questions', response_model = Questions)
def create_questions(req_data: QuestionRequest,
                     current_user = Depends(verify_jwt_token)):
    req_data = req_data.dict()
    req_data["id"] = 2
    questions.append(req_data)
    return req_data

@app.get('/questions', response_model = list[Questions])
def get_questions(current_user = Depends(verify_jwt_token)):
    return questions


@app.post('/options', response_model=Options)
def post_options(req_data: OptionsRequest, current_user = Depends(verify_jwt_token)):
    req_data = req_data.dict()
    req_data["id"] = 2
    options.append(req_data)
    return req_data
    
@app.get('/options', response_model=list[Options])
def get_options(current_user = Depends(verify_jwt_token)):
    return options

@app.post('/question_options', response_model=QuestionOptionsAssociation)
def post_question_options_ass(req_data: QuestionOptionsAssociationRequest, 
                              current_user = Depends(verify_jwt_token)):
    req_data = req_data.dict()
    req_data["id"] = 2
    questions_options.append(req_data)
    return req_data
    
@app.get('/question_options', response_model=list[QuestionOptionsAssociation])
def get_question_options_ass(current_user = Depends(verify_jwt_token)):
    return questions_options
    
@app.post('/user_answers', response_model=UserAnswers)
def post_user_answers(req_data: UserAnswersRequest, current_user = Depends(verify_jwt_token)):
    req_data = req_data.dict()
    req_data["id"] = 2
    user_answers.append(req_data)
    return req_data

@app.get('/user_answers', response_model=list[UserAnswers])
def get_user_answers(current_user = Depends(verify_jwt_token)):
    return user_answers

@app.post('/friend_answers', response_model=FriendAnswers)
def post_friend_answers(req_data: FriendAnswersRequest, current_user = Depends(verify_jwt_token)):
    req_data = req_data.dict()
    req_data["id"] = 2
    friend_answers.append(req_data)
    return req_data

@app.get('/friend_answers', response_model=list[UserAnswers])
def get_friend_answers(current_user = Depends(verify_jwt_token)):
    data: FriendAnswers = friend_answers
    return friend_answers
    
@app.get('/connection_score')
def get_connection_score(uid:int, fid:int, current_user = Depends(verify_jwt_token)):
    current_user_answers: UserAnswers = [x for x in user_answers if x.uid == uid]
    current_friend_answers: FriendAnswers = [x for x in friend_answers if x.uid == uid and x.fid == fid]

    user_qid_oid = {(ua.qid, ua.oid) for ua in current_user_answers}
    friend_qid_oid = {(fa.qid, fa.oid) for fa in current_friend_answers}

    matching_pairs_count = len(user_qid_oid.intersection(friend_qid_oid))
    
    return {
        'result': matching_pairs_count
    }


# Run the application using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
