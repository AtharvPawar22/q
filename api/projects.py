from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

project_data = {
  "easy": [
    {
      "title": "Favorite Recipe Card",
      "description": "Design a single-page recipe layout with the dish name, ingredients list, and step-by-step instructions.",
      "tech": ["html", "css"]
    },
    {
      "title": "Typing Speed Tester",
      "description": "Measures how fast a user can type a passage, with visual feedback on accuracy.",
      "tech": ["javascript", "html", "css"]
    },
    {
      "title": "Interactive Story Game",
      "description": "Choose-your-own-adventure style story app with branching paths and memory save feature.",
      "tech": ["html", "css", "javascript"] 
    },
    {
      "title": "Command-Line To-Do List",
      "description": "A terminal-based task manager with add, list, and delete functionality using file I/O.",
      "tech": ["c++"]
    },
    {
      "title": "Quote of the Day CLI",
      "description": "A command-line tool that displays a random inspirational quote each time it's run, with options to filter by category or author using flags.",
      "tech": ["go"]
    },
    {
      "title": "Quote of the Day CLI",
      "description": "A command-line tool that displays a random inspirational quote each time it's run, with options to filter by category or author using flags.",
      "tech": ["golang"]
    },
    {
      "title": "Random Password Generator",
      "description": "Generate secure, random passwords based on user preferences like length, symbols, and digits.",
      "tech": ["python"]
    },
    {
      "title": "BMI Calculator App",
      "description": "Simple iOS app to calculate and categorize Body Mass Index based on input.",
      "tech": ["swift"]
    },
    {
      "title": "AI Image Caption Bot",
      "description": "Upload an image and generate a descriptive or fun caption using a lightweight ML API.",
      "tech": ["html", "css", "javascript", "python"]
    },
    {
      "title": "Static Portfolio Generator",
      "description": "Generate a static HTML portfolio from YAML or Markdown content using Ruby.",
      "tech": ["ruby"]
    },
    {
      "title": "Virtual Plant Care Assistant",
      "description": "A reminder app to help users manage watering, pruning, and fertilizing plants.",
      "tech": ["html", "css", "javascript"]
    },
    {
      "title": "Micro Journal App",
      "description": "Minimalist journaling app for short daily reflections with export support.",
      "tech": ["html", "css", "javascript", "python"]
    },
    {
      "title": "Note Organizer",
      "description": "Desktop Java app to create, search, and organize text-based notes.",
      "tech": ["java"]
    },
    {
      "title": "Mood-Based Music Suggester",
      "description": "Suggest music based on selected mood with animations and playlist integration.",
      "tech": ["react", "javascript", "html", "css"]
    },
    {
      "title": "AR Card Viewer (Marker-Based)",
      "description": "Use webcam and AR.js to overlay content on printable markers.",
      "tech": ["javascript", "html", "css"]
    }
  ],
  "moderate": [
    {
      "title": "Command-Line Budget Tracker",
      "description": "Track expenses and income from the command line with support for categories and balance reporting.",
      "tech": ["python"]
    },
    {
      "title": "Dream Journal Analyzer",
      "description": "Users log dreams and detect recurring themes using basic NLP + trend visualization.",
      "tech": ["python", "javascript", "react", "html", "css"]
    },
    {
      "title": "Offline Markdown Blog Compiler",
      "description": "Convert Markdown posts to static HTML pages using a custom compiler.",
      "tech": ["typescript"]
    },
    {
      "title": "Storyboarding Tool for Creators",
      "description": "Arrange scenes, characters, and scripts visually for creative planning.",
      "tech": ["react", "javascript", "python"]
    },
    {
      "title": "Pomodoro CLI Timer",
      "description": "A terminal-based productivity timer with breaks, written in Rust.",
      "tech": ["rust"]
    },
    {
      "title": "Local Event Explorer",
      "description": "Search for local events with Google Maps + Ticketmaster APIs.",
      "tech": ["react", "javascript", "html", "css"]
    },
    {
      "title": "Expense Tracker with CSV Export",
      "description": "Track expenses with visualizations and import/export CSV capability.",
      "tech": ["c++"]
    },
    {
      "title": "Digital Time Capsule",
      "description": "Users write and lock messages that unlock at a chosen future date.",
      "tech": ["python", "javascript", "react"]
    },
    {
      "title": "Language Flashcard App",
      "description": "iOS flashcard app that uses spaced repetition for vocabulary learning.",
      "tech": ["swift"]
    },
    {
      "title": "Voice-Controlled Dashboard",
      "description": "Navigate a dashboard using the Web Speech API and React.",
      "tech": ["javascript", "react", "html", "css"]
    },
    {
      "title": "Fictional Language Generator",
      "description": "Create new languages or naming conventions using probabilistic rules.",
      "tech": ["python", "javascript", "html", "css"]
    }
  ],
  "difficult": [
    {
      "title": "Text-Based Chatbot Framework",
      "description": "Build a modular chatbot that can handle different topics using keyword recognition and state management.",
      "tech": ["python"]
    },
    {
      "title": "Collaborative Code Editor",
      "description": "A real-time web-based code editor with WebSocket syncing and syntax highlighting.",
      "tech": ["typescript", "react", "node.js", "monaco-editor"]
    },
    {
      "title": "Personal Finance Analyzer",
      "description": "CLI + web hybrid app that analyzes bank statements and visualizes spend data.",
      "tech": ["rust", "javascript", "react"]
    },
    {
      "title": "AI Research Assistant",
      "description": "Reads academic papers, extracts key insights, and auto-generates citations.",
      "tech": ["python", "react", "html", "css"]
    },
    {
      "title": "Command-Line Flashcard Quizzer",
      "description": "A CLI app where users can create, edit, and quiz themselves with flashcards. Stores decks in JSON and tracks quiz performance. Useful for learning file I/O, data structures, and CLI navigation.",
      "tech": ["python"]
    },
    {
      "title": "Remote Music Jam Session",
      "description": "Musicians can jam live with synced audio/video using WebRTC and buffer correction.",
      "tech": ["go", "python", "react", "webrtc"]
    },
    {
      "title": "Remote Music Jam Session",
      "description": "Musicians can jam live with synced audio/video using WebRTC and buffer correction.",
      "tech": ["golang", "python", "react", "webrtc"]
    },
    {
      "title": "Distributed Chat Server",
      "description": "Peer-to-peer chat app with multithreading and history sync using Java.",
      "tech": ["java"]
    },
    {
      "title": "Neural Style Transfer App",
      "description": "Apply art styles to uploaded images using TensorFlow.js and React.",
      "tech": ["javascript", "python", "react"]
    },
    {
      "title": "Decentralized Voting Platform",
      "description": "Secure blockchain-style voting using only PHP and SQL validation.",
      "tech": ["php", "sql"]
    },
    {
      "title": "Terminal-Based GitHub Issue Tracker",
      "description": "Use GitHub's API to view, search, and create issues from the terminal. Includes auth via personal token, error handling, and clean output formatting. Great for working with APIs and building robust CLI tools.",
      "tech": ["python"]
    },
    {
      "title": "Behavior-Based NPC Simulator",
      "description": "Simulate a 2D environment where non-player characters (NPCs) interact using behavior trees or rule-based systems. Users can edit rules to change how NPCs respond to objects, events, or each other. Runs entirely in-browser with canvas and vanilla JavaScript. Teaches design patterns, game logic, and canvas rendering.",
      "tech": ["html", "css", "javascript"]
    },
    {
      "title": "Personal Knowledge Graph",
      "description": "Graph-based note-taking app with relationship mapping using Neo4j.",
      "tech": ["python", "react", "neo4j"]
    },
    {
      "title": "IoT Smart Home Simulator",
      "description": "Simulate smart devices and sensors with event-driven state logic.",
      "tech": ["c++", "javascript", "react"]
    }
  ]
}

def handler(request):
    """Vercel serverless function handler"""
    from flask import Flask, request as flask_request
    
    app = Flask(__name__)
    
    with app.test_request_context(
        path=request.url,
        method=request.method,
        headers=dict(request.headers),
        data=request.get_data(),
        query_string=request.query_string
    ):
        if flask_request.method == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Methods': 'POST'
                }
            }
        
        if flask_request.method == 'POST':
            try:
                data = flask_request.get_json()
                if not data:
                    return {
                        'statusCode': 400,
                        'headers': {'Access-Control-Allow-Origin': '*'},
                        'body': json.dumps({"error": "No JSON data provided"})
                    }
                    
                tech_stack = [tech.lower().strip() for tech in data.get('tech_stack', [])]
                
                if not tech_stack:
                    return {
                        'statusCode': 400,
                        'headers': {'Access-Control-Allow-Origin': '*'},
                        'body': json.dumps({"error": "Tech stack is required"})
                    }
                
                result = {}
                
                for difficulty in ['easy', 'moderate', 'difficult']:
                    matching_projects = []
                    
                    for project in project_data[difficulty]:
                        if any(tech in project['tech'] for tech in tech_stack):
                            matching_tech = [tech for tech in project['tech'] if tech in tech_stack]
                            
                            project_copy = project.copy()
                            project_copy['matching_tech'] = matching_tech
                            matching_projects.append(project_copy)
                    
                    result[difficulty] = matching_projects
                
                return {
                    'statusCode': 200,
                    'headers': {
                        'Access-Control-Allow-Origin': '*',
                        'Content-Type': 'application/json'
                    },
                    'body': json.dumps(result)
                }
            
            except Exception as e:
                return {
                    'statusCode': 500,
                    'headers': {'Access-Control-Allow-Origin': '*'},
                    'body': json.dumps({"error": str(e)})
                }
        
        return {
            'statusCode': 405,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({"error": "Method not allowed"})
        }
