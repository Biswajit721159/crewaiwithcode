from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key
from crewai import Crew, Process
from djangobackend.NewAgent import CodeAgents
from djangobackend.NewTask import CodeTasks


@csrf_exempt
async def Excute(request):
    try:
        GetDatabaseConnectionCode = CodeAgents().GetDatabaseConnectionCode()
        GetRouteCode = CodeAgents().GetRouteCode()
        GetReactCodeForDispalyUser = CodeAgents().GetReactCodeForDispalyUser()
        GetReactCodeForAddUser = CodeAgents().GetReactCodeForAddUser()
        GetReactCodeForUpdateUser = CodeAgents().GetReactCodeForUpdateUser()
        GetReactCodeForAppJs = CodeAgents().GetReactCodeForAppJs()
        # Sumarize=CodeAgents().Sumarize()

        DataBaseConnectionTask = CodeTasks().DataBaseConnectionTask(
            GetDatabaseConnectionCode
        )
        RouteTask = CodeTasks().RouteTask(GetRouteCode, DataBaseConnectionTask)
        GetReactCodeForDispalyUserTask = CodeTasks().GetReactCodeForDispalyUserTask(
            GetReactCodeForDispalyUser, GetRouteCode, RouteTask
        )
        GetReactCodeForAddUserTask = CodeTasks().GetReactCodeForAddUserTask(
            GetReactCodeForAddUser, GetRouteCode, RouteTask
        )
        GetReactCodeForUpdateUserTask = CodeTasks().GetReactCodeForUpdateUserTask(
            GetReactCodeForUpdateUser, GetRouteCode, RouteTask
        )
        GetReactCodeForAppJsTask = CodeTasks().GetReactCodeForAppJsTask(
            GetReactCodeForAppJs,
            GetReactCodeForDispalyUserTask,
            GetReactCodeForAddUserTask,
            GetReactCodeForUpdateUserTask,
        )
        # SumarizeTask=CodeTasks().SumarizeTask(Sumarize,GetRouteCode,RouteTask,GetReactCodeForDispalyUserTask,GetReactCodeForAddUserTask,GetReactCodeForUpdateUserTask)
        # SumarizeTask=CodeTasks().SumarizeTask(Sumarize,GetRouteCode,RouteTask)

        crew = Crew(
            # agents=[GetDatabaseConnectionCode,GetRouteCode,Sumarize],
            # tasks=[DataBaseConnectionTask,RouteTask,SumarizeTask],
            agents=[
                GetDatabaseConnectionCode,
                GetRouteCode,
                GetReactCodeForDispalyUser,
                GetReactCodeForAddUser,
                GetReactCodeForUpdateUser,
                GetReactCodeForAppJs,
            ],
            tasks=[
                DataBaseConnectionTask,
                RouteTask,
                GetReactCodeForDispalyUserTask,
                GetReactCodeForAddUserTask,
                GetReactCodeForUpdateUserTask,
                GetReactCodeForAppJsTask,
            ],
            process=Process.sequential,
            # full_output=True,
            # memory=True,
            # verbose=True,
            # embedder={
            #     "provider": "openai",
            #     "config":{
            #         "model": 'gpt-4-vision-preview',
            #     }
            # }
        )
        result = crew.kickoff()

        ans = []
        html_content = await FrontendCode()
        data = solve(html_content)
        ans.append({"FrontendCode": data})
        # ans.append({"FrontendcodeEditor":html_content})

        html_content = await BackendCode()
        data = solve(html_content)
        ans.append({"BackendCode": data})
        # ans.append({"BackendcodeEditor":html_content})

        return JsonResponse(ans, safe=False)

    except Exception as error:
        print(error)
        return JsonResponse("data not found", safe=False)


current_directory = os.path.dirname(os.path.abspath(__file__))
backendcode_directory = os.path.dirname(current_directory)


async def FrontendCode():
    ans = ""

    markdown_file_path = os.path.join(backendcode_directory, "AppJS.md")
    with open(markdown_file_path, "r") as f:
        markdown_content = f.read()
    ans += markdown_content
    ans += "\n"

    markdown_file_path = os.path.join(backendcode_directory, "DisplayUser.md")
    with open(markdown_file_path, "r") as f:
        markdown_content = f.read()
    ans += markdown_content
    ans += "\n"

    markdown_file_path = os.path.join(backendcode_directory, "AddUser.md")
    with open(markdown_file_path, "r") as f:
        markdown_content = f.read()
    ans += markdown_content
    ans += "\n"

    markdown_file_path = os.path.join(backendcode_directory, "UpdateUser.md")
    with open(markdown_file_path, "r") as f:
        markdown_content = f.read()
    ans += markdown_content
    ans += "\n"
    return ans


async def BackendCode():
    markdown_file_path = os.path.join(backendcode_directory, "Backendoutput.md")
    with open(markdown_file_path, "r") as f:
        markdown_content = f.read()
    return markdown_content


def solve(string):
    ans = []
    n = len(string)
    word = ""
    i = 0
    while i < n:
        if (
            i + 2 < n
            and string[i] == "`"
            and string[i + 1] == "`"
            and string[i + 2] == "`"
        ):
            ans.append({"text": word})
            word = ""
            j = i + 3
            while j < n:
                if (
                    j + 2 < n
                    and string[j] == "`"
                    and string[j + 1] == "`"
                    and string[j + 2] == "`"
                ):
                    ans.append({"code": word})
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
        ans.append({"text": word})

    return ans
