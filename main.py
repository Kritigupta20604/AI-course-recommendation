from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserForm(BaseModel):
    name: str
    interest: str
    experience: str
    goal: str

class CourseUpdate(BaseModel):
    name: str
    interest: str
    level: str
    goal: str

courses = [
    {
        "id": 1,
        "name": "Python for beginners",
        "interest": "Python",
        "level": "Beginner",
        "goal": "programming"
        },
    {
        "id": 2,
        "name": "Advanced Python",
        "interest": "Python",
        "level": "Intermediate",
        "goal": "programming"
        },
    {
        "id": 3,
        "name": "Data Science Essentials",
        "interest": "Data Science",
        "level": "Beginner",
        "goal": "Data Analysis"
        },

    {
        "id": 4,
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

        elif experience == "intermediate":
            return {
                "recommendation": "Advanced Python",
                "reason": "This course is suitable for learners who already have Python experience.",
                "alternative": "AI Fundamentals"
            }

    
    elif interest == "ai":
        if experience == "beginner":
            return{
                "course": "AI Fundamentals",
                "reason": "This course provides and introduction to Artificial Intelligence.",
                "alternative": "Python for beginners"
            }
        elif experience == "intermediate":

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

@app.get("/")
def home():
    return {"Course Recommendation System"}

@app.post("/recommend")
def recommend_course(user: UserForm):

    recommendation = get_recommendation(user)

    return {
        "user": user.name,
        "recommendation": recommendation
    }

@app.get("/courses")
def get_courses():
    return courses

@app.delete("/courses/{course_id}")
def delete_course(course_id : int):
    for course in courses:
        if course["id"] == course_id:
            courses.remove(course)
            return "course deleted successfully"
    return "course not found"

@app.put("/course/{course_id}")
def update_course(course_id: int, updated_course: CourseUpdate):

    for course in courses:
        if course["id"] == course_id:
            course["name"] = updated_course.name
            course["interest"] = updated_course.interest
            course["level"] = updated_course.level
            course["goal"] = updated_course.goal

            return{
                "message": "Course updated successfully",
                "course": course
            }

        return "course not found"
        