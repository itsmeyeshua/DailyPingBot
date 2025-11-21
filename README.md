# Daily Site Ping Script

A simple Python script that automatically pings your websites daily to keep them active and monitor their health. Perfect for keeping Vercel free tier deployments from going to sleep.

## 🎯 Purpose

This script helps you:
- Keep your Vercel sites active by sending daily requests
- Monitor the health and response time of your websites
- Get notified if any site goes down
- Prevent free-tier platforms from suspending inactive sites

## 🚀 Features

- Pings multiple sites in one run
- Measures response times
- Provides detailed status reports
- Automated daily execution via GitHub Actions
- Completely free to run

## 📋 Prerequisites

- Python 3.7 or higher
- `requests` library
- GitHub account (for automation)

## 🛠️ Installation

### Local Setup

1. Clone this repository:
```bash
git clone https://github.com/itsmeyeshua/DailyPingBot.git
cd DailyPingBot
```

2. Install dependencies:
```bash
pip install requests
```

3. Update the `SITES` list in `ping_sites.py` with your URLs:
```python
SITES = [
    "https://your-site-1.vercel.app",
    "https://your-site-2.vercel.app",
]
```

4. Run the script manually:
```bash
python ping_sites.py
```

## ⚙️ Automation with GitHub Actions

This project includes a GitHub Actions workflow that runs the script automatically every day.

### Setup Steps:

1. **Fork or create this repository** on GitHub

2. **Add your URLs** to `ping_sites.py`

3. **Commit and push** your changes:
```bash
git add .
git commit -m "Add my site URLs"
git push
```

4. **Enable GitHub Actions**:
   - Go to your repository on GitHub
   - Click the "Actions" tab
   - Enable workflows if prompted

5. **Test the workflow manually**:
   - Go to "Actions" → "Daily Site Ping"
   - Click "Run workflow" → "Run workflow"
   - Check the logs to verify it works

### Schedule Configuration

The workflow runs daily at **12:00 PM UTC** by default. To change the schedule:

1. Edit `.github/workflows/actions.yml`
2. Modify the cron expression:
```yaml
schedule:
  - cron: '0 12 * * *'  # Minute Hour Day Month DayOfWeek
```

**Note:** GitHub Actions free tier includes 2,000 minutes/month, which is more than enough for daily pings.

## 📊 Output Example

```
============================================================
Site Health Check - 2025-01-15 12:00:00
============================================================

Pinging https://pomodorfocustimer.vercel.app... ✓ OK (0.45s)
Pinging https://quote-generatorfront.vercel.app... ✓ OK (0.52s)
Pinging https://alarm-buzzer.vercel.app... ✓ OK (0.38s)

============================================================
Summary: 3/3 sites responding correctly
============================================================
```