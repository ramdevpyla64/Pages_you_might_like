:📄 Page Recommendation System (JSON-based)
A simple Python-based recommendation engine that suggests pages a user might like based on other users’ liked pages. The program reads data from a JSON file, analyzes shared interests among users, and recommends new pages ranked by similarity score. It demonstrates the core concept behind collaborative filtering — finding similar users and suggesting what they enjoy.
This project helps understand how basic recommendation logic works without relying on complex machine learning models. It is lightweight, easy to test, and scalable for larger datasets. Users can modify the dataset to simulate a real-world social media–like environment.
Key Features:


Reads user data and liked pages from a JSON file


Identifies shared interests between users


Suggests new pages not yet liked by the user


Ranks recommendations based on similarity strength


Works efficiently even with thousands of users


How It Works:


Each user has a list of liked pages.


The program compares the target user’s likes with every other user.


It counts how many liked pages overlap.


Pages liked by similar users (but not by the target user) are recommended.


Recommendations are sorted by how many mutual likes exist.


Example Use Case:
If Alice and Bob both like pages 101 and 102, and Bob also likes page 104, the system will recommend page 104 to Alice, assuming she hasn’t liked it yet.
Why This Project:
This project serves as a beginner-friendly introduction to recommendation systems, JSON handling, and Python logic building. It’s ideal for students and developers exploring data-driven algorithms.
Requirements:
Only Python 3 is needed — no external libraries.
Future Enhancements:


Use Jaccard or cosine similarity for more accuracy


Add a database instead of a JSON file


Integrate with a web dashboard using Flask or FastAPI


Author:
Ramdev Pyla
Visakhapatnam, Andhra Pradesh
GitHub | LinkedIn
📧 ramdevpyla64@gmail.com
License:
MIT License — free to use, modify, and distribute.
⭐ If you found this useful, consider giving the repository a star!
