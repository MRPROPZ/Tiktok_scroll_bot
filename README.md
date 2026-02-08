# TikTok Scroll Bot

This Python script automates the process of scrolling through TikTok's "For You" page, enabling a hands-free viewing experience. It launches a Chrome browser, navigates to TikTok, and periodically scrolls to the next video.

## Features

*   Automatic scrolling through the TikTok "For You" feed.
*   A 10-second delay between scrolls to allow time for watching videos.
*   Graceful shutdown by pressing `Ctrl+C` in the terminal.
*   Robust process management ensures the browser is completely closed upon script termination, preventing leftover processes.

## Prerequisites

Before you begin, ensure you have the following installed:
*   Python 3.x
*   Google Chrome

## Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/mrpropz/tiktok_scroll_bot.git
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd tiktok_scroll_bot
    ```

3.  **Install the required Python packages:**
    ```sh
    pip install selenium webdriver-manager psutil
    ```

## Usage

1.  **Run the script from your terminal:**
    ```sh
    python tiktok_scroll_bot.py
    ```

2.  A new Chrome window will open, navigate to `tiktok.com/foryou`, and begin scrolling down every 10 seconds. Console messages will indicate the script's status.

3.  **To stop the bot**, press `Ctrl+C` in the terminal window where the script is running. The script will handle closing the browser window and its associated processes cleanly.

## How It Works

*   **Selenium:** Automates and controls the Google Chrome browser.
*   **webdriver-manager:** Automatically downloads and sets up the correct `chromedriver` executable for your installed version of Chrome.
*   **psutil:** Tracks the process ID (PID) of the Chrome instance launched by the script. Upon exit, it ensures that the browser process is fully terminated.
