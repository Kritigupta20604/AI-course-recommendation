from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserForm(BaseModel):
    name: str
    interest: str
    experience: str
    goal: str

courses = [
    {
        "id": 1
        "name": "Python for beginners",
        "interest": "Python",
        "level": "Beginner",
        "goal": "programming"
    },
    {
        "id": 2
        "name": "Advanced Python",
        "interest": "Python",
        "level": "Intermediate",
        "goal": "programming"
        },
    {
        "id": 3
        "name": "Data Science Essentials",
        "interest": "Data Science",
        "level": "Beginner",
        "goal": "Data Analysis"
        },

    {
        "id": 4
        "name": "AI Fundamentals",
        "interest": "AI",
        "level": "Beginner",
        "goal": "Artificial Intelligence"
        },
]

def get_recommendation(user):

    experience = user.experience.lower()
    interest = user.interest.lower()
    goal = user.goal.lower()

    valid_experiences = ["beginner", "intermediate"]

    if experience not in valid_experiences:
        return{
            "error": "Invalid experience level",
            "message": "experience must be Beginner or Intermediate"
        }
    
    if interest == "python":

        if experience == "beginner" and goal == "programming":
            return {
                "course": "Python for beginners",
                "reason": "This course is suitable for beginners who want to learn programming with Python.",
                "alternative": "Data science Essentials"
             }

        elif experience == "Intermediate":
            return {
                "recommendation": "Advanced Python",
                "reason": "This course is suitable for learners who already have Python experience.",
                "alternative": "AI Fundamentals"
            }

    
    elif interest == "ai":
        if experience == "beginner":
            return{
                "course": "AI fundamentals",
                "reason": "This course provides and introduction to Artificial Intelligence.",
                "alternative": "Python for beginners"
            }
        elif interest == "intermediate":

            return{
                "course": "Machine Learning Basics",
                "reason": "This course is suitable for learners with some technical experience.",
                "alternative": "AI Fundamentals"
            }
    elif interest == "data science":
        return {
            "course": "Data Science Essentials",
            "reason": "This course introduces the fundamental concepts of Data Science.",
            "alternative": "Python for Beginners"
        }
    
    else:
        return {
            "course": "General Programming Essentials",
            "reason": "We could not find an exact match for your preference",
            "alternative": "Python for Beginners"
        }

@app.post("/recommend")
def recommend_course(user: UserForm):

    recommendation = get_recommendation(user)

    return {
        "user": user.name,
        "recommendation": recommendation
    }

@app.get("/")
def home():
    return {"message": "Course Recommendation System"}


@app.get("/courses")
def get_courses():
    return courses

