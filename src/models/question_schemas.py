from typing import List
from pydantic import BaseModel, Field, validator

class MCQQuestions(BaseModel):
    question : str = Field(description="The Question Text")
    options: List[str] = Field(description="List of 4 options")
    correct_answer : str = Field(description="The correct answer from the options")

    @validator('question', pre=True)
    def clean_question(cls, v):
        if isinstance(v, dict):
            return v.get('description', str(v))
        return str(v)

class FillBlankQuestion(BaseModel):
    question : str = Field(description="The question text with '____' for the blank")
    answer : str = Field(description="the correct word or phrase for the blank")
    
    @validator('question', pre=True)
    def clean_question(cls, v):
        if isinstance(v, dict):
            return v.get('description', str(v))
        return str(v)
    
    
    
