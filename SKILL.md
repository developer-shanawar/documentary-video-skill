---
name: documentary-video
description: Make a full original documentary video in the locked 2D sticky-man explorer style — write the whole script and give a complete video editing guide. Use when the user asks for a documentary video, a history/mystery/science explainer video, a full video script, or a video editing guide with 10-second segments, visuals, motion, cuts, and on-screen text. Covers topic and angle, fact-checking, full script writing (hook, evidence, payoff), 10-second storyboard segments, image/diagram prompts, voiceover, editing guide and checklist, thumbnail, title, and SEO.
---

# Documentary Video Skill

Make a full original documentary video — history, mystery, science, or a place — with a clear host, real evidence, and visuals that match the narration beat by beat.

This skill is NOT only planning. It is a full video-making helper. It does two jobs:

1. **Script writing** — give it a topic and it writes the full script: hook, evidence, payoff, in beats, with voiceover lines ready to record.
2. **Video editing guide** — it tells the editor exactly what to do in every 10-second segment: what visual, what motion, what on-screen text, where to cut away, where to zoom/pan, and an editing checklist to check before export.

This skill needs NO API key. It is only instructions. An AI that reads it understands what to make and works in that style. An API is only needed if the user themself wants to use a separate video-generation tool's API to generate clips — that is optional, and this skill works without it.

This skill is for one video at a time. Do not copy another creator's footage or script. Use techniques, never copied lines.

## Try it

After adding this skill, write:

> Use the documentary-video skill, make a 5-minute documentary plan on [topic]

The AI must return, in this order:

1. Angle in one sentence
2. Full script — 5 parts, 6 beats per part, each beat ~10 seconds with a voiceover line in Roman Urdu
3. Storyboard table — time, voice line, visual, motion, on-screen text for every beat
4. Image/diagram prompts — one per beat, no repeats
5. Voiceover script — clean lines with timecodes, ready to record
6. Editing guide — per segment: cut, cutaway, zoom/pan, text timing, and the editing checklist from `references/editing-guide.md`
7. Thumbnail + title + SEO — title, 3–4 word thumbnail text, description with timestamps, tags within 500 characters

For a 1-minute video, return the same output with 1 part / 6 beats. For an 8-minute video, 8 parts / 48 beats. Always work in 1-minute parts, then combine.

## The locked style — follow it every time

### Host

- Sticky-man explorer v2: large round white head, dot eyes/nose, smile + eyebrows only, NO ears/hair, khaki cap, teal vest, brown backpack, khaki cargo pants, brown boots.
- Setting: warm studio / his own room with a board, deep teal + warm amber, clean 2D style.
- Host roles only: Hook Question, Document Explainer, History Viewer (host in foreground, NOT inserted into history), Map/Measurement/Flow split, Payoff/Lesson.
- Host is silent in the visuals: mouth closed, no talking on screen. Narration is background voiceover only.
- Host movement: subtle walking, head turn, gentle body motion. Hands DOWN — no waving, no pointing, no gesturing.

### Visuals

- 2D animation matching the host's cartoon style. NOT photorealistic workers or realistic people footage for village/people scenes.
- First 10 seconds must be ANIMATION. Later, mix animation with real images/video — but only with visible zoom/pan motion.
- Real images: public-domain / freely licensed only. Label them as real. Never present a real present-day photo as ancient footage. Never present a reconstruction as a real photo.
- Old topics must look OLD throughout: old houses, old drains, old tools — not modern versions.
- Every 10-second segment must have continuous MOTION: walking, flowing water, moving people, camera movement. No frozen/stuck segment. No element fully frozen for more than 4–5 seconds.
- Camera variety: change angle every 8–10 seconds (Wide → Medium close-up → Over-the-shoulder). Subtle slow zoom-in/pan on important points. Full-screen cutaways / B-roll for ruins, maps, tools, diagrams instead of the character standing still.

### Scene–voice matching

- Every visual must match exactly what the voiceover is saying at that moment. If the voice says "drain under the house", show a drain under an old house, not a street.
- No silent gaps. Narration fills each segment. Trim dead air longer than 1–2 seconds between voiceover lines.
- End a beat on a question when it is a part of a longer video — but do NOT repeat "agle part mein samjhenge / agle minute mein dekhenge" in every part.

### On-screen text system (locked)

- DATE: small, TOP-RIGHT corner, inside a small ROUNDED PILL (dark rounded bar, animated fade), stays for the beat.
- NAME: small ROUNDED CARD, BOTTOM-LEFT corner (x=40, y=H-90), only 2 seconds (t=1–3s), then gone.
- Date and name are NEVER in the same row.
- No top bar. No solid box behind any text. No generic titles like THE QUESTION / THE FIRST NAME / THE NAME / THE NUMBER / WHO SURVIVED / THE OPEN QUESTION.
- One small text per beat, white with black outline, fade in/out ~0.8s, different position each beat.
- No part labels on screen: no "Part 1 / Part 2" for viewers. Segments must flow into each other.

### Audio

- Voiceover ONLY by default. Young 3, speed 100, Roman Urdu + balanced technical English words.
- NO music, NO SFX unless the user explicitly asks for them. If they do, follow `references/sound-design.md`: one clean whoosh on a part change, one soft pop on a text reveal, BGM balanced under the voiceover, and licence-check every sound before monetised/commercial use.
- Openings: relaxed, curious questions. NOT shouting hooks.
- Full video is built in 1-minute parts, then combined at the end. Ratio: horizontal 16:9 for long videos, vertical 9:16 only for Shorts.

### Structure and honesty

- Structure every video as: full-stack hook + evidence + diagram + real image + payoff.
- Hook: counter-claim then a question in the first 15 seconds.
- Science / evidence first, then an explicit pivot to text/interpretation if any.
- Fact vs interpretation must stay separate. Interpretation is labelled interpretation, never presented as proof. A sacred text is never claimed to name something it does not name.
- One number repeated in 3 pictures where it helps (for example a measurement shown as a diagram, a map, and a real image).
- Word-to-picture matching, slow zoom + blurred foreground + one big label where useful.
- Ending: open question + personal sign-off. No hard subscribe graphic.

## Workflow — 8 steps

### 1. Topic + angle

Ask or confirm: topic, length (1 min / 5 min / 8 min), audience, and one angle in one sentence. Example angle: "No king, no palace, no throne — who ruled Mohenjo-daro?" — not "tell me about Mohenjo-daro."

Do not start scripting until the angle is locked. If the user gives only a topic, propose 3 angles and let them pick one.

### 2. Fact-check

Before writing a word of script, verify: dates, numbers, names, places, and what is still disputed. See `references/fact-check-checklist.md`.

- Use "lakhon log" for an uncertain population, never a fixed invented number.
- Describe decline as gradual around a date (for example around 1900 BCE), not a sudden vanishing, unless the evidence says sudden.
- Mark every claim: verified / disputed / interpretation. Keep the source note with the claim in your working notes, even if it is not shown on screen.

### 3. Full script writing

Write the FULL script, not just an outline. 6 beats per 1-minute part. Each beat is ~10 seconds of voiceover — about 25–30 words in Roman Urdu at speed 100.

Each beat needs: voiceover line, visual idea, on-screen text (date pill and/or name card), and motion note. Use `templates/script-template.md`.

Script shape per part: hook (beat 1), evidence (beats 2–4), payoff or question (beats 5–6). Full video shape: hook + evidence + diagram + real image + payoff. Tight pacing: action-first opening, visual change every beat, no boring repetition.

Write the voiceover in clean Roman Urdu, ready to record. No stage directions inside the spoken lines.

### 4. Storyboard in 10-second segments

Turn the beats into a storyboard table: time, voice line, visual, motion, text. Use `templates/storyboard-template.md` or run `scripts/make_storyboard.py` from a beats JSON file.

Check every row: does the visual show exactly what the voice says? Is something moving in every row? Is the first 10 seconds animation?

### 5. Image / diagram prompts

Write one prompt per visual, from `references/image-prompts.md`. One visual per narration beat — NO repeats.

- Diagrams: slight zoom 100% to ~108%, main part highlighted with arrows, inside a framed dark-teal border, whole image stays in frame.
- Timeline year: small lower-left badge, about 1/6 of the frame, clear in the first 3 seconds and spoken.
- Real images: only public-domain / freely licensed, whole image in frame, only zoom/crop, real colours unchanged.

### 6. Voiceover script

Deliver the final voiceover as clean Roman Urdu lines, one per beat, with timecodes. No stage directions inside the spoken lines. No "agle part mein" promise at the end of a middle part.

### 7. Video editing guide

Give a complete editing guide the editor can follow clip by clip. See `references/editing-guide.md` for the full rules. For every 10-second segment, say:

- What visual is on screen, and what it must show (scene–voice match)
- What moves (host walk, water flow, camera pan, zoom 100% → 108%)
- What on-screen text appears and when: date pill top-right for the beat, name card bottom-left (x=40, y=H-90) only 1–3s, then gone — never both in the same row, never a top bar, never a solid box
- Where to cut away: full-screen cutaway / B-roll for ruins, maps, tools, diagrams instead of holding on the host
- Where to zoom/pan: slow zoom-in on the important point, slow pan across a map or diagram, camera angle change every 8–10 seconds (Wide → Medium close-up → Over-the-shoulder)
- What to cut: dead air over 1–2 seconds, any frozen/stuck segment, any visual that does not match the voice line

End with the editing checklist: motion in every segment, first 10 seconds animation, text system correct, host silent with hands down, no invented facts, audio is voiceover only unless the user asked for music/SFX.

### 8. Thumbnail + title + SEO

Use `templates/thumbnail-title-checklist.md` and `references/thumbnail-guide.md`, and fill in `templates/thumbnail-brief.md` first. Make 3 thumbnail concepts, pick 1. Title is a question or a counter-claim, not a summary. Thumbnail is 3–4 words maximum, readable on a phone in 1 second, one subject only, deep teal + warm amber, no fake claim. Description has timestamps, keywords, and hashtags. Tags stay within YouTube's 500-character limit. For engaging scripting throughout, follow `references/engaging-scripting.md`: one question per part, a new visual or fact every 10 seconds, one number in 3 pictures, evidence before opinion.

## Do NOT do

- Do NOT copy footage, script, or narration from another creator.
- Do NOT use realistic worker-type footage/animation for village/people scenes.
- Do NOT freeze the host or any scene for more than 4–5 seconds.
- Do NOT put hands waving/pointing, a top bar, a solid box behind text, or a name card in the middle of the screen.
- Do NOT invent facts, numbers, dates, or quotes. If you cannot verify it, say so or leave it out.
- Do NOT present interpretation as proof, or a reconstruction as real footage.
- Do NOT promise views, virality, or a specific RPM.
- Do NOT add music or SFX unless the user explicitly asks.
- Do NOT use 100% word-by-word lip sync claims — the host is silent on screen.

## Files in this skill

- `references/style-guide.md` — full visual, host, text, and audio rules
- `references/script-structure.md` — 5–8 min structure, 1-min parts, hook and ending formulas
- `references/fact-check-checklist.md` — what to verify before scripting
- `references/image-prompts.md` — prompt templates for animation, diagrams, maps
- `references/editing-guide.md` — full video editing guide: cuts, cutaways, zoom/pan, text timing, editing checklist
- `references/competitor-analysis.md` — analyse 3–5 competitor videos, technique only, never copied footage/script
- `references/youtube-upload-checklist.md` — full upload checklist for YouTube Studio; the skill does not upload by itself
- `references/sound-design.md` — optional sound layer: whoosh, pop, BGM rules, licence check; default is voiceover only
- `references/sound-effects-catalogue.md` — 80 named sounds by category, names + uses only, no audio files; licence-check before monetised use
- `references/thumbnail-guide.md` — engaging thumbnail style: 3 concepts, phone test, prompts, mistakes
- `references/thumbnail-styles-library.md` — 50 reusable thumbnail patterns in 10 groups, not copied thumbnails
- `references/visual-assets-guide.md` — icons, template images, real vs 2D images, how a video runs beat by beat
- `references/youtube-seo.md` — YouTube SEO: short vs meaningful title, description, tags, upload, engagement tracking, next video topics
- `templates/seo-package-template.md` — fill-in SEO package + after-upload tracking, one per video
- `references/engaging-scripting.md` — hooks, open loops, pattern interrupts, numbers in 3 pictures, payoff
- `templates/script-template.md` — fill-in script
- `templates/storyboard-template.md` — 10-sec segment table
- `templates/thumbnail-title-checklist.md` — title, thumbnail, SEO
- `templates/thumbnail-brief.md` — fill-in thumbnail brief, one per video
- `examples/mohenjo-daro-outline.md` — original outline example
- `examples/sample-output-1min.md` — complete 1-minute sample output: script, storyboard, prompts, editing, thumbnail + SEO
- `scripts/make_storyboard.py` — beats JSON → storyboard markdown
- `CHANGELOG.md` — what changed in each release, with real dates
- `ROADMAP.md` — plan for next versions, not a promise of dates
