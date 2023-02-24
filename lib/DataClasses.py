from dataclasses import dataclass, asdict
from datetime import datetime
import json

# TypedDict might be an option if perf is too slow
class BaseModel:

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}
    
    def format_datetime(self, datetime: datetime):
        return datetime.strftime("%m/%d/%Y %H:%M")
    
    def to_json(self, field: dict):
        return json.dumps(field)
    
    @classmethod
    def headers(cls):
        return list(cls.__annotations__.keys())
    
@dataclass
class User(BaseModel):
    username: str
    email: str
    password_hash: str
    create_datetime: datetime
    user_id: str

    def __post_init__(self):
        self.create_datetime = self.format_datetime(self.create_datetime)

@dataclass
class Routine(BaseModel):
    name: str
    description: str
    create_datetime: datetime
    modify_datetime: datetime

@dataclass
class Exercise(BaseModel):
    name: str
    is_unilateral: bool
    is_bodyweight: bool
    details: dict

@dataclass
class ExerciseSet(BaseModel):
    exercise_id: int
    routine_id: int
    display_order: int
    unit: str
    count: int
    details: dict

@dataclass
class RoutineMap(BaseModel):
    routine_id: int
    user_id: int
    config: dict

@dataclass
class SetHistory(BaseModel):
    set_id: int
    unit: str
    count: int
    load: int
    record_date: datetime

@dataclass
class RoutineLock(BaseModel):
    routine_id: int
    user_id: int
    start_datetime: datetime

@dataclass
class UserConfig(BaseModel):
    user_id: int
    param_name: str
    param_value: str
    modify_datetime: datetime

