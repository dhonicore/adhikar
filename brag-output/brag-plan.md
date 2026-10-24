# Brag Plan: Adhikar

## What is this app?
Adhikar is a Fetch.ai multi-agent scholarship appeal system that turns a wrongful rejection into a filed, trackable appeal inside ASI:One — complete with legal analysis, PDF generation, and direct email to the Nodal Officer.

## The angle
Most scholarship portals in India have a "reject" button but no "appeal" button. Adhikar closes that gap with an autonomous agent team that doesn't just chat — it reads the rules, checks the law, drafts the paperwork, and sends it. The twist: if the rejection is legally correct, it refuses to file a false appeal.

## Hook (first 2-3 seconds)
A phone screen flashes: "Scholarship Rejected: Income Certificate Invalid." Red alert. No appeal button. The viewer feels the dead end before the solution appears.

## Key moments (the middle)
- ASI:One chat with Adhikar's intake form card — the entry point is a conversational form, not a government website.
- Four terminal panes light up in sequence: Backend (:9000), Analyst (:8002), Drafter (:8003), Intake Agent (:8001) — the hybrid architecture made visible.
- Gmail inbox: the appeal email arrives with a PDF attachment; cut back to the reference card `SCHLR/E/2026/1234`.
- Red honesty card: "❌ I cannot file an appeal" — Adhikar refuses false appeals.

## Outro / punchline
"Adhikar. Built for Fetch-A-Thon 3.0." — logo lockup, clear and confident.

## User flow worth showing
Entry: student receives rejection SMS → opens ASI:One chat → fills the intake form.  
Action: Intake agent routes to Analyst, Analyst checks rules/precedents, Drafter generates PDF and emails it.  
Result: student sees the filed-appeal card with Reference ID and SLA timer.

## Tone
- Preset: cinematic
- Creative direction: urgent, empathetic, and legally authoritative
- Interpretation: fast cuts and big type for urgency, a steady confident voice for legal authority, and one humanizing pause on the student's dead-end moment before the solution sweeps in.

## Format: landscape — 1920x1080
## Duration: 25s

## Visual identity (from the project)
- Background: `#0B0F19` (deep navy/slate — authority and night-work urgency)
- Accent: `#F59E0B` (amber/gold — justice, urgency, India government warmth)
- Text: `#F8FAFC` (off-white — readability on dark)
- Error/red: `#EF4444` (rejection, honesty refusal)
- Success/green: `#22C55E` (appeal approved, email sent)
- Display font: "Inter" or "Space Grotesk" — bold, legal-doc confident
- Body font: "Inter" — clean, government-accessible
- Strongest visual element: the ASI:One card UI defined in `agents/intake/cards.py` (intake form, detail cards with summary_rows and CTAs)

## Share copy (draft)
"Scholarship rejected with no appeal button? Adhikar's agent team reads the rules, drafts the PDF, and emails the Nodal Officer — all inside ASI:One. And it refuses to file a false appeal. Built for Fetch-A-Thon 3.0."

## Audio direction
- Role: dense rhythmic layer / cinematic support — driving but not chaotic
- Music: `happy-beats-business-moves-vol-1-by-ende-dot-app.mp3` (120 BPM, strong back-half cues)
- Music treatment: start on the first downbeat after the hook reveal; keep the bed up and energetic; duck under voiceover to ~0.12-0.15; let the final logo land on a strong cue.
- Music cue guidance: read from bundled preset `happy-beats-business-moves-vol-1-by-ende-dot-app.music-cues.json`. Target strong cues near 17.02s, 17.52s, 18.52s, 20.02s for the email/reveal/honesty-card sequence; target 23.02s/23.52s for the final logo. Beat grid available from 3.02s onward for terminal-pane arrivals and card sequences.
- Audio-reactive treatment: subtle; use bass/RMS to pulse the accent glow on active cards and terminal cursors, never waveform bars or heavy strobing.
- SFX posture: moderate and motion-matched — alert tone for the rejection SMS, soft key ticks for terminal text, paper/whoosh for PDF reveal, send swoosh for email, firm thud for logo land.
- Audio-coupled moments:
  - Rejection SMS alert lands with a short digital chime.
  - Terminal panes light up on consecutive beats.
  - Reference ID card pops on a strong cue.
  - Final logo locks to the last strong cue.
- Restraint rule: music must not fight the voiceover; no busy SFX during narration; silence the music bed cleanly at 25s.

## Storyboard

### Scene 1 — The Problem — 0.0-4.5s
A smartphone notification card slides in from the top: red header, white text reading "Scholarship Rejected: Income Certificate Invalid." Below it, a small label: "No appeal button on the portal." Background is dark. A subtle red pulse on the card.  
Sequential/interaction: yes — notification slides in, then the "No appeal button" label fades in below it.  
Audio intent: alert chime + low drone; music bed enters with tension.  
Audio-coupled idea: alert sound on notification arrival.  
Music: tense bed building.  
Transition mood: hard cut → Scene 2.

### Scene 2 — Meet Adhikar — 4.5-9.0s
Clean ASI:One chat interface. The Adhikar intake form card appears in the chat stream. Title: "Tell me about your scholarship rejection." Fields visible: Scheme, Status, Stated reason, Certificate issue date, Issuing authority, Annual family income, Income proof type. A "Check my case" CTA button at the bottom. A text bubble above reads "I can help you appeal this. First, a few details:".  
Sequential/interaction: yes — form card scales up into view; fields appear in quick sequence; CTA button pulses subtly.  
Audio intent: music lifts from tension to hope/solution.  
Audio-coupled idea: card arrival on beat; soft UI click on CTA highlight.  
Music: bed opens up, brighter.  
Transition mood: clean wipe → Scene 3.

### Scene 3 — The Hybrid Architecture — 9.0-13.5s
Four terminal panes arranged in a 2x2 grid on a dark background. Labels: Backend :9000, Analyst :8002, Drafter :8003, Intake Agent :8001. Each pane lights up in sequence with green status indicators and scrolling boot logs. Arrows or connection lines draw between them to show the flow.  
Sequential/interaction: yes — panes light up one by one (Intake → Analyst → Drafter → Backend); connection lines animate after all four are live.  
Audio intent: driving tech rhythm; each pane gets a short power-up tone.  
Audio-coupled idea: pane arrivals snapped to consecutive beat-grid points.  
Music: full energy, tech pulse.  
Transition mood: hard cut → Scene 4.

### Scene 4 — Real Action — 13.5-18.5s
Cut to a Gmail inbox mockup. A new email arrives at the top: "Scholarship Appeal - Case ADH-123456" with a PDF attachment icon. It slides in. Quick cut back to the ASI:One chat showing the filed-appeal detail card: title "✅ Appeal Filed Successfully", summary rows Reference ID `SCHLR/E/2026/1234`, SLA Deadline "7 days", Assigned To "District Scholarship Officer".  
Sequential/interaction: yes — email slides in, attachment icon bounces, cut to chat card, card scales up, Reference ID highlights.  
Audio intent: triumphant reveal; send swoosh on email, bright chime on Reference ID.  
Audio-coupled idea: Reference ID reveal locked to a strong cue (~17-18s).  
Music: peak energy.  
Transition mood: dramatic wipe → Scene 5.

### Scene 5 — The Honesty Mechanic — 18.5-22.5s
A red detail card centered on screen: "❌ I cannot file an appeal". Below: summary rows — Outcome: No Grounds, Grounds: None, Citations: None. A subtitle: "The rejection appears correct." This contrasts the previous success card.  
Sequential/interaction: yes — card flips from green side to red side, or red card scales in with a firm thud.  
Audio intent: shift to serious/authoritative; lower register thud.  
Audio-coupled idea: red card lands on a strong beat.  
Music: bed pulls back slightly for the voiceover emphasis.  
Transition mood: clean cut → Outro.

### Outro — Built for Fetch-A-Thon 3.0 — 22.5-25.0s
Dark background. "ADHIKAR" in large display type, with a small tagline "AI Advocate for Students" and below it "Built for Fetch-A-Thon 3.0". Accent glow behind the logo.  
Sequential/interaction: logo scales in, tagline fades in, event line types out.  
Audio intent: final logo hit; music fades out.  
Audio-coupled idea: logo lands on the final strong cue (~23.5s).  
Music: resolves and fades.  
Transition mood: end card.

## Voiceover script

| Time | Line |
|------|------|
| 0.0-4.5s | "In India, millions of students are wrongfully denied scholarships due to clerical errors. The government portal has no appeal button. Most students simply give up." |
| 4.5-9.0s | "Meet Adhikar. An autonomous multi-agent team that turns a wrongful rejection into a filed, trackable appeal — all inside ASI:One." |
| 9.0-13.5s | "We built a hybrid architecture. The Intake agent handles the chat. Local FastAPI servers handle the deterministic legal rules and the real-world action, guaranteeing one hundred percent execution reliability." |
| 13.5-18.5s | "The Drafter generates a PDF and emails it directly to the Nodal Officer. The student gets a trackable Reference ID and an SLA timer." |
| 18.5-22.5s | "And if the denial was legally correct? Adhikar refuses to file a false appeal. It doesn't just discover schemes — it enforces your rights." |
| 22.5-25.0s | "Adhikar. Built for Fetch-A-Thon 3.0." |

**Music mood for this video:** driving tech/cinematic bed with urgency.  
**Audio summary:** A 120 BPM electronic bed starts tense under the rejection hook, lifts into solution energy for the chat and architecture scenes, peaks on the email/Reference ID reveal, pulls back for the honesty mechanic, and resolves with a clean logo hit.
