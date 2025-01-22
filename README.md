
When you put code between them, it looks like this:

Adding this to an IOS app called GainGrid

```python

workout_plan = {
    "Monday (Chest)": {
        "Warm-Up": "Chest Press Machine (Light) - 2 sets of 12-15 reps",
        "Workouts": [
            "Chest Press Machine: 5 sets of 4-6 reps (heavy)",
            "Incline Chest Press Machine: 4 sets of 6-8 reps",
            "Pec Deck (Chest Fly Machine): 4 sets of 10-12 reps",
            "Decline Chest Press Machine: 4 sets of 6-8 reps",
            "Cable Crossovers (High to Low): 4 sets of 10-12 reps",
            "Push-Ups (Weighted, Optional): 3 sets to failure"
        ],
        "Cardio": "15 minutes incline treadmill walk"
    },
    "Tuesday (Shoulders)": {
        "Warm-Up": "Overhead Press Machine (Light) - 2 sets of 12-15 reps",
        "Workouts": [
            "Overhead Shoulder Press Machine: 5 sets of 4-6 reps (heavy)",
            "Lateral Raise Machine: 4 sets of 12-15 reps",
            "Front Raises (Cable): 4 sets of 12-15 reps",
            "Reverse Pec Deck (Rear Delts): 4 sets of 12-15 reps",
            "Cable Upright Row: 4 sets of 8-10 reps",
            "Smith Machine Shrugs: 4 sets of 8-10 reps"
        ],
        "Cardio": "15 minutes elliptical machine"
    },
    "Wednesday (Legs)": {
        "Warm-Up": "Leg Press (Light) - 2 sets of 12-15 reps",
        "Workouts": [
            "Leg Press Machine: 5 sets of 4-6 reps (heavy)",
            "Leg Curl Machine (Hamstrings): 4 sets of 8-10 reps",
            "Leg Extension Machine (Quads): 4 sets of 8-10 reps",
            "Glute Kickback Machine: 4 sets of 10-12 reps",
            "Standing Calf Raise Machine: 4 sets of 12-15 reps",
            "Seated Calf Raise Machine: 4 sets of 12-15 reps"
        ],
        "Cardio": "15 minutes stair climber"
    },
    "Thursday (Back)": {
        "Warm-Up": "Lat Pulldown (Light) - 2 sets of 12-15 reps",
        "Workouts": [
            "Lat Pulldown Machine: 5 sets of 4-6 reps (heavy)",
            "Seated Row Machine: 4 sets of 6-8 reps",
            "Assisted Pull-Ups (Weight Stack): 4 sets of 8-10 reps",
            "Single-Arm Row (Cable): 4 sets of 8-10 reps per arm",
            "Face Pulls (Cable, Upper Back): 4 sets of 12-15 reps",
            "Reverse Pec Deck (Rear Delts): 4 sets of 12-15 reps"
        ],
        "Cardio": "15 minutes rowing machine"
    },
    "Friday (Biceps & Triceps)": {
        "Warm-Up": "Tricep Pushdowns (Light) - 2 sets of 12-15 reps",
        "Workouts": [
            "Preacher Curl Machine (Biceps): 4 sets of 8-10 reps",
            "Hammer Curl Machine (Biceps): 4 sets of 10-12 reps",
            "Cable Concentration Curls: 4 sets of 12-15 reps",
            "Tricep Pushdown (Cable): 4 sets of 8-10 reps",
            "Overhead Tricep Extension (Cable): 4 sets of 10-12 reps",
            "Dips (Machine-Assisted, Optional): 4 sets of 6-8 reps"
        ],
        "Cardio": "15 minutes jump rope or light treadmill run"
    }
}
