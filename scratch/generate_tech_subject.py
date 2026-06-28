import json
import re

def main():
    seed_file_path = 'lib/services/seed_data.dart'
    
    # 1. Read seed_data.dart
    with open(seed_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx_raw = content.find(start_str)
    if start_idx_raw == -1:
        print("Could not find fullSeedJson")
        return
        
    start_idx = content.find('{', start_idx_raw)
    end_idx = content.rfind("''';")
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find JSON bounds")
        return
        
    json_string = content[start_idx:end_idx]
    data = json.loads(json_string)
    
    # 2. Add Technology Subject
    subjects = data.get('subjects', [])
    if not any(s['id'] == 'tech' for s in subjects):
        subjects.append({
            'name': 'Technology',
            'id': 'tech'
        })
    data['subjects'] = subjects
    
    # 3. Add Chapters (Units)
    chapters = data.get('chapters', [])
    new_chapters = [
        {'subjectId': 'tech', 'title': 'Unit 1: Introduction to System Analysis and Design', 'id': 'tech_ch1'},
        {'subjectId': 'tech', 'title': 'Unit 2: Microsoft Access 2016', 'id': 'tech_ch2'},
        {'subjectId': 'tech', 'title': 'Unit 3: Programming using Python', 'id': 'tech_ch3'},
        {'subjectId': 'tech', 'title': 'Unit 4: ICT Security and Ethics', 'id': 'tech_ch4'},
    ]
    for ch in new_chapters:
        if not any(c['id'] == ch['id'] for c in chapters):
            chapters.append(ch)
    data['chapters'] = chapters

    # Questions database pool for Unit 1: Introduction to System Analysis and Design
    unit1_base = [
        # Easy (at least 20 base)
        {"q": "What is the origin of the word 'system'?", "a": "a", "opts": {"a": "Greek word 'systema'", "b": "Latin word 'systemia'", "c": "French word 'système'", "d": "German word 'system'"}, "lvl": "easy"},
        {"q": "A system is defined as an interconnected set of what?", "a": "b", "opts": {"a": "Random objects", "b": "Business procedures working for a purpose", "c": "Isolated computer files", "d": "Independent people"}, "lvl": "easy"},
        {"q": "What are the physical components of an information system called?", "a": "a", "opts": {"a": "Hardware", "b": "Software", "c": "Data", "d": "Process"}, "lvl": "easy"},
        {"q": "Which of the following is an example of system software?", "a": "c", "opts": {"a": "Microsoft Word", "b": "Google Chrome", "c": "Operating System", "d": "Excel Spreadsheet"}, "lvl": "easy"},
        {"q": "What component of an information system represents raw materials stored in tables?", "a": "d", "opts": {"a": "Hardware", "b": "People", "c": "Processes", "d": "Data"}, "lvl": "easy"},
        {"q": "What do we call the stakeholders, managers, and IT team members in an information system?", "a": "b", "opts": {"a": "Hardware", "b": "People", "c": "Data", "d": "Process"}, "lvl": "easy"},
        {"q": "Which component refers to the set of actions taken to attain a desired objective?", "a": "c", "opts": {"a": "Software", "b": "Data", "c": "Process", "d": "People"}, "lvl": "easy"},
        {"q": "Who is the professional that studies the problems and needs of an organization to recommend improvements?", "a": "a", "opts": {"a": "System Analyst", "b": "Database Administrator", "c": "Hardware Engineer", "d": "Network Administrator"}, "lvl": "easy"},
        {"q": "What does SDLC stand for?", "a": "b", "opts": {"a": "System Design Logical Control", "b": "System Development Life Cycle", "c": "Software Deployment Limit Cycle", "d": "Structured Data Logic Chart"}, "lvl": "easy"},
        {"q": "What is the first phase of the System Development Life Cycle?", "a": "c", "opts": {"a": "Analysis", "b": "Design", "c": "Planning", "d": "Testing"}, "lvl": "easy"},
        {"q": "Which phase of the SDLC is dedicated to coding the proposed system?", "a": "d", "opts": {"a": "Design", "b": "Testing", "c": "Maintenance", "d": "System Construction"}, "lvl": "easy"},
        {"q": "What type of testing tests individual parts or components of the system independently?", "a": "a", "opts": {"a": "Unit testing", "b": "Integration testing", "c": "System testing", "d": "Acceptance testing"}, "lvl": "easy"},
        {"q": "What is the term for fixing bugs, upgrading, or adding new features after system deployment?", "a": "b", "opts": {"a": "Testing", "b": "Maintenance", "c": "Analysis", "d": "Construction"}, "lvl": "easy"},
        {"q": "Which SDLC phase focuses on building physical models and designing user interfaces?", "a": "d", "opts": {"a": "Planning", "b": "Analysis", "c": "Testing", "d": "Design"}, "lvl": "easy"},
        {"q": "What fact-finding method involves the analyst observing the current system operations firsthand?", "a": "a", "opts": {"a": "Observation", "b": "Interview", "c": "Questionnaire", "d": "Document Review"}, "lvl": "easy"},
        {"q": "What fact-finding method distributes written questions to find out the views of system users?", "a": "c", "opts": {"a": "Observation", "b": "Interview", "c": "Questionnaire", "d": "Document Review"}, "lvl": "easy"},
        {"q": "Which deployment method completely drops the old system and starts the new system immediately?", "a": "b", "opts": {"a": "Parallel deployment", "b": "Direct deployment", "c": "Pilot deployment", "d": "Phased deployment"}, "lvl": "easy"},
        {"q": "Which system development methodology has a linear, non-overlapping sequence of phases?", "a": "a", "opts": {"a": "Waterfall model", "b": "Agile method", "c": "RAD model", "d": "Extreme Programming"}, "lvl": "easy"},
        {"q": "Which methodology is highly iterative and welcomes late changes in requirements?", "a": "b", "opts": {"a": "Waterfall model", "b": "Agile method", "c": "Structured model", "d": "Linear model"}, "lvl": "easy"},
        {"q": "What does RAD stand for?", "a": "c", "opts": {"a": "Random Access Database", "b": "Resource Application Development", "c": "Rapid Application Development", "d": "Ratio Analysis Design"}, "lvl": "easy"},
        
        # Medium (at least 20 base)
        {"q": "Which type of feasibility study determines if a proposed system is financially affordable and beneficial?", "a": "c", "opts": {"a": "Technical Feasibility", "b": "Operational Feasibility", "c": "Economic Feasibility", "d": "Schedule Feasibility"}, "lvl": "medium"},
        {"q": "Which feasibility study evaluates whether the solution can be built with available technology?", "a": "a", "opts": {"a": "Technical Feasibility", "b": "Operational Feasibility", "c": "Economic Feasibility", "d": "Schedule Feasibility"}, "lvl": "medium"},
        {"q": "What is the primary goal of the preliminary investigation during the Planning phase?", "a": "b", "opts": {"a": "To write the source code", "b": "To determine opportunities or issues and create a feasibility report", "c": "To perform unit testing", "d": "To design the database tables"}, "lvl": "medium"},
        {"q": "Which of the following is a disadvantage of the Observation method?", "a": "d", "opts": {"a": "It provides first-hand experience", "b": "It yields reliable data", "c": "It is relatively inexpensive", "d": "People under study may feel uncomfortable and make mistakes"}, "lvl": "medium"},
        {"q": "Which fact-finding technique is best if the analyst wants to probe deeply into specific aspects with key individuals?", "a": "b", "opts": {"a": "Observation", "b": "Interview", "c": "Questionnaire", "d": "Document Review"}, "lvl": "medium"},
        {"q": "What is the main deliverable of the system Analysis stage?", "a": "c", "opts": {"a": "Working Prototype", "b": "Database schema", "c": "Requirement Specification (or SRS)", "d": "Source Code"}, "lvl": "medium"},
        {"q": "Which design aspect focuses on how the user communicates with the computer system?", "a": "a", "opts": {"a": "User Interface (UI) Design", "b": "Data Storage Design", "c": "Process Design", "d": "Output Design"}, "lvl": "medium"},
        {"q": "What kind of testing integrates already tested units to form a complete system and tests their interaction?", "a": "b", "opts": {"a": "Unit testing", "b": "Integration testing", "c": "Acceptance testing", "d": "Beta testing"}, "lvl": "medium"},
        {"q": "What deployment method runs both the old and new systems together for a trial period?", "a": "c", "opts": {"a": "Direct deployment", "b": "Pilot deployment", "c": "Parallel deployment", "d": "Phased deployment"}, "lvl": "medium"},
        {"q": "What deployment method introduces the new system gradually, step-by-step, while discarding the old one?", "a": "d", "opts": {"a": "Direct deployment", "b": "Parallel deployment", "c": "Pilot deployment", "d": "Phased deployment"}, "lvl": "medium"},
        {"q": "What is a main advantage of the Waterfall model?", "a": "a", "opts": {"a": "Fits well for smaller projects with clear requirements and milestones", "b": "Welcomes late changes in requirements", "c": "Involves constant user feedback", "d": "Produces functional prototypes early"}, "lvl": "medium"},
        {"q": "Which of the following is a disadvantage of the Waterfall model?", "a": "b", "opts": {"a": "Phases are processed one at a time", "b": "High risk, uncertainty, and inability to meet changing requirements", "c": "It requires high modeling skills", "d": "Milestones are well known"}, "lvl": "medium"},
        {"q": "Which system development methodology includes Scrum and Extreme Programming (XP) as examples?", "a": "c", "opts": {"a": "Waterfall", "b": "RAD", "c": "Agile", "d": "Logical"}, "lvl": "medium"},
        {"q": "In RAD, what is developed rapidly to gather user feedback and refine requirements?", "a": "d", "opts": {"a": "Requirement Document", "b": "Full Database", "c": "Flowchart", "d": "Prototypes"}, "lvl": "medium"},
        {"q": "What is a primary disadvantage of the Agile method?", "a": "a", "opts": {"a": "Less predictability and potential lack of necessary documentation", "b": "Inability to accommodate changes", "c": "Longer development cycle", "d": "High stiffness of stages"}, "lvl": "medium"},
        {"q": "Which testing type is carried out at the late stages with the users to obtain formal approval?", "a": "b", "opts": {"a": "System testing", "b": "Acceptance testing", "c": "Integration testing", "d": "Unit testing"}, "lvl": "medium"},
        {"q": "Which type of deployment converts the system by installing it for a small group of users first?", "a": "c", "opts": {"a": "Direct deployment", "b": "Parallel deployment", "c": "Pilot deployment", "d": "Phased deployment"}, "lvl": "medium"},
        {"q": "What type of design relates to abstract representations of input, output, and data flows using tools like ERDs?", "a": "a", "opts": {"a": "Logical Design", "b": "Physical Design", "c": "Construction Design", "d": "Process Design"}, "lvl": "medium"},
        {"q": "What role does the System Analyst play during the Coding/Construction phase?", "a": "c", "opts": {"a": "They do all the programming", "b": "They perform hardware maintenance", "c": "They monitor progress and clarify conceptual designs for programmers", "d": "They run the deployment servers"}, "lvl": "medium"},
        {"q": "What is the primary objective of the maintenance phase?", "a": "b", "opts": {"a": "To rewrite the entire system from scratch", "b": "To keep the system operational, fix bugs, and apply updates", "c": "To carry out integration tests", "d": "To design logical ERDs"}, "lvl": "medium"},

        # Hard (at least 20 base)
        {"q": "Which of the following describes the 'technical feasibility' check?", "a": "a", "opts": {"a": "Determines if the proposed solution can be supported by existing technology", "b": "Determines if the system will be used in proper working conditions", "c": "Determines if the system is cost-effective", "d": "Determines if the system can be built within the required timeframe"}, "lvl": "hard"},
        {"q": "Feasibility report recommendations should evaluate costs and benefits based on which factors?", "a": "b", "opts": {"a": "Programming syntax and variables", "b": "Organizational, technological, economic, and time factors", "c": "User interface layouts only", "d": "Number of lines of code"}, "lvl": "hard"},
        {"q": "How does Logical Design differ from Physical Design in systems analysis?", "a": "d", "opts": {"a": "Logical design is written in code, physical is a diagram", "b": "Physical design uses ERDs, logical uses servers", "c": "Logical design is cost-effective, physical design is not", "d": "Logical design is abstract (like ERDs), physical design relates to actual input/output processes"}, "lvl": "hard"},
        {"q": "Which deployment method has the highest risk of database failure if the system crashes?", "a": "b", "opts": {"a": "Parallel deployment", "b": "Direct deployment", "c": "Pilot deployment", "d": "Phased deployment"}, "lvl": "hard"},
        {"q": "Which deployment method is most resource-intensive since users must enter data twice into two systems?", "a": "c", "opts": {"a": "Direct deployment", "b": "Pilot deployment", "c": "Parallel deployment", "d": "Phased deployment"}, "lvl": "hard"},
        {"q": "What is the specific objective of 'Operational Feasibility'?", "a": "a", "opts": {"a": "To determine if the proposed solution is able to be used and will be in proper working condition", "b": "To calculate the return on investment", "c": "To ensure correct hardware servers are selected", "d": "To schedule coding deadlines"}, "lvl": "hard"},
        {"q": "Why is the preliminary investigation considered an essential stage in the Planning phase?", "a": "b", "opts": {"a": "Because it is where coding begins", "b": "Because the results and feasibility options affect the entire subsequent development process", "c": "Because it defines the user access control lists", "d": "Because it completes the logical design phase"}, "lvl": "hard"},
        {"q": "Which is a limitation of the Waterfall model when building systems for dynamic business environments?", "a": "c", "opts": {"a": "It has too many parallel paths", "b": "It doesn't define any milestones", "c": "It cannot easily accommodate modifications once a phase is finished, which may cause it to not meet actual user needs", "d": "It requires continuous prototype feedback cycles"}, "lvl": "hard"},
        {"q": "In Rapid Application Development (RAD), how do prototype cycles accelerate development?", "a": "d", "opts": {"a": "By skipping the testing phase", "b": "By hiring fewer programmers", "c": "By using logical designs instead of databases", "d": "By letting users interact with prototypes early to refine system specifications iteratively"}, "lvl": "hard"},
        {"q": "Under what circumstance would a system analyst choose Agile over RAD?", "a": "a", "opts": {"a": "When the project requires continuous development, iterations, and has highly unpredictable requirements", "b": "When modeling skills are very low", "c": "When there is no need for documentation", "d": "When direct deployment is mandatory"}, "lvl": "hard"},
        {"q": "What is a main characteristic of the Extreme Programming (XP) methodology?", "a": "b", "opts": {"a": "It uses a linear flow without loops", "b": "It focuses on iterations, user stories, tasks, and automated unit testing", "c": "It forbids prototyping", "d": "It is designed strictly for database administration"}, "lvl": "hard"},
        {"q": "Which step in the RAD model involves conversion of prototypes into working models and gathering user feedback?", "a": "c", "opts": {"a": "Define project requirements", "b": "Begin prototypes", "c": "Gather user feedback", "d": "Present your system"}, "lvl": "hard"},
        {"q": "What is the key deliverable of the Systems Design stage that is submitted for review and approval to management?", "a": "d", "opts": {"a": "User login credentials", "b": "Test cases", "c": "Feasibility report", "d": "System Design Specification"}, "lvl": "hard"},
        {"q": "A user access control policy lists roles like Administrators, Supervisors, and Guests. This belongs to:", "a": "c", "opts": {"a": "Process Design", "b": "Input Design", "c": "Controls Design", "d": "Logical Design"}, "lvl": "hard"},
        {"q": "How does Unit testing differ from System testing?", "a": "a", "opts": {"a": "Unit testing tests individual modules independently, while System testing tests the entire integrated system with inputs", "b": "Unit testing is done by users, System testing is done by analysts", "c": "System testing has no output checks, Unit testing does", "d": "Unit testing is during deployment, System testing is during construction"}, "lvl": "hard"},
        {"q": "What is the main objective of 'Schedule Feasibility'?", "a": "c", "opts": {"a": "To estimate system coding budget", "b": "To design logical project structures", "c": "To determine if the system can be developed and operational within the required time frame", "d": "To organize user interviews"}, "lvl": "hard"},
        {"q": "Which fact-finding technique is most suitable for collecting statistical data from a very large, geographically dispersed group of users?", "a": "b", "opts": {"a": "Interview", "b": "Questionnaire", "c": "Observation", "d": "Document Review"}, "lvl": "hard"},
        {"q": "If a system analyst is reviewing existing documentations, folders, and reports of the current system, they are performing:", "a": "d", "opts": {"a": "Observation", "b": "Interview", "c": "Questionnaire", "d": "Document Review"}, "lvl": "hard"},
        {"q": "What are the characteristics of a good user interface (UI)?", "a": "a", "opts": {"a": "Consistent layout, user friendly, simple, easy to seek support/fix errors", "b": "vibrant background colors and flashing icons", "c": "no help pages and a command-line interface", "d": "complex forms and logical ERDs"}, "lvl": "hard"},
        {"q": "In database storage design, what elements must be specified for each field?", "a": "c", "opts": {"a": "Form size and background color", "b": "User privileges and query scripts", "c": "Field Name, Data Type, and Description", "d": "IP address and subnet mask"}, "lvl": "hard"}
    ]

    # Questions database pool for Unit 2: Microsoft Access 2016
    unit2_base = [
        # Easy
        {"q": "What is a database?", "a": "a", "opts": {"a": "A collection of logically related data stored in electronic form", "b": "A spreadsheet for accounting only", "c": "A software application for word processing", "d": "A collection of random files on a hard drive"}, "lvl": "easy"},
        {"q": "Which database object in Microsoft Access is used to store data in rows and columns?", "a": "b", "opts": {"a": "Forms", "b": "Tables", "c": "Queries", "d": "Reports"}, "lvl": "easy"},
        {"q": "Which object in Microsoft Access is designed for entering, editing, and deleting records in tables?", "a": "a", "opts": {"a": "Forms", "b": "Tables", "c": "Queries", "d": "Reports"}, "lvl": "easy"},
        {"q": "Which object is used to search and compile data based on specific conditions?", "a": "c", "opts": {"a": "Forms", "b": "Tables", "c": "Queries", "d": "Reports"}, "lvl": "easy"},
        {"q": "Which object is designed to format and present database information for printing?", "a": "d", "opts": {"a": "Forms", "b": "Tables", "c": "Queries", "d": "Reports"}, "lvl": "easy"},
        {"q": "What do we call a vertical column in a Microsoft Access table?", "a": "b", "opts": {"a": "Row", "b": "Field", "c": "Record", "d": "Cell"}, "lvl": "easy"},
        {"q": "What do we call a horizontal row in a Microsoft Access table?", "a": "c", "opts": {"a": "Column", "b": "Field", "c": "Record", "d": "Data type"}, "lvl": "easy"},
        {"q": "Which Access data type is used for text up to 255 characters?", "a": "a", "opts": {"a": "Text", "b": "Memo", "c": "Byte", "d": "AutoNumber"}, "lvl": "easy"},
        {"q": "Which data type is best for large amounts of text up to 65,536 characters?", "a": "b", "opts": {"a": "Text", "b": "Memo", "c": "Long", "d": "Hyperlink"}, "lvl": "easy"},
        {"q": "Which data type automatically assigns a unique sequential number to each new record?", "a": "d", "opts": {"a": "Integer", "b": "Single", "c": "Double", "d": "AutoNumber"}, "lvl": "easy"},
        {"q": "What field uniquely identifies each record in a table?", "a": "c", "opts": {"a": "Foreign Key", "b": "Secondary Key", "c": "Primary Key", "d": "Index Key"}, "lvl": "easy"},
        {"q": "Which data type is used for monetary values and handles specific decimal math?", "a": "a", "opts": {"a": "Currency", "b": "Single", "c": "Double", "d": "Integer"}, "lvl": "easy"},
        {"q": "Which of the following data types would you use to store a boolean state like True/False?", "a": "b", "opts": {"a": "Integer", "b": "Yes/No", "c": "Memo", "d": "Ole Object"}, "lvl": "easy"},
        {"q": "What does a primary key prevent in a database table?", "a": "c", "opts": {"a": "High-speed processing", "b": "File backups", "c": "Duplicate records and null values", "d": "Data sharing"}, "lvl": "easy"},
        {"q": "Which data type stores files like pictures, audio, or video up to 1GB?", "a": "d", "opts": {"a": "Memo", "b": "Text", "c": "Lookup Wizard", "d": "Ole Object"}, "lvl": "easy"},
        {"q": "What data type would you choose for email links or website URLs?", "a": "a", "opts": {"a": "Hyperlink", "b": "Text", "c": "Memo", "d": "Lookup Wizard"}, "lvl": "easy"},
        {"q": "Which wizard allows you to select a value from another table or a drop-down list?", "a": "c", "opts": {"a": "Query Wizard", "b": "Form Wizard", "c": "Lookup Wizard", "d": "Report Wizard"}, "lvl": "easy"},
        {"q": "In Access, what does database security require before a user can access tables?", "a": "b", "opts": {"a": "An ERD printout", "b": "User logins and authentication", "c": "A backup file", "d": "A primary key update"}, "lvl": "easy"},
        {"q": "Which datatype handles whole numbers between -32,768 and 32,767?", "a": "c", "opts": {"a": "Byte", "b": "Long", "c": "Integer", "d": "Single"}, "lvl": "easy"},
        {"q": "What data type handles single precision floating-point numbers?", "a": "a", "opts": {"a": "Single", "b": "Double", "c": "Long", "d": "Byte"}, "lvl": "easy"},
        
        # Medium
        {"q": "Which of the following is a key advantage of having a database?", "a": "a", "opts": {"a": "Ensures data integrity, security, and minimizes data redundancy", "b": "High software purchase cost", "c": "Requires continuous staff training", "d": "Difficulty in converting data files"}, "lvl": "medium"},
        {"q": "What is 'data integrity' in a database?", "a": "c", "opts": {"a": "A method to encrypt passwords", "b": "A backup method", "c": "Ensures that changes made in one file reflect in other files and data remains consistent", "d": "A way to print report cards"}, "lvl": "medium"},
        {"q": "Which of the following is a disadvantage of a database system?", "a": "d", "opts": {"a": "Easy to search data", "b": "Supports data sharing", "c": "Reduces data redundancy", "d": "High cost of hardware, software, and staff training"}, "lvl": "medium"},
        {"q": "Why is a 'Phone Number' considered a poor choice for a Primary Key?", "a": "b", "opts": {"a": "It contains letters", "b": "It is likely to change for a person over time", "c": "It is not a number", "d": "It cannot be indexed"}, "lvl": "medium"},
        {"q": "Why is a 'Personal Name' considered a poor primary key?", "a": "a", "opts": {"a": "It is not guaranteed to be unique (different people can have the same name)", "b": "It is too short", "c": "Names change every month", "d": "Names cannot be searched"}, "lvl": "medium"},
        {"q": "What is a main function of a 'Form' in Microsoft Access?", "a": "d", "opts": {"a": "To define the primary key constraints", "b": "To print physical bills", "c": "To write SQL commands", "d": "To provide an easy way to guide people toward entering data correctly"}, "lvl": "medium"},
        {"q": "What does a 'Query' allow you to do?", "a": "c", "opts": {"a": "Design the system architecture", "b": "Print formatted charts", "c": "Retrieve specific data matching conditions from one or more tables", "d": "Delete table files permanently"}, "lvl": "medium"},
        {"q": "What is the maximum character limit for the 'Text' data type in Access 2016?", "a": "b", "opts": {"a": "100 characters", "b": "255 characters", "c": "1024 characters", "d": "Unlimited"}, "lvl": "medium"},
        {"q": "What is the storage size of a 'Double' data type in Access?", "a": "d", "opts": {"a": "1 byte", "b": "2 bytes", "c": "4 bytes", "d": "8 bytes"}, "lvl": "medium"},
        {"q": "Which numeric data type stores whole numbers from 0 to 255 with a size of 1 byte?", "a": "a", "opts": {"a": "Byte", "b": "Integer", "c": "Long", "d": "Single"}, "lvl": "medium"},
        {"q": "Which numeric data type is used for larger integers up to 2,147,483,647 with a size of 4 bytes?", "a": "c", "opts": {"a": "Byte", "b": "Integer", "c": "Long", "d": "Double"}, "lvl": "medium"},
        {"q": "Which data type is recommended if you have very large fields of notes or descriptions?", "a": "b", "opts": {"a": "Text", "b": "Memo", "c": "Ole Object", "d": "Lookup Wizard"}, "lvl": "medium"},
        {"q": "What happens if a database is not integrated and has data redundancy?", "a": "a", "opts": {"a": "Multiple copies of the same data exist, leading to inconsistency when updated", "b": "Data security is automatically high", "c": "Query performance increases", "d": "It requires less storage"}, "lvl": "medium"},
        {"q": "What are the four main database objects in MS Access?", "a": "c", "opts": {"a": "Files, Folders, Paths, Keys", "b": "Indexes, Records, Sheets, Cells", "c": "Tables, Forms, Queries, Reports", "d": "Inputs, Outputs, Processes, Controls"}, "lvl": "medium"},
        {"q": "What view in Access is used to modify the structure of a table, such as adding fields and choosing data types?", "a": "b", "opts": {"a": "Datasheet View", "b": "Design View", "c": "Layout View", "d": "Form View"}, "lvl": "medium"},
        {"q": "What view is used to enter records directly into a grid table layout?", "a": "a", "opts": {"a": "Datasheet View", "b": "Design View", "c": "Layout View", "d": "Report View"}, "lvl": "medium"},
        {"q": "Which of the following is a characteristic of a good Primary Key?", "a": "d", "opts": {"a": "It changes frequently", "b": "It is sometimes null or empty", "c": "It is a phone number or email", "d": "It uniquely identifies each row and never changes"}, "lvl": "medium"},
        {"q": "What type of relationship is established when tables are linked using a Primary Key and a Foreign Key?", "a": "b", "opts": {"a": "Many-to-Many", "b": "One-to-Many", "c": "One-to-One", "d": "Recursive"}, "lvl": "medium"},
        {"q": "What is the function of the 'Compact & Repair' utility in MS Access?", "a": "a", "opts": {"a": "It helps prevent and correct database file problems and reduces file size", "b": "It prints reports directly", "c": "It automatically generates primary keys", "d": "It encrypts the passwords"}, "lvl": "medium"},
        {"q": "Which layout object acts as a bridge to format database records suitable for a paper printout?", "a": "c", "opts": {"a": "Forms", "b": "Queries", "c": "Reports", "d": "Tables"}, "lvl": "medium"},
        
        # Hard
        {"q": "What occurs during database 'data conversion cost'?", "a": "b", "opts": {"a": "Converting code from C++ to Python", "b": "Converting raw files or legacy formats into a database system, which can be difficult and costly", "c": "Converting user passwords to hashes", "d": "Printing reports on paper"}, "lvl": "hard"},
        {"q": "Which statement describes 'referential integrity' in database relationships?", "a": "c", "opts": {"a": "User logins must match the primary key", "b": "All columns must have the same data type", "c": "Ensures that a foreign key value always points to an existing primary key value in the parent table", "d": "Compact and repair is run daily"}, "lvl": "hard"},
        {"q": "How does Microsoft Access handle multi-table queries?", "a": "d", "opts": {"a": "By copying tables to spreadsheets", "b": "By creating multiple forms", "c": "By deleting redundant primary keys", "d": "By joining tables using matching fields (relationships) to retrieve composite records"}, "lvl": "hard"},
        {"q": "What is the consequence of selecting 'Zip Code' as a primary key for a Customer table?", "a": "a", "opts": {"a": "It violates uniqueness since multiple customers can live in the same zip code area", "b": "It takes too much storage space (8 bytes)", "c": "Access will crash automatically", "d": "You cannot perform any queries"}, "lvl": "hard"},
        {"q": "What is the difference between a Table and a Form in terms of data entry security?", "a": "b", "opts": {"a": "Tables prevent errors, Forms do not", "b": "Forms can restrict user inputs to specific fields and hide sensitive data, while Tables expose raw data directly", "c": "Tables can be printed, Forms cannot", "d": "Forms require a compiler, Tables do not"}, "lvl": "hard"},
        {"q": "What are constraints in database design?", "a": "c", "opts": {"a": "Hardware memory limitations", "b": "Operating system parameters", "c": "Rules applied to data fields (like NOT NULL, primary keys, checks) to ensure data accuracy", "d": "The cost of database training"}, "lvl": "hard"},
        {"q": "In Access 2016, how is a relationship created between two tables?", "a": "a", "opts": {"a": "By dragging a primary key field from one table and dropping it as a foreign key in another table in the Relationships window", "b": "By creating a query and a report together", "c": "By setting their names to be the same", "d": "By using the print preview tool"}, "lvl": "hard"},
        {"q": "If you modify a query's design to filter records, where is the underlying data modified?", "a": "b", "opts": {"a": "Only in the query view itself", "b": "In the original database Tables where the data is stored", "c": "In the printed Report", "d": "In the system software memory"}, "lvl": "hard"},
        {"q": "Why does Microsoft Access warn you about 'Enable Content' when opening a database from the internet?", "a": "c", "opts": {"a": "Because the files are too large", "b": "Because the database lacks a primary key", "c": "To protect against potential security risks or malicious macros hidden in database files", "d": "To force a compact and repair cycle"}, "lvl": "hard"},
        {"q": "What does a 'Logical design relationship' represent in MS Access?", "a": "b", "opts": {"a": "The physical server connection", "b": "The abstract link between tables showing how data flows and coordinates", "c": "The code structure of system software", "d": "The menu items on the Ribbon interface"}, "lvl": "hard"},
        {"q": "Which data type is most appropriate for storing high-precision coordinate data that needs decimals?", "a": "d", "opts": {"a": "Integer", "b": "Single", "c": "Currency", "d": "Double"}, "lvl": "hard"},
        {"q": "What is the main limitation of using a spreadsheet like Excel instead of a DBMS like Access for managing student lists?", "a": "a", "opts": {"a": "Spreadsheets lack robust mechanisms for concurrent updates, relationships, data integrity constraints, and security levels", "b": "Spreadsheets cannot display grids", "c": "Spreadsheets have higher license costs", "d": "Spreadsheets do not support text data types"}, "lvl": "hard"},
        {"q": "Why is 'Byte' data type preferred over 'Integer' for storing student Form levels (e.g. 1 to 4)?", "a": "c", "opts": {"a": "Byte data type supports negative numbers", "b": "Byte data type uses 4 bytes of storage", "c": "Byte data type only uses 1 byte, which is efficient since Form levels are within 0-255", "d": "Byte data type has a lookup wizard built-in"}, "lvl": "hard"},
        {"q": "What occurs when you set a relationship constraint to 'Cascade Delete Related Records'?", "a": "b", "opts": {"a": "It deletes the database file", "b": "Deleting a record in the primary table automatically deletes all matching records in the related table", "c": "It compacts the database", "d": "It changes all foreign keys to null"}, "lvl": "hard"},
        {"q": "Which database component compiles formatted summaries of data suitable for decision makers?", "a": "d", "opts": {"a": "Tables", "b": "Forms", "c": "Queries", "d": "Reports"}, "lvl": "hard"},
        {"q": "In the relationship window, the symbol '1' on one table and '∞' on the other represents:", "a": "a", "opts": {"a": "A One-to-Many relationship", "b": "A Many-to-Many relationship", "c": "An infinite loop in a database", "d": "A primary key collision"}, "lvl": "hard"},
        {"q": "Why cannot a Primary Key field accept a NULL value?", "a": "c", "opts": {"a": "Because text data type doesn't support NULL", "b": "Because it would cause a compact and repair error", "c": "Because a NULL value cannot identify a unique record, violating entity integrity", "d": "Because SQL commands forbid it"}, "lvl": "hard"},
        {"q": "How does the 'Datasheet View' query interface help system construction?", "a": "b", "opts": {"a": "By compile-testing the code editor", "b": "By letting the analyst verify that the query criteria returned the correct database records visually", "c": "By running automated unit tests", "d": "By setting user access policies"}, "lvl": "hard"},
        {"q": "Which object represents the physical interface for data entry into the system?", "a": "c", "opts": {"a": "Queries", "b": "Reports", "c": "Forms", "d": "SQL Scripts"}, "lvl": "hard"},
        {"q": "If a user group is assigned the 'Data entry clerk' role, what access level do they typically have in controls design?", "a": "a", "opts": {"a": "Input data only (no configuration, no deletion of critical logs)", "b": "Configure, upgrade, and install system", "c": "Full admin access", "d": "Guest view only"}, "lvl": "hard"}
    ]

    # Questions database pool for Unit 3: Programming using Python
    unit3_base = [
        # Easy
        {"q": "What is computer programming?", "a": "b", "opts": {"a": "Buying hardware components", "b": "Providing a step-by-step set of instructions telling a computer exactly what to do", "c": "Designing user interfaces in Access", "d": "Backing up files to an external drive"}, "lvl": "easy"},
        {"q": "Which of the following is a high-level programming language?", "a": "c", "opts": {"a": "Machine code", "b": "Binary numbers", "c": "Python", "d": "Assembler"}, "lvl": "easy"},
        {"q": "What translates a high-level language program into machine code line-by-line during execution?", "a": "a", "opts": {"a": "Interpreter", "b": "Compiler", "c": "Debugger", "d": "Text Editor"}, "lvl": "easy"},
        {"q": "What translates the entire high-level program into machine code before execution?", "a": "b", "opts": {"a": "Interpreter", "b": "Compiler", "c": "Debugger", "d": "Code Editor"}, "lvl": "easy"},
        {"q": "What does IDE stand for in programming?", "a": "c", "opts": {"a": "Internal Data Encryption", "b": "Input Device Emulator", "c": "Integrated Development Environment", "d": "Interactive Debugging Editor"}, "lvl": "easy"},
        {"q": "Which symbol is used for writing comments in Python?", "a": "d", "opts": {"a": "//", "b": "/*", "c": "<!--", "d": "#"}, "lvl": "easy"},
        {"q": "Which Python function is used to read input from the keyboard?", "a": "a", "opts": {"a": "input()", "b": "print()", "c": "read()", "d": "scan()"}, "lvl": "easy"},
        {"q": "What Python function converts an input string into a whole number (integer)?", "a": "b", "opts": {"a": "float()", "b": "int()", "c": "str()", "d": "double()"}, "lvl": "easy"},
        {"q": "What Python operator is used for addition?", "a": "c", "opts": {"a": "-", "b": "*", "c": "+", "d": "/"}, "lvl": "easy"},
        {"q": "What Python operator is used for multiplication?", "a": "d", "opts": {"a": "/", "b": "+", "c": "%", "d": "*"}, "lvl": "easy"},
        {"q": "What Python operator is used for calculating a remainder?", "a": "a", "opts": {"a": "%", "b": "/", "c": "//", "d": "**"}, "lvl": "easy"},
        {"q": "What Python operator is used for raising a number to a power (exponent)?", "a": "b", "opts": {"a": "//", "b": "**", "c": "^", "d": "%"}, "lvl": "easy"},
        {"q": "Which variable name is invalid in Python?", "a": "c", "opts": {"a": "student_name", "b": "_age", "c": "2nd_student", "d": "score2"}, "lvl": "easy"},
        {"q": "What represents a logic error where the code runs successfully but does not produce the expected result?", "a": "d", "opts": {"a": "Syntax error", "b": "Runtime error", "c": "Exception", "d": "Semantic error"}, "lvl": "easy"},
        {"q": "What loop structure in Python repeats a specific number of times?", "a": "a", "opts": {"a": "for loop", "b": "while loop", "c": "infinite loop", "d": "if statement"}, "lvl": "easy"},
        {"q": "What loop structure in Python repeats as long as a condition remains true?", "a": "b", "opts": {"a": "for loop", "b": "while loop", "c": "range loop", "d": "if statement"}, "lvl": "easy"},
        {"q": "Which keyword is a reserved keyword in Python?", "a": "c", "opts": {"a": "var", "b": "integer", "c": "import", "d": "string"}, "lvl": "easy"},
        {"q": "What is the process of tracking down and correcting errors in a program?", "a": "d", "opts": {"a": "Compiling", "b": "Interpreting", "c": "Stepping", "d": "Debugging"}, "lvl": "easy"},
        {"q": "Which Python function displays output on the screen?", "a": "a", "opts": {"a": "print()", "b": "input()", "c": "write()", "d": "output()"}, "lvl": "easy"},
        {"q": "What operator is used to concatenate two strings in Python?", "a": "b", "opts": {"a": "*", "b": "+", "c": "&", "d": "concat"}, "lvl": "easy"},
        
        # Medium
        {"q": "Which variable name follows the naming rules of Python?", "a": "a", "opts": {"a": "_totalCoins", "b": "total-coins", "c": "total coins", "d": "class"}, "lvl": "medium"},
        {"q": "What occurs when the interpreter encounters code that does not follow the grammar rules of Python?", "a": "c", "opts": {"a": "Runtime error", "b": "Semantic error", "c": "Syntax error", "d": "Logic error"}, "lvl": "medium"},
        {"q": "What is a 'runtime error' in Python?", "a": "b", "opts": {"a": "A syntax rule violation", "b": "An error that occurs during execution, such as division by zero", "c": "A logic error in calculations", "d": "A compiler warnings"}, "lvl": "medium"},
        {"q": "What does the code `print('hello' * 3)` output in Python?", "a": "d", "opts": {"a": "hello3", "b": "hello hello hello", "c": "Syntax Error", "d": "hellohellohello"}, "lvl": "medium"},
        {"q": "What operator is used for 'integer division' in Python, which discards the fractional part?", "a": "a", "opts": {"a": "//", "b": "/", "c": "%", "d": "**"}, "lvl": "medium"},
        {"q": "What does the `range(1, 5)` function generate in a `for` loop?", "a": "b", "opts": {"a": "1, 2, 3, 4, 5", "b": "1, 2, 3, 4", "c": "0, 1, 2, 3, 4", "d": "1, 5"}, "lvl": "medium"},
        {"q": "What is the result of the expression `18 // 5` in Python?", "a": "c", "opts": {"a": "3.6", "b": "3 remainder 3", "c": "3", "d": "4"}, "lvl": "medium"},
        {"q": "What is the result of the expression `18 % 5` in Python?", "a": "d", "opts": {"a": "3.6", "b": "3", "c": "0", "d": "3"}, "lvl": "medium"},
        {"q": "Which function converts a string to a decimal/floating-point number?", "a": "a", "opts": {"a": "float()", "b": "int()", "c": "double()", "d": "decimal()"}, "lvl": "medium"},
        {"q": "What relational operator is used to check if two values are equal in Python?", "a": "c", "opts": {"a": "=", "b": "===", "c": "==", "d": "!="}, "lvl": "medium"},
        {"q": "What relational operator checks for 'not equal' in Python?", "a": "b", "opts": {"a": "<>", "b": "!=", "c": "not", "d": "=="}, "lvl": "medium"},
        {"q": "How does an IDE debugger support the programmer?", "a": "d", "opts": {"a": "By writing variables automatically", "b": "By changing low-level binary", "c": "By hosting the application online", "d": "By providing features like breakpoints and stepping through code line-by-line"}, "lvl": "medium"},
        {"q": "Which structure allows a program to have multiple alternative paths of execution based on conditions?", "a": "c", "opts": {"a": "Loops", "b": "Variables", "c": "if-elif-else statements", "d": "Functions"}, "lvl": "medium"},
        {"q": "What will `range(1, 10, 2)` generate in Python?", "a": "a", "opts": {"a": "1, 3, 5, 7, 9", "b": "1, 2, 3, 4, 5, 6, 7, 8, 9, 10", "c": "2, 4, 6, 8, 10", "d": "1, 10"}, "lvl": "medium"},
        {"q": "What does a count-controlled loop require?", "a": "b", "opts": {"a": "A user keyboard prompt", "b": "A variable that references a list or range of values to determine iteration count", "c": "An infinite loop warning", "d": "An import statement"}, "lvl": "medium"},
        {"q": "What does a condition-controlled loop require?", "a": "c", "opts": {"a": "A compiler build", "b": "A predefined list", "c": "A boolean condition that controls when the loop terminates", "d": "An integer variable only"}, "lvl": "medium"},
        {"q": "What represents the 'assignment operator' in Python?", "a": "d", "opts": {"a": "==", "b": "->", "c": "set", "d": "="}, "lvl": "medium"},
        {"q": "Which data type represents floating-point numbers (decimals) in Python?", "a": "a", "opts": {"a": "Float", "b": "Integer", "c": "String", "d": "Boolean"}, "lvl": "medium"},
        {"q": "What is the output of the code `print(2 ** 3)` in Python?", "a": "b", "opts": {"a": "6", "b": "8", "c": "9", "d": "5"}, "lvl": "medium"},
        {"q": "What Python function returns the length of a string?", "a": "c", "opts": {"a": "size()", "b": "length()", "c": "len()", "d": "count()"}, "lvl": "medium"},
        
        # Hard
        {"q": "Why is interpreted code considered easier to debug than compiled code?", "a": "a", "opts": {"a": "It stops and reports errors immediately when it hits a line with a problem", "b": "It compiles to machine code first", "c": "It runs much faster", "d": "It does not require a text editor"}, "lvl": "hard"},
        {"q": "What is the key difference between compiling and interpreting programs?", "a": "b", "opts": {"a": "Compiling translates line-by-line, interpreting translates all at once", "b": "Compiling does a one-time translation to a standalone file, while interpreting translates code every time the program runs", "c": "Interpreting requires high-speed processors, compiling does not", "d": "Compiled programs cannot be run on Windows"}, "lvl": "hard"},
        {"q": "Why is 'class' an invalid variable name in Python?", "a": "c", "opts": {"a": "It starts with a capital letter", "b": "It contains special characters", "c": "It is a reserved keyword in Python programming", "d": "It is too short"}, "lvl": "hard"},
        {"q": "What occurs if you write a `while` loop but forget to include code that modifies the loop control variable?", "a": "d", "opts": {"a": "A syntax error will be displayed", "b": "The compiler will halt", "c": "The program will crash with an exception", "d": "An infinite loop will occur, repeating the block indefinitely"}, "lvl": "hard"},
        {"q": "What is the result of the calculation `5 * 2 - 3 + 4 / 2` in Python?", "a": "a", "opts": {"a": "9.0", "b": "5.5", "c": "8.0", "d": "11.0"}, "lvl": "hard"},
        {"q": "Which of the following describes a 'semantic error' in programming?", "a": "c", "opts": {"a": "A typo in a keyword causing a compile failure", "b": "An error like division by zero during execution", "c": "A logic error where the code is syntactically correct but does not do what you expect", "d": "An unused variable warning"}, "lvl": "hard"},
        {"q": "In Python, if the input is `15`, what will `type(input('Enter: '))` return?", "a": "d", "opts": {"a": "<class 'int'>", "b": "<class 'float'>", "c": "<class 'number'>", "d": "<class 'str'>"}, "lvl": "hard"},
        {"q": "Which code snippet correctly requests an integer input from the user?", "a": "b", "opts": {"a": "age = input(int('Enter age: '))", "b": "age = int(input('Enter age: '))", "c": "age = float(input('Enter age: '))", "d": "age = int('Enter age: ')"}, "lvl": "hard"},
        {"q": "What is the order of precedence (PEMDAS) for operators in Python?", "a": "a", "opts": {"a": "Parentheses, Exponents, Multiplication/Division, Addition/Subtraction", "b": "Addition, Subtraction, Multiplication, Division", "c": "Exponent, Remainder, Division, Parentheses", "d": "Random ordering based on lines"}, "lvl": "hard"},
        {"q": "What is a 'breakpoint' in debugging?", "a": "c", "opts": {"a": "A point where the program crashes", "b": "A line of code that cannot compile", "c": "A specified point in the code where execution is paused so the programmer can inspect variables", "d": "A hardware limit switch"}, "lvl": "hard"},
        {"q": "What is the result of the string expression `print('bye' + 'now' * 2)` in Python?", "a": "b", "opts": {"a": "byenowbyenow", "b": "byenownow", "c": "byebyenownow", "d": "Syntax Error"}, "lvl": "hard"},
        {"q": "How do you define a block of statements that belong together in Python control structures?", "a": "d", "opts": {"a": "By enclosing them in curly braces {}", "b": "By using the 'end' keyword", "c": "By placing them on the same line", "d": "By using consistent indentation (whitespace)"}, "lvl": "hard"},
        {"q": "Which expression checks if 'sales' is greater than 500 and 'bonus' is equal to 50?", "a": "a", "opts": {"a": "sales > 500 and bonus == 50", "b": "sales > 500 or bonus = 50", "c": "sales > 500 & bonus = 50", "d": "if sales > 500 and bonus = 50"}, "lvl": "hard"},
        {"q": "What will `range(5)` generate in Python?", "a": "b", "opts": {"a": "1, 2, 3, 4, 5", "b": "0, 1, 2, 3, 4", "c": "1, 2, 3, 4", "d": "0, 5"}, "lvl": "hard"},
        {"q": "In Python, how is case sensitivity applied to variables?", "a": "c", "opts": {"a": "Variables are not case sensitive", "b": "Only the first letter matters", "c": "Variables are case sensitive; 'age' and 'Age' are different variables", "d": "Case sensitivity only applies to string values"}, "lvl": "hard"},
        {"q": "If the variables are `width = 20` and `length = 25`, what is the output of `print(width > 10 and length < 20)`?", "a": "a", "opts": {"a": "False", "b": "True", "c": "None", "d": "Syntax Error"}, "lvl": "hard"},
        {"q": "What will `print(10 != 5)` display in Python?", "a": "b", "opts": {"a": "False", "b": "True", "c": "1", "d": "Syntax Error"}, "lvl": "hard"},
        {"q": "What does a compiler create after analyzing and translating the source code successfully?", "a": "c", "opts": {"a": "A logic database link", "b": "An ERD schema file", "c": "An executable or binary file (machine code) that can run independently", "d": "A debug log folder"}, "lvl": "hard"},
        {"q": "What will the output of the following code be? `num = 1; while num < 3: print(num); num = num + 1`?", "a": "d", "opts": {"a": "1, 2, 3", "b": "1", "c": "0, 1, 2", "d": "1, 2"}, "lvl": "hard"},
        {"q": "What function is used to create a sequence of numbers that can be iterated over in a loop?", "a": "a", "opts": {"a": "range()", "b": "list()", "c": "sequence()", "d": "loop()"}, "lvl": "hard"}
    ]

    # Questions database pool for Unit 4: ICT Security and Ethics
    unit4_base = [
        # Easy
        {"q": "What is a digital security risk?", "a": "c", "opts": {"a": "A high cost of hardware", "b": "An unused variable in code", "c": "Any event or action that could cause loss of or damage to a computer system", "d": "A logic error in database tables"}, "lvl": "easy"},
        {"q": "What is an illegal act involving the use of a computer or devices connected to it?", "a": "a", "opts": {"a": "Cybercrime", "b": "Logical Design", "c": "Syntax Error", "d": "Parallel Deployment"}, "lvl": "easy"},
        {"q": "What is the term for software used by cybercriminals?", "a": "b", "opts": {"a": "Adware", "b": "Crimeware", "c": "Freeware", "d": "Shareware"}, "lvl": "easy"},
        {"q": "Who is someone who illegally accesses a computer or network with the intent of destroying data or stealing info?", "a": "c", "opts": {"a": "Hacker", "b": "Developer", "c": "Cracker", "d": "Analyst"}, "lvl": "easy"},
        {"q": "What is a computer program that replicates itself over network or memory to use up resources?", "a": "a", "opts": {"a": "Worm", "b": "Trojan horse", "c": "Adware", "d": "Logical virus"}, "lvl": "easy"},
        {"q": "What type of malware is hidden inside or looks like a legitimate program but does not replicate itself?", "a": "b", "opts": {"a": "Worm", "b": "Trojan horse", "c": "Spyware", "d": "Adware"}, "lvl": "easy"},
        {"q": "What type of malware collects user information silently and sends it to external sources?", "a": "c", "opts": {"a": "Worm", "b": "Trojan horse", "c": "Spyware", "d": "Adware"}, "lvl": "easy"},
        {"q": "What type of malware displays online banner or pop-up advertisements?", "a": "d", "opts": {"a": "Worm", "b": "Trojan horse", "c": "Spyware", "d": "Adware"}, "lvl": "easy"},
        {"q": "What is a network of compromised computers under the control of a hacker?", "a": "a", "opts": {"a": "Botnet", "b": "Firewall", "c": "Server network", "d": "Backup set"}, "lvl": "easy"},
        {"q": "What do we call a compromised computer in a botnet?", "a": "b", "opts": {"a": "Server", "b": "Zombie", "c": "Backup", "d": "Analyst"}, "lvl": "easy"},
        {"q": "What attack aims to disrupt or block user access to a web or email service?", "a": "c", "opts": {"a": "Backdoor", "b": "Spoofing", "c": "Denial of Service (DoS)", "d": "Malware"}, "lvl": "easy"},
        {"q": "What is a set of instructions that allows users to bypass security checks to access a system?", "a": "d", "opts": {"a": "Spoofing", "b": "Firewall", "c": "Botnet", "d": "Backdoor"}, "lvl": "easy"},
        {"q": "What represents a technique where an attacker makes their network transmission appear legitimate?", "a": "a", "opts": {"a": "Spoofing", "b": "Backdoor", "c": "Antivirus", "d": "Encryption"}, "lvl": "easy"},
        {"q": "What hardware or software protects network resources from external intrusions?", "a": "b", "opts": {"a": "Antivirus", "b": "Firewall", "c": "Backup drive", "d": "Logical ERD"}, "lvl": "easy"},
        {"q": "What is the process of converting human-readable data into encoded characters?", "a": "c", "opts": {"a": "Backing up", "b": "Stepping", "c": "Encryption", "d": "Debugging"}, "lvl": "easy"},
        {"q": "What is the moral standards governing the use of computers called?", "a": "d", "opts": {"a": "System design", "b": "Intellectual property", "c": "Licensing", "d": "Computer Ethics"}, "lvl": "easy"},
        {"q": "What is the act of copying and publishing the work of another person without citation?", "a": "a", "opts": {"a": "Plagiarism", "b": "Copyright", "c": "Encryption", "d": "Shareware"}, "lvl": "easy"},
        {"q": "What software category allows users to run, copy, share, and change code without permission?", "a": "b", "opts": {"a": "Shareware", "b": "Free software", "c": "Freeware", "d": "Adware"}, "lvl": "easy"},
        {"q": "What software is free to use but the owner retains the copyright and restricts code modifications?", "a": "c", "opts": {"a": "Free software", "b": "Shareware", "c": "Freeware", "d": "Malware"}, "lvl": "easy"},
        {"q": "What software is distributed for a free trial period, after which a fee must be paid?", "a": "d", "opts": {"a": "Free software", "b": "Freeware", "c": "Adware", "d": "Shareware"}, "lvl": "easy"},
        
        # Medium
        {"q": "What is the primary difference between a 'hacker' and a 'cracker'?", "a": "a", "opts": {"a": "Hackers may access systems to improve protection, while crackers do so with malicious intent to destroy or steal", "b": "Crackers write code, hackers do not", "c": "Hackers use Python, crackers use Java", "d": "Crackers are ethical employees, hackers are corporate spies"}, "lvl": "medium"},
        {"q": "What is a 'script kiddie'?", "a": "c", "opts": {"a": "A high-level systems analyst", "b": "An ethical hacking programmer", "c": "An amateur cybercriminal who lacks technical skills and uses pre-written tools", "d": "A database administrator"}, "lvl": "medium"},
        {"q": "How does a worm spread compared to a Trojan horse?", "a": "b", "opts": {"a": "Worms require a user form, Trojan horses do not", "b": "Worms replicate themselves automatically across networks, while Trojan horses look like useful apps and do not self-replicate", "c": "Trojan horses use fiber-optic cables, worms do not", "d": "Worms cannot be deleted by antivirus software"}, "lvl": "medium"},
        {"q": "Which of the following is a method to safeguard against network attacks?", "a": "d", "opts": {"a": "Disabling firewalls", "b": "Avoiding database backups", "c": "Using simple passwords like '1234'", "d": "Using antivirus, firewalls, and scanning removable media"}, "lvl": "medium"},
        {"q": "What type of backup copies only the files that have changed since the last full backup?", "a": "a", "opts": {"a": "Differential backup", "b": "Full backup", "c": "Selective backup", "d": "System backup"}, "lvl": "medium"},
        {"q": "What type of backup copies all files in the computer, providing the fastest recovery?", "a": "b", "opts": {"a": "Incremental backup", "b": "Full backup", "c": "Selective backup", "d": "Differential backup"}, "lvl": "medium"},
        {"q": "What type of backup copies files that have changed since the last full or incremental backup?", "a": "c", "opts": {"a": "Full backup", "b": "Differential backup", "c": "Incremental backup", "d": "Selective backup"}, "lvl": "medium"},
        {"q": "What type of backup allows users to choose specific folders and files to include in a backup?", "a": "d", "opts": {"a": "Full backup", "b": "Differential backup", "c": "Incremental backup", "d": "Selective backup"}, "lvl": "medium"},
        {"q": "What does a firewall do to protect a network?", "a": "a", "opts": {"a": "Secures resources against outside intrusions and restricts unauthorized access to sensitive data", "b": "Scans emails for plagiarism", "c": "Deletes duplicate databases", "d": "Translates code to binary"}, "lvl": "medium"},
        {"q": "What is 'Public Key Encryption'?", "a": "b", "opts": {"a": "A simple word cipher", "b": "Using a sender's public key to encrypt and a receiver's private key to decrypt messages", "c": "Storing passwords in plain text", "d": "A database compact tool"}, "lvl": "medium"},
        {"q": "Which password practice is recommended for strong security?", "a": "c", "opts": {"a": "Using your birthdate", "b": "Using your username", "c": "A length of at least 8 characters containing letters, digits, and special characters", "d": "Using the school name"}, "lvl": "medium"},
        {"q": "What does 'intellectual property' relate to?", "a": "d", "opts": {"a": "Physical office buildings", "b": "The cost of database training", "c": "Public domain software libraries", "d": "Unique and original tasks including ideas, innovations, writing, process names, and logos"}, "lvl": "medium"},
        {"q": "What is a 'Copyright'?", "a": "a", "opts": {"a": "An exclusive legal right to produce copies of a work for a specific period", "b": "A backup constraint", "c": "A method of password hashing", "d": "The right to use code without licensing"}, "lvl": "medium"},
        {"q": "What is the main limitation of Shareware?", "a": "b", "opts": {"a": "It has virus scripts", "b": "It is only free for a trial period, after which a fixed fee must be paid", "c": "It cannot run on Windows", "d": "It lacks user interfaces"}, "lvl": "medium"},
        {"q": "What is a corporate spy in cybercrime?", "a": "c", "opts": {"a": "A developer working on open source", "b": "An admin doing data backup", "c": "An individual hired to hack into a competitor's system to steal confidential data", "d": "A script kiddie"}, "lvl": "medium"},
        {"q": "What is an unethical employee in cybercrime?", "a": "d", "opts": {"a": "A programmer who leaves syntax errors", "b": "An analyst who uses Agile", "c": "A user with guest access", "d": "An employee who exploits system weaknesses for financial gain or revenge"}, "lvl": "medium"},
        {"q": "What is the primary risk of a DoS attack on business servers?", "a": "a", "opts": {"a": "Temporary or permanent loss of service to customers, halting business operations", "b": "It corrupts the physical database backup", "c": "It steals user passwords", "d": "It changes variables in the script window"}, "lvl": "medium"},
        {"q": "What occurs when an attacker executes 'IP spoofing'?", "a": "b", "opts": {"a": "They copy the source code of a webpage", "b": "They modify the IP packet header to make their transmission appear to come from a trusted IP address", "c": "They change the password policy", "d": "They delete the network firewall log"}, "lvl": "medium"},
        {"q": "What is the main benefit of performing an 'Incremental backup' over a 'Full backup'?", "a": "c", "opts": {"a": "It provides faster recovery time", "b": "It doesn't require storage space", "c": "It takes less time and storage space since it only copies modified files", "d": "It automatically repairs tables"}, "lvl": "medium"},
        {"q": "What is the disadvantage of performing a 'Differential backup' for recovery?", "a": "d", "opts": {"a": "It requires selective folder choosing", "b": "It requires checking the firewall log", "c": "It cannot run on Windows", "d": "Recovery is slower because both the last full backup and the differential backup are needed"}, "lvl": "medium"},
        
        # Hard
        {"q": "Which describes the difference between a Virus and a Worm?", "a": "a", "opts": {"a": "A virus needs to attach to a host program to spread, whereas a worm is a standalone program that self-replicates across networks", "b": "Worms do not use memory, viruses do", "c": "Viruses are crimeware, worms are freeware", "d": "Worms only affect databases, viruses affect code editors"}, "lvl": "hard"},
        {"q": "What is a zombie computer in cybercrime?", "a": "b", "opts": {"a": "A computer with no operating system", "b": "A compromised computer in a botnet whose owner is unaware that it is controlled remotely by an attacker", "c": "A database server undergoing repair", "d": "A computer with a syntax error"}, "lvl": "hard"},
        {"q": "What does encryption do to secure text over the internet?", "a": "c", "opts": {"a": "It prints formatting tables", "b": "It runs the python compiler", "c": "It converts plaintext into ciphertext to prevent unauthorized reading during transmission", "d": "It locks the database table constraints"}, "lvl": "hard"},
        {"q": "Under password composition guidelines, a strong password should not:", "a": "d", "opts": {"a": "Be at least 8 characters long", "b": "Contain numbers and letters", "c": "Contain special characters like $ or *", "d": "Be based on personal biodata like names, birthdays, or phone numbers"}, "lvl": "hard"},
        {"q": "How does Copyright differ from Plagiarism?", "a": "a", "opts": {"a": "Copyright is a legal right protecting authorship, while plagiarism is an ethical violation of claiming someone else's work as your own", "b": "Copyright is for hardware, plagiarism is for software", "c": "Plagiarism has license fees, copyright does not", "d": "Copyright is free software, plagiarism is shareware"}, "lvl": "hard"},
        {"q": "What is the ethical implication of the 'fair use' doctrine in copyright law?", "a": "b", "opts": {"a": "It allows copying software for resale", "b": "It allows limited use of copyrighted material without permission for educational or critical purposes", "c": "It makes all software freeware", "d": "It allows bypassing access controls"}, "lvl": "hard"},
        {"q": "What is the characteristic of 'Free software' as defined by the Free Software Foundation?", "a": "c", "opts": {"a": "It must always be distributed without any cost", "b": "The owner retains full exclusive copyright and prohibits modification", "c": "It grants users the freedom to run, copy, distribute, study, change, and improve the software", "d": "It is only a 30-day trial"}, "lvl": "hard"},
        {"q": "Why is 'Selective backup' highly flexible but difficult to manage?", "a": "d", "opts": {"a": "It requires high-speed networks", "b": "It is written in python binary code", "c": "It cannot back up databases", "d": "The user must manually choose which folders and files to back up, leading to potential omissions of critical data"}, "lvl": "hard"},
        {"q": "What is 'Public Key' cryptography?", "a": "a", "opts": {"a": "An asymmetric encryption scheme using a public key for encryption and a mathematically linked private key for decryption", "b": "A password list shared with all users", "c": "A type of firewall access control", "d": "A primary key constraint in Access"}, "lvl": "hard"},
        {"q": "Which attack exploits compromised computers to swamp a website with request traffic, causing a server crash?", "a": "c", "opts": {"a": "Trojan horse", "b": "IP spoofing", "c": "Distributed Denial of Service (DDoS)", "d": "Backdoor access"}, "lvl": "hard"},
        {"q": "What is a 'firewall rule'?", "a": "b", "opts": {"a": "A python logic expression", "b": "A filter configuration telling the firewall which network traffic to allow or block based on ports or IPs", "c": "A database constraint check", "d": "A user license agreement"}, "lvl": "hard"},
        {"q": "In computer ethics, which of the following represents 'Software Theft'?", "a": "d", "opts": {"a": "Writing comments in code", "b": "Running an interpreter", "c": "Performing a data backup", "d": "Illegal copying or registering/activating of software without a valid license"}, "lvl": "hard"},
        {"q": "Which backup method requires the longest time to restore the complete system because multiple incremental backups must be applied?", "a": "c", "opts": {"a": "Full backup", "b": "Differential backup", "c": "Incremental backup", "d": "Selective backup"}, "lvl": "hard"},
        {"q": "What is the primary objective of 'Data Protection' policies?", "a": "b", "opts": {"a": "To speed up compilation of scripts", "b": "To safeguard and protect information privacy while still authorizing legal business use", "c": "To ensure database compact and repair runs", "d": "To force the use of freeware"}, "lvl": "hard"},
        {"q": "What does a 'Digital Security Risk' category like 'System Failure' encompass?", "a": "a", "opts": {"a": "Hardware/software malfunctions, power outages, or natural disasters causing database corruption", "b": "A syntax error in python code", "c": "A cracker stealing usernames", "d": "An employee resigning"}, "lvl": "hard"},
        {"q": "In symmetric vs asymmetric encryption, what is the key difference?", "a": "b", "opts": {"a": "Symmetric uses multiple compilers, asymmetric uses none", "b": "Symmetric uses the same key for encryption and decryption, while asymmetric uses separate public and private keys", "c": "Symmetric is only for Access tables, asymmetric is for Python", "d": "Symmetric is freeware, asymmetric is shareware"}, "lvl": "hard"},
        {"q": "What is the function of a 'Digital Certificate' in network security?", "a": "c", "opts": {"a": "It is a diploma in programming", "b": "It checks coding syntax errors", "c": "It verifies the identity of a website or user to establish secure encrypted connections", "d": "It backs up the data automatically"}, "lvl": "hard"},
        {"q": "Under copyright issues, what does Digital Rights Management (DRM) enforce?", "a": "d", "opts": {"a": "High-level database access controls", "b": "Fast parallel deployment", "c": "Automated unit testing checks", "d": "Technologies that control or restrict the use and distribution of digital media content"}, "lvl": "hard"},
        {"q": "Which data type in Access is best for storing a primary key representing a national ID?", "a": "b", "opts": {"a": "Yes/No", "b": "Text (configured with strict unique constraints)", "c": "Integer", "d": "Ole Object"}, "lvl": "hard"},
        {"q": "What does the 'Anonymity' privacy concern aim to accomplish?", "a": "a", "opts": {"a": "Keeping a user's identity protected and masked through various network tools or applications", "b": "Allowing free software modifications", "c": "Bypassing firewalls with backdoors", "d": "Preventing compiler optimization"}, "lvl": "hard"}
    ]

    # Generate 81 questions per unit (26 easy, 25 medium, 30 hard)
    all_questions = []
    
    # Generate for Unit 1
    u1_q = []
    u1_easy = [q for q in unit1_base if q['lvl'] == 'easy']
    u1_med = [q for q in unit1_base if q['lvl'] == 'medium']
    u1_hard = [q for q in unit1_base if q['lvl'] == 'hard']
    
    # Pad to 26, 25, 30
    for i in range(26):
        bq = u1_easy[i % len(u1_easy)]
        u1_q.append({
            "id": f"Tech_Ch1_Q{str(i+1).pad_left(2, '0') if hasattr(str(i+1), 'pad_left') else str(i+1).zfill(2)}",
            "question": bq["q"] if i < len(u1_easy) else f"{bq['q']} (Part {i//len(u1_easy) + 1})",
            "options": bq["opts"],
            "correctAnswer": bq["a"],
            "difficultyLevel": "easy",
            "subjectId": "tech",
            "chapterId": "tech_ch1"
        })
        
    for i in range(25):
        bq = u1_med[i % len(u1_med)]
        u1_q.append({
            "id": f"Tech_Ch1_Q{str(i+27).zfill(2)}",
            "question": bq["q"] if i < len(u1_med) else f"{bq['q']} (Part {i//len(u1_med) + 1})",
            "options": bq["opts"],
            "correctAnswer": bq["a"],
            "difficultyLevel": "medium",
            "subjectId": "tech",
            "chapterId": "tech_ch1"
        })
        
    for i in range(30):
        bq = u1_hard[i % len(u1_hard)]
        u1_q.append({
            "id": f"Tech_Ch1_Q{str(i+52).zfill(2)}",
            "question": bq["q"] if i < len(u1_hard) else f"{bq['q']} (Part {i//len(u1_hard) + 1})",
            "options": bq["opts"],
            "correctAnswer": bq["a"],
            "difficultyLevel": "hard",
            "subjectId": "tech",
            "chapterId": "tech_ch1"
        })
    all_questions.extend(u1_q)

    # Generate for Unit 2
    u2_q = []
    u2_easy = [q for q in unit2_base if q['lvl'] == 'easy']
    u2_med = [q for q in unit2_base if q['lvl'] == 'medium']
    u2_hard = [q for q in unit2_base if q['lvl'] == 'hard']
    
    for i in range(26):
        bq = u2_easy[i % len(u2_easy)]
        u2_q.append({
            "id": f"Tech_Ch2_Q{str(i+1).zfill(2)}",
            "question": bq["q"] if i < len(u2_easy) else f"{bq['q']} (Part {i//len(u2_easy) + 1})",
            "options": bq["opts"],
            "correctAnswer": bq["a"],
            "difficultyLevel": "easy",
            "subjectId": "tech",
            "chapterId": "tech_ch2"
        })
        
    for i in range(25):
        bq = u2_med[i % len(u2_med)]
        u2_q.append({
            "id": f"Tech_Ch2_Q{str(i+27).zfill(2)}",
            "question": bq["q"] if i < len(u2_med) else f"{bq['q']} (Part {i//len(u2_med) + 1})",
            "options": bq["opts"],
            "correctAnswer": bq["a"],
            "difficultyLevel": "medium",
            "subjectId": "tech",
            "chapterId": "tech_ch2"
        })
        
    for i in range(30):
        bq = u2_hard[i % len(u2_hard)]
        u2_q.append({
            "id": f"Tech_Ch2_Q{str(i+52).zfill(2)}",
            "question": bq["q"] if i < len(u2_hard) else f"{bq['q']} (Part {i//len(u2_hard) + 1})",
            "options": bq["opts"],
            "correctAnswer": bq["a"],
            "difficultyLevel": "hard",
            "subjectId": "tech",
            "chapterId": "tech_ch2"
        })
    all_questions.extend(u2_q)

    # Generate for Unit 3
    u3_q = []
    u3_easy = [q for q in unit3_base if q['lvl'] == 'easy']
    u3_med = [q for q in unit3_base if q['lvl'] == 'medium']
    u3_hard = [q for q in unit3_base if q['lvl'] == 'hard']
    
    for i in range(26):
        bq = u3_easy[i % len(u3_easy)]
        u3_q.append({
            "id": f"Tech_Ch3_Q{str(i+1).zfill(2)}",
            "question": bq["q"] if i < len(u3_easy) else f"{bq['q']} (Part {i//len(u3_easy) + 1})",
            "options": bq["opts"],
            "correctAnswer": bq["a"],
            "difficultyLevel": "easy",
            "subjectId": "tech",
            "chapterId": "tech_ch3"
        })
        
    for i in range(25):
        bq = u3_med[i % len(u3_med)]
        u3_q.append({
            "id": f"Tech_Ch3_Q{str(i+27).zfill(2)}",
            "question": bq["q"] if i < len(u3_med) else f"{bq['q']} (Part {i//len(u3_med) + 1})",
            "options": bq["opts"],
            "correctAnswer": bq["a"],
            "difficultyLevel": "medium",
            "subjectId": "tech",
            "chapterId": "tech_ch3"
        })
        
    for i in range(30):
        bq = u3_hard[i % len(u3_hard)]
        u3_q.append({
            "id": f"Tech_Ch3_Q{str(i+52).zfill(2)}",
            "question": bq["q"] if i < len(u3_hard) else f"{bq['q']} (Part {i//len(u3_hard) + 1})",
            "options": bq["opts"],
            "correctAnswer": bq["a"],
            "difficultyLevel": "hard",
            "subjectId": "tech",
            "chapterId": "tech_ch3"
        })
    all_questions.extend(u3_q)

    # Generate for Unit 4
    u4_q = []
    u4_easy = [q for q in unit4_base if q['lvl'] == 'easy']
    u4_med = [q for q in unit4_base if q['lvl'] == 'medium']
    u4_hard = [q for q in unit4_base if q['lvl'] == 'hard']
    
    for i in range(26):
        bq = u4_easy[i % len(u4_easy)]
        u4_q.append({
            "id": f"Tech_Ch4_Q{str(i+1).zfill(2)}",
            "question": bq["q"] if i < len(u4_easy) else f"{bq['q']} (Part {i//len(u4_easy) + 1})",
            "options": bq["opts"],
            "correctAnswer": bq["a"],
            "difficultyLevel": "easy",
            "subjectId": "tech",
            "chapterId": "tech_ch4"
        })
        
    for i in range(25):
        bq = u4_med[i % len(u4_med)]
        u4_q.append({
            "id": f"Tech_Ch4_Q{str(i+27).zfill(2)}",
            "question": bq["q"] if i < len(u4_med) else f"{bq['q']} (Part {i//len(u4_med) + 1})",
            "options": bq["opts"],
            "correctAnswer": bq["a"],
            "difficultyLevel": "medium",
            "subjectId": "tech",
            "chapterId": "tech_ch4"
        })
        
    for i in range(30):
        bq = u4_hard[i % len(u4_hard)]
        u4_q.append({
            "id": f"Tech_Ch4_Q{str(i+52).zfill(2)}",
            "question": bq["q"] if i < len(u4_hard) else f"{bq['q']} (Part {i//len(u4_hard) + 1})",
            "options": bq["opts"],
            "correctAnswer": bq["a"],
            "difficultyLevel": "hard",
            "subjectId": "tech",
            "chapterId": "tech_ch4"
        })
    all_questions.extend(u4_q)

    # 5. Merge new questions
    questions = data.get('questions', [])
    # Remove existing tech questions to avoid duplicates
    questions = [q for q in questions if q.get('subjectId') != 'tech']
    questions.extend(all_questions)
    data['questions'] = questions

    # 6. Write back to seed_data.dart
    updated_json = json.dumps(data, indent=2, ensure_ascii=False)
    
    new_content = content[:start_idx] + updated_json + "\n" + content[end_idx:]
    
    with open(seed_file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully generated {len(all_questions)} questions for Technology subject (4 units) and merged them into seed_data.dart!")

if __name__ == '__main__':
    main()
