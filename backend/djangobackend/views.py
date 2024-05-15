from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key
from djangobackend.Task import Tasks
from djangobackend.Agent import Agents
from crewai import Crew, Process
import json 
import markdown

from openai import OpenAI



@csrf_exempt 
async def Order_Product(request):
    try:
        # ConnectToDataBaseExpert = Agents().ConnectToDataBaseExpert()
        # FetchDataFromDataBaseExpert = Agents().FetchDataFromDataBaseExpert()
        # DisplayItIntoTableExpert = Agents().DisplayItIntoTableExpert()
        # SummarizeExpert=Agents().SummarizeExpert()
        # DataBaseConnectionAndFetchRecordExpert=Agents().DataBaseConnectionAndFetchRecordExpert()
        
        # ConnectToDataBaseTask = Tasks().ConnectToDataBaseTask(ConnectToDataBaseExpert)
        # FetchDataFromDataBaseTask=Tasks().FetchDataFromDataBaseTask(FetchDataFromDataBaseExpert)
        # DisplayItIntoTableTask=Tasks().DisplayItIntoTableTask(DisplayItIntoTableExpert)
        # SummarizeTask=Tasks().SummarizeTask(SummarizeExpert)
        # DataBaseConnectionAndFetchRecordTask=Tasks().DataBaseConnectionAndFetchRecordTask(DataBaseConnectionAndFetchRecordExpert)
        
        ConnectToDataBaseandFetchRecordExpert=Agents().ConnectToDataBaseandFetchRecordExpert()
        OutputCheckerExpert=Agents().OutputCheckerExpert()
        ReactJsExpert=Agents().ReactJsExpert()
        ReactJsOutputCheckerExpert=Agents().ReactJsOutputCheckerExpert()
        
        ConnectToDataBaseandFetchRecordTask=Tasks().ConnectToDataBaseandFetchRecordTask(ConnectToDataBaseandFetchRecordExpert)
        OutputCheckerTask=Tasks().OutputCheckerTask(OutputCheckerExpert)
        ReactJsTask=Tasks().ReactJsTask(ReactJsExpert)
        ReactJsOutputCheckerTask=Tasks().ReactJsOutputCheckerTask(ReactJsOutputCheckerExpert)
        
        crew = Crew(
            agents=[ConnectToDataBaseandFetchRecordExpert,OutputCheckerExpert,ReactJsExpert,ReactJsOutputCheckerExpert],
            tasks=[ConnectToDataBaseandFetchRecordTask,OutputCheckerTask,ReactJsTask,ReactJsOutputCheckerTask],
            # agents=[ConnectToDataBaseExpert,FetchDataFromDataBaseExpert,DataBaseConnectionAndFetchRecordExpert,DisplayItIntoTableExpert,SummarizeExpert],
            # tasks=[ConnectToDataBaseTask,FetchDataFromDataBaseTask,DataBaseConnectionAndFetchRecordTask,DisplayItIntoTableTask,SummarizeTask],
            process=Process.sequential 
        )
        result = crew.kickoff()
        ans=[]
        
        # html_content=await file1()
        # data=solve(html_content)
        # ans.append({"ConnectToDataBaseOutput":data})
    
        # html_content=await file2()
        # data=solve(html_content)
        # ans.append({"FetchDataFromDataBaseOutput":data})
    
        # html_content=await file3()
        # data=solve(html_content)
        # ans.append({"DisplayItIntoTableOutput":data})
        
        # html_content=await file()
        # data=solve(html_content)
        # ans.append({"SummarizeOutput":data})
        
        
        html_content=await FrontendCode()
        data=solve(html_content)
        ans.append({"FrontendCode":data})
        
        html_content=await BackendCode()
        data=solve(html_content)
        ans.append({"BackendCode":data})
        
        return JsonResponse(ans,safe=False)
    except Exception as error:
            print("Error is ok ######### ",error)
            return JsonResponse([{"ConnectToDataBaseOutput":"Your maximum context is reached or your query is invalid. Please refresh this page and write your query again."}], safe=False)
 
current_directory = os.path.dirname(os.path.abspath(__file__))
backendcode_directory = os.path.dirname(current_directory)
 

async def FrontendCode():
    markdown_file_path = os.path.join(backendcode_directory, 'frontendcode.md')
    with open(markdown_file_path, 'r') as f:
        markdown_content = f.read()
    return markdown_content       
 
async def BackendCode():
    markdown_file_path = os.path.join(backendcode_directory, 'Backendoutput.md')
    with open(markdown_file_path, 'r') as f:
        markdown_content = f.read()
    return markdown_content        
 
 
 
# async def file():
#     markdown_file_path = os.path.join(backendcode_directory, 'output.md')
#     with open(markdown_file_path, 'r') as f:
#         markdown_content = f.read()
#     return markdown_content        
        
        
# async def file1():
#     markdown_file_path1 = os.path.join(backendcode_directory, 'output1.md')
#     with open(markdown_file_path1, 'r') as f:
#         markdown_content = f.read()
#     return markdown_content


# async def file2():
#     markdown_file_path2 = os.path.join(backendcode_directory, 'output2.md')
#     with open(markdown_file_path2, 'r') as f:
#         markdown_content = f.read()
#     return markdown_content


# async def file3():
#     markdown_file_path3 = os.path.join(backendcode_directory, 'output3.md')
#     with open(markdown_file_path3, 'r') as f:
#         markdown_content = f.read()
#     return markdown_content
    
    
    
def solve(string):
    
    ans = []
    #start
    ans.append({'code':string})
    return  ans
    #end
    n = len(string)
    word = ""
    i = 0
    while i < n:
        if i + 2 < n and string[i] == '`' and string[i + 1] == '`' and string[i + 2] == '`':
            ans.append({'text': word})
            word = ""
            j = i + 3
            while j < n:
                if j + 2 < n and string[j] == '`' and string[j + 1] == '`' and string[j + 2] == '`':
                    ans.append({'code': word})
                    i = j + 2
                    word = ""
                    break
                else:
                    word += string[j]
                j += 1
        else:
            word += string[i]
        i += 1

    if len(word) != 0:
        ans.append({'text': word})

    return ans

