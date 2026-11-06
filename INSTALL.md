# Install the Documentary Video Skill

## How it works (read this first)

1. **Download** this skill folder / `SKILL.md` from GitHub. The code is open source — everyone can download it, read it, and use it for free.
2. **Upload or add it** to your AI — Claude, ChatGPT, or Muse (steps below for each one).
3. **Ask** — once the skill is added, the AI understands what to make and works in that style. You do not need to explain the style again.

**No API key is needed for this skill.** It is only instructions (text files). It does not call any API and does not ask for a key. An API is only needed if *you* want to use a separate video-generation tool's API to generate clips yourself — that is optional, and this skill works without it.

You need the files in this repo. Download the whole folder, or clone it:

```bash
git clone <your-repo-url>
cd documentary-video-skill
```

Replace `<your-repo-url>` with the GitHub repo URL you push this folder to. Do not invent a URL — use your own repo's URL after you create it on GitHub.

## Claude

Claude supports Agent Skills as a folder containing a `SKILL.md` file.

1. Find your Claude skills folder. In Claude Code, skills live under your project's `.claude/skills/` folder, or your personal `~/.claude/skills/` folder.
2. Copy this whole folder there and rename it to `documentary-video`:

```bash
cp -r documentary-video-skill ~/.claude/skills/documentary-video
```

3. Restart Claude / open a new session.
4. Test it:

> Use the documentary-video skill. Topic: The Great Bath of Mohenjo-daro. Length: 1 minute. Give me the script beats and storyboard.

If Claude asks which skill to use, point it to `SKILL.md` in that folder.

## ChatGPT

ChatGPT does not have a native skills folder in the same way. Upload the skill as files:

1. Start a new chat.
2. Upload `SKILL.md` plus the files in `references/` and `templates/` you want it to use (at minimum `SKILL.md` and `references/style-guide.md`).
3. Say:

> Follow the uploaded documentary-video skill for this whole chat. Topic: [your topic]. Length: [1 / 5 / 8 minutes].

4. Keep the same chat for the whole video, so the style rules stay in context.

Tip: for a long video, do it in 1-minute parts, one part per chat turn, then combine at the end.

## Muse

1. Upload this folder as a skill, or upload `SKILL.md` and the `references/` and `templates/` files to the chat.
2. Say:

> Use the documentary-video skill in the uploaded files. Topic: [your topic]. Length: [your length].

3. Ask for one part at a time, and check each part against the storyboard before moving on.

## Try it (works everywhere)

After adding the skill, write exactly this (replace the topic with yours):

> Use the documentary-video skill, make a 5-minute documentary plan on [topic]

For example:

> Use the documentary-video skill, make a 5-minute documentary plan on why the Indus cities declined

The AI must return, in this order:

1. Angle in one sentence
2. Full script — 5 parts, 6 beats per part, each beat ~10 seconds with a voiceover line in Roman Urdu
3. Storyboard table — time, voice line, visual, motion, on-screen text for every beat
4. Image/diagram prompts — one per beat, no repeats
5. Voiceover script — clean lines with timecodes, ready to record
6. Editing guide — per segment: cut, cutaway, zoom/pan, text timing, plus the editing checklist
7. Thumbnail + title + SEO — title, 3–4 word thumbnail text, description with timestamps, tags within 500 characters

### Short test (1 minute)

Use this sample prompt after installing:

> Use the documentary-video skill. Topic: Why did the Indus cities decline? Length: 1 minute. Give me: 1) the angle in one sentence, 2) 6 beats with voiceover lines, 3) a storyboard table with visual + motion + on-screen text for each beat, 4) the editing guide for those 6 beats.

A correct result should have:

- 6 beats, each about 10 seconds
- Full script lines, not just an outline
- First beat is animation, not a still real photo
- Every visual matches its voice line
- Editing guide for every segment: what moves, where to cut away, where to zoom/pan
- Date in a top-right pill, name in a bottom-left card for 2 seconds only — never a top bar or a solid box behind text
- Host silent, hands down, no pointing
- No invented numbers, and interpretation labelled as interpretation

If any of those are missing, say: "Check SKILL.md again and fix the storyboard" — and point to the rule that was broken.

## Updating

When a new version of this skill is released, replace the whole folder and re-test with the sample prompt above.
