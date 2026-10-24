# Each target runs one agent in the foreground. Open a separate terminal per
# agent. Every agent is independent (no central router) and ASI:One discovers and
# routes to the right one based on its Agentverse description.
#
#   make <agent>

.PHONY: intake analyst drafter tracker

intake:
	.venv/bin/python -m agents.intake.intake_agent

analyst:
	.venv/bin/python -m agents.analyst.analyst_agent

drafter:
	.venv/bin/python -m agents.drafter.drafter_agent

tracker:
	.venv/bin/python -m agents.tracker.tracker_agent
