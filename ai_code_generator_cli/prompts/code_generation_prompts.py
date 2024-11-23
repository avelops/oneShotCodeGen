from langchain.prompts import PromptTemplate

# V1 Prompts - Separate DB, Backend, and Frontend
CODE_GENERATION_V1_DB = """
You are an expert backend developer. Tasked with generating the **Data Models** and **Database Setup** for an application.
Based on the provided technical and functional specifications, generate the code and output it in JSON format as specified.

Functional Requirements:
{functional_requirements}

Technical Requirements:
{technical_requirements}

**Code Generation Guidelines:**

- Use modern JavaScript (ES6+) syntax.
- Define models with attributes, data types, validations, and associations.
- Include necessary imports and exports.
- Do not include any code outside the code that goes into the file content.
- Do not include comments explaining each part of the code.
- create some mock data in all the tables and a mock user with email user@example.com and password 123456, this data should be automatically added when the server starts.
- make sure you share the mkdir command for backend
 - Make sure there are no commands that run on a file as we first run the commands for installation and then create the files, so if you give commands that run on a file like node server.js it will fail as the file does not exist yet
 - All the subsequent commands to install the packages should be shared in the commands key with prefix cd backend
 - Do not share startup commands like npm start, npm run dev, etc
 - Share project intialisation commands like npm init -y, etc after the mkdir command and add the prefix cd backend this is needed as commands will be run in the parent directory
 - Do not share any other mkdir commands to create sub folders, they are not needed as they get automatically created when files are created
 - share commands to install the dependencies related to DB
 - Do not share any other commands that are not related to DB
Provide the implementation in JSON format:
{{
    "folders": ["list of folders to create"],
    "files": {{
        "path/to/file": "file content" 
    }},
    "commands": ["list of commands to run"] 
}}
"""
CODE_GENERATION_V1_API = """
You are an expert backend developer. Ttasked with generating the **Backend API Endpoints** and **Business Logic** for the application, using Express.js and Sequelize ORM. 
Based on the provided technical and functional specifications, generate the code and output it in JSON format as specified.


Functional Requirements:
{functional_requirements}

Technical Requirements:
{technical_requirements}

Database Structure:
{database_structure}

**Code Generation Guidelines:**

- Organize code into controllers, routes, and middleware.
- Include necessary imports and exports.
- Use async/await for asynchronous operations.
- Do not include comments explaining each part of the code.
- Do not include any code outside the code that goes into the file content.
- Run backend on port 3000 and main server file runs in server.js and cors is enabled
- For commands do not share mkdir command as backend folder is created previously
 - Make sure there are no commands that run on a file as we first run the commands for installation and then create the files, so if you give commands that run on a file like node server.js it will fail as the file does not exist yet
 - All the subsequent commands to install the packages should be shared in the commands key with prefix cd backend
 - Do not share startup commands like npm start, npm run dev, etc
 - Share project intialisation commands like npm init -y, etc after the mkdir command and add the prefix cd backend this is needed as commands will be run in the parent directory
 - Do not share any other mkdir commands to create sub folders, they are not needed as they get automatically created when files are created
 - share commands to install the dependencies related to backend API and business logic
 - Do not share any other commands that are not related to backend API and business logic

Provide the implementation in JSON format:
{{
    "folders": ["list of folders to create"],
    "files": {{
        "path/to/file": "file content" 
    }},
    "commands": ["list of commands to run"] 
}}
"""

CODE_GENERATION_V1_FRONTEND = """
You are an expert frontend developer. Tasked with generating the **Frontend Components** and **UI Logic** for the application, using React.js and Material-UI.

Functional Requirements:
{functional_requirements}

Technical Requirements:
{technical_requirements}

Database Structure:
{database_structure}

Backend API Code:
{backend_code}



**Code Generation Guidelines:**

- Use functional components and React Hooks
- Implement form handling, validations, and API interactions
- Ensure form fields match database schema
- Ensure API calls match backend endpoints
- Include TypeScript interfaces/types that match database models
- Do not add comments
- Ensure without fail that all UI elements/component/pages are generated in the code ouput
- Ensure all the events click are linked to backend action, do not leave any action unmapped
- Follow the ESLint Airbnb style guide
- Do not include any code outside the code that goes into the file content
- Run frontend on port 3001 and and ensure frontend is calling the backend API correctly to port 3000
- Ensure that if any other librarry is imported in frontend we share the commands to install the dependencies, specially for MUI if we are using the icons library
- As we will use npx to setup a base react app, do share if any changes are needed in app.js, app.css or index.js or index.css
- make sure for frontend call the npx command to intiatlise and create the folder
 - All the subsequent commands to install the packages should be shared in the commands key with prefix cd frontend
 - Do not share startup commands like npm start, npm run dev, etc
 - Share other dependecy installation commands and add the prefix cd backend this is needed as commands will be run in the parent directory
 - Do not share any other mkdir commands to create sub folders, they are not needed as they get automatically created when files are created
 - share commands to install the dependencies related to frontend
 - Do not share any other commands that are not related to frontend
 
 Provide the implementation in JSON format:
{{
    "folders": ["list of folders to create"],
    "files": {{
        "path/to/file": "file content"  
    }},
    "commands": ["list of commands to run"] 
}}
"""

# V2 Prompts - Combined API (DB + Backend) and Frontend
CODE_GENERATION_V2_BACKEND = """
You are an expert backend developer. Tasked with generating the **Entire Backend Code** for the application, including Data Models, APIs, and Business Logic, using Express.js and Sequelize ORM.
Based on the provided technical and functional specifications, generate the code and output it in JSON format as specified.

Functional Requirements:
{functional_requirements}

Technical Requirements:
{technical_requirements}

**Code Generation Guidelines:**

- Generate both database models and API endpoints in a cohesive manner
- Use modern JavaScript (ES6+) syntax
- Define models with attributes, data types, validations, and associations
- Implement RESTful API endpoints that properly utilize the models
- Organize code into models, controllers, routes, and middleware
- Include necessary imports and exports
- Use async/await for asynchronous operations
- Implement proper error handling and validation
- Do not include comments explaining each part of the code
- Do not include any code outside the code that goes into the file content
- Run backend on port 3000 and main server file runs in server.js and cors is enabled
- create some mock data in all the tables and a mock user with email user@example.com and password 123456, this data should be automatically added when the server starts.
- make sure you share the mkdir command for backend
 - Make sure there are no commands that run on a file as we first run the commands for installation and then create the files, so if you give commands that run on a file like node server.js it will fail as the file does not exist yet
 - All the subsequent commands to install the packages should be shared in the commands key with prefix cd backend
 - Do not share startup commands like npm start, npm run dev, etc
 - Share project intialisation commands like npm init -y, etc after the mkdir command and add the prefix cd backend this is needed as commands will be run in the parent directory
 - Do not share any other mkdir commands to create sub folders, they are not needed as they get automatically created when files are created
 - share commands to install the dependencies related to entire backend
 - Do not share any other commands that are not related to entire backend
 Provide the implementation in JSON format:
{{
    "folders": ["list of folders to create"],
    "files": {{
        "path/to/file": "file content"  
    }},
    "commands": ["list of commands to run"] 
}}
"""
CODE_GENERATION_V2_FRONTEND = """
You are an expert frontend developer. Tasked with generating the **Frontend Components** and **UI Logic** for the application, using React.js and Material-UI.

Functional Requirements:
{functional_requirements}

Technical Requirements:
{technical_requirements}

Backend API Code:
{backend_code}

**Code Generation Guidelines:**

- Use functional components and React Hooks
- Implement form handling, validations, and API interactions
- Ensure API calls match backend endpoints exactly
- Include TypeScript interfaces/types that match backend models
- Implement proper error handling and loading states
- Do not add comments
- Ensure without fail that all UI elements/component/pages are generated in the code ouput
- Ensure all the events click are linked to backend action, do not leave any action unmapped
- Follow the ESLint Airbnb style guide
- Do not include any code outside the code that goes into the file content
- Run frontend on port 3001 and and ensure frontend is calling the backend API correctly to port 3000
- Ensure that if any other librarry is imported in frontend we share the commands to install the dependencies, specially for MUI if we are using the icons library
- As we will use npx to setup a base react app, do share if any changes are needed in app.js, app.css or index.js or index.css
- make sure for frontend call the npx command to intiatlise and create the folder
 - All the subsequent commands to install the packages should be shared in the commands key with prefix cd frontend
 - Do not share startup commands like npm start, npm run dev, etc
 - Share other dependecy installation commands and add the prefix cd backend this is needed as commands will be run in the parent directory
 - Do not share any other mkdir commands to create sub folders, they are not needed as they get automatically created when files are created
 - share commands to install the dependencies related to frontend
 - Do not share any other commands that are not related to frontend
 
Provide the implementation in JSON format:
{{
    "folders": ["list of folders to create"],
    "files": {{
        "path/to/file": "file content"  
    }},
    "commands": ["list of commands to run"] 
}}
"""

# V3 Prompts
CODE_GENERATION_V3_API = """
You are an expert backend developer. Tasked with generating the **Entire Backend Code** for the application, including Data Models, APIs, and Business Logic, using Express.js and Sequelize ORM.
Based on the provided technical and functional specifications and code templates, generate the code and output it in JSON format as specified.

Functional Requirements:
{functional_requirements}

Technical Requirements:
{technical_requirements}

Code Templates:
{backend_code_templates}

**Code Generation Guidelines:**

- Follow the provided code templates structure and patterns
- Generate both database models and API endpoints
- Use modern JavaScript (ES6+) syntax
- Implement all required functionalities as per specifications
- Ensure proper error handling and validation
- Do not include comments explaining each part of the code
- Do not include any code outside the code that goes into the file content
- Run backend on port 3000 and main server file runs in server.js and cors is enabled
- create some mock data in all the tables and a mock user with email user@example.com and password 123456, this data should be automatically added when the server starts.
- make sure you share the mkdir command for backend
 - Make sure there are no commands that run on a file as we first run the commands for installation and then create the files, so if you give commands that run on a file like node server.js it will fail as the file does not exist yet
 - All the subsequent commands to install the packages should be shared in the commands key with prefix cd backend
 - Do not share startup commands like npm start, npm run dev, etc
 - Share project intialisation commands like npm init -y, etc after the mkdir command and add the prefix cd backend this is needed as commands will be run in the parent directory
 - Do not share any other mkdir commands to create sub folders, they are not needed as they get automatically created when files are created
 - share commands to install the dependencies related to entire backend
 - Do not share any other commands that are not related to entire backend

Provide the implementation in JSON format:
{{
    "folders": ["list of folders to create"],
    "files": {{
        "path/to/file": "file content"  
    }},
    "commands": ["list of commands to run"] 
}}
"""

CODE_GENERATION_V3_FRONTEND = """
You are an expert frontend developer. Tasked with generating the **Frontend Components** and **UI Logic** for the application, using React.js and Material-UI.

Functional Requirements:
{functional_requirements}

Technical Requirements:
{technical_requirements}

Backend API Code:
{backend_code}

Code Templates:
{frontend_code_templates}

**Code Generation Guidelines:**

- Follow the provided code templates structure and patterns
- Use functional components and React Hooks
- Implement form handling, validations, and API interactions
- Ensure API calls match backend endpoints exactly
- Include TypeScript interfaces/types that match backend models
- Do not add comments
- Ensure without fail that all UI elements/component/pages are generated in the code ouput
- Ensure all the events click are linked to backend action, do not leave any action unmapped
- Follow the ESLint Airbnb style guide
- Do not include any code outside the code that goes into the file content
- Run frontend on port 3001 and and ensure frontend is calling the backend API correctly to port 3000
- Ensure that if any other librarry is imported in frontend we share the commands to install the dependencies, specially for MUI if we are using the icons library
- As we will use npx to setup a base react app, do share if any changes are needed in app.js, app.css or index.js or index.css
- make sure for frontend call the npx command to intiatlise and create the folder
 - All the subsequent commands to install the packages should be shared in the commands key with prefix cd frontend
 - Do not share startup commands like npm start, npm run dev, etc
 - Share other dependecy installation commands and add the prefix cd backend this is needed as commands will be run in the parent directory
 - Do not share any other mkdir commands to create sub folders, they are not needed as they get automatically created when files are created
 - share commands to install the dependencies related to frontend
 - Do not share any other commands that are not related to frontend

Provide the implementation in JSON format:
{{
    "folders": ["list of folders to create"],
    "files": {{
        "path/to/file": "file content"  
    }},
    "commands": ["list of commands to run"] 
}}
"""

# Version configurations
CODE_GENERATION_CONFIGS = {
    "v1": {
        "prompts": {
            "database": PromptTemplate(
                input_variables=["functional_requirements", "technical_requirements"],
                template=CODE_GENERATION_V1_DB
            ),
            "backend": PromptTemplate(
                input_variables=["functional_requirements", "technical_requirements", "database_structure"],
                template=CODE_GENERATION_V1_API
            ),
            "frontend": PromptTemplate(
                input_variables=[
                    "functional_requirements",
                    "technical_requirements",
                    "database_structure",
                    "backend_code"
                ],
                template=CODE_GENERATION_V1_FRONTEND
            )
        }
    },
    "v2": {
        "prompts": {
            "backend": PromptTemplate(
                input_variables=["functional_requirements", "technical_requirements"],
                template=CODE_GENERATION_V2_BACKEND
            ),
            "frontend": PromptTemplate(
                input_variables=[
                    "functional_requirements",
                    "technical_requirements",
                    "backend_code"
                ],
                template=CODE_GENERATION_V2_FRONTEND
            )
        }
    },
    "v3": {
        "prompts": {
            "backend": PromptTemplate(
                input_variables=[
                    "functional_requirements",
                    "technical_requirements",
                    "backend_code_templates"
                ],
                template=CODE_GENERATION_V3_API
            ),
            "frontend": PromptTemplate(
                input_variables=[
                    "functional_requirements",
                    "technical_requirements",
                    "backend_code",
                    "frontend_code_templates"
                ],
                template=CODE_GENERATION_V3_FRONTEND
            )
        }
    }
}

def get_code_generation_prompts(version: str, backend_template: str = None, frontend_template: str = None) -> dict:
    """Get the code generation prompts for the specified version."""
    if version not in CODE_GENERATION_CONFIGS:
        raise ValueError(f"Invalid code generation prompt version: {version}")
    
    prompts = CODE_GENERATION_CONFIGS[version]["prompts"]
    
    # If version is v3, add templates to the prompts
    if version == "v3":
        if backend_template and "backend" in prompts:
            prompts["backend"].template = prompts["backend"].template.replace(
                "{backend_code_templates}", backend_template
            )
        if frontend_template and "frontend" in prompts:
            prompts["frontend"].template = prompts["frontend"].template.replace(
                "{frontend_code_templates}", frontend_template
            )
    
    return prompts 