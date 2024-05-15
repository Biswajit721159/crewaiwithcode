from crewai import Task

Tablename = "users"
column = "id int AI PK , full_name varchar(100) , mobile_number varchar(15) , email varchar(100)"


class CodeTasks:

    def DataBaseConnectionTask(self, agent):
        return Task(
            description=f""" 
            Please provide MySQL database connection code with the following configuration: host: 'localhost', user: 'root', password: '190183', database: 'Users'. 
            Please use the mysql2 package for this code. The code should be encapsulated within a function so that it can be easily used in our application.
            Please ensure the code and packages are up-to-date to avoid any errors.
            """,
            expected_output=f"""
            Please provide instructions for installing the mysql2 package and utilizing 'mysql2/promise'. 
            Additionally, return a function that facilitates connection to the MySQL database.
            Try to use latest code and packages
            """,
            output_file="Connection.md",
            agent=agent,
        )

    def RouteTask(self, agent, DataBaseConnectionTask):
        return Task(
            description=f"""
            Retrieve the connection context field.
            Please provide a complete Node.js code that includes GET for all record,GET for id, POST, PUT, and DELETE methods.
            The code should operate on the ${Tablename} table with the following columns: ${column}. 
            When defining each route, ensure you utilize the connection code obtained from the context field.
            Note that the application should run on port 5000.
            """,
            expected_output=f"""
            First give the connection code .
            Utilize the connection code within the same file and integrate it into our routing code for connection purposes. 
            Please provide a comprehensive code that creates all routes and ensure it's production-ready. 
            Additionally, include instructions for installing necessary packages.Try to use latest code and packages.
            Also use Try Catch for error handling and cors error.
            """,
            agent=agent,
            context=[DataBaseConnectionTask],
            output_file="Backendoutput.md",
        )

    def GetReactCodeForDispalyUserTask(self, originalagent, subagent, RouteTask):
        return Task(
            description=f""" 
            Please establish a connection with the ${subagent} agent to determine the connected port or the route required to retrieve all users. 
            On this page, add a button labeled 'Add User' that redirects users to the 'Add User' page upon clicking. 
            After fetching the data, display it in a table format, with the first row's columns populated using data[0] through a looping method. 
            For each user, include 'Update' and 'Delete' buttons to facilitate user updates and deletions.
            Clicking the 'Update' button should navigate users to another page for updating user details. 
            Aim to deliver high-quality, production-ready code suitable for integration into our environment.
            """,
            expected_output=f"""
            Please establish a connection with the ${subagent} agent to determine the connected port or the route required to retrieve all users. 
            On this page, add a button labeled 'Add User' that redirects users to the 'Add User' page upon clicking. 
            After fetching the data, display it in a table format, Try to give all the column name when you display those data into a table format .
            For more about table field see this ${column}
            For each user, include 'Update' and 'Delete' buttons to facilitate user updates and deletions.
            Clicking the 'Update' button should navigate users to another page for updating user details. 
            Also when user click on the delete button then also that data should be delete.
            Aim to deliver high-quality, production-ready code suitable for integration into our environment.
            Please provide instructions for installing packages.
            Try to use latest code and packages with react functional component.
            Also use Try Catch for error handling and use proper api.
            """,
            agent=originalagent,
            context=[RouteTask],
            output_file="DisplayUser.md",
        )

    def GetReactCodeForAddUserTask(self, originalagent, subagent, RouteTask):
        return Task(
            description=f""" 
            Please consult the ${subagent} agent to determine the required HTML fields and the necessary API for inserting records into our database. 
            The goal is to deliver high-quality code suitable for deployment in our production environment.
            """,
            expected_output=f"""
            Please provide the HTML page for adding a user and ensure proper validation. Aim to deliver production-ready code.
            Identify the required HTML fields for completing this task.After that you need to back to the main page.
            Please provide instructions for installing packages.
            Try to use latest code and packages with react functional component.
            Also use Try Catch for error handling and use proper api.
            """,
            agent=originalagent,
            context=[RouteTask],
            output_file="AddUser.md",
        )

    def GetReactCodeForUpdateUserTask(self, originalagent, subagent, RouteTask):
        return Task(
            description=f""" 
            Please consult the ${subagent} agent to identify the necessary HTML fields and API calls for updating data in our database. 
            The goal is to deliver high-quality code suitable for deployment in our production environment.
            """,
            expected_output=f"""
            Please provide the HTML code for updating a user and ensure proper validation. 
            Aim to deliver production-ready code. Identify the required HTML fields for completing this task. After that go back to the main page.
            Note if you passing some data from another component then you need to get those data and use that
            Please provide instructions for installing packages.
            Try to use latest code and packages with react functional component.
            Also use Try Catch for error handling and use proper api.
            """,
            agent=originalagent,
            context=[RouteTask],
            output_file="UpdateUser.md",
        )

    def GetReactCodeForAppJsTask(
        self,
        originalagent,
        GetReactCodeForDispalyUserTask,
        GetReactCodeForAddUserTask,
        GetReactCodeForUpdateUserTask,
    ):
        return Task(
            description=f""" 
            give us the correct react app.js code . where you need to route all the pages for more connect to 'context' field.
            Try to latest react-router-dom code.Because Your code is give me some error when using 'switch'.
            properly see the 'context' field for file name.
            """,
            expected_output="""
            To create all necessary pages and facilitate navigation, provide the code for App.js. 
            Aim to deliver high-quality, production-ready code suitable for integration into our environment.
            Please try to give the proper name for those file and try to describe those file.
            Please give the display user , add user , update user route.
            Please use latest code and packages.previously i see your code is not latest and it is give some error.
            example, 1.When you are using 'switch' from raect-router-dom  it is not working .
            2. When you are using like - <Route exact path="/" component={Users} /> . Here i see 'component' is not working  you need to use 'element' .
            
            """,
            agent=originalagent,
            context=[
                GetReactCodeForDispalyUserTask,
                GetReactCodeForAddUserTask,
                GetReactCodeForUpdateUserTask,
            ],
            output_file="AppJS.md",
        )

    def SumarizeTask(self, agent, subagent, RouteTask):
        return Task(
            description=f""" 
            Try to see the all the output of Agent and summerize all of them and give an output of all those
            
            """,
            expected_output=f"""
            
            1. give us the App.js file in React.js .Try to latest react-router-dom code . Because Your code is give me some error when you are using switch .
            Please establish a connection with the ${subagent} agent to determine the connected port or the route required to retrieve all users ,
            insert user,delete user and also update user. Please provide instructions for installing packages.
            
            2.give us the Display user page . After fetching the data, display it in a table format, with the first row's columns populated using data[0] through a looping method. 
            For each user, include 'Update' and 'Delete' buttons to facilitate user updates and deletions.
            Clicking the 'Update' button should navigate users to another page for updating user details. 
            To create all necessary pages and facilitate navigation, provide the code for App.js. 
            On this page, add a button labeled 'Add User' that redirects users to the 'Add User' page upon clicking. 
            Aim to deliver high-quality, production-ready code suitable for integration into our environment.
            Please provide instructions for installing packages.
            
            
            3.Please provide the HTML page for adding a user and ensure proper validation. Aim to deliver production-ready code.
            Identify the required HTML fields for completing this task.
            Please provide instructions for installing packages.
            Try to use latest code and packages
            
            4.Please provide the HTML code for updating a user and ensure proper validation. 
            Aim to deliver production-ready code. Identify the required HTML fields for completing this task.
            Please provide instructions for installing packages.
            Try to use latest code and packages
            
            """,
            agent=agent,
            # context=[RouteTask,GetReactCodeForDispalyUserTask,GetReactCodeForAddUserTask,GetReactCodeForUpdateUserTask],
            output_file="Output.md",
        )
