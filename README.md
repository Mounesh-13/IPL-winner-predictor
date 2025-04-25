Live : web-production-b312.up.railway.app

# Screenshots
<img width="508" alt="image" src="https://github.com/user-attachments/assets/50b58344-9f16-44a0-b4e3-a9bc023da57a" />

<img width="508" alt="image" src="https://github.com/user-attachments/assets/6bdcf5c9-14fd-45ca-9e53-5e6901b21ff8" />

# IPL Winner Predictor (2020–2024)

A modern web application that predicts the winner between any two IPL teams based on their overall win/loss records from the last 5 completed IPL seasons (2020–2024). Built with Flask, Bootstrap, and Chart.js for a beautiful, responsive experience.

---

## 🚩 Features
- Uses real IPL match results (2020–2024)
- Calculates each team’s overall winning percentage
- Predicts the winner between any two teams based on historical performance
- Interactive web UI with dark theme and IPL-inspired visuals
- Dynamic charts for team win percentages
- Clean error handling and user feedback
- Easily updatable dataset for future seasons

---

## 🖥️ Live Demo (Local)
After setup, visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📦 Project Structure
```
ipl_winner_predictor/
├── app.py                # Main Flask app
├── predictor.py          # CLI version (optional)
├── ipl_results_2020_2024.csv  # IPL match data
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Main web template
├── static/               # (Optional: for custom CSS/JS)
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone or Download This Project
```
git clone https://github.com/yourusername/ipl_winner_predictor.git
cd ipl_winner_predictor
```

### 2. Install Python Dependencies
```
pip install -r requirements.txt
```

### 3. Run the Web App
```
python app.py
```
Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📝 Usage Guide
1. **Select two IPL teams** from the dropdown menus.
2. Click **Predict Winner**.
3. View:
   - Each team’s 5-year win percentage
   - A prediction based on historical data
   - A dynamic bar chart comparing win rates
4. Use **Reload Data** if you update the CSV file while the app is running.

---

## ⚙️ Customization
- **Update Data:**
  - Replace or expand `ipl_results_2020_2024.csv` with new match data.
  - Format: `Season,Team1,Team2,Winner`
- **Change Theme:**
  - Edit `templates/index.html` and CSS for custom colors or branding.
- **Add Features:**
  - Extend `app.py` for more analytics (recent form, player stats, etc).

---

## 🛠️ Deployment

### 🚀 Deploy on Render (Recommended)
1. **Push your code to GitHub.**
2. Go to [https://dashboard.render.com/](https://dashboard.render.com/) and click "New Web Service".
3. Connect your GitHub repo and select it.
4. Set the following settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Python Version:** 3.10+ (or your preferred version)
   - **Port:** 10000 (Render auto-detects from gunicorn)
5. Click "Create Web Service" and wait for deployment.

### 🚀 Deploy on Railway
1. **Push your code to GitHub.**
2. Go to [https://railway.app/](https://railway.app/) and click "New Project" > "Deploy from GitHub repo".
3. Select your repo and follow prompts.
4. Railway will detect the `Procfile` and use `gunicorn app:app` automatically.
5. Set environment variables if needed (none required by default).
6. Deploy and get your public URL!

### 🚀 Deploy with Docker (Any Cloud)
1. Build the image:
   ```sh
   docker build -t ipl-winner-predictor .
   ```
2. Run the container:
   ```sh
   docker run -p 8080:8080 ipl-winner-predictor
   ```

---

## 🧩 Tech Stack
- **Python 3**
- **Flask** (web framework)
- **Pandas** (data handling)
- **Bootstrap** (responsive UI)
- **Chart.js** (interactive charts)

---

## ❓ Troubleshooting
- **Port already in use:** Change the port in `app.py` (`app.run(port=XXXX)`)
- **Missing dependencies:** Double-check `pip install -r requirements.txt`
- **Data not updating:** Click **Reload Data** or restart the app after editing the CSV.
- **App not loading:** Ensure you are in the correct directory and using Python 3.

---

## 🤝 Contribution
Pull requests and suggestions are welcome! Please fork the repo and open an issue or PR.

---

## 📝 License
This project is open source under the MIT License.

---

## 🙏 Credits
- IPL match data sourced from public cricket databases.
- Inspired by IPL fans and data science enthusiasts.

---

Enjoy predicting IPL winners! 🏏

## Example CSV Row
```
Season,Team1,Team2,Winner
2022,Gujarat Titans,Rajasthan Royals,Gujarat Titans
```

## Limitations
- This tool only considers overall win/loss percentage (2020–2024)
- Does **not** account for head-to-head stats, player form, injuries, pitch, toss, or squad changes

## Credits
- Data sources: [IPL Official Website](https://www.iplt20.com/), [ESPNcricinfo](https://www.espncricinfo.com/)
- Built with Python and pandas

---

Feel free to expand or modify this project for more advanced IPL analytics!
