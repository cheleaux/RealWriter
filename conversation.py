import os
import autogen
from tools.fetchArticles import fetch_articles
from autogen import UserProxyAgent, register_function
from agents import researcherAgent, plannerAgent, qualityExaminer, copywriterAgent
from qualityOfficerAgent import MemGPT_qualityOfficer


# USER PROXY CONFIGURATION
config_list =  [{"model": "gpt-4-turbo-preview", "api_key": os.environ.get("OPENAI_API_KEY")}]

llm_config = {"config_list": config_list}
exe_config = {"work_dir": ".", "use_docker": False,}
userProxyAgent = UserProxyAgent(
    "userProxy",
    description="This agent is a user proxy.",
    llm_config= llm_config,
    code_execution_config= exe_config,
    human_input_mode="NEVER",
    system_message="Say 'TERMINATE' if request has been completed to satisfaction"
)


# SIMPLE USER PROXY CONFIGURATION
simple_config_list = [{ 'model': 'gpt-4' }]

simple_llm_config = {"config_list": simple_config_list, "seed": 42}
simple_exe_config = {"last_n_messages": 2, "work_dir": "groupchat", "use_docker": False}
simple_user_proxy = UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config=simple_exe_config,
    human_input_mode='ALWAYS',
)


# # INTEGRATES THE SEARCH FUNCTION AND MAKES IT CALLABLE FOR RESEARCHER AGENT
# register_function(
#     fetch_articles,
#     caller=researcherAgent,
#     executor=userProxyAgent,
#     name="fetch_articles",
#     description="A function to return accessable pdf links of research artciles sourced with arXiv on a given topic",
# )


groupchat = autogen.GroupChat(agents=[simple_user_proxy, MemGPT_qualityOfficer], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=simple_llm_config)

simple_user_proxy.initiate_chat(MemGPT_qualityOfficer, message="")
