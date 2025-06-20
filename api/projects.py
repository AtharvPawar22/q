from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            tech_stack = [tech.lower().strip() for tech in data.get('tech_stack', [])]
            
            if not tech_stack:
                self.send_error_response(400, "Tech stack is required")
                return
        
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
                        "tech": ["go", "golang"]
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
                    },
                    {
                        "title": "Simple Vue.js Weather Widget",
                        "description": "A clean weather display component that fetches data from a free weather API and shows current conditions with icons.",
                        "tech": ["vue.js", "javascript", "html", "css"]
                    },
                    {
                        "title": "TypeScript Number Guessing Game",
                        "description": "A browser-based guessing game with type safety, difficulty levels, and score tracking.",
                        "tech": ["typescript", "html", "css"]
                    },
                    {
                        "title": "Bootstrap Landing Page Template",
                        "description": "Create a responsive landing page template using Bootstrap components and custom styling.",
                        "tech": ["bootstrap", "html", "css", "javascript"]
                    },
                    {
                        "title": "TailwindCSS Component Library",
                        "description": "Build a small collection of reusable UI components like buttons, cards, and forms using TailwindCSS.",
                        "tech": ["tailwindcss", "html", "css"]
                    },
                    {
                        "title": "Express.js Hello World API",
                        "description": "Create a simple REST API with basic routes for learning Express.js fundamentals and JSON responses.",
                        "tech": ["express", "node.js", "javascript"]
                    },
                    {
                        "title": "Flutter Habit Tracker",
                        "description": "A mobile app to track daily habits with checkboxes, streaks, and simple statistics.",
                        "tech": ["flutter", "dart"]
                    },
                    {
                        "title": "Kotlin Android Calculator",
                        "description": "A basic calculator app for Android with clean UI and standard mathematical operations.",
                        "tech": ["kotlin", "android"]
                    },
                    {
                        "title": "Unity 2D Platformer Prototype",
                        "description": "Create a simple 2D platformer with player movement, jumping, and basic collision detection.",
                        "tech": ["unity", "c#"]
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
                    },
                    {
                        "title": "Angular Task Management Board",
                        "description": "A Kanban-style task board with drag-and-drop functionality, user authentication, and local storage.",
                        "tech": ["angular", "typescript", "html", "css"]
                    },
                    {
                        "title": "Django Recipe Sharing Platform",
                        "description": "A web platform where users can share recipes, rate them, and create collections with user profiles.",
                        "tech": ["django", "python", "html", "css", "sql"]
                    },
                    {
                        "title": "Flask API with MongoDB",
                        "description": "Build a RESTful API for a book library system with CRUD operations and user authentication.",
                        "tech": ["flask", "python", "mongodb"]
                    },
                    {
                        "title": "Spring Boot Inventory System",
                        "description": "A backend system for managing product inventory with REST endpoints and PostgreSQL integration.",
                        "tech": ["spring boot", "java", "postgresql", "sql"]
                    },
                    {
                        "title": "Redis-Cached News Aggregator",
                        "description": "Aggregate news from multiple APIs with Redis caching for improved performance and rate limiting.",
                        "tech": ["node.js", "express", "redis", "javascript"]
                    },
                    {
                        "title": "Docker Multi-Service App",
                        "description": "Containerize a full-stack application with separate containers for frontend, backend, and database.",
                        "tech": ["docker", "node.js", "react", "postgresql"]
                    },
                    {
                        "title": "GraphQL Movie Database",
                        "description": "Create a GraphQL API for movie data with complex queries, mutations, and real-time subscriptions.",
                        "tech": ["graphql", "node.js", "javascript", "mongodb"]
                    },
                    {
                        "title": "Sass-Powered Design System",
                        "description": "Build a comprehensive design system with variables, mixins, and modular components using Sass.",
                        "tech": ["sass", "html", "css", "javascript"]
                    },
                    {
                        "title": "Webpack Module Federation App",
                        "description": "Create a micro-frontend architecture using Webpack's module federation with shared components.",
                        "tech": ["webpack", "javascript", "react", "html", "css"]
                    },
                    {
                        "title": "Vite Plugin Development",
                        "description": "Develop a custom Vite plugin that transforms files or adds development features to the build process.",
                        "tech": ["vite", "javascript", "typescript", "node.js"]
                    },
                    {
                        "title": "Next.js E-commerce Store",
                        "description": "Build a server-side rendered e-commerce site with product pages, cart functionality, and payment integration.",
                        "tech": ["next.js", "react", "javascript", "html", "css"]
                    },
                    {
                        "title": "Nuxt.js Blog with CMS",
                        "description": "Create a static blog site with content management, SEO optimization, and automatic deployment.",
                        "tech": ["nuxt.js", "vue.js", "javascript", "html", "css"]
                    },
                    {
                        "title": "Svelte Weather Dashboard",
                        "description": "Build a reactive weather dashboard with multiple city tracking, charts, and weather alerts.",
                        "tech": ["svelte", "javascript", "html", "css"]
                    },
                    {
                        "title": "Laravel Social Media API",
                        "description": "Create a social media backend with user posts, following system, and real-time notifications.",
                        "tech": ["laravel", "php", "mysql", "sql"]
                    },
                    {
                        "title": "Ruby on Rails Marketplace",
                        "description": "Build a marketplace platform with seller profiles, product listings, and transaction management.",
                        "tech": ["ruby on rails", "ruby", "postgresql", "sql"]
                    },
                    {
                        "title": ".NET Core Microservice",
                        "description": "Develop a microservice architecture with API gateways, service discovery, and inter-service communication.",
                        "tech": [".net", "c#", "sql", "azure"]
                    },
                    {
                        "title": "React Native Fitness Tracker",
                        "description": "A cross-platform mobile app for tracking workouts, progress photos, and fitness goals with offline support.",
                        "tech": ["react native", "javascript", "react"]
                    },
                    {
                        "title": "Unreal Engine VR Experience",
                        "description": "Create an immersive VR environment with interactive objects, spatial audio, and hand tracking.",
                        "tech": ["unreal engine", "c++"]
                    },
                    {
                        "title": "Blender Python Automation",
                        "description": "Develop Python scripts to automate 3D modeling tasks, batch processing, and custom tool creation in Blender.",
                        "tech": ["blender", "python"]
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
                        "description": "A CLI app where users can create, edit, and quiz themselves with flashcards. Stores decks in JSON and tracks quiz performance.",
                        "tech": ["python"]
                    },
                    {
                        "title": "Remote Music Jam Session",
                        "description": "Musicians can jam live with synced audio/video using WebRTC and buffer correction.",
                        "tech": ["go", "golang", "python", "react", "webrtc"]
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
                        "description": "Use GitHub's API to view, search, and create issues from the terminal. Includes auth via personal token, error handling, and clean output formatting.",
                        "tech": ["python"]
                    },
                    {
                        "title": "Behavior-Based NPC Simulator",
                        "description": "Simulate a 2D environment where non-player characters (NPCs) interact using behavior trees or rule-based systems.",
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
                    },
                    {
                        "title": "Angular Enterprise Dashboard",
                        "description": "Build a complex enterprise dashboard with real-time data visualization, role-based access control, and advanced filtering.",
                        "tech": ["angular", "typescript", "node.js", "postgresql", "sql"]
                    },
                    {
                        "title": "Django Machine Learning Pipeline",
                        "description": "Create a web platform for training, evaluating, and deploying ML models with data preprocessing and model versioning.",
                        "tech": ["django", "python", "postgresql", "redis", "docker"]
                    },
                    {
                        "title": "Flask Microservices Architecture",
                        "description": "Design a distributed system with multiple Flask services, API gateway, service discovery, and centralized logging.",
                        "tech": ["flask", "python", "docker", "redis", "postgresql"]
                    },
                    {
                        "title": "Spring Boot Event Sourcing System",
                        "description": "Implement an event-driven architecture with CQRS pattern, event store, and eventual consistency.",
                        "tech": ["spring boot", "java", "postgresql", "mongodb", "docker"]
                    },
                    {
                        "title": "Kubernetes Orchestrated Application",
                        "description": "Deploy a multi-tier application on Kubernetes with auto-scaling, health checks, and rolling updates.",
                        "tech": ["kubernetes", "docker", "node.js", "postgresql", "redis"]
                    },
                    {
                        "title": "AWS Serverless Data Pipeline",
                        "description": "Build a serverless data processing pipeline using Lambda, S3, and DynamoDB with real-time analytics.",
                        "tech": ["aws", "python", "node.js", "sql"]
                    },
                    {
                        "title": "Azure DevOps CI/CD Platform",
                        "description": "Create a complete DevOps solution with automated testing, deployment pipelines, and infrastructure as code.",
                        "tech": ["azure", ".net", "c#", "docker", "sql"]
                    },
                    {
                        "title": "Git-Based Code Review System",
                        "description": "Build a web-based code review platform that integrates with Git repositories and provides diff visualization.",
                        "tech": ["git", "node.js", "react", "postgresql", "typescript"]
                    },
                    {
                        "title": "GraphQL Federation Gateway",
                        "description": "Implement a federated GraphQL architecture that combines multiple services into a unified API schema.",
                        "tech": ["graphql", "node.js", "typescript", "docker", "postgresql"]
                    },
                    {
                        "title": "Advanced Sass Framework",
                        "description": "Create a comprehensive CSS framework with theming system, responsive utilities, and component architecture.",
                        "tech": ["sass", "javascript", "webpack", "html", "css"]
                    },
                    {
                        "title": "Webpack Plugin Ecosystem",
                        "description": "Develop a suite of Webpack plugins for code optimization, asset management, and development workflow enhancement.",
                        "tech": ["webpack", "javascript", "typescript", "node.js"]
                    },
                    {
                        "title": "Vite-Powered Monorepo",
                        "description": "Set up a monorepo with multiple packages, shared dependencies, and optimized build processes using Vite.",
                        "tech": ["vite", "typescript", "node.js", "react", "vue.js"]
                    },
                    {
                        "title": "Next.js Full-Stack SaaS Platform",
                        "description": "Build a complete SaaS application with authentication, subscription billing, admin dashboard, and API management.",
                        "tech": ["next.js", "react", "typescript", "postgresql", "stripe"]
                    },
                    {
                        "title": "Nuxt.js Headless CMS",
                        "description": "Create a headless CMS with content management, API generation, and multi-site deployment capabilities.",
                        "tech": ["nuxt.js", "vue.js", "typescript", "mongodb", "graphql"]
                    },
                    {
                        "title": "Svelte Compiler Extension",
                        "description": "Extend the Svelte compiler with custom transformations, optimizations, and development tools.",
                        "tech": ["svelte", "javascript", "typescript", "node.js"]
                    },
                    {
                        "title": "Laravel Enterprise API",
                        "description": "Build a scalable enterprise API with advanced authentication, rate limiting, caching, and comprehensive documentation.",
                        "tech": ["laravel", "php", "redis", "mysql", "docker"]
                    },
                    {
                        "title": "Ruby on Rails Multi-Tenant SaaS",
                        "description": "Develop a multi-tenant SaaS platform with tenant isolation, custom domains, and scalable architecture.",
                        "tech": ["ruby on rails", "ruby", "postgresql", "redis", "docker"]
                    },
                    {
                        "title": ".NET Distributed System",
                        "description": "Create a distributed system with message queues, event sourcing, and microservices communication patterns.",
                        "tech": [".net", "c#", "azure", "sql", "docker"]
                    },
                    {
                        "title": "Swift iOS AR Shopping App",
                        "description": "Build an augmented reality shopping app with 3D product visualization, gesture recognition, and payment integration.",
                        "tech": ["swift", "arkit", "ios"]
                    },
                    {
                        "title": "Kotlin Multiplatform Framework",
                        "description": "Develop a cross-platform framework that shares business logic between Android, iOS, and web applications.",
                        "tech": ["kotlin", "android", "ios"]
                    },
                    {
                        "title": "Flutter Desktop Enterprise App",
                        "description": "Create a cross-platform desktop application with complex UI, database integration, and native system integration.",
                        "tech": ["flutter", "dart", "sql", "desktop"]
                    },
                    {
                        "title": "React Native AR/VR Platform",
                        "description": "Build a mobile AR/VR platform with 3D rendering, spatial tracking, and cross-platform compatibility.",
                        "tech": ["react native", "javascript", "react", "ar", "vr"]
                    },
                    {
                        "title": "Unity Multiplayer Game Engine",
                        "description": "Develop a multiplayer game with networked physics, real-time synchronization, and scalable server architecture.",
                        "tech": ["unity", "c#", "networking", "multiplayer"]
                    },
                    {
                        "title": "Unreal Engine Procedural World Generator",
                        "description": "Create a system for generating vast, detailed game worlds using procedural algorithms and advanced rendering techniques.",
                        "tech": ["unreal engine", "c++", "procedural generation"]
                    },
                    {
                        "title": "Blender Production Pipeline",
                        "description": "Develop a complete 3D production pipeline with automated rendering, asset management, and team collaboration tools.",
                        "tech": ["blender", "python", "pipeline", "automation"]
                    }
                ]
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
            
            self.send_success_response(result)
            
        except Exception as e:
            self.send_error_response(500, str(e))

    def send_success_response(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def send_error_response(self, status_code, message):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        error_response = {"error": message}
        self.wfile.write(json.dumps(error_response).encode('utf-8'))
