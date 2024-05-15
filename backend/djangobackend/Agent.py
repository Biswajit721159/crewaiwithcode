from crewai import Agent
class Agents():
    def ConnectToDataBaseandFetchRecordExpert(self):
        return Agent(
                role='Connect to DataBase and fetch data from database',
                goal="""
                Please provide me the code for connecting to the database and fetch data from the database. 
                I'm looking for code that covers mysql database connection scenarios and meets production-level standards.
                """,
                backstory="""You are the best person to provide the correct code for connecting to the database and fetch data from database.""",    
                verbose=True,  
                allow_delegation=True,  
                memory=True  
        )
    def OutputCheckerExpert(self):
        return Agent(
                role='Output Checker',
                goal="""Please provided a database connection code and Fetch record from database in javascript language""",
                backstory=""" You are best person to check output """,
                verbose=True,  
                allow_delegation=True,  
                memory=True  
            ) 
    def ReactJsExpert(self):
        return Agent(
                role='React js Expart',
                goal="""
                Please provide me with the code in react js such that we show some arrays of data into a table format. 
                I'm looking for code that covers all those scenarios and meets production-level standards.
                """,
                backstory="""You are the best person to provide the Recat js code for showingdata into a table format""",    
                verbose=True,  
                allow_delegation=True,  
                memory=True  
        )
    def ReactJsOutputCheckerExpert(self):
        return Agent(
                role='React js output checker',
                goal="""Please check the output if it is possible to create a react js table code such such that we can shown those data into a table format""",
                backstory="""You are best person to check output""",
                verbose=True,  
                allow_delegation=True,  
                memory=True  
            )    
    
          
              
    # def FetchDataFromDataBaseExpert(self):
    #     return Agent(
    #             role='Fetch Data From DataBase',
    #             goal="""Please provide code to fetch data from the database. 
    #             Include connection code for mysql databases, ensuring it meets production standards. 
    #             Return the data in a format suitable for frontend integration via API calls.
    #             please try to describe how install the dependencies and also give those comamnd.""",
    #             backstory=""" You are best person to fetch record from database's """,
    #             verbose=True,  
    #             allow_delegation=True,  
    #             memory=True  
    #         )
    # def SummarizeExpert(self):
        return Agent(
                role='Summarize Expert',
                goal="""Retrieve outputs from the 'Connect to Database,' 'Fetch Data From Database,' and 'Display It Into Table' agents. 
                Summarize all outputs and provide production-level code that impresses all our users.
                please try to describe how install the dependencies and also give those comamnd.""",
                backstory="""You are the best person to summarize data """,
                verbose=True,  
                allow_delegation=True,  
                memory=True  
            )                         
        
        