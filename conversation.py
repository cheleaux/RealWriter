from tools.fetchArticles import arxiv_search
from autogen import UserProxyAgent, register_function
from agents import researcherAgent, plannerAgent, qualityExaminer, copywriterAgent


userProxyAgent = UserProxyAgent(
    "userProxy",
    description="This agent is a user proxy.",
    llm_config={"config_list": [{"model": "gpt-4-turbo-preview", "api_key": os.environ.get("OPENAI_API_KEY")}]},
    code_execution_config=False,
    human_input_mode="ALWAYS",
    is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
)


# INTEGRATES THE SEARCH FUNCTION AND MAKES IT CALLABLE FOR RESEARCHER AGENT
register_function(
    arxiv_search,
    caller=researcherAgent,
    executor=researcherAgent,
    name="fetch_articles",
    description="A function to return accessable pdf links of research artciles sourced with arXiv on a given topic",
)

register_function(
    arxiv_search,
    caller=researcherAgent,
    executor=researcherAgent,
    name="fetch_articles",
    description="A function to return accessable pdf links of research artciles sourced with arXiv on a given topic",
)