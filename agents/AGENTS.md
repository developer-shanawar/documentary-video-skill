# Agents — Documentary Video Skill

36 agents, in pipeline order. The Orchestrator (31) routes a job through them. Agents 32-36 are the designer / editor agents. Each agent file has role, input, output, steps, rules, and honest limits.

| # | Agent | Job |
| --- | --- | --- |
| 01 | [YouTube Analyser](01-youtube-analyser.md) | See file. |
| 02 | [Frame Extractor (Python)](02-frame-extractor.md) | See file. |
| 03 | [Frame Analyser](03-frame-analyser.md) | See file. |
| 04 | [Story Writer](04-story-writer.md) | See file. |
| 05 | [Script Writer (Engaging)](05-script-writer.md) | See file. |
| 06 | [Image Prompt Writer](06-image-prompt-writer.md) | See file. |
| 07 | [Clip Planner](07-clip-planner.md) | See file. |
| 08 | [Voiceover Writer](08-voiceover-writer.md) | See file. |
| 09 | [Editing Planner](09-editing-planner.md) | See file. |
| 10 | [Sound Designer](10-sound-designer.md) | See file. |
| 11 | [Thumbnail Designer](11-thumbnail-designer.md) | See file. |
| 12 | [Title + SEO Writer](12-title-seo-writer.md) | See file. |
| 13 | [Description + Tag Writer](13-description-tag-writer.md) | See file. |
| 14 | [Competitor Analyser](14-competitor-analyser.md) | See file. |
| 15 | [Fact Checker](15-fact-checker.md) | See file. |
| 16 | [Host Style Keeper](16-host-style-keeper.md) | See file. |
| 17 | [Storyboard Builder](17-storyboard-builder.md) | See file. |
| 18 | [Motion Planner](18-motion-planner.md) | See file. |
| 19 | [Text Overlay Planner](19-text-overlay-planner.md) | See file. |
| 20 | [Upload Checker](20-upload-checker.md) | See file. |
| 21 | [Engagement Tracker](21-engagement-tracker.md) | See file. |
| 22 | [Next Topic Finder](22-next-topic-finder.md) | See file. |
| 23 | [Channel Analyser](23-channel-analyser.md) | See file. |
| 24 | [Playlist Planner](24-playlist-planner.md) | See file. |
| 25 | [Short Clip Cutter](25-short-clip-cutter.md) | See file. |
| 26 | [Caption Writer](26-caption-writer.md) | See file. |
| 27 | [Music Licence Checker](27-music-licence-checker.md) | See file. |
| 28 | [Quality Reviewer](28-quality-reviewer.md) | See file. |
| 29 | [Release Manager](29-release-manager.md) | See file. |
| 30 | [Maintainer / Issue Triager](30-maintainer.md) | See file. |
| 31 | [Orchestrator](31-orchestrator.md) | See file. |
| 32 | [Video Editor](32-video-editor.md) | See file. |
| 33 | [Motion Graphic Designer](33-motion-graphic-designer.md) | See file. |
| 34 | [Graphic Designer](34-graphic-designer.md) | See file. |
| 35 | [Icon Designer](35-icon-designer.md) | See file. |
| 36 | [Diagram + Map Designer](36-diagram-map-designer.md) | See file. |

## Pipeline

1. Analyse: 01, 14, 23
2. Frames: 02, 03 (Python, ffmpeg, every 2 or 5 seconds)
3. Story + script: 04, 05, 08, 15
4. Visuals: 06, 07, 16, 17, 18, 19, 35, 36
5. Edit + sound + motion: 09, 10, 27, 32, 33
6. Design: 11, 34, 35, 36
7. Thumbnail + SEO: 11, 12, 13
8. Review + upload + track: 28, 20, 21, 22, 24, 25, 26
9. Maintain: 29, 30
10. Route it all: 31

## How to use an agent

In Claude / ChatGPT / Muse, after adding this skill, write: `Use agent 05-script-writer from the documentary-video skill to write a 5-minute script on [topic]`. Or write to the Orchestrator: `Use agent 31-orchestrator, make a video on [topic]`.
