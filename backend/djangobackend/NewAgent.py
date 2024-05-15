from crewai import Agent


class CodeAgents:
    def GetDatabaseConnectionCode(self):
        return Agent(
            role="Node js developer",
            goal="""
                Please provide me the code for mysql database connection. 
                I'm looking for node js code that covers mysql database connection and meets production-level standards.
                Try to use latest code and packages .
                """,
            backstory="""You are the best person to provide the correct code""",
            verbose=True,
            allow_delegation=True,
            memory=True,
        )

    def GetRouteCode(self):
        return Agent(
            role="Node js developer",
            goal="""
                Please provide me with code for routing where GET, POST, PUT, and DELETE methods shall be present. 
                I'm looking for code that covers Node.js routing and meets production-level standards.
                Try to use latest code and packages.
                """,
            backstory="""You are the best person to provide the correct code.""",
            verbose=True,
            allow_delegation=False,
            memory=True,
        )

    def GetReactCodeForDispalyUser(self):
        return Agent(
            role="React js developer",
            goal="""
                Please provide me the code for Display User into a table format. 
                I'm looking for react js code that covers Display user and meets production-level standards.
                Try to use latest code and packages with react functional component. use tailwind css for styling.
                """,
            backstory="""You are the best person to provide the correct code Display user into a table""",
            verbose=True,
            allow_delegation=True,
            memory=True,
        )

    def GetReactCodeForAddUser(self):
        return Agent(
            role="React js developer",
            goal="""
                Please provide me the code for Add user. 
                I'm looking for code that covers Add user and meets production-level standards.
                Try to use latest code and packages with react functional component. use tailwind css for styling.
                """,
            backstory="""You are the best person to provide the correct code for Add user""",
            verbose=True,
            allow_delegation=True,
            memory=True,
        )

    def GetReactCodeForUpdateUser(self):
        return Agent(
            role="React js developer",
            goal="""
                Please provide me the code for Update user. 
                I'm looking for code that Update user and meets production-level standards.
                Try to use latest code and packages with react functional component. use tailwind css for styling.
                """,
            backstory="""You are the best person to provide the correct code for Update user.""",
            verbose=True,
            allow_delegation=True,
            memory=True,
        )

    def GetReactCodeForAppJs(self):
        return Agent(
            role="React js developer",
            goal="""
                Please provide me the code for App.js code in React js. 
                I'm looking for code for App.js and that meets production-level standards.
                Try to use latest code and packages. use tailwind css for styling.
                """,
            backstory="""You are the best person to provide the correct code for App.js.""",
            verbose=True,
            allow_delegation=True,
            memory=True,
        )

    def Sumarize(self):
        return Agent(
            role="React js developer",
            goal="""
                Sumarize all the Task and give one output.
                Try to use latest code and packages with react functional component. use tailwind css for styling.
                """,
            backstory="""You are the best person to provide the Sumarize Task""",
            verbose=True,
            allow_delegation=True,
            memory=True,
        )
