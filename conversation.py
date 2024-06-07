import os
import autogen
from tools.fetchArticles import fetch_articles
from autogen import UserProxyAgent, register_function
from agents import researcherAgent, plannerAgent, qualityExaminer, copywriterAgent
from qualityOfficerAgent import MemGPT_qualityOfficer


# USER PROXY CONFIGURATION
config_list = [{
    "model": "gpt-4-turbo-preview",
    "api_key": os.environ.get("OPENAI_API_KEY")
}]

llm_config = {"config_list": config_list }
exe_config = {"work_dir": ".", "use_docker": False }
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


# INTEGRATES THE SEARCH FUNCTION AND MAKES IT CALLABLE FOR RESEARCHER AGENT
register_function(
    fetch_articles,
    caller=researcherAgent,
    executor=researcherAgent,
    name="fetch_articles",
    description="A function to return accessable pdf links of research artciles sourced with arXiv on a given topic",
)

previusSpeaker = None

def state_transition(last_speaker, groupchat):
    messages = groupchat.messages

    if last_speaker is userProxyAgent:
        return researcherAgent
    if last_speaker is researcherAgent and "information sheet" in messages[-1]["content"]:
        return plannerAgent
    elif last_speaker is plannerAgent:
        return copywriterAgent
    elif last_speaker is copywriterAgent and "- END OF ARTICLE -" in messages[-1]["content"]:
        return None
    elif last_speaker is copywriterAgent:
        return copywriterAgent
    else: 
        return researcherAgent


groupchat = autogen.GroupChat(
    agents=[ userProxyAgent, researcherAgent, plannerAgent, copywriterAgent ],
    messages=[], max_round=15,
    speaker_selection_method=state_transition,
)

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

manager.initiate_chat( manager, message="write an article about lightning, how it works and intereacts with the clouds")
