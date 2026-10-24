# adhikar-agents

A Fetch.ai multi-agent project: several **independent** agents, each an expert at
one task. There is **no orchestrator** — every agent speaks the Agent Chat
Protocol and registers on Agentverse, and **ASI:One discovers and routes** each
request to the right agent. Generated with
[create-fetch-agent](https://github.com/anishkancherla-fetchai/create-fetch-agent).

## How routing works

```
                 user request
                      │
                      ▼
                  ASI:One   ──discovers + ranks agents on Agentverse──►
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   intake
   analyst
   drafter
   tracker
```

ASI:One's agentic model searches the Agentverse marketplace and picks the agent
whose description best matches the request. So each agent's **description and
Agentverse profile (README + keywords) is what makes routing work** — fill in the
`AGENT_DESCRIPTION` in each agent file with a specific, one-line summary of what
that agent does.

## Agents

| Agent | Port | File | Run |
| ----- | ---- | ---- | --- |
| intake | 8001 | `agents/intake/intake_agent.py` | `make intake` |
| analyst | 8002 | `agents/analyst/analyst_agent.py` | `make analyst` |
| drafter | 8003 | `agents/drafter/drafter_agent.py` | `make drafter` |
| tracker | 8004 | `agents/tracker/tracker_agent.py` | `make tracker` |

## Setup

Seeds are already generated for you in `.env`. Install dependencies:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

Each agent runs in its own terminal:

```bash
make intake
```

```bash
make analyst
```

```bash
make drafter
```

```bash
make tracker
```

## Where to add your logic

Each agent has a `<name>_workflow(query)` function — the single extension point.
Read the query, do the one thing that agent is an expert at, return a response.
For example, in `agents/intake/intake_agent.py`:

```python
def intake_workflow(query: str) -> str:
    return my_llm_or_rag_call(query)
```

## Talk to it on ASI:One

Every agent sets `mailbox=True` and `publish_agent_details=True`, so connect each
one through its Agentverse inspector URL (logged on startup) and give it a clear
description. Then chat on [ASI:One](https://asi1.ai) — its agentic model routes
your request to whichever agent fits. See the "Register on Agentverse" output
from the scaffolder, or the [Agentverse docs](https://agentverse.ai).

> **The chat protocol is already wired** in every agent (`agent.include(chat_proto,
> publish_manifest=True)`). This is what makes each agent chattable + discoverable
> — the #1 thing builders forget. You'll see `Manifest published successfully:
> AgentChatProtocol` in each agent's startup logs, and Agentverse's "Add Chat
> Protocol" checklist item is already satisfied. Connecting a mailbox alone is
> **not** enough; don't remove the `publish_manifest=True` line.
