# Large Language Model Icebreaker

## Overview:
The Large Language Model Icebreaker is a web-based application designed to generate meaningful conversation starters based on a person's LinkedIn profile. Using cutting-edge large language models (OpenAI’s GPT-3.5 Turbo) and APIs like TavilySearchResults and Proxycurl, the tool scrapes LinkedIn profile data, generates personalized summaries, finds topics of interest, and suggests creative icebreakers. The project is designed to facilitate networking by giving users quick, tailored conversation starters and insights about professionals.

## Features:
1. LinkedIn Profile Lookup: Automatically fetches the LinkedIn profile URL of a person based on their full name.<br>
2. Profile Scraping: Scrapes LinkedIn profile data using Proxycurl for detailed information about the individual.<br>
3. Summary Generation: Provides a concise summary along with two interesting facts about the person from their LinkedIn profile.<br>
4. Interest Discovery: Suggests three topics that might interest the person based on their LinkedIn activity.<br>
5. Icebreaker Suggestions: Creates two unique icebreakers tailored to the individual, incorporating insights from their LinkedIn and Twitter activities.<br>
6. Flask-Based Web Interface: A simple and user-friendly web interface for inputting names and receiving summarized information, interests, and icebreakers in JSON format.<br>

## Methodology:
### 1. LinkedIn Profile Search:
The application uses the TavilySearchResults API to find the LinkedIn profile URL of the given name by searching for valid LinkedIn profile links.<br>

### 2. Profile Scraping:
The Proxycurl API scrapes detailed profile data from the fetched LinkedIn URL. It removes unnecessary information like certifications and people also viewed.<br>

### 3. LLM Processing:

a. Generate a summary of the person’s professional background.
b. List two interesting facts about the person.
c. Identify three topics that might interest them.
d. Craft two creative icebreakers based on LinkedIn and Twitter activity.

### 4. Flask Integration:
The application runs a Flask server, where users can input the name of the individual they want insights on, and receive output in JSON format containing summaries, icebreakers, and interests.

## Output:
### A. Summary: <br>
A short description of the person based on their LinkedIn profile.<br>
Two interesting facts derived from the profile.<br>

### B. Topics of Interest:<br>
Three potential topics that could interest the person, helping in starting meaningful conversations.

### C. Icebreakers:<br>
Two creative icebreakers derived from the individual’s LinkedIn and Twitter activity, tailored to initiate engaging dialogue.
<br>
![image](https://github.com/user-attachments/assets/399a7eaa-3e0d-45fa-afed-deb12c5709fa)<br><br>
![image](https://github.com/user-attachments/assets/7911e850-6a1a-4e82-b584-97a29e221162)

