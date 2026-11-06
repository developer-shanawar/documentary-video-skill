# Video Editing Guide — Documentary Video Skill

This is the editing job, step by step. The editor follows this after the script and storyboard are done. One row of the storyboard = one 10-second edit.

## The edit in one line

Every 10 seconds: a new visual that matches the voice, something moving, at most one small text — then cut.

## 1. Timeline setup

- Project: horizontal 16:9, 1280x720 minimum, for long videos. Vertical 9:16 only for Shorts.
- Build in 1-minute parts, then combine the parts at the end. No part labels on screen.
- Audio track 1: voiceover only (Young 3, speed 100, Roman Urdu). No music, no SFX unless the user explicitly asks.
- Cut dead air longer than 1–2 seconds between voiceover lines. Narration must fill each segment — no padded silence.

## 2. Per-segment edit (repeat for every 10 seconds)

For each segment, check in this order:

| Check | Rule |
| --- | --- |
| Visual | Does it show exactly what the voice says right now? If not, replace it. |
| Motion | Is something moving — host walking, water flowing, people moving, camera panning? If nothing moves, add a slow zoom or pan, or replace the clip. |
| First 10s | Segment 1 must be animation, never a still real photo. |
| Cutaway | For ruins, maps, tools, or diagrams, cut to a full-screen cutaway / B-roll instead of holding on the host. |
| Zoom / pan | Slow zoom-in on the important point (diagram: 100% → ~108%). Slow pan across a map. Never a sudden jump cut in the middle of a sentence. |
| Camera angle | Change angle every 8–10 seconds: Wide → Medium close-up → Over-the-shoulder. |
| Text | Date pill top-right for the beat, OR name card bottom-left for 2 seconds (t=1–3s) — never both in the same row, never a top bar, never a solid box behind text. One small text per beat, white with black outline, fade in/out ~0.8s. |
| Host | Silent, mouth closed, hands down, no waving, no pointing. Subtle walking / head turn only. |

## 3. Cutaways — when to cut away from the host

Cut away (full screen, no host) when the voice mentions:

- A ruin, a place, or a map — show the ruin / map, with slow zoom/pan.
- A tool, a seal, a brick, a diagram — show it large, main part highlighted with arrows.
- A number — show it in 3 pictures across the video (diagram, map, real image), same value each time.
- A document — show the document, highlight 3–4 key lines only.

Cut back to the host only for the Hook Question, the Document Explainer, and the Payoff/Lesson.

## 4. Zoom and pan — how much

- Diagram zoom: 100% → ~108%, slow, inside a framed dark-teal border. Whole image stays in frame.
- Real image zoom/pan: slight only, real colours unchanged, only zoom/crop. A real image with no motion is a frozen still — never export that.
- Timeline year badge: small lower-left, about 1/6 of the frame, clear in the first 3 seconds and spoken in the voiceover.

## 5. Text timing

- Date pill: appears with the beat, top-right, small rounded pill, stays for the beat.
- Name card: appears at t=1s, disappears at t=3s, bottom-left corner (x=40, y=H-90). Never in the middle of the screen — it used to cover the main visual there.
- Never put date and name in the same row. Never use generic titles (THE QUESTION, THE FIRST NAME, THE NAME, THE NUMBER, WHO SURVIVED, THE OPEN QUESTION).
- Text is added in the edit, never baked into the generated clip. If a clip already has baked-in text or a fake watermark, reject it and regenerate it clean.

## 6. Audio edit

- Voiceover only by default. No background music, no scene SFX.
- If the user explicitly asks for music/SFX: light SFX only on a graphic/text reveal or a screen change, BGM balanced to the mood. Licence-check every sound before monetised/commercial use.
- Audio fade: soft 0.5s fade-in on the first beat only. No other fades unless a scene genuinely ends.

## 7. Editing checklist — check before export

- [ ] Every 10-second segment has continuous motion — no frozen/stuck segment
- [ ] First 10 seconds are animation
- [ ] Every visual matches its voice line exactly
- [ ] Camera angle changes every 8–10 seconds
- [ ] Cutaways used for ruins, maps, tools, diagrams — not the host standing still
- [ ] Date pill top-right, name card bottom-left for 2 seconds only, never a top bar or solid box
- [ ] Host silent, mouth closed, hands down, no pointing
- [ ] No dead air over 1–2 seconds, no silent gaps
- [ ] Old topics look old throughout — no modern buildings, clothes, or objects in an old scene
- [ ] Real images labelled as real, reconstructions labelled as reconstructions, present-day photos never presented as ancient footage
- [ ] No invented numbers, dates, or quotes; interpretation labelled as interpretation
- [ ] No part labels on screen, no repeated "agle part mein" promise
- [ ] Thumbnail, title, and description checked against `templates/thumbnail-title-checklist.md`
