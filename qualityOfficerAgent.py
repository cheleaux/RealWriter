from memgpt.autogen.memgpt_agent import create_memgpt_autogen_agent_from_config
from memgpt.autogen.memgpt_agent import load_autogen_memgpt_agent


MemGPT_qualityOfficer = load_autogen_memgpt_agent(agent_config={"name": "qualityOfficer"}, auto_save=True)

# Quality Officer uses the Memgpt-autogen package to load pre-trained quality officer agent.
# The agent wont work if both the Mempgpt and Memgpt-autogen packages are not installed for this projects in a conda env.
# To access the trained agent, install pymemgpt, run memgpt folder and replace this directory with that of the .memgpt directory
# in the assets folder.
# Agent should be functional after replacing the db file but replace everthing if not.