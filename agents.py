import os
from autogen import ConversableAgent



with open(r'./prompts/researcherPrompt.txt', 'r', encoding='utf-8' ) as researcherPrompt:
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
        code_execution_config={
            "work_dir": ".",
            "use_docker": False,
        },
        human_input_mode="NEVER",
        max_consecutive_auto_reply=6,
        # is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
    )


with open(r'./prompts/plannerPrompt.txt', 'r', encoding='utf-8') as plannerPrompt:
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


with open(r'./prompts/copywriterPrompt.txt', 'r', encoding='utf-8') as writerPrompt:
    copywriterAgent = ConversableAgent(
        "Writer",
        system_message=writerPrompt.read(),
        description="This agent is a copywriter. This agent uses the information gathered by the researcher agent to write engaging content that abides by the examiners corrections.",
        llm_config={
            "config_list": [{
                "model": "gpt-4-turbo-preview",
                "api_key": os.environ.get("OPENAI_API_KEY")
                }],
            "temperature": 1.2
        },
        code_execution_config=False,
        human_input_mode="NEVER",
        max_consecutive_auto_reply=6,
        is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
    )

with open(r'./prompts/qualityExaminerPrompt.txt', 'r', encoding='utf-8' ) as examinerPrompt:
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
        code_execution_config={
            "work_dir": ".",
            "use_docker": False,
        },
        human_input_mode="NEVER",
        max_consecutive_auto_reply=6,
        is_termination_msg=lambda x: True if "TERMINATE" in x.get("content") else False,
    )

    