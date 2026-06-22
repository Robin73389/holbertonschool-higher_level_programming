#!/usr/bin/python3
"""Consuming and processing data from an API using Python"""


import requests
import csv


def fetch_and_print_posts():
    """Recupére la requete via API"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code == 200:
        data = r.json()

        for i in data:
            print(i['title'])


def fetch_and_save_posts():
    """Récupére la requete et la save dans CSV file"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        data = r.json()

        posts_list = []

        for post in data:
            posts_list.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])

            writer.writeheader()
            writer.writerows(posts_list)


if __name__ == "__main__":

    fetch_and_print_posts()
    fetch_and_save_posts()
