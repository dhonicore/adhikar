# Hyperframes Composition Brief: Adhikar

## Objective
Create a 25-second cinematic launch video for Adhikar that communicates the problem (wrongful scholarship rejections with no appeal path), the solution (a multi-agent appeal system inside ASI:One), the hybrid architecture, real-world action (PDF + email + Reference ID), and the honesty mechanic (refusing false appeals). Voiceover is required.

## Output
- Composition directory: `brag-output/composition/`
- Rendered video: `brag-output/brag.mp4`
- Format: landscape — 1920x1080
- Duration: 25 seconds

## Source Material
- Project root: `/home/dhon1/adhikar/adhikar-agents`
- Primary files read:
  - `README.md` — project overview, agent table, ASI:One routing
  - `agents/intake/intake_agent.py` — chat flow, analyst/drafter routing, cards
  - `agents/intake/cards.py` — intake form and card payload structure
  - `agents/analyst/analyst_agent.py` — FastAPI analyst proxy
  - `agents/drafter/drafter_agent.py` — PDF generation and email sending
  - `backend/gateway.py` — legal rule engine and reference ID generation
  - `backend/rules.json` — NSP Pre-Matric rules and Delhi High Court precedent
- Product name: Adhikar
- Tagline / strongest claim: "AI Advocate for Students"
- Key UI or visual moment to recreate:
  - ASI:One chat with the intake form card (fields: Scheme, Status, Stated reason, Certificate issue date, Issuing authority, Annual family income, Income proof type)
  - Four terminal panes for Backend :9000, Analyst :8002, Drafter :8003, Intake Agent :8001
  - Gmail-style inbox with appeal email + PDF attachment
  - Filed-appeal detail card showing Reference ID `SCHLR/E/2026/1234`
  - Red honesty card "❌ I cannot file an appeal"
- Copy that must appear verbatim:
  - "Scholarship Rejected: Income Certificate Invalid"
  - "No appeal button on the portal"
  - "Tell me about your scholarship rejection"
  - "Check my case"
  - "Backend :9000", "Analyst :8002", "Drafter :8003", "Intake Agent :8001"
  - "Scholarship Appeal - Case ADH-123456"
  - "✅ Appeal Filed Successfully"
  - "Reference ID: SCHLR/E/2026/1234"
  - "SLA Deadline: 7 days"
  - "❌ I cannot file an appeal"
  - "Adhikar. Built for Fetch-A-Thon 3.0."

## Creative Direction
- Tone preset: cinematic
- Creative direction: urgent, empathetic, and legally authoritative
- Interpretation: The edit should feel like a fast-paced advocacy trailer — quick cuts and urgent motion in the first half, then steady confident reveals in the second half. Big type, high contrast, and a single humanizing pause on the rejection moment before the solution arrives. Avoid comedy; keep it serious and empowering.
- Hook: A flashing rejection SMS with no appeal path.
- Outro / punchline: "Adhikar. Built for Fetch-A-Thon 3.0."
- Avoid:
  - Generic SaaS language like "streamline workflow" or "unlock potential"
  - Abstract motion graphics not tied to the product
  - Unrelated visual redesign — stay close to the dark terminal + chat card aesthetic of the actual code
  - Making the red honesty card feel punitive; it should feel like a feature of integrity

## Visual Identity
- Background: `#0B0F19`
- Text: `#F8FAFC`
- Accent: `#F59E0B` (amber/gold for urgency and justice)
- Success: `#22C55E`
- Error/refusal: `#EF4444`
- Display font: "Space Grotesk" or "Inter" — bold, confident
- Body font: "Inter" — clean, readable
- Visual references from the project:
  - ASI:One card protocol: detail cards with `title`, `summary_rows` (label/value pairs), and `ctas`
  - Intake form fields from `agents/intake/cards.py`
  - Terminal/server aesthetic from `Makefile` and local FastAPI services
  - Reference ID format from `backend/gateway.py`: `SCHLR/E/{year}/{4-digit}`

## Storyboard
Use the storyboard in `brag-output/brag-plan.md` as the creative contract.

Scene summary:
1. The Problem (0.0-4.5s) — rejection SMS alert, "No appeal button" label
2. Meet Adhikar (4.5-9.0s) — ASI:One chat with intake form card
3. The Hybrid Architecture (9.0-13.5s) — four terminal panes light up in sequence
4. Real Action (13.5-18.5s) — Gmail appeal email arrives with PDF, cut to Reference ID card
5. The Honesty Mechanic (18.5-22.5s) — red "❌ I cannot file an appeal" card
6. Outro (22.5-25.0s) — "Adhikar. Built for Fetch-A-Thon 3.0."

## Audio
- Audio role: dense rhythmic layer / cinematic support — driving tech bed with urgency
- Music: `happy-beats-business-moves-vol-1-by-ende-dot-app.mp3` (120 BPM, energetic, strong back-half cues)
- Music treatment: start the bed under the rejection hook; lift into solution energy at Scene 2; keep it driving through the architecture and action scenes; pull back slightly for the honesty mechanic; resolve and fade on the final logo. Duck music under voiceover to 0.12-0.15.
- Music cue guidance: bundled preset at `<skill-dir>/assets/music/cues/happy-beats-business-moves-vol-1-by-ende-dot-app.music-cues.json`. Target strong cues near 17.02s, 17.52s, 18.52s, 20.02s for the email/Reference ID reveal sequence; target 23.02s/23.52s for the final logo. Use the beat grid from 3.02s onward for sequential terminal-pane arrivals and card reveals.
- Audio-reactive treatment: subtle; use bass/RMS to pulse the amber accent glow behind active cards and terminal cursors. No waveform/equalizer visuals, no heavy pulsing, no strobe.
- Audio-coupled moments:
  - Scene 1: alert chime on rejection SMS arrival
  - Scene 2: card arrival sound on intake form pop-in; UI click on CTA highlight
  - Scene 3: terminal panes light up on consecutive beats; connection lines draw after all four are live
  - Scene 4: send swoosh on email arrival; bright success chime on Reference ID reveal
  - Scene 5: firm low thud as red honesty card lands
  - Outro: deep bell/logo hit on final wordmark lockup
- SFX selection guidance: cinematic tone = 2-3 big moments. Use `impact/impactBell_heavy_000` or `_004` for the Reference ID and logo, `impact/impactSoft_medium_*` for card reveals, `interface/bong_001` sparingly for dramatic emphasis. For typing/terminal text, use `keyboard/keypress-*.wav` randomized very quietly if visible typing is animated.
- SFX analysis guidance: `sfx-analysis.md` in `<skill-dir>/assets/sfx/`. Prefer low/medium HF-risk files for repeated or polished moments.
- Exact SFX choice: Hyperframes should choose filenames, timestamps, density, and volume based on the implemented animation.
- Audio files: copy the chosen music and any Hyperframes-selected SFX into `brag-output/composition/assets/`

## Voiceover
Enabled. Generate via Kokoro through Hyperframes.

Script file: `brag-output/brag-plan.md` — Voiceover script section.

Voice characteristics: clear, confident, legally authoritative but empathetic. Pace must fit the 25-second runtime. Duck music to 0.12-0.15 during voiceover.

## Hyperframes Instructions
Load the Hyperframes domain skills — `hyperframes-core` (composition contract + `data-*` timing), `hyperframes-animation` (motion), `hyperframes-creative` (design spec, beats, audio-reactive), `hyperframes-keyframes` (seek-safe keyframes), and `hyperframes-cli` (lint/check/render). /brag is its own workflow — do not enter the `hyperframes` entry-point intent interview and do not route into its generic promo / launch-video workflow. Prefer native Hyperframes conventions over anything in `/brag`.

Requirements:
- Show at least one real UI, copy, or visual element from the source project (the intake form card, terminal pane labels, and Reference ID are all grounded in the code).
- Keep all text readable in the final render.
- Keep the video within 25 seconds.
- Include the planned music/SFX layer.
- Treat `/brag` audio notes as guidance, not a fixed cue sheet. Choose SFX after the visual animation exists.
- Treat music cue metadata as optional timing hints. Hyperframes decides exact animation timing and should ignore cues that hurt readability, scene pacing, or the product story.
- Major reveals may move toward nearby strong cues within about 0.15s. Smaller entrances may align to nearby beat points within about 0.10s.
- Use SFX to support motion and interaction: bell for major payoffs, soft thud for card reveals, send swoosh for email, alert chime for SMS.
- Honor planned music treatment: duck under voiceover, fade out cleanly at 25s.
- Use local assets for audio and any required runtime/media dependencies.
- Run `hyperframes check` before render — it is brag's single gate.
- Keep creation and rendering local.

## Deliverables checklist
- [ ] `brag-output/brag-plan.md` exists with full storyboard and voiceover script
- [ ] `brag-output/composition-brief.md` exists (this file)
- [ ] Music file copied to `brag-output/composition/assets/music/`
- [ ] SFX files copied to `brag-output/composition/assets/sfx/`
- [ ] Voiceover generated and wired into composition
- [ ] `hyperframes check` passes
- [ ] `brag-output/brag.mp4` rendered
- [ ] Best poster frame picked and baked as frame 0
- [ ] `brag-output/share-copy.txt` written
