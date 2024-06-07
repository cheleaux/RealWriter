from memgpt.autogen.memgpt_agent import create_memgpt_autogen_agent_from_config
from memgpt.autogen.memgpt_agent import load_autogen_memgpt_agent
import os




MemGPT_qualityOfficer = load_autogen_memgpt_agent(agent_config={"name": "qualityOfficer"}, auto_save=True)