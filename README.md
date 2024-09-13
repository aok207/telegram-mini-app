# Mini Bookmark

Mini Bookmark is a Telegram mini-app that allows users to enter a URL, scrape its contents, and display the scraped data directly within the telegram. Users also have the option to download the scraped content as a JSON file. Try the bot here: [@content_crawl_bot](https://t.me/content_crawl_bot)

## Features

- Input a URL to scrape content.
- View the scraped contents within the Telegram interface.
- Download the scraped data as a JSON file.

## Technologies Used

- **Frontend/UI:** React
- **Backend API:** FastAPI (Python)
- **Telegram Bot Framework:** python-telegram-bot library

## Getting Started

### Prerequisites

Make sure you have the following installed on your local machine:

- **Python** (version 3.8 or higher)
- **Node.js** and **npm** (or any other package manager)
- **pip** (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aok207/telegram-mini-app.git
   cd telegram-mini-app
   ```

2. Install the necessary dependencies for the backend and bot:

   ```bash
   cd server
   pip install -r requirements.txt
   ```

3. Install the frontend dependencies:

   ```bash
   cd ui
   npm install
   ```

### Running the App Locally

You'll need three terminal tabs or windows to run this project.

1. **Terminal 1:** Run the FastAPI backend:

   ```bash
   cd server
   fastapi dev app/main.py
   ```

2. **Terminal 2:** Run the React frontend:

   ```bash
   cd ui
   npm run dev
   ```

3. **Terminal 3:** Run the Telegram bot:

   ```bash
   cd server
   python bot.py
   ```

### Usage

1. Open the Telegram app and interact with the bot.
2. Enter a URL to scrape its contents.
3. View the scraped content or download it as a JSON file.
