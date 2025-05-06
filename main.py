import random
from datetime import datetime, timedelta
import csv
import json

teams = [
    "Chennai Super Kings",
    "Delhi Capitals",
    "Gujarat Titans",
    "Kolkata Knight Riders",
    "Lucknow Super Giants",
    "Mumbai Indians",
    "Punjab Kings",
    "Rajasthan Royals",
    "Royal Challengers Bengaluru",
    "Sunrisers Hyderabad"
]

most_popular_team = "Royal Challengers Bengaluru"

# Generate 2 matches for each pair (home and away)
matches = []
for i in range(len(teams)):
    for j in range(i + 1, len(teams)):
        matches.append([teams[i], teams[j]])
        matches.append([teams[j], teams[i]])

random.shuffle(matches)

start_date = datetime(2025, 3, 22)
end_date = datetime(2025, 5, 26)
current_date = start_date

# Track last played date for each team
last_played = {team: start_date - timedelta(days=10) for team in teams}
schedule = []
match_index = 0
total_matches = 70
extra_sunday_matches = []

while current_date <= end_date and match_index < total_matches:
    matches_today = []
    is_sunday = current_date.weekday() == 6

    tries = 0
    found_match = False

    # Try to find a valid match for the day
    for i in range(len(matches)):
        if match_index >= total_matches:
            break
        team1, team2 = matches[i]
        if (
            (current_date - last_played[team1]).days >= 4 and
            (current_date - last_played[team2]).days >= 4
        ):
            matches_today.append((team1, team2))
            last_played[team1] = current_date
            last_played[team2] = current_date
            matches.pop(i)
            match_index += 1
            found_match = True
            break

    # On Sundays, try for a second match if needed
    if is_sunday and match_index < total_matches:
        for i in range(len(matches)):
            team1, team2 = matches[i]
            if (
                (current_date - last_played[team1]).days >= 4 and
                (current_date - last_played[team2]).days >= 4
            ):
                matches_today.append((team1, team2))
                last_played[team1] = current_date
                last_played[team2] = current_date
                matches.pop(i)
                match_index += 1
                extra_sunday_matches.append(current_date.strftime("%d %B"))
                break

    # Add matches to schedule
    for i, (team1, team2) in enumerate(matches_today):
        suffix = "" if i == 0 else " (Second Match)"
        schedule.append({
            "date": current_date.strftime("%A, %d %B %Y") + suffix,
            "match": f"{team1} vs {team2}"
        })

    current_date += timedelta(days=1)

# Export
with open("ipl_schedule.csv", mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["date", "match"])
    writer.writeheader()
    writer.writerows(schedule)

with open("ipl_schedule.json", mode='w') as file:
    json.dump(schedule, file, indent=4)

with open("ipl_schedule.txt", "w") as file:
    for entry in schedule:
        file.write(f"{entry['date']}: {entry['match']}\n")

print(f"✅ IPL schedule generated with {len(schedule)} matches.")
if extra_sunday_matches:
    print(f"📅 Double-headers on these Sundays: {', '.join(extra_sunday_matches)}")
