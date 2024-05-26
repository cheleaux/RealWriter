import os
from tools.fetchArticles import arxiv_search
from autogen import ConversableAgent, UserProxyAgent, register_function


researcherPrompt = open(r'./prompts/researcherPrompt.txt', 'r')
plannerPrompt = open(r'./prompts/plannerPrompt.txt', 'r')
writerPrompt = open(r'./prompts/copywriterPrompt.txt', 'r')
examinerPrompt = open(r'./prompts/qualityExaminerPrompt.txt', 'r')


userProxyAgent = UserProxyAgent(
    "userProxy",
    system_message="You are a helpful AI agent that relays user messages to other agent in the chat/session",
    description="This agent is a user proxy.",
    llm_config={"config_list": [{"model": "gpt-4-turbo-preview", "api_key": os.environ.get("OPENAI_API_KEY")}]},
    code_execution_config=False,
    human_input_mode="ALWAYS",
    is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
)

researcherAgent = ConversableAgent(
    "Researcher",
    system_message=researcherPrompt.read(),
    description="This agent is a content researcher who always goes first, This agent is responsible for gathering all the context and information about the topic for a piece of content, and then write an information sheet for the planner to plan the content with",
    llm_config={
        "config_list": [{
            "model": "gpt-4-turbo-preview",
            "api_key": os.environ.get("OPENAI_API_KEY")
        }],
        "temperature": 0.5
    },
    code_execution_config=True,
    human_input_mode="NEVER",
    max_consecutive_auto_reply=6,
    is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
)


plannerAgent = ConversableAgent(
    "Planner",
    system_message=plannerPrompt.read(),
    description="This agent is a content planner and is the first act on a users request. This agent writes detailed content plans to help the writer agent and research agent structure and organsise their tasks with the context of the users request",
    llm_config={
        "config_list": [{
            "model": "gpt-4-turbo-preview",
            "api_key": os.environ.get("OPENAI_API_KEY")
            }],
        "temperature": 0.9
    },
    code_execution_config=False,
    human_input_mode="NEVER",
    max_consecutive_auto_reply=6,
    is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
)


copywriterAgent = ConversableAgent(
    "Writer",
    system_message=writerPrompt.read(),
    description="This agent is a copywriter. This agent uses the information gathered by the researcher agent to write engaging content that abides by the examiners corrections.",
    llm_config={
        "config_list": [{
            "model": "gpt-4-turbo-preview",
            "api_key": os.environ.get("OPENAI_API_KEY")
            }],
        "temperature": 1.4
    },
    code_execution_config=False,
    human_input_mode="NEVER",
    max_consecutive_auto_reply=6,
    is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
)

qualityExaminer = ConversableAgent(
    "Quality Examiner",
    system_message=examinerPrompt.read(),
    description="This agent is a content quality examiner. This agent analyses the content written by the copywriter agent and examined it based on the based the google search Quality control guidelines",
    llm_config={
        "config_list": [{
            "model": "gpt-4-turbo-preview",
            "api_key": os.environ.get("OPENAI_API_KEY")
            }],
        "temperature": 0.4
    },
    code_execution_config=True,
    human_input_mode="NEVER",
    max_consecutive_auto_reply=6,
    is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,

)

register_function(
    arxiv_search,
    caller=researcherAgent,
    executor=researcherAgent,
    name="fetch_articles",
    description="A function to return accessable pdf links of research artciles sourced with arXiv on a given topic",
) 