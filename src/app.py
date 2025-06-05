@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
   """Sign up a student for an activity"""
   # Validate activity exists
   if activity_name not in activities:
      raise HTTPException(status_code=404, detail="Activity not found")

   # Get the activity
   activity = activities[activity_name]

   # Validate student is not already signed up
   if email in activity["participants"]:
      raise HTTPException(status_code=400, detail="Student is already signed up")

   # Add student
   activity["participants"].append(email)
   return {"message": f"Signed up {email} for {activity_name}"}

# Example activities dictionary with more activities
activities = {
    "soccer": {"type": "sport", "participants": []},
    "basketball": {"type": "sport", "participants": []},
    "tennis": {"type": "sport", "participants": []},
    "swimming": {"type": "sport", "participants": []},
    "painting": {"type": "artistic", "participants": []},
    "sculpture": {"type": "artistic", "participants": []},
    "music": {"type": "artistic", "participants": []},
    "theater": {"type": "artistic", "participants": []},
    "chess": {"type": "intellectual", "participants": []},
    "debate": {"type": "intellectual", "participants": []},
    "math_club": {"type": "intellectual", "participants": []},
    "robotics": {"type": "intellectual", "participants": []},
}