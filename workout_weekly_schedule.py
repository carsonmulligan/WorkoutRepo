# Weekly Machine-Based Heavy Lifting Plan
# Goal: Build strength and muscle efficiently using machines

def weekly_workout_machines():
    # Each day targets specific muscle groups with machine-based exercises.
    # Compound lifts first for strength, accessory lifts for hypertrophy.

    workout_plan = {
        "Monday (Chest & Triceps)": [
            "Chest Press Machine: 5 sets of 4-6 reps (heavy)",
            "Incline Chest Press Machine: 4 sets of 8-10 reps",
            "Pec Deck (Chest Fly Machine): 4 sets of 10-12 reps",
            "Tricep Pushdown (Cable): 4 sets of 10-12 reps",
        ],
        "Tuesday (Back & Biceps)": [
            "Lat Pulldown Machine: 5 sets of 4-6 reps (heavy)",
            "Seated Row Machine: 4 sets of 8-10 reps",
            "Assisted Pull-Ups (Weight Stack): 4 sets of 8-10 reps",
            "Preacher Curl Machine: 4 sets of 10-12 reps",
        ],
        "Wednesday (Shoulders & Traps)": [
            "Overhead Shoulder Press Machine: 5 sets of 4-6 reps (heavy)",
            "Lateral Raise Machine: 4 sets of 12-15 reps",
            "Front Raise (Cable or Dumbbell): 4 sets of 12-15 reps",
            "Shrug Machine (or Smith Machine Shrugs): 4 sets of 8-10 reps",
        ],
        "Thursday (Rest or Active Recovery)": ["Light cardio, stretching, or yoga"],
        "Friday (Legs & Glutes)": [
            "Leg Press Machine: 5 sets of 4-6 reps (heavy)",
            "Leg Curl Machine (Hamstrings): 4 sets of 8-10 reps",
            "Leg Extension Machine (Quads): 4 sets of 8-10 reps",
            "Glute Kickback Machine: 4 sets of 10-12 reps",
            "Standing Calf Raise Machine: 4 sets of 15-20 reps",
        ],
        "Saturday (Upper Body - Mix)": [
            "Incline Chest Press Machine: 4 sets of 8-10 reps",
            "Seated Row Machine: 4 sets of 8-10 reps",
            "Cable Lateral Raise: 4 sets of 12-15 reps",
            "Hammer Curl Machine: 4 sets of 10-12 reps",
            "Tricep Pushdown: 4 sets of 10-12 reps",
        ],
        "Sunday (Rest or Active Recovery)": ["Foam rolling, yoga, or swimming"],
    }

    return workout_plan


# Function to print the workout plan for the week
def print_workout(workout_plan):
    print("Weekly Heavy Lifting Plan (Machine-Based):")
    for day, exercises in workout_plan.items():
        print(f"\n{day}:")
        for exercise in exercises:
            print(f"- {exercise}")


# Generate and print the machine-based workout plan
workout_plan_machines = weekly_workout_machines()
print_workout(workout_plan_machines)
