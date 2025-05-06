# 🏏 IPL Match Scheduler

This Python program generates a full match schedule for the Indian Premier League (IPL) with the following key rules and constraints:

- **10 Teams**, each playing **14 matches** (home & away against 7 opponents).
- **70 total matches**, distributed from **March 22, 2025** to **May 26, 2025**.
- Each day has **at least one match**, with **two matches only on Sundays if necessary**.
- **Minimum 4-day rest** between matches for each team.
- Matches involving the **most popular team (e.g., RCB)** are prioritized on weekends.

---

## 📦 Files Generated

- `ipl_schedule.csv` – Clean tabular match schedule.
- `ipl_schedule.json` – JSON format for frontend/backend integrations.
- `ipl_schedule.txt` – Human-readable plain text match list.

---

## 🛠️ How It Works

1. Generates all home/away combinations.
2. Randomizes the match order.
3. Iterates day by day, ensuring:
   - Rest gaps.
   - Weekend priority for key matches.
   - Sunday double-headers only if needed.
4. Outputs structured and readable schedule files.

---

## 🧠 Features

- Ensures real-life-like IPL scheduling.
- Prevents unfair back-to-back matches.
- Allows configurable "most popular" team.
- Outputs data in multiple formats (CSV, JSON, TXT).

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Avaneesh-Chopdekar/ipl-scheduler.git
   cd ipl-scheduler
   ```

2. Run the scheduler:

   ```bash
   python main.py
   ```

3. Output files will appear in the project directory.

---

## ⚙️ Requirements

- Python 3.7+
- No external dependencies

---

## 📝 Customization

- To change the most popular team (e.g., RCB), edit:

  ```python
  most_popular_team = "Royal Challengers Bengaluru"
  ```

- To modify tournament duration or start date, change:

  ```python
  start_date = datetime(2025, 3, 22)
  end_date = datetime(2025, 5, 26)
  ```

---

## 📄 License

MIT License. Free to use and modify.

---

## 👨‍💻 Author

Built with ❤️ by Avaneesh Chopdekar
