# Adhikar Terminal Demo
# Render with: vhs demo.brag
# Output: demo.mp4

Output demo.mp4

# Terminal styling — cinematic, readable, dark
Set FontSize 22
Set FontFamily "JetBrains Mono"
Set Width 1600
Set Height 900
Set Padding 20
Set Margin 0
Set BorderRadius 0
Set Theme "Catppuccin Mocha"
Set TypingSpeed 5ms
Set CursorBlink true

# ------------------------------------------------------------------
# Scene 1: Title card
# ------------------------------------------------------------------
Type "clear"
Enter
Sleep 500ms

Type "echo -e '\033[1;36m'
Enter
Type "echo '    ___    __  __    ___   ____    __    ___   ____'"
Enter
Type "echo '   /   |  / / / /   /   | / __ \  / /   /   | / __ \'"
Enter
Type "echo '  / /| | / /_/ /   / /| |/ / / / / /   / /| |/ / / /'"
Enter
Type "echo ' / ___ |/ __  /   / ___ / /_/ / / /___/ ___ / /_/ / '"
Enter
Type "echo '/_/  |_/_/ /_/   /_/  |_\____/ /_____/_/  |_\____/  '"
Enter
Type "echo -e '\033[0m\033[1;32m        AI ADVOCATE FOR STUDENTS\033[0m'"
Enter
Sleep 1000ms

# ------------------------------------------------------------------
# Scene 2: Spin up the four local servers
# ------------------------------------------------------------------
Type "clear"
Enter
Sleep 100ms

Type "echo -e '\033[1;34m[ADHIKAR]\033[0m Booting multi-agent architecture...'"
Enter
Sleep 100ms

Type "echo -e '\033[1;33m  →\033[0m Starting Backend      on \033[1;36m:9000\033[0m'"
Enter
Sleep 100ms
Type "echo -e '\033[90m        python -m backend.app --port 9000\033[0m'"
Enter
Sleep 100ms
Type "echo -e '\033[1;32m        ✓ Backend online      (port 9000)\033[0m'"
Enter
Sleep 100ms

Type "echo -e '\033[1;33m  →\033[0m Starting Intake Agent on \033[1;36m:8001\033[0m'"
Enter
Sleep 100ms
Type "echo -e '\033[90m        make intake\033[0m'"
Enter
Sleep 100ms
Type "echo -e '\033[1;32m        ✓ Intake Agent online (port 8001)\033[0m'"
Enter
Sleep 100ms

Type "echo -e '\033[1;33m  →\033[0m Starting Analyst      on \033[1;36m:8002\033[0m'"
Enter
Sleep 100ms
Type "echo -e '\033[90m        make analyst\033[0m'"
Enter
Sleep 100ms
Type "echo -e '\033[1;32m        ✓ Analyst online      (port 8002)\033[0m'"
Enter
Sleep 100ms

Type "echo -e '\033[1;33m  →\033[0m Starting Drafter      on \033[1;36m:8003\033[0m'"
Enter
Sleep 100ms
Type "echo -e '\033[90m        make drafter\033[0m'"
Enter
Sleep 100ms
Type "echo -e '\033[1;32m        ✓ Drafter online      (port 8003)\033[0m'"
Enter
Sleep 100ms

Type "echo -e '\033[1;32m  ✓ All four services are online\033[0m'"
Enter
Sleep 600ms

# ------------------------------------------------------------------
# Scene 3: User submits a scholarship appeal in ASI:One chat
# ------------------------------------------------------------------
Type "clear"
Enter
Sleep 100ms

Type "echo -e '\033[1;35m╔══════════════════════════════════════════════════════════════╗\033[0m'"
Enter
Type "echo -e '\033[1;35m║\033[0m  \033[1;36mASI:One\033[0m — Chat with Adhikar                            \033[1;35m║\033[0m'"
Enter
Type "echo -e '\033[1;35m╚══════════════════════════════════════════════════════════════╝\033[0m'"
Enter
Sleep 500ms

Type "echo -e '\033[1;34mAdhikar:\033[0m Hi! I can help you appeal a scholarship decision. Please describe your situation.'"
Enter
Sleep 100ms

Type "echo -e '\033[1;33mUser:\033[0m My scholarship was discontinued even though my family income dropped after my father lost his job. Can you help me appeal?'"
Enter
Sleep 100ms

Type "echo -e '\033[1;34mAdhikar:\033[0m I understand. I will route this to the intake agent and draft a formal appeal. One moment...'"
Enter
Sleep 500ms

# ------------------------------------------------------------------
# Scene 4: Logs cascade through the agents
# ------------------------------------------------------------------
Type "clear"
Enter
Sleep 100ms

Type "echo -e '\033[1;34m[ADHIKAR ORCHESTRATOR]\033[0m Received appeal request'"
Enter
Sleep 600ms

Type "echo -e '\033[90m'$(date +%H:%M:%S)'\033[0m \033[1;33m[intake]\033[0m Parsing student grievance...'"
Enter
Sleep 100ms

Type "echo -e '\033[90m'$(date +%H:%M:%S)'\033[0m \033[1;33m[intake]\033[0m Identified category: \033[1;36mSCHOLARSHIP DISCONTINUATION\033[0m'"
Enter
Sleep 100ms

Type "echo -e '\033[90m'$(date +%H:%M:%S)'\033[0m \033[1;33m[intake]\033[0m Routing to analyst for legal review'"
Enter
Sleep 100ms

Type "echo -e '\033[90m'$(date +%H:%M:%S)'\033[0m \033[1;36m[analyst]\033[0m Querying case law & policy corpus...'"
Enter
Sleep 500ms

Type "echo -e '\033[90m'$(date +%H:%M:%S)'\033[0m \033[1;36m[analyst]\033[0m Found precedent: change in financial circumstance'"
Enter
Sleep 500ms

Type "echo -e '\033[90m'$(date +%H:%M:%S)'\033[0m \033[1;36m[analyst]\033[0m Recommendation payload:'"
Enter
Type "printf '%b\n' '  { \x22outcome\x22: \x22\033[1;32mAPPEAL\033[0m\x22, \x22citation\x22: \x22\033[1;36mDelhi High Court\033[0m\x22 }'"
Enter
Sleep 100ms

Type "echo -e '\033[90m'$(date +%H:%M:%S)'\033[0m \033[1;33m[intake]\033[0m Outcome is APPEAL — invoking drafter'"
Enter
Sleep 600ms

Type "echo -e '\033[90m'$(date +%H:%M:%S)'\033[0m \033[1;35m[drafter]\033[0m Generating formal appeal PDF...'"
Enter
Sleep 700ms

Type "echo -e '\033[90m'$(date +%H:%M:%S)'\033[0m \033[1;35m[drafter]\033[0m Attached: income_proof.pdf, previous_scholarship_letter.pdf'"
Enter
Sleep 500ms

Type "echo -e '\033[90m'$(date +%H:%M:%S)'\033[0m \033[1;35m[drafter]\033[0m \033[1;32m✅ Email Sent to Nodal Officer\033[0m'"
Enter
Sleep 500ms

# ------------------------------------------------------------------
# Scene 5: Final reference ID
# ------------------------------------------------------------------
Type "clear"
Enter
Sleep 100ms

Type "echo -e '\033[1;32m✅ Appeal submitted successfully.\033[0m'"
Enter
Sleep 500ms

Type "echo -e '\033[1;34mReference ID:\033[0m'"
Enter
Sleep 100ms

Type "echo -e '\033[1;37;44m  SCHLR/E/2026/1234  \033[0m'"
Enter
Sleep 1000ms

# ------------------------------------------------------------------
# Scene 6: Outro
# ------------------------------------------------------------------
Type "clear"
Enter
Sleep 100ms

Type "echo -e '\033[1;36mADHIKAR\033[0m'"
Enter
Type "echo -e '\033[1;32mAI Advocate for Students\033[0m'"
Enter
Sleep 600ms

Type "echo -e '\033[1;33mBuilt for Fetch-A-Thon 3.0\033[0m'"
Enter
Sleep 1200ms
