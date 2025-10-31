def calculate_energy_expended(activity_type, duration_minutes, intensity):

    if activity_type == "running":
        if intensity == "low":
            rate = 10
        elif intensity == "medium":
            rate = 14
        else:
            rate = 18
    elif activity_type == "cycling":
        if intensity == "low":
            rate = 7
        elif intensity == "medium":
            rate = 11
        else:
            rate = 15
    elif activity_type == "swimming":
        if intensity == "low":
            rate = 9
        elif intensity == "medium":
            rate = 13
        else:
            rate = 17
    else:
        rate = 0  

    energy = rate * duration_minutes
    return energy
def calculate_performance_intensity(age, baseline_hr, training_hr):
    max_hr = 220 - age  
    heart_rate_reserve = max_hr - baseline_hr
    intensity_percent = (training_hr - baseline_hr) / heart_rate_reserve * 100
    return intensity_percent
def determine_effort_level(intensity_percent):
    if intensity_percent < 50:
        return "Recovery Level"
    elif intensity_percent < 60:
        return "Endurance Level"
    elif intensity_percent < 70:
        return "Aerobic Level"
    elif intensity_percent <= 85:
        return "Threshold Level"
    else:
        return "Peak Power Level"
def calculate_training_points(energy, duration, level_bonus):
    base_points = energy * 0.1 + duration * 2
    final_points = base_points * level_bonus
    return round(final_points, 1)  
def requires_recovery(training_days, total_minutes, avg_intensity):
    if training_days >= 6:
        return True
    elif total_minutes > 450 and avg_intensity > 70:
        return True
    elif training_days >= 4 and avg_intensity > 80:
        return True
    else:
        return False
def generate_training_summary(athlete, activity_type, duration, intensity, age, baseline_hr, training_hr, training_days):
    level_bonuses = {
        "Recovery Level": 0.5,
        "Endurance Level": 1.0,
        "Aerobic Level": 1.2,
        "Threshold Level": 1.5,
        "Peak Power Level": 1.8}
    
    energy = calculate_energy_expended(activity_type, duration, intensity)
    intensity_percent = calculate_performance_intensity(age, baseline_hr, training_hr)
    effort_level = determine_effort_level(intensity_percent)
    bonus = level_bonuses[effort_level]
    points = calculate_training_points(energy, duration, bonus)
    recovery = requires_recovery(training_days, duration * training_days, intensity_percent)

    print("="*35)
    print("Training Summary for:", athlete)
    print("-"*30)
    print("Activity Type:", activity_type)
    print("Duration:", duration, "minutes")
    print("Intensity Level:", intensity)
    print("Energy Expended:", energy)
    print("Performance Analysis:")
    print("    Age:", age, "Baseline HR:", baseline_hr, "Training HR:", training_hr)
    print("    Intensity:", round(intensity_percent, 1), "%")
    print("    Effort Level:", effort_level)
    print("Training Points:", points)
    print("Consecutive Training Days:", training_days)
    print("Recovery Day Required:", "Yes" if recovery else "No")

print(f"Sport training analiser")
print("="*35)
athlete = input("Enter the athlete name: ")
activity_type = input("Activity type (running/cycling/swimming): ")
duration = int(input("Enter duration in minutes: "))
intensity = input("Intensity (low/medium/high): ")
age = int(input("How old is athlete: "))
baseline_hr = int(input("Enter the baseline heart rate: "))
training_hr = int(input("Enter ath;ete's training heart rate: "))
training_days = int(input("How many consecutive training days: "))
generate_training_summary(athlete, activity_type, duration, intensity, age, baseline_hr, training_hr, training_days)
