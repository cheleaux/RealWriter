from memgpt.autogen.memgpt_agent import create_memgpt_autogen_agent_from_config
from memgpt.autogen.memgpt_agent import load_autogen_memgpt_agent
import os

# create a config for the MemGPT AutoGen agent
config_list_memgpt = [
    {
        "model": "gpt-4",
        "context_window": 8192,
        "preset": "memgpt_chat",  # NOTE: you can change the preset here
        # OpenAI specific
        "model_endpoint_type": "google_ai",
        "openai_key": os.environ.get('OPENAI_API_KEY'),
    },
]
llm_config_memgpt = {"config_list": config_list_memgpt, "seed": 42}

# there are some additional options to do with how you want the interface to look (more info below)
interface_kwargs = {
    "debug": False,
    "show_inner_thoughts": True,
    "show_function_outputs": False,
}

# then pass the config to the constructor
MemGPT_qualityOfficer = create_memgpt_autogen_agent_from_config(
    "qualityOfficer",
    llm_config=llm_config_memgpt,
    system_message="""
            Your job is to analyse the content created by the writer agent and assess whether it satisfies the the Google Quality Control guidelines outlined in document
            The Google quality control document contains guidelines for making good content that ranks highly on google and is recieved well by readers.
            You should understand these guidelines thoroughly.
            Compliant content cannot be flagged as AI generated.
            You should ensure that no content passes your inspectino unless it satifies these guidelines.
            You must assess whether the content appears AI-genenrated, regardless of the fact that we know it is.
            When assessing the content, penalise everything this does not meet the guidelines
            When analysing the content, penalise anything within the content that the guidelines outline as unfavourable or undesired in content.
            When inspecting the content, penalise all parts in the content that arent directly pointed out in the guidelines but that the guidelines infers is problematic.
            Include explainations from the guidelines in feedback. 
            """,
    interface_kwargs=interface_kwargs,
    default_auto_reply="...",
    skip_verify=False,  # NOTE: you should set this to True if you expect your MemGPT AutoGen agent to call a function other than send_message on the first turn
    auto_save=True ,  # NOTE: set this to True if you want the MemGPT AutoGen agent to save its internal state after each reply - you can also save manually with .save()
)



# To load an AutoGen+MemGPT agent you previously created, you can use the load function:
# MemGPT_qualityOfficer = load_autogen_memgpt_agent(agent_config={"name": "qualityOfficer"}, auto_save=True)