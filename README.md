# Documentary Video Skill

An open-source Agent Skill that helps you make original documentary videos — history, mystery, science, or places — with a locked, consistent style.

It turns a topic into a full video: a fact-checked script (hook, evidence, payoff), a 10-second storyboard, image/diagram prompts, a voiceover script, a complete video editing guide, and a thumbnail + title + SEO package.

This skill is a full video-making helper, not only planning:

1. **Script writing** — give it a topic and it writes the whole script in beats, ready to record.
2. **Video editing guide** — for every 10-second segment it tells the editor what visual, what motion, what on-screen text (date pill top-right, name card bottom-left for 2 seconds), where to cut away, and where to zoom/pan, plus an editing checklist.

## Who it is for

- YouTube documentary creators who want one consistent visual style across videos
- Beginners who want a clear structure instead of a blank page
- Anyone using Claude, ChatGPT, or Muse who wants the AI to follow the same style rules every time

## What is inside

The style is built from real published work: a Mohenjo-daro documentary (8:11, "No King, No Palace, No Throne — Who Ruled Mohenjo-Daro?") and a multi-part dinosaur-mystery video. The rules in this skill are the rules that were actually used there:

- A sticky-man explorer host (white round head, khaki cap, teal vest, brown backpack) who explains on a board, silent on screen, with subtle movement and hands down
- 2D animation matching the host — never photorealistic workers for people scenes
- First 10 seconds always animation, later real images only with visible zoom/pan motion
- Scene-voice matching: every visual shows exactly what the voiceover says at that moment
- A locked text system: date in a small rounded pill top-right, name in a small rounded card bottom-left for 2 seconds only
- Voiceover only by default (Young 3, speed 100, Roman Urdu + balanced technical English), no music or SFX unless asked
- Fact vs interpretation kept separate — interpretation is labelled, never presented as proof

## How to use — download, upload, ask

The code is open source: anyone can download it from GitHub, read it, and use it for free.

1. **Download from GitHub** — download this skill folder / `SKILL.md` from GitHub. All the code is available to everyone (open source, MIT license).
2. **Add it to your AI** — upload it or add it to Claude, ChatGPT, or Muse. Follow the exact steps in `INSTALL.md` for your app.
3. **Ask** — once the skill is added, the AI understands what to make and works in that style. You do not need to explain the style again.

### Try it

After adding the skill, write exactly this (replace the topic):

> Use the documentary-video skill, make a 5-minute documentary plan on [topic]

The AI will return: angle in one sentence, full script (5 parts, 6 beats per part), storyboard table, image/diagram prompts, voiceover script with timecodes, editing guide, and thumbnail + title + SEO. That output list is written in `SKILL.md`, so the AI knows exactly what to deliver.

### No API key needed

This skill does **not** ask for any API key. It is only instructions — text files that tell the AI how to make the video.

An API is only needed if *you* want to use a separate video-generation tool's API to generate clips yourself. That is optional, and this skill works without it: you can make the clips with any tool you like, or by hand, following the script, storyboard, and editing guide the skill gives you.

## What it does NOT do

- It does not generate video, audio, or images by itself. It writes the plan, script, storyboard, and prompts — you (or your video tools) make the clips.
- It does not copy another creator's footage or script.
- It does not invent facts. If a date or number cannot be verified, it says so.

## Files

- `SKILL.md` — the skill itself (start here)
- `INSTALL.md` — install steps for Claude, ChatGPT, and Muse
- `references/` — style guide, script structure, engaging scripting, fact-check checklist, image prompts, editing guide, sound design, thumbnail guide, competitor analysis, YouTube upload checklist
- `templates/` — script template, storyboard template, thumbnail/title checklist, thumbnail brief
- `examples/mohenjo-daro-outline.md` — an original outline example
- `examples/sample-output-1min.md` — complete 1-minute sample output
- `scripts/make_storyboard.py` — beats JSON → storyboard markdown
- `CHANGELOG.md` and `ROADMAP.md` — what is done, and what is planned next

## Quick example

Topic: Mohenjo-daro
Angle: "No King, No Palace, No Throne — Who Ruled Mohenjo-Daro?"
Result: 6 beats per minute, each beat ~10 seconds, each with a voice line, a moving 2D visual, and at most one small on-screen text. See `examples/mohenjo-daro-outline.md`.

## License

MIT — see `LICENSE`. Free to use, copy, and improve. Credit is appreciated but not required.
