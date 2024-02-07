from database import get_db
from schema import UserAnswersBase, FriendAnswersBase
from models import UserAnswer, FriendAnswer
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/')
def get_connection_score(uid:int, fid:int, db:Session= Depends(get_db)):
    user_answers = db.query(UserAnswer).all()
    friend_answers = db.query(FriendAnswer).all()
    current_user_answers: UserAnswersBase = [x for x in user_answers if x.uid == uid]
    current_friend_answers: FriendAnswersBase = [x for x in friend_answers if x.uid == uid and x.fid == fid]

    user_qid_oid = {(ua.qid, ua.oid) for ua in current_user_answers}
    friend_qid_oid = {(fa.qid, fa.oid) for fa in current_friend_answers}

    matching_pairs_count = len(user_qid_oid.intersection(friend_qid_oid))
    
    return {
        'result': matching_pairs_count
    }