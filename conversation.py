import os
from tools.fetchArticles import fetch_articles
from autogen import UserProxyAgent, register_function
from agents import researcherAgent, plannerAgent, qualityExaminer, copywriterAgent


userProxyAgent = UserProxyAgent(
    "userProxy",
    description="This agent is a user proxy.",
    llm_config={"config_list": [{"model": "gpt-4-turbo-preview", "api_key": os.environ.get("OPENAI_API_KEY")}]},
    code_execution_config={
            "work_dir": ".",
            "use_docker": False,
        },
    human_input_mode="NEVER",
    system_message="Say 'TERMINATE' if request has been completed to satisfaction"
    # is_termination_msg = lambda x: x is not None and "TERMINATE" in x.get("content", "")
)


# INTEGRATES THE SEARCH FUNCTION AND MAKES IT CALLABLE FOR RESEARCHER AGENT
register_function(
    fetch_articles,
    caller=researcherAgent,
    executor=userProxyAgent,
    name="fetch_articles",
    description="A function to return accessable pdf links of research artciles sourced with arXiv on a given topic",
)

chatResult = userProxyAgent.initiate_chat(
    researcherAgent,
    message="can you make me an information sheet about the effects of caffine on headaches?"
)