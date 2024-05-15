from crewai import Task
from crewai_tools import SerperDevTool
search_tool = SerperDevTool()

database='MYSQL'
        
code="""demo code:-
            `     
            var express = require('express');
            var mysql = require('mysql2/promise');
            var app = express();
            async function connection(){
                var connection = mysql.createConnection({
                    host: 'localhost',
                    user: 'root',
                    password: '190183',
                    database: 'classicmodels'
                });
                return connection
            }
            async function fetchdata(){
                let sql = 'SELECT * FROM products limit 100';
                const db = await connection()
                let [result] = await db.execute(sql);
                return result
            }
            fetchdata()
            `"""

ReactjsCode=""" 
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import { Table } from 'react-bootstrap';

function DataTable(props) {

  const location = useLocation();
  const { data } = location?.state;

  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          {data?.length > 0 && Object.keys(data?.[0]).map((key) => (
            <th key={key}>{key}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data?.map((item, index) => (
          <tr key={index}>
            {Object?.values(item)?.map((value, i) => (
              <td key={i}>{value}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </Table>
  );
}
export default DataTable; 
"""                
                
class Tasks():   
    
    def ConnectToDataBaseandFetchRecordTask(self,agent):
        return Task(
            description=f""" 
            Provide the correct code for connecting to the ${database} database and fetch record from ${database} database . 
            Aim to deliver high-quality code suitable for implementation in our production environment for an example ${code} .
            """,
            expected_output=f"""
            Result should be as we want in bellow . Do not return other thing .Try to give us correct result.
            here is some ${code} how you can connect to database and fetch data from the database.
            Please do not add other thing inorder to give the result. I have already give you many thing like user,password,host,database etc.
            """,
            agent=agent,
        )
    
    def OutputCheckerTask(self,agent):
        return Task(
            description=""" 
            What ever 'Connect to DataBase and fetch data from database' agent give the output try to convert into a javascript code .
            if as such other thing is present then remove those .""",
            expected_output=f"""Verify if output is a javascript code . 
            if not Remove other paragraph thing such that we can save those data into a js file.
            Remembar i want the output in a js file should be valid it is not give us any error""",
            agent=agent,
            output_file="backendcode.md"
        )
        
    def ReactJsTask(self,agent):
        return Task(
            description=f""" 
            Please provide the correct React.js code following the template - ${ReactjsCode}.
            Only provide the code without additional elements. We integrate this code directly into our work without prior validation. 
            Aim to deliver high-quality code suitable for our production environment.
            """,
            expected_output=f"""
            The expected outcome should match the provided structure below.
            Please refrain from including any additional elements in the result. 
            Ensure accuracy and adherence to the specified structure using the template - ${ReactjsCode}. 
            Avoid introducing any new components or features beyond what has already been provided. 
            Your adherence to these guidelines is appreciated.
            """,
            agent=agent,
        )
    
    def ReactJsOutputCheckerTask(self,agent):
        return Task(
            description=f""" 
            What ever 'React js Expart' agent give the output try to convert into a React js code .
            if as such other thing is present then remove those . Try to follow this rules ${ReactjsCode}""",
            expected_output=f"""Verify if output is a React js code . follow this code for more result ${ReactjsCode}
            if not Remove other paragraph thing such that we can save those data into a js file.
            Remembar i want the output in a js file should be valid and it not give us any error.""",
            agent=agent,
            output_file="frontendcode.md"
        )    
        
        
    # def FetchDataFromDataBaseTask(self,agent):
    #     return Task(
    #         description=""" Retrieve data from the database. 
    #         Provide high-quality code suitable for implementation in our production environment.""",
    #         expected_output=f"""First you need to say how to install all the dependencies.Give  Node js code for how to fetch Data from a ${database} DataBase.
    #          Always give us the latest dependencies.""",
    #         agent=agent,
    #         # tools=[search_tool],
    #         output_file="output2.md"
    #     )
    
    
    # def DisplayItIntoTableTask(self,agent):
        # return Task(
        #     description="""Display the data in a table. Provide high-quality code suitable for implementation in our production environment.""",
        #     expected_output=f"""First you need to say how to install all the dependencies .
        #     When you write the code then try fetch the column from the data set whcich is coming from backend
        #     Give React js code for how to diaplay data into a table and also give like how to use api inorder to get data from that.
        #      Always give us the latest dependencies.""",
        #     agent=agent,
        #     tools=[search_tool],
        #     output_file="output3.md"
        # ) 
    
        # return Task(
        #     description=""" Summarize the tasks from all the agents and provide the correct code. 
        #     Aim to deliver high-quality code suitable for implementation in our production environment """,
        #     expected_output="""Write the code into Java script language . First, provide the database connection code. 
        #     Second, supply the code for fetching data from the database. 
        #     Finally, offer the code for displaying the data in a table.
        #     Please ensure that all code provided meets production-level standards. with that give us all the dependencies.
        #      Always give us the latest dependencies.""",
        #     agent=agent,
        #     # tools=[search_tool],
        #     output_file="output.md"
        # )        