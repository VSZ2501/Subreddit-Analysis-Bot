# main.py

import praw
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import os

CONFIG_FILE = 'reddit_config.txt'

# Fonction pour lire le subreddit à partir du fichier
def lire_subreddit():
    with open('subreddit.txt', 'r') as file:
        return file.read().strip()

# Fonction pour récupérer les posts du subreddit
def recuperer_posts(client_id, client_secret, user_agent, subreddit):
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)
    posts = reddit.subreddit(subreddit).top(time_filter='month', limit=30)
    return [(datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d'),
             datetime.fromtimestamp(post.created_utc).strftime('%H:%M'),
             post.ups,
             post.title) for post in posts]

# Fonction pour exporter les données vers Google Sheets
def exporter_vers_google_sheets(data, sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1

    for row in data:
        sheet.append_row(row)

def enregistrer_config(client_id, client_secret, user_agent):
    with open(CONFIG_FILE, 'w') as file:
        file.write(f"{client_id}\n{client_secret}\n{user_agent}")

def charger_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            lines = file.readlines()
            if len(lines) == 3:
                return lines[0].strip(), lines[1].strip(), lines[2].strip()
    return None, None, None

def main():
    root = tk.Tk()
    root.title("Subreddit Analysis Bot")

    # Charger la configuration existante
    client_id, client_secret, user_agent = charger_config()

    tk.Label(root, text="Reddit Client ID:").grid(row=0, column=0)
    client_id_entry = tk.Entry(root, width=50)
    client_id_entry.grid(row=0, column=1)
    client_id_entry.insert(0, client_id if client_id else "")

    tk.Label(root, text="Reddit Client Secret:").grid(row=1, column=0)
    client_secret_entry = tk.Entry(root, width=50)
    client_secret_entry.grid(row=1, column=1)
    client_secret_entry.insert(0, client_secret if client_secret else "")

    tk.Label(root, text="Reddit User Agent:").grid(row=2, column=0)
    user_agent_entry = tk.Entry(root, width=50)
    user_agent_entry.grid(row=2, column=1)
    user_agent_entry.insert(0, user_agent if user_agent else "")

    tk.Label(root, text="Google Sheets File Name:").grid(row=3, column=0)
    sheet_name_entry = tk.Entry(root, width=50)
    sheet_name_entry.grid(row=3, column=1)

    def on_submit():
        client_id = client_id_entry.get().strip()
        client_secret = client_secret_entry.get().strip()
        user_agent = user_agent_entry.get().strip()
        sheet_name = sheet_name_entry.get().strip()

        if not all([client_id, client_secret, user_agent, sheet_name]):
            messagebox.showerror("Error", "All fields must be filled out.")
            return

        try:
            subreddit = lire_subreddit()
            posts = recuperer_posts(client_id, client_secret, user_agent, subreddit)
            exporter_vers_google_sheets(posts, sheet_name)
            enregistrer_config(client_id, client_secret, user_agent)
            messagebox.showinfo("Success", "Data exported successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.grid(row=4, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()