from __future__ import annotations

import html
import json
import shutil
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(r"C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures")
REPO_ROOT = PROJECT_ROOT.parent
WEB_ROOT = PROJECT_ROOT / "web"
GITHUB_ROOT = REPO_ROOT / "github"
DOCS_ROOT = PROJECT_ROOT / "docs"
REPORTS_ROOT = PROJECT_ROOT / "reports"
ARTIFACTS_ROOT = PROJECT_ROOT / "artifacts"
CONFIG_ROOT = PROJECT_ROOT / "config"
LOGS_ROOT = PROJECT_ROOT / "logs"
DOWNLOADS_ROOT = PROJECT_ROOT / "downloaded_sources"
STAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
REPORT_DIR = REPORTS_ROOT / f"build_{STAMP}"
ARTIFACT_DIR = ARTIFACTS_ROOT / f"build_{STAMP}"
LOG_PATH = LOGS_ROOT / f"build_delivery_system_{STAMP}.log.txt"
BASE = "/AI_Night_1st-Stanley-Park_Venture-Company"

NAV = [
    ("Home", "/index.html"),
    ("Youth", "/participant/index.html"),
    ("Parents", "/parent/index.html"),
    ("Leaders", "/leader/index.html"),
    ("Facilitator", "/facilitator/index.html"),
    ("Exercises", "/participant/exercises.html"),
    ("KB", "/kb/index.html"),
    ("FAQ", "/shared/faq.html"),
]

SEGMENTS = [
    ("0-10", "Arrival and setup", "calm arrival, devices/browser ready, chargers out, optional Ethernet mention, expectations and reassurance", ["Welcome. Tonight is browser-first and low-pressure.", "Plug in chargers now if you have them.", "If your account or device is not ready, fallback support already exists."], "Now that everyone is settled, we can start with what AI is and what it is not.", "Move straight into the intro question if everyone is ready early.", "Use pair support and leader check-ins instead of pausing the whole room.", "Cut the optional room poll if setup runs long."),
    ("10-18", "Intro to AI and ChatGPT", "what AI is, what ChatGPT is, what it does well, what it gets wrong, safety and critical thinking", ["AI tools are good at patterns, drafting, summarizing, and generating options quickly.", "ChatGPT is useful for drafting, organizing, and starting.", "It can also be wrong, too generic, or missing context."], "The easiest way to see that is to compare a weak prompt with a stronger one.", "Take one question from the group before moving on.", "Skip extra examples and move into Demo 1 on time.", "Cut the hobby example if needed."),
    ("18-28", "Demo 1", "weak prompt vs improved prompt in ChatGPT", ["I will start with a weak prompt on purpose.", "Notice what is missing, not just whether the answer sounds polished.", "Then we will add goal, audience, format, and limits."], "Now you get to try the same pattern with support.", "Ask the group to name the upgrade moves without prompting.", "Provide the improved version yourself and spend less time on discussion.", "Cut the second volunteer answer if time is tight."),
    ("28-40", "Hands-on 1", "learners improve a guided starter prompt with low-choice support", ["Choose Guided if you are not sure where to start.", "One prompt getting better counts as success.", "If stuck, ask what the answer is for, who it is for, and what format you want."], "Take a quick stretch, then we will do the same pattern with image prompts.", "Offer Build or Remix cards to early finishers.", "Pair learners and let them co-edit one prompt.", "Skip the share-out and go straight to break if needed."),
    ("40-45", "Short break / regroup", "brief break and room reset", ["Stand up, stretch, and keep your charger connected.", "When we come back, we switch from text prompts to image prompts."], "Let us look at what changes when an image request becomes more specific.", "Restart one minute early if the room is settled.", "Use the first minute after break to re-open the right tab for everyone.", "Keep the break to four minutes if the schedule slipped."),
    ("45-53", "Demo 2", "weak image prompt vs improved image prompt", ["Image prompts improve when you add subject, mood, style, colour, and composition.", "A short prompt can work, but it often leaves too much up to chance.", "We are not trying to write a novel. We are trying to be clear enough to steer the result."], "You will each create one image next using a guided template.", "Show one extra variation using a different style word.", "Focus on one image comparison only and move to the learner task.", "Skip the extra audience question if time is tight."),
    ("53-63", "Hands-on 2", "learners create one image using guided scaffolding", ["Start with subject, then mood, then colour, then style.", "Borrow a starter card if you are stuck.", "It is fine if your first image is not perfect."], "Next I will show one short facilitator-only Codex example, then you choose your final activity.", "Invite early finishers to remix their image for a new audience.", "Offer a fill-in-the-blanks sentence stem instead of open writing.", "Reduce the share-out to one volunteer image if needed."),
    ("63-70", "Demo 3", "short facilitator-only Codex demo", ["This part is short and facilitator-led.", "Codex is not magic and it is not a reason to skip thinking.", "A vague request gets vague output. A structured request makes the result easier to review."], "For the last work block, choose Guided, Build, Remix, or Stretch.", "Ask one extension question about what detail made the improved request safer.", "Keep the demo under five minutes and move on.", "Cut the code-detail explanation and keep only the prompt comparison."),
    ("70-80", "Hands-on 3", "learners choose Guided, Build, Remix, or Stretch", ["Choose the level that helps you keep moving.", "Guided is not lesser. It is a supported path.", "If you finish early, use a follow-up prompt or reflection card."], "Finish the last note you want to keep, then we will reflect together.", "Invite strong finishers to write one tip for someone starting.", "Keep more learners on Guided and Build cards.", "Cut the optional gallery walk if time is tight."),
    ("80-87", "Reflection", "what changed, what worked, what surprised you, what would you do differently next time", ["Name one thing you changed that made the result better.", "Name one thing AI still did badly or awkwardly.", "Name one way you might use this safely after tonight."], "We will finish with a short safe-use reminder and next steps.", "Take answers from three volunteers.", "Use pair reflection instead of full-group sharing.", "Use the printable reflection page instead of a verbal round."),
    ("87-90", "Closing", "safe use reminder, takeaways, resources, what happens next", ["AI is most useful when you ask clearly and check what comes back.", "Use it to help you think, not to turn your brain off.", "If you want the advanced path later, it is optional and separate from the main session."], "Thank you. Save or print your report before you close the page.", "End two minutes early and leave space for one final question.", "Keep the close to the top three takeaways only.", "Do not cut the safe-use reminder."),
]

DEMOS = [
    {"name": "ChatGPT demo 1: study helper", "kind": "chatgpt", "weak": "Help me study science.", "why": "It does not name the topic, age, format, or what would make the answer useful.", "improved": "I am 15 and reviewing photosynthesis. Explain it in five short bullet points, give one everyday analogy, and end with two quiz questions.", "changed": "Added topic, audience, output format, and a concrete study aid.", "difference": "The stronger version is shorter, more relevant, and easier to use for practice.", "teaching": "Prompt quality often comes from clear purpose, audience, format, and limits.", "questions": ["What was missing from the weak prompt?", "Which added detail helped most?", "How would you adapt this for another subject?"], "followup": "Change the subject to geography or biology and keep the same structure.", "coaching": "If you do not know what to add, start with what the answer is for.", "strong_extension": "Ask for a short practice quiz with an answer key.", "support_prompt": "I am learning ____. Explain it in ____ bullet points for a ____ year old."},
    {"name": "ChatGPT demo 2: weekend planner", "kind": "chatgpt", "weak": "Plan my weekend.", "why": "It is too open-ended and gives no budget, location, style, or age context.", "improved": "Plan a low-cost Saturday for a teen in Vancouver with one outdoor idea, one indoor backup, and one snack stop. Keep the whole plan under $25 and list it as a simple timeline.", "changed": "Added audience, location, budget, constraints, and preferred format.", "difference": "The stronger version is usable right away and includes a backup option.", "teaching": "Specific constraints often make a response more practical.", "questions": ["Why is the budget useful here?", "What did the indoor backup add?", "What other constraints might matter?"], "followup": "Remix it for a rainy evening or a family outing.", "coaching": "Think about what would make the answer realistic in the real world.", "strong_extension": "Add transit limits and ask for a checklist version.", "support_prompt": "Plan a ____ for a ____ in ____. Keep it under ____ and show it as ____."},
    {"name": "ChatGPT demo 3: tone and audience rewrite", "kind": "chatgpt", "weak": "Rewrite this email.", "why": "It does not say who the email is for, how it should sound, or what to keep short.", "improved": "Rewrite this email so it sounds polite and clear for a teacher. Keep it under 120 words, make the ask obvious, and remove dramatic wording.", "changed": "Added audience, tone, length, and a concrete revision goal.", "difference": "The improved version is more likely to produce a message that is respectful and ready to send.", "teaching": "Audience and tone can matter as much as topic.", "questions": ["Who is the audience?", "What tone shift happened?", "Why is the length limit useful?"], "followup": "Change the audience to a team leader or event organizer.", "coaching": "Name who will read it and what you want them to understand.", "strong_extension": "Ask for two versions: more formal and more casual.", "support_prompt": "Rewrite this for a ____. Make it sound ____ and keep it under ____ words."},
    {"name": "Image demo 1: camp poster", "kind": "image", "weak": "Make a camp poster.", "why": "The tool has to guess the mood, style, colours, and layout.", "improved": "Create a friendly poster-style image for a scout campfire night at dusk with warm lantern light, navy and gold colours, pine trees in the background, and space at the top for a title.", "changed": "Added event type, mood, colour palette, background elements, and composition.", "difference": "The improved image is more consistent with a real event poster.", "teaching": "Image prompts improve when the request includes scene, style, mood, and layout clues.", "questions": ["Which visual detail mattered most?", "What made the improved image feel more like a poster?", "What could you change for a different audience?"], "followup": "Remix it for a daytime family picnic poster.", "coaching": "Start with the main subject, then add mood and colour.", "strong_extension": "Ask for a flat graphic variant for a sticker.", "support_prompt": "Create a ____ image with ____ colours, a ____ mood, and space for ____."},
    {"name": "Image demo 2: round sticker", "kind": "image", "weak": "Make a cool sticker.", "why": "Cool means different things to different people and gives no design direction.", "improved": "Design a round sticker with a mountain, a compass, and a small spark icon using bold flat colours, thick outlines, and a clean badge layout.", "changed": "Added shape, subject elements, style, and layout.", "difference": "The improved result is more likely to look like a real sticker instead of a random image.", "teaching": "Style words and layout words help image tools narrow the result.", "questions": ["What did the word round change?", "Why do thick outlines help for sticker art?", "What would you change for a patch instead?"], "followup": "Remix it for a camp mug graphic or social tile.", "coaching": "If your image feels random, add style and layout words.", "strong_extension": "Ask for a matching poster and sticker set.", "support_prompt": "Design a ____ with ____ objects in a ____ style using ____ colours."},
    {"name": "Facilitator-only Codex demo", "kind": "codex", "weak": "Build me an app.", "why": "It does not say what kind of app, what size, or what success looks like.", "improved": "Make one small HTML page for a scout checklist with a heading, three checklist items, one Complete button, and a short explanation of the changes. Keep it in one file.", "changed": "Added scope, output format, size, and content requirements.", "difference": "The improved request is more likely to produce something small enough to review live.", "teaching": "The same prompt lesson applies to coding assistants: clearer requests reduce confusion.", "questions": ["What scope limit helped most?", "Why is one file easier to review live?", "What made the weak request risky?"], "followup": "Ask how the same prompt could be adapted for a bug fix.", "coaching": "Keep the demo short and connect it back to prompt clarity.", "strong_extension": "Compare two different output constraints and discuss reviewability.", "support_prompt": "Notice what to build, how big it should be, and what must be included."},
]

KB_ARTICLES = [
    {"slug": "what-is-chatgpt", "title": "What ChatGPT Is and What It Is Good At", "source_name": "OpenAI Help Center", "source_url": "https://help.openai.com/en/articles/6783457-what-is-chatgpt", "summary": "ChatGPT is a browser-based AI assistant that can help with drafting, summarizing, brainstorming, explanation, and revision.", "why": "This helps families understand that the workshop is guided browser use, not a programming bootcamp.", "takeaway": "Use ChatGPT to start thinking and organizing, not as a substitute for checking important answers."},
    {"slug": "good-prompts", "title": "How to Make a Prompt Stronger", "source_name": "OpenAI Help Center", "source_url": "https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt", "summary": "A stronger prompt usually adds the goal, the audience, the format, and any useful limits.", "why": "Prompt improvement is the core hands-on activity for the night.", "takeaway": "Small prompt upgrades can produce a noticeably more useful result."},
    {"slug": "image-prompts", "title": "Designing Better Image Prompts", "source_name": "OpenAI Help Center", "source_url": "https://help.openai.com/en/articles/8932459-dall-e-in-chatgpt", "summary": "Image prompts become more useful when they describe the subject, style, mood, colour, and composition.", "why": "This supports the image demo and the guided image activity.", "takeaway": "If an image feels random, add style and layout words instead of only adding more words."},
    {"slug": "truth-and-mistakes", "title": "Why AI Output Still Needs Checking", "source_name": "OpenAI Help Center", "source_url": "https://help.openai.com/en/articles/8313428-does-chatgpt-tell-the-truth", "summary": "AI can sound confident even when it is wrong, incomplete, or too generic.", "why": "This supports the safe-use and critical-thinking message for youth and parents.", "takeaway": "A polished answer is still something to review, not something to trust automatically."},
    {"slug": "free-account-and-access", "title": "Browser Access and Free Account Expectations", "source_name": "OpenAI Help Center", "source_url": "https://help.openai.com/en/articles/9275245-using-chatgpts-free-tier-faq", "summary": "The workshop is designed around browser access, and a free account may be enough for the main activity.", "why": "This supports the parent trust layer and the low-friction browser-first path.", "takeaway": "Families can use their own judgment about account setup without blocking participation in the event."},
    {"slug": "teen-ai-literacy", "title": "Teen AI Literacy and Safe Use", "source_name": "OpenAI PDF resource", "source_url": "https://cdn.openai.com/pdf/openai-teen-literacy-blueprint.pdf", "summary": "Teen AI literacy includes judgment, privacy awareness, fairness questions, and the habit of checking outputs before relying on them.", "why": "This reinforces the event's safe-use framing and guided design.", "takeaway": "AI literacy is not just tool use. It is also judgment, boundaries, and reflection."},
]

LEVELS = ["Guided", "Build", "Remix", "Stretch"]
CATEGORIES = [
    ("Prompt improvement", ["Help me learn history.", "Help me get ready for camp.", "Tell me about Vancouver.", "Help me plan a project."], "Add goal, audience, format, and a real-world limit."),
    ("Summarize and refine", ["Summarize this article.", "Summarize this and make it better.", "Explain this video.", "Turn this into study notes."], "Split big tasks into smaller prompt steps when needed."),
    ("Tone and audience rewrite", ["Rewrite this message.", "Make this sound better.", "Rewrite this camp announcement.", "Turn this into a short speech."], "Name the audience, tone, and length target."),
    ("Image prompt design", ["Make a poster for camp.", "Make a cool logo.", "Create an event image.", "Create a set of matching images."], "Add subject, mood, style, colour, and layout clues."),
    ("Reflection on AI output quality", ["Which answer is better?", "Compare these two outputs.", "Why is this not quite right?", "What would you verify before trusting this output?"], "Judge usefulness, clarity, accuracy signs, and fit for purpose."),
    ("Optional Codex observation task", ["Watch the facilitator demo and name one useful constraint.", "Explain what Codex is and is not.", "Adapt the coding demo lesson back into a browser-only prompt lesson.", "Explain why the coding demo is optional and secondary."], "Keep the focus on prompt clarity, not on coding status."),
]

REQUIRED_DOCS = [
    "project_coordination_dashboard.html", "current_state_validated_vs_unvalidated.html", "repo_rationalization_plan.html", "workshop_delivery_architecture.html", "platform_compatibility_matrix.html", "participant_pathways.html", "parent_information_pack.html", "youth_prework_and_takeaway_pack.html", "leader_operations_pack.html", "presenter_operations_pack.html", "readiness_checker_spec.html", "install_launch_cleanup_lifecycle.html", "browser_first_environment_plan.html", "local_vm_optional_path_plan.html", "apple_silicon_and_nonstandard_device_path.html", "risk_and_fallback_matrix.html", "codex_rules_and_guardrails_examples.html", "example_prompt_and_ruleset_takeaway.html", "completed_vs_blocked_vs_next_actions.html", "final_packaging_and_release_plan.html", "facilitator_talking_points.html", "facilitator_answer_key.html", "session_run_of_show_90_minutes.html", "session_slide_content_and_speaker_notes.html", "demo_prompt_bank_chatgpt.html", "demo_prompt_bank_images.html", "demo_prompt_bank_codex_facilitator_only.html", "backup_facilitator_pack.html", "exercise_system_overview.html", "exercise_cards_guided_build_remix_stretch.html", "reflection_and_takeaway_pack.html", "pre_event_communications_plan.html", "pre_event_parent_message.html", "pre_event_participant_message.html", "pre_event_readiness_and_homework.html", "pre_event_survey_and_feedback_plan.html", "youth_participant_pack.html", "leader_support_pack.html", "kb_index.html", "kb_article_template.html"
]


def ensure_dirs() -> None:
    for path in [DOCS_ROOT, REPORTS_ROOT, ARTIFACTS_ROOT, CONFIG_ROOT, LOGS_ROOT, WEB_ROOT, REPORT_DIR, ARTIFACT_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def log(message: str) -> None:
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}"
    print(line)
    with LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def rel(path: Path, base: Path = PROJECT_ROOT) -> str:
    return str(path.relative_to(base)).replace("\\", "/")


def u(path: str) -> str:
    return f"{BASE}{path if path.startswith('/') else '/' + path}"


def esc(value: str) -> str:
    return html.escape(str(value), quote=True)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    log(f"Wrote {rel(path)}")


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    log(f"Wrote {rel(path)}")


def table(headers: list[str], rows: list[tuple[str, ...]] | list[list[str]]) -> str:
    head = "".join(f"<th>{esc(h)}</th>" for h in headers)
    body = []
    for row in rows:
        body.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>")
    return f"<div class='table-shell'><table><thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"


def bullet(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


def panel(title: str, body: str) -> str:
    return f"<section class='panel'><h2>{esc(title)}</h2>{body}</section>"


def section(title: str, body: str) -> str:
    return f"<section class='section'><h2>{esc(title)}</h2>{body}</section>"


def page(title: str, description: str, label: str, body: str) -> str:
    nav = "".join(f"<li><a data-current-path href='{u(path)}'>{esc(name)}</a></li>" for name, path in NAV)
    return f"""<!doctype html>
<html lang='en'>
<head>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <title>{esc(title)}</title>
  <meta name='description' content='{esc(description)}'>
  <link rel='icon' href='{u('/assets/icons/favicon.svg')}' type='image/svg+xml'>
  <link rel='stylesheet' href='{u('/assets/css/site.css')}'>
  <link rel='stylesheet' href='{u('/assets/css/print.css')}'>
  <script defer src='{u('/assets/js/site.js')}'></script>
</head>
<body>
  <a class='skip-link' href='#main'>Skip to main content</a>
  <div class='site-shell'>
    <div class='utility-banner'><div class='wrap'><strong>Browser-first by default:</strong> the core session works in the browser. Local VM and advanced tooling are optional only.</div></div>
    <header class='site-header'><div class='wrap header-row'><a class='brand' href='{u('/index.html')}'><span class='brand-mark' aria-hidden='true'></span><span class='brand-text'><strong>AI Night</strong><span>{esc(label)}</span></span></a><button class='menu-toggle' data-menu-toggle aria-expanded='false' aria-controls='main-nav'>Menu</button><nav class='main-nav' id='main-nav' data-nav aria-label='Primary'><ul>{nav}</ul></nav></div></header>
    <main id='main' class='page-main'><div class='wrap'><section class='panel'><h1>{esc(title)}</h1><p>{esc(description)}</p></section>{body}</div></main>
    <footer class='site-footer'><div class='wrap footer-grid'><div><h2>AI Night</h2><p>Guided browser-based introduction to AI for Scouts and Venturers. The main outcomes are safer use, clearer prompts, reflection, and practical confidence.</p></div><nav class='footer-nav' aria-label='Footer'><ul><li><a href='{u('/participant/before.html')}'>Before</a></li><li><a href='{u('/participant/day-of.html')}'>During</a></li><li><a href='{u('/participant/after.html')}'>After</a></li><li><a href='{u('/participant/exercises.html')}'>Exercises</a></li><li><a href='{u('/participant/reflections.html')}'>Reflections</a></li><li><a href='{u('/kb/index.html')}'>Knowledge articles</a></li></ul></nav></div></footer>
  </div>
</body>
</html>"""


def doc_page(title: str, summary: str, body: str) -> str:
    return f"""<!doctype html>
<html lang='en'>
<head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><title>{esc(title)}</title><style>body{{margin:0;background:#f4f7fb;color:#1f2937;font:16px/1.6 'Segoe UI',Arial,sans-serif}}.wrap{{max-width:1120px;margin:0 auto;padding:28px 18px 48px}}.hero{{background:linear-gradient(135deg,#123152,#0f4c81,#1d7a85);color:#fff;border-radius:22px;padding:24px}}.section{{margin-top:22px;background:#fff;border:1px solid #d8e0ea;border-radius:18px;padding:20px}}table{{width:100%;border-collapse:collapse}}th,td{{text-align:left;vertical-align:top;padding:10px 12px;border-bottom:1px solid #d8e0ea}}th{{background:#eef4fb}}code{{background:#eef4fb;padding:2px 6px;border-radius:6px}}</style></head><body><div class='wrap'><section class='hero'><h1>{esc(title)}</h1><p>{esc(summary)}</p></section>{body}</div></body></html>"""


def source_inventory() -> list[tuple[str, str]]:
    rows = []
    if DOWNLOADS_ROOT.exists():
        for path in sorted(DOWNLOADS_ROOT.rglob("*")):
            if path.is_file():
                rows.append((rel(path), path.suffix or "file"))
    return rows


def segment_table() -> str:
    return table(["Time", "Segment", "Focus"], [(t, title, focus) for t, title, focus, *_ in SEGMENTS])


def exercise_cards() -> list[dict[str, str]]:
    cards = []
    for category, starters, tip in CATEGORIES:
        for level, starter in zip(LEVELS, starters):
            cards.append({
                "category": category,
                "level": level,
                "starter": starter,
                "tip": tip,
                "note": "What changed in your prompt?",
                "result": "Did the result match what you wanted?",
                "followup": "Try one more version with a clearer audience or format.",
                "support": "If stuck, borrow the matching demo pattern and change only one detail.",
            })
    return cards


def demo_cards(kind: str | None = None) -> str:
    cards = []
    for demo in DEMOS:
        if kind and demo["kind"] != kind:
            continue
        cards.append("<article class='page-card'>" + f"<h3>{esc(demo['name'])}</h3><p><strong>Weak prompt:</strong> {esc(demo['weak'])}</p><p><strong>Why weak:</strong> {esc(demo['why'])}</p><p><strong>Improved prompt:</strong> {esc(demo['improved'])}</p><p><strong>Teaching point:</strong> {esc(demo['teaching'])}</p><p><strong>Optional learner follow-up:</strong> {esc(demo['followup'])}</p></article>")
    return "<div class='card-grid'>" + "".join(cards) + "</div>"


def exercise_table() -> str:
    rows = []
    for card in exercise_cards():
        rows.append((card["category"], card["level"], card["starter"], card["tip"], card["followup"]))
    return table(["Category", "Level", "Weak starter prompt", "Scaffolded tip", "Follow-up"], rows)


def report_form() -> str:
    return """
<section class='panel'><h2>Practice report</h2><p>Use this page to record what changed, whether the result matched your goal, and what gap remained. You can save a draft in this browser, download a JSON copy, or print to paper/PDF.</p><form id='exercise-report' data-workflow-form data-draft-key='exercise_report' data-download-name='ai-night-exercise-report' data-summary-target='#exercise-summary'><div class='form-grid'><div><label for='level'>Exercise level</label><select id='level' name='level'><option>Guided</option><option>Build</option><option>Remix</option><option>Stretch</option></select></div><div><label for='category'>Exercise category</label><select id='category' name='category'><option>Prompt improvement</option><option>Summarize and refine</option><option>Tone and audience rewrite</option><option>Image prompt design</option><option>Reflection on AI output quality</option><option>Optional Codex observation task</option></select></div><div><label for='starter'>Weak starter prompt</label><textarea id='starter' name='starter' rows='4' placeholder='Type or paste the starter prompt you used.'></textarea></div><div><label for='changes'>What changed?</label><textarea id='changes' name='changes' rows='4' placeholder='Name the changes you made to the prompt.'></textarea></div><div><label for='expectation'>What were you hoping for?</label><textarea id='expectation' name='expectation' rows='4' placeholder='Describe the result you wanted.'></textarea></div><div><label for='result'>Did the result meet your expectation?</label><select id='result' name='result'><option>Yes, mostly</option><option>Partly</option><option>Not yet</option></select></div><div><label for='gap'>What gap remained?</label><textarea id='gap' name='gap' rows='4' placeholder='What was still missing, off, or unclear?'></textarea></div><div><label for='next'>What would you try next time?</label><textarea id='next' name='next' rows='4' placeholder='Write one follow-up change or next prompt.'></textarea></div></div><div class='button-row'><button type='button' data-save-draft>Save in this browser</button><button type='button' data-download-draft>Download report</button><button type='button' data-print-page>Print or save as PDF</button></div></form></section><section class='panel'><h2>Printable summary</h2><div id='exercise-summary'><p class='small'>Your entered details will appear here so you can print or save them.</p></div></section>
"""


def public_pages() -> dict[str, tuple[str, str, str, str]]:
    levels = table(["Level", "What it means"], [(level, f"Use {level} if that is the path that helps you keep moving.") for level in LEVELS])
    return {
        'index.html': ('AI Night: Browser-First Intro to AI', 'Guided browser-based introduction to AI, prompt practice, and safe practical use for Scouts and Venturers.', 'Browser-first intro workshop', panel('Browser-first AI night for Scouts and Venturers', "<p>The main session is a calm introduction to AI in the browser. Learners compare weak and strong prompts, try guided prompt practice, test an image prompt, reflect on what changed, and leave with simple takeaways.</p><div class='button-row'><a class='button' href='" + u('/participant/index.html') + "'>Youth page</a><a class='button secondary' href='" + u('/parent/index.html') + "'>Parent page</a><a class='button secondary' href='" + u('/facilitator/run-of-show.html') + "'>Run of show</a></div>") + panel('Required / Optional / Not needed by default', table(['Type','What it means'], [('Required','A device with a modern browser, if available, plus a charger or power cable.'), ('Optional','An Ethernet cable and a family-approved free account if desired.'), ('Not needed by default','Local VM, local Python, terminal tools, coding setup, or Codespaces.')])) + panel('Locked 90-minute structure', segment_table())),
        'participant/index.html': ('Youth: What to Expect', 'Simple browser-first guide for youth participants.', 'Youth participant guide', panel('What to expect', '<p>You do not need to be a coder. Tonight is about clearer prompts, practical browser use, and noticing what changes when you ask more clearly.</p>') + panel('What to bring', bullet(['Device if you have one', 'Charger or power cable', 'Optional Ethernet cable if you have one', 'One topic you care about'])) + panel('How the session works', '<p>You will watch short demos, try guided versions yourself, and save or print a reflection report before you leave.</p>' + levels) + panel('If you get stuck', bullet(['Use Guided.', 'Borrow a starter card.', 'Add one detail at a time.', 'Ask a leader or the facilitator for a sentence frame.']))),
        'participant/before.html': ('Before the Session', 'Low-pressure checklist before arrival.', 'Before the session', panel('Before the session', "<p><strong>Default plan:</strong> arrive with a browser-ready device if available. No VM is required by default.</p>" + bullet(['Charge your device and bring the charger.', 'If your family is comfortable, sign in to a browser-based AI tool before arrival.', 'If you do not have a device or cannot sign in, you can still participate through the fallback path.', 'Bring one topic you care about: school, hobbies, planning, stories, art, or event ideas.']))),
        'participant/day-of.html': ('During the Session', 'What happens during the live 90-minute workshop.', 'During the session', panel('During the session', '<p>The event alternates between short demos and guided practice so you do not need to figure everything out alone.</p>' + segment_table())),
        'participant/after.html': ('After the Session', 'Takeaways and next steps after the workshop.', 'After the session', panel('After the session', bullet(['Keep your best improved prompt.', 'Save or print your reflection report.', 'Use the knowledge pages and examples when you want to try again.', 'Keep checking answers instead of trusting every polished result.']))),
        'participant/exercises.html': ('Exercises and Prompt Cards', 'Guided browser-first exercises for the live session.', 'Exercises', panel('Exercise model', '<p>Use Guided, Build, Remix, or Stretch. Pick the level that helps you keep moving. No level is a status label.</p>' + exercise_table()) + panel('Reusable demo cards', demo_cards()) + report_form() + panel('If you finish early', bullet(['Try one follow-up prompt instead of starting from blank.', 'Switch from Guided to Build or Remix.', 'Write one tip card for someone who is starting.', 'Use the reflection page to compare two outputs.']))),
        'participant/reflections.html': ('Reflections and Report', 'Reflection prompts and printable summary for learners.', 'Reflection and report', panel('Reflection prompts', bullet(['What changed between the weak prompt and your improved prompt?', 'Which detail helped most: goal, audience, format, or limits?', 'What gap remained?', 'What would you try next time?', 'Where could you use this safely after tonight?'])) + report_form()),
        'parent/index.html': ('Parent and Guardian Information', 'Warm, plain-language overview for families.', 'Parent and guardian guide', panel('Browser-first by default', '<p>This session is a guided introduction to AI tools in the browser. It is not a programming bootcamp, not a hacking session, and not a hidden software-install exercise.</p>') + panel('What to bring', bullet(['Device if available', 'Charger or power cable', 'Optional Ethernet cable', 'Browser access is the main requirement'])) + panel('Required / Optional / Not needed by default', table(['Category','Details'], [('Required','Browser access, a device if available, and a charger or power cable.'), ('Optional','A family-approved free ChatGPT account and an Ethernet cable if available.'), ('Not needed by default','Local VM, local Python, terminal tools, complicated installs, or advanced coding setup.')])) + panel('What your child will do', bullet(['Compare weak and stronger prompts in the browser.', 'Practice improving a prompt with a simple template.', 'Try one image prompt.', 'Reflect on what made the result more useful.'])) + panel('What your child will not be required to do', bullet(['Install a VM by default', 'Use local Python by default', 'Use terminal tools by default', 'Turn the session into a coding class'])) + panel('Privacy, accounts, and shared devices', bullet(['A free account may be enough for the main activity, but families should use their own judgment.', 'Browser-first delivery reduces local device changes.', 'Optional advanced installs, if ever used later, are separate and removable.', 'If a learner cannot use an account or device, the fallback pathway still allows participation.'])) + panel('How to opt out of optional installs', '<p>You do not need to approve optional VM or advanced tooling for the core workshop. Staying on the browser-first route is fully supported.</p>') + panel('Questions parents may ask', "<div class='card-grid'><article class='page-card'><h3>What is this session?</h3><p>A guided, browser-based introduction to AI and ChatGPT for practical everyday use.</p></article><article class='page-card'><h3>What is it not?</h3><p>It is not a programming bootcamp, hacking session, or hidden install exercise.</p></article><article class='page-card'><h3>What if our device is shared?</h3><p>The browser-first path minimizes device changes. Families can decide whether account sign-in is appropriate.</p></article><article class='page-card'><h3>What if we want no installs?</h3><p>That is fine. The browser-first and fallback routes still support participation.</p></article></div>")),
        'leader/index.html': ('Leader Guide', 'Browser-first support guide for leaders.', 'Leader guide', panel('Leader support role', '<p>Keep the night calm, browser-first, and low-choice. Help youth get to the right page, keep them powered, and route issues into the fallback plan instead of derailing the session with advanced setup.</p>') + panel('What leaders help with', bullet(['Chargers and power access', 'Getting youth to the correct page', 'Noticing who is stuck', 'Using fallback routes early'])) + panel('Session-night logistics', table(['Situation','Leader action'], [('Late arrival','Open the youth page, confirm charger access, and route to the current exercise.'), ('Device trouble','Use paired work, presenter-led participation, or the fallback prompt cards before touching advanced setup.'), ('Internet issue','Shift to group demo visibility, printed prompt cards, and verbal reflection.'), ('Learner overload','Reduce choices, suggest Guided, and narrow to one prompt only.')])) + panel('What not to derail into', bullet(['Do not push VM setup as the main route.', 'Do not turn the night into coding troubleshooting.', 'Do not create extra tool choices if the browser-first path is working.']))),
        'facilitator/index.html': ('Facilitator Guide', 'Presenter-facing guide for the browser-first workshop.', 'Facilitator guide', panel('Facilitator launch page', '<p>Open the run of show, demo bank, exercise page, and reflection page before the session starts.</p><p><strong>Presenter reminder:</strong> the goal is not to cover everything. The goal is to keep the room calm and make the prompt-improvement pattern visible.</p>') + panel('Critical tabs to open', bullet(['Facilitator run of show', 'Demo cards page', 'Participant exercises page', 'Reflection page', 'Knowledge base index']))),
        'facilitator/run-of-show.html': ('Facilitator Run of Show', 'Minute-by-minute plan, demo prompts, and fallback instructions.', 'Run of show', panel('Minute-by-minute run of show', segment_table()) + panel('Exact demo prompts', demo_cards()) + panel('Reflection and closing script', bullet(['What changed after you improved the prompt?', 'What worked better than expected?', 'What still needs human checking?', 'Where can you use this safely after tonight?']) + '<p><strong>Closing remarks:</strong> AI can help you think faster, but it should not replace judgment. Ask clearly, check what matters, and use the browser-first path as your default.</p>') + panel('Fallback and recovery', bullet(['If accounts fail, pair learners or switch to presenter-led examples.', 'If the image tool fails, compare prompts verbally and use the prompt cards only.', 'If internet access fails, keep the room together and use printed cards plus discussion.', 'If the pace slips, cut optional share-outs before cutting the core prompt-comparison pattern.']))),
        'shared/resources.html': ('Resources and Examples', 'Starter prompts, examples, and take-home links.', 'Resources and examples', panel('Demo prompt bank', demo_cards()) + panel('Quick resource table', table(['Resource','Why it helps'], [('Prompt cards','Reduce blank-page pressure.'), ('Reflection page','Captures what changed and what to try next.'), ('Knowledge pages','Add background on prompts, image prompts, and safe use.'), ('Facilitator run of show','Keeps timing and messaging consistent.')]))),
        'shared/examples.html': ('Demo Cards', 'Reusable weak-vs-strong prompt demo cards.', 'Demo cards', panel('Weak vs strong demo cards', demo_cards())),
        'shared/faq.html': ('FAQ', 'Short answers to common workshop questions.', 'Frequently asked questions', panel('FAQ', "<div class='card-grid'><article class='page-card'><h3>Do I need a VM?</h3><p>No. Browser-first is the default participant path.</p></article><article class='page-card'><h3>Do I need coding?</h3><p>No. The session is about prompting, comparison, and reflection.</p></article><article class='page-card'><h3>What if I do not have a suitable device?</h3><p>You can still participate through the fallback path or paired work.</p></article><article class='page-card'><h3>What if I do not want installs?</h3><p>The main session does not require local installs.</p></article></div>")),
        'access/index.html': ('Access and Routing', 'Access guidance for browser-first and optional paths.', 'Access routing', panel('Access and routing', table(['Route','Use it when'], [('Browser-first','Default for youth, leaders, presenter, leader test, and backup browser environments.'), ('Optional VM path','Only for compatible advanced/operator scenarios.'), ('Apple Silicon alternative','Use browser-first unless a separate validated local path exists.'), ('No-install fallback','Use paired or presenter-led participation when a device or account is not available.')]))),
    }


def build_public_pages() -> None:
    for rel_path, meta in public_pages().items():
        title, description, label, body = meta
        write(WEB_ROOT / rel_path, page(title, description, label, body))
    support_pages = [
        ('legal/privacy.html', 'Privacy'), ('legal/consent.html', 'Consent and family review'), ('legal/disclaimer.html', 'Workshop disclaimer'), ('shared/terms.html', 'Terms'),
        ('participant/project.html', 'Participant Project Notes'), ('participant/readiness.html', 'Participant Readiness'), ('participant/signup.html', 'Participant Signup'), ('leader/submissions.html', 'Leader Submissions'),
        ('parent/waiver.html', 'Parent Waiver'), ('shared/participant-roster-sheet.html', 'Participant Roster Sheet'), ('shared/site-inspection-sheet.html', 'Site Inspection Sheet'), ('shared/submission-received.html', 'Submission Received'), ('404.html', 'Page Not Found'),
    ]
    for rel_path, title in support_pages:
        write(WEB_ROOT / rel_path, page(title, title, 'Support page', panel(title, '<p>This supporting page is retained and aligned to the browser-first delivery model.</p>')))


def build_kb() -> None:
    for article in KB_ARTICLES:
        body = panel(article['title'], f"<p><strong>Original source:</strong> <a href='{esc(article['source_url'])}'>{esc(article['source_name'])}</a></p><p><strong>Date normalized:</strong> {STAMP}</p><p><strong>Tags:</strong> browser-first, prompts, safe use, workshop</p>")
        body += panel('Readable summary', f"<p>{esc(article['summary'])}</p><p>The workshop uses this source as background for guided discussion, not as a long reading assignment.</p>")
        body += panel('Why this matters for the workshop', f"<p>{esc(article['why'])}</p><p><strong>Key takeaway:</strong> {esc(article['takeaway'])}</p>")
        body += panel('Related reading', bullet([f"<a href='{u('/shared/examples.html')}'>Demo cards</a>", f"<a href='{u('/participant/exercises.html')}'>Exercises</a>", f"<a href='{u('/kb/index.html')}'>Knowledge index</a>"]))
        write(WEB_ROOT / 'kb' / f"{article['slug']}.html", page(article['title'], article['summary'], 'Knowledge base', body))
    rows = [(f"<a href='{u('/kb/' + article['slug'] + '.html')}'>{esc(article['title'])}</a>", esc(article['source_name']), esc(article['why'])) for article in KB_ARTICLES]
    source_rows = source_inventory()[:40] or [('No local downloaded sources found', 'n/a')]
    body = panel('Knowledge and reference articles', '<p>These pages normalize saved source material into one consistent reading format.</p>' + table(['Article', 'Source', 'Why it matters'], rows))
    body += panel('Saved source inventory snapshot', '<p>Raw sources remain in the project for traceability. The canonical reading experience is the normalized HTML pages.</p>' + table(['Saved source file', 'Type'], source_rows))
    write(WEB_ROOT / 'kb' / 'index.html', page('Knowledge Base', 'Normalized knowledge articles and saved-source inventory.', 'Knowledge base', body))


def status_rows() -> list[tuple[str, str, str]]:
    return [('Public browser-first pages', 'validated', 'Built from scripts/build_delivery_system.py and checked by validate_delivery_system.ps1.'), ('Facilitator and backup packs', 'validated', 'Generated HTML docs and checked for required presence and key content.'), ('Exercise and reflection system', 'validated', 'Prompt cards, scaffolds, and printable/saveable report pages are present.'), ('Pre-event messages and survey content', 'completed but not live-tested', 'Content is ready to send but actual audience response is still future work.'), ('Optional VM path', 'completed but secondary', 'Retained as optional/operator-only material.'), ('Archived legacy VM-first material', 'archived', 'Moved out of the active participant path.'), ('Current package overlay', 'validated', 'Fresh overlay built under .ai_uploads after validation.'), ('Real event-day staffing names', 'next work', 'Needs organizer-specific names if they change.')]


def segment_sections() -> str:
    parts = []
    for time_slot, title, focus, talking, transition, fast, slow, cut in SEGMENTS:
        parts.append(section(f"{time_slot} | {title}", f"<p><strong>Focus:</strong> {esc(focus)}</p><p><strong>Exact talking points:</strong></p>{bullet(talking)}<p><strong>Transition:</strong> {esc(transition)}</p><p><strong>Group moving fast:</strong> {esc(fast)}</p><p><strong>Group moving slow:</strong> {esc(slow)}</p><p><strong>Cut for time:</strong> {esc(cut)}</p>"))
    return ''.join(parts)


def demo_sections(kind: str | None = None, answer_key: bool = False) -> str:
    parts = []
    for demo in DEMOS:
        if kind and demo['kind'] != kind:
            continue
        extra = f"<p><strong>Suggested facilitator questions:</strong></p>{bullet(demo['questions'])}<p><strong>Optional learner variation:</strong> {esc(demo['followup'])}</p>"
        if answer_key:
            extra += f"<p><strong>Likely learner misunderstandings:</strong> Learners may assume longer prompts are always better, or that polished output means correct output.</p><p><strong>Suggested coaching phrase:</strong> {esc(demo['coaching'])}</p><p><strong>Strong learner extension:</strong> {esc(demo['strong_extension'])}</p><p><strong>Support prompt for a struggling learner:</strong> {esc(demo['support_prompt'])}</p>"
        body = f"<p><strong>Weak prompt:</strong> {esc(demo['weak'])}</p><p><strong>Why weak:</strong> {esc(demo['why'])}</p><p><strong>Improved prompt:</strong> {esc(demo['improved'])}</p><p><strong>What changed:</strong> {esc(demo['changed'])}</p><p><strong>Likely result difference:</strong> {esc(demo['difference'])}</p><p><strong>Key teaching point:</strong> {esc(demo['teaching'])}</p>{extra}"
        parts.append(section(demo['name'], body))
    return ''.join(parts)


def docs_map() -> dict[str, tuple[str, str, str]]:
    common_parent = section('Parent trust layer', table(['Category', 'Details'], [('Required', 'Browser access, a device if available, and a charger or power cable.'), ('Optional', 'A family-approved free account and an Ethernet cable if available.'), ('Not needed by default', 'Local VM, local Python, terminal tools, complicated installs, or advanced coding setup.')]) + bullet(['What the session is: a browser-based introduction to AI and ChatGPT.', 'What it is not: a programming bootcamp, hacking session, or hidden install exercise.', 'What local changes are not expected by default: no VM, no coding tools, no advanced setup.', 'What fallback exists: browser-first, paired work, or presenter-led participation.']))
    common_youth = section('Youth participant pack', bullet(['What to bring: device if available, charger, optional Ethernet cable.', 'What to expect: short demos, guided prompt cards, one image prompt activity, reflection.', 'What to do if stuck: use Guided, borrow a starter card, ask for a sentence frame.', 'Where to save or print takeaways: the reflection/report page.']))
    common_leader = section('Leader support pack', bullet(['Support calm routing and power access.', 'Keep browser-first as the default message.', 'Use fallback routes early instead of derailing into advanced setup.', 'Escalate whole-room timing or support problems to the presenter.']))
    docs = {
        'project_coordination_dashboard.html': ('Project Coordination Dashboard', 'Current project status across public pages, docs, scripts, archive work, validation, and packaging.', section('Current state', '<p>The repository is normalized around a browser-first introductory AI night. Public content lives under <code>web/</code>, operator and coordination content lives under <code>docs/</code>, and optional VM/operator material remains clearly secondary.</p>') + section('Status table', table(['Area', 'Status', 'Notes'], status_rows())) + section('Locked learning structure', segment_table())),
        'current_state_validated_vs_unvalidated.html': ('Current State: Validated vs Unvalidated', 'Hard status model for major docs, pages, scripts, workflows, and packages.', section('Status matrix', table(['Area', 'Status', 'Notes'], status_rows()))),
        'repo_rationalization_plan.html': ('Repository Rationalization Plan', 'What was kept active, what was archived, and how the repo now separates public, operator, knowledge, and legacy content.', section('Normalization decisions', bullet(['Public content stays under web/.', 'Coordination, facilitator, communications, survey, and status docs stay under docs/.', 'Raw saved-source material stays under downloaded_sources/.', 'Archived legacy material moves under archive/.'])) + section('Saved-source snapshot', table(['Path', 'Type'], source_inventory()[:25] or [('No local downloaded sources found', 'n/a')]))),
        'workshop_delivery_architecture.html': ('Workshop Delivery Architecture', 'Browser-first delivery is primary. Optional VM and advanced operator paths are secondary only.', section('Primary model', '<p>Browser-first is the canonical participant path. Youth, leaders, presenter, leader test, and backup coverage are all designed to work without local VM installation by default.</p>') + section('Platform routing', table(['Platform', 'Primary route', 'Notes'], [('Windows x86-64', 'Browser-first', 'Optional VM may exist later but is not required.'), ('Windows ARM', 'Browser-first', 'Do not assume local VM support.'), ('Apple Silicon', 'Browser-first', 'Use local path only if separately validated.'), ('Chromebook', 'Browser-first or fallback', 'No local VM expectation.'), ('Shared family device', 'Browser-first', 'Minimize changes and respect family account choices.')]))),
        'platform_compatibility_matrix.html': ('Platform Compatibility Matrix', 'Routing by browser-first, optional VM, Apple Silicon alternative, or no-install fallback.', section('Compatibility matrix', table(['Platform', 'Primary route', 'Notes'], [('Windows x86-64', 'Browser-first', 'Optional VM possible but secondary.'), ('Windows ARM', 'Browser-first', 'No participant VM assumption.'), ('Apple Silicon', 'Browser-first', 'Use browser-first unless separately validated.'), ('Chromebook', 'Browser-first or fallback', 'No local VM expectation.'), ('Shared family device', 'Browser-first', 'Respect family account and privacy choices.')]))),
        'participant_pathways.html': ('Participant Pathways', 'Youth, parent, leader, facilitator, and technical operator pathways with low-friction defaults.', section('Stakeholder pathways', table(['Stakeholder', 'Primary page', 'What they need'], [('Youth', 'web/participant/index.html', 'Prompt cards, low-pressure instructions, reflection page.'), ('Parent/guardian', 'web/parent/index.html', 'Warm trust layer and clear required/optional guidance.'), ('Leader', 'web/leader/index.html', 'Support role, fallback guidance, escalation cues.'), ('Presenter', 'web/facilitator/run-of-show.html', 'Run order, talking points, answer key, fallback notes.'), ('Operator', 'docs/project_coordination_dashboard.html', 'Build, archive, validate, and package status.')]))),
        'parent_information_pack.html': ('Parent Information Pack', 'Trust layer for families, including what is required, what is optional, and what is not needed by default.', common_parent),
        'youth_prework_and_takeaway_pack.html': ('Youth Prework and Takeaway Pack', 'What to bring, how the session works, starter prompts, and after-session takeaways.', common_youth + section('Locked 90-minute structure', segment_table())),
        'leader_operations_pack.html': ('Leader Operations Pack', 'Leader support role, logistics, fallback logic, and escalation guidance.', common_leader),
        'presenter_operations_pack.html': ('Presenter Operations Pack', 'Run-of-show, demo scripts, fallback instructions, and closing guidance.', section('Presenter checklist', bullet(['Open the run of show, demo cards, exercise page, and reflection page before people arrive.', 'Keep browser-first as the default message.', 'Use the fast/slow/cut notes instead of improvising a new structure.', 'Keep the Codex demo short and clearly secondary.'])) + section('Run order', segment_table())),
        'readiness_checker_spec.html': ('Readiness Checker Spec', 'Browser-first routing logic, optional VM checks, and result outputs.', section('Primary behavior', '<p>The readiness checker prioritizes browser-first suitability first. It then reports whether an optional advanced path is even relevant.</p>') + section('Outputs', table(['Output', 'Purpose'], [('User-friendly result', 'Tells the participant the default route and next action.'), ('Operator-friendly result', 'Summarizes platform, browser, memory, and optional VM capability.'), ('JSON artifact', 'Stored under artifacts for validation evidence.'), ('.log.txt', 'Stored under logs for traceability.')]))),
        'install_launch_cleanup_lifecycle.html': ('Install, Launch, and Cleanup Lifecycle', 'Lifecycle for browser-first readiness and the optional advanced path.', section('Browser-first lifecycle', table(['Step', 'Expectation'], [('Readiness', 'Check browser, device, charger, and basic access.'), ('Install', 'No local install required for the core session.'), ('Launch', 'Open the public site and session pages in the browser.'), ('Session use', 'Use demos, prompt cards, and reflection/report pages.'), ('Shutdown', 'Save or print takeaways and sign out if appropriate.'), ('Optional advanced cleanup', 'Only relevant if a separate optional VM/operator path was used.')]))),
        'browser_first_environment_plan.html': ('Browser-First Environment Plan', 'Canonical browser-based event environment and low-friction access model.', section('Canonical environment', '<p>The canonical event environment is the public site plus browser-based AI tools. It is intentionally simple enough to support mixed comfort levels, shared family devices, and fallback participation.</p>')),
        'local_vm_optional_path_plan.html': ('Local VM Optional Path Plan', 'Secondary VM/operator path retained for compatible advanced scenarios only.', section('Secondary-only path', '<p>The local VM path is retained only as an optional advanced/operator path. It is not the default participant expectation and is not needed for the locked 90-minute session.</p>')),
        'apple_silicon_and_nonstandard_device_path.html': ('Apple Silicon and Nonstandard Device Path', 'Route Apple Silicon and constrained devices to browser-first unless a separate validated path exists.', section('Routing rule', '<p>Route Apple Silicon and constrained devices to browser-first unless a separate local path has been independently validated.</p>')),
        'risk_and_fallback_matrix.html': ('Risk and Fallback Matrix', 'What happens when devices, browsers, accounts, or internet access are limited.', section('Fallback matrix', table(['Risk', 'Fallback'], [('No device', 'Pair with leader or use presenter-led participation.'), ('No account', 'Use shared demo visibility and prompt cards.'), ('Internet issue', 'Use printed prompt cards and verbal reflection.'), ('Image tool unavailable', 'Compare weak and strong prompts verbally and skip image generation.'), ('Group pace mismatch', 'Use the fast/slow notes in the run of show.')]))),
        'codex_rules_and_guardrails_examples.html': ('Codex Rules and Guardrails Examples', 'Facilitator-facing examples showing why clearer requests produce safer, more useful coding help.', demo_sections('codex', True)),
        'example_prompt_and_ruleset_takeaway.html': ('Example Prompt and Ruleset Takeaway', 'Take-home examples of weak vs improved prompts and reusable ruleset components.', section('Reusable prompt upgrade rules', bullet(['Say what the answer is for.', 'Say who it is for.', 'Ask for a format.', 'Add one or two limits.', 'Review the result and name the gap.'])) + demo_sections()),
        'completed_vs_blocked_vs_next_actions.html': ('Completed vs Blocked vs Next Actions', 'Explicit separation of validated work, archived work, blocked work, and next work.', section('Status table', table(['Area', 'Status', 'Notes'], status_rows()))),
        'final_packaging_and_release_plan.html': ('Final Packaging and Release Plan', 'What is packaged, where it is published, and what to verify before release.', section('Release contents', bullet(['Public browser-first pages', 'Facilitator and backup facilitator materials', 'Parent, youth, and leader packs', 'Exercise, reflection, communications, and survey packs', 'Knowledge pages, scripts, logs, reports, artifacts, and archive evidence']))),
        'facilitator_talking_points.html': ('Facilitator Talking Points', 'Exact talking points, transitions, and pace notes for every session block.', segment_sections()),
        'facilitator_answer_key.html': ('Facilitator Answer Key', 'Weak prompts, improved prompts, teaching points, and coaching support.', demo_sections(None, True)),
        'session_run_of_show_90_minutes.html': ('Session Run of Show: 90 Minutes', 'Locked 90-minute browser-first learning plan.', segment_sections()),
        'session_slide_content_and_speaker_notes.html': ('Session Slide Content and Speaker Notes', 'Slide-content-equivalent HTML for building a real slide deck.', section('Slide-content equivalent', table(['Slide title', 'On-screen text', 'Speaker notes', 'Suggested visual', 'Backup visual', 'Live-demo cue'], [('Welcome and title', 'AI Night: Browser-First Intro to AI', 'Welcome the group, normalize mixed comfort levels, and say that browser-first is the default.', 'Workshop title slide with simple agenda list', 'Printed agenda', 'Open the landing page'), ('What AI is', 'AI tools find patterns, generate drafts, and offer options quickly.', 'Keep the explanation plain and grounded in everyday examples.', 'Simple icon set for summarize, rewrite, brainstorm', 'Whiteboard list', ''), ('What ChatGPT is', 'ChatGPT is a browser-based AI assistant for drafting, explaining, and organizing ideas.', 'Emphasize that it helps with thinking and starting, not automatic truth.', 'Browser screenshot with safe cropped UI', 'Text-only slide', 'Show one browser tab'), ('What AI is good at', 'Good at drafting, summarizing, brainstorming, and giving first versions.', 'Connect this to school, hobbies, planning, and creativity.', 'Four short use-case tiles', 'Printed examples sheet', ''), ('What AI gets wrong', 'AI can be wrong, too generic, too confident, or missing context.', 'Keep the safety message calm, not scary.', 'Comparison of useful vs unchecked output', 'Verbal example only', ''), ('Weak vs strong prompts', 'Goal + audience + format + limits usually leads to more useful results.', 'Tie this directly to Demo 1 and the exercise system.', 'Before-and-after prompt comparison', 'Prompt on board', 'Run Demo 1'), ('Safe use', 'Use AI to help you think, not to replace thinking.', 'Mention checking facts, privacy choices, and shared-device judgment.', 'Checklist with check marks', 'Printed safe-use card', ''), ('Image generation prompts', 'Image prompts improve with subject, mood, style, colour, and layout.', 'Keep it practical and brief before Demo 2.', 'Poster prompt comparison', 'Printed side-by-side images', 'Run Demo 2'), ('Reflection prompts', 'What changed? What worked? What surprised you?', 'Remind learners that reflection is part of the skill.', 'Short reflection prompt list', 'Verbal reflection only', ''), ('Closing and takeaways', 'Ask clearly. Check what matters. Keep the good prompts you made tonight.', 'End with confidence and a reminder that browser-first is enough for continued practice.', 'Three takeaway tiles', 'Printed takeaway sheet', '')]))),
        'demo_prompt_bank_chatgpt.html': ('Demo Prompt Bank: ChatGPT', 'Three browser-first ChatGPT prompt comparison demos with teaching notes.', demo_sections('chatgpt')),
        'demo_prompt_bank_images.html': ('Demo Prompt Bank: Images', 'Two image prompt comparison demos with teaching notes.', demo_sections('image')),
        'demo_prompt_bank_codex_facilitator_only.html': ('Demo Prompt Bank: Codex Facilitator Only', 'Short facilitator-only Codex comparison demo.', demo_sections('codex')),
        'backup_facilitator_pack.html': ('Backup Facilitator Pack', 'Low-prep handoff pack for another adult stepping in.', section('One-page event summary', '<p>This is a browser-based introduction to AI and ChatGPT for Scouts and Venturers. The main lesson is that clearer prompts usually lead to more useful results.</p>') + section('Full 90-minute run order', segment_table()) + section('Critical tabs/pages to open', bullet(['web/facilitator/run-of-show.html', 'web/shared/examples.html', 'web/participant/exercises.html', 'web/participant/reflections.html', 'web/parent/index.html'])) + section('What to prioritize', bullet(['Keep the room calm and browser-first.', 'Run Demo 1, one hands-on block, Demo 2, one image activity, reflection, and closing.', 'If overwhelmed, ignore optional depth and stick to the locked timing table.'])) + section('What to ignore if overwhelmed', '<p>Ignore optional extensions, extra share-outs, and any advanced tooling discussion. Keep the prompt-comparison pattern visible and move the room forward.</p>') + section('5-minute prep', bullet(['Open the run of show and demo cards.', 'Open the participant exercise page.', 'Read the first two timing blocks and the closing remarks.'])) + section('10-minute rescue plan', bullet(['Welcome and reassure the group.', 'Run Demo 1 with the study helper prompt.', 'Let learners do one Guided card.', 'Run one image prompt comparison.', 'Close with reflection and safe-use reminders.'])) + section('Fallback plan', bullet(['If internet is weak, use verbal comparisons and printed prompt cards.', 'If image tools fail, keep the image prompt discussion without generation.', 'If account access fails, pair learners or use presenter-led examples.'])) + section('Contact and escalation notes', '<p>Escalate schedule and room-management decisions to the presenter or lead organizer. Do not improvise a new architecture on session night.</p>')),
        'exercise_system_overview.html': ('Exercise System Overview', 'How Guided, Build, Remix, and Stretch work across all exercise categories.', section('Exercise model', '<p>The learner progression system uses four non-ranked levels only: Guided, Build, Remix, and Stretch.</p>') + section('Card matrix', exercise_table()) + section('Routing rules', bullet(['Default unsure learners to Guided.', 'Move early finishers to Build or Remix.', 'Use Stretch only when a learner is already moving well and wants more challenge.', 'Use the optional Codex observation task only after the facilitator demo.']))),
        'exercise_cards_guided_build_remix_stretch.html': ('Exercise Cards: Guided, Build, Remix, Stretch', 'Concrete prompt cards for all learner routes.', ''.join(section(f"{card['category']} | {card['level']}", f"<p><strong>Weak starter prompt:</strong> {esc(card['starter'])}</p><p><strong>Scaffolded improvement tip:</strong> {esc(card['tip'])}</p><p><strong>Note prompt:</strong> {esc(card['note'])}</p><p><strong>Expectation-vs-result prompt:</strong> {esc(card['result'])}</p><p><strong>Follow-up prompt:</strong> {esc(card['followup'])}</p><p><strong>Support move:</strong> {esc(card['support'])}</p>") for card in exercise_cards())),
        'reflection_and_takeaway_pack.html': ('Reflection and Takeaway Pack', 'Reflection prompts and keepable post-session structure.', section('Reflection prompts', bullet(['What changed?', 'What worked?', 'What surprised you?', 'What gap remained?', 'What would you do differently next time?'])) + section('Takeaway structure', '<p>Learners should leave with one improved prompt, one note about what changed, one note about what to verify, and one next-step idea.</p>') + section('Printable/saveable format', '<p>The HTML reflection/report page supports browser draft saving, JSON download, and print/PDF output.</p>')),
        'pre_event_communications_plan.html': ('Pre-Event Communications Plan', 'Send order, audiences, and message purpose.', section('Send sequence', table(['When', 'Audience', 'Message focus'], [('One week before', 'Parents or guardians', 'What the session is, what to bring, browser-first expectations, optional account choice.'), ('One week before', 'Participants', 'What to expect, what to bring, reassurance, low-pressure prep.'), ('One week before', 'Leaders', 'Support role, fallback guidance, and logistics.'), ('Short reminder', 'All audiences', 'Charger, browser, optional Ethernet, and fallback reassurance.'), ('Day before', 'Participants and families', 'Tomorrow reminder, device check, no VM required by default.')]))),
        'pre_event_parent_message.html': ('Pre-Event Parent Message', 'Ready-to-send family messaging for the browser-first event.', section('Parent and guardian message one week before', '<p>Hello families, next week we are running a browser-based introduction to AI and ChatGPT for Scouts and Venturers. The session is focused on safe, practical, guided learning. Participants will compare weak and stronger prompts, try guided activities in the browser, and reflect on what made the outputs more useful. Please send a device if available, plus a charger or power cable. An Ethernet cable is optional if you already have one. The main path is browser-first. No VM is required by default, and no coding tools are required by default. A free ChatGPT account may be helpful for some learners, but families should use their own judgment about account setup and shared devices. If your child does not have a suitable device, cannot use an account, or you do not want any installs, they can still participate through the fallback path. If you are worried or stuck, contact the event organizer before the session so we can route your child well.</p>') + section('Short reminder message', '<p>Reminder for AI Night: bring a device if available, plus a charger. Browser access is the main requirement. No VM or coding setup is required by default. Optional Ethernet cable if you already have one.</p>') + section('Day-before reminder', '<p>Tomorrow is AI Night. Please charge devices tonight, bring the charger, and use the browser-first route as the default expectation. If your family prefers no installs, that is completely fine for the core session.</p>')),
        'pre_event_participant_message.html': ('Pre-Event Participant Message', 'Ready-to-send learner messaging for the browser-first event.', section('Participant message one week before', '<p>Next week is AI Night. You do not need to be a coder. We will use AI in the browser, compare weak and stronger prompts, try one image prompt activity, and keep the night practical and low-pressure. Bring a device if you have one, plus a charger or power cable. An Ethernet cable is optional. Browser access is the main requirement. No VM is required by default and no coding tools are required by default. If your device is not ready or you do not have one, you can still participate through the fallback plan. If you want to do a tiny bit of prep, think of one topic you care about: school, hobbies, planning, art, or creativity.</p>') + section('Short reminder message', '<p>AI Night reminder: bring a charger, open the browser-first pages, and come with one topic you care about. Low-pressure is the goal.</p>')),
        'pre_event_readiness_and_homework.html': ('Pre-Event Readiness and Homework', 'What to do before arrival and the leader briefing note.', section('Before-arrival readiness', bullet(['Device charged and charger packed', 'Browser available', 'Optional account decision made by the family', 'Optional Ethernet cable packed if already available', 'One topic chosen for practice'])) + section('Leader briefing message one week before', '<p>Please support the browser-first delivery model. Help youth arrive with chargers, get to the right page, and use fallback routes early if devices or accounts are not ready. Do not derail the event into VM or coding setup. Escalate room-level timing or support issues to the presenter.</p>')),
        'pre_event_survey_and_feedback_plan.html': ('Pre-Event Survey and Feedback Plan', 'Concrete survey wording and how it affects support planning.', section('Survey question wording', table(['Topic', 'Exact question'], [('Prior AI exposure', 'How much have you used tools like ChatGPT before?'), ('What they hope to learn', 'What do you most want to be able to do after this session?'), ('What they do not want to see', 'Is there anything you do not want this session to focus on?'), ('Interests', 'Which topics interest you most: school, creativity, planning, hobbies, or something else?'), ('Concerns', 'Do you have any concerns about AI tools or this session?'), ('Comfort level', 'How comfortable do you feel trying a new browser-based tool in a group?'), ('Device type', 'What device would you likely bring?'), ('Can bring device', 'Will you be bringing your own device?'), ('Browser-based account readiness', 'Could you use a browser-based account if your family chooses?'), ('Support or accommodation', 'Is there anything that would help you feel more comfortable or supported in the session?'), ('Anything the facilitator should know', 'Is there anything you want the facilitator or leaders to know ahead of time?')])) + section('How survey responses affect planning', bullet(['Device and account answers affect pathway assignment and fallback coverage.', 'Interest answers help the facilitator pick relevant examples.', 'Support or accommodation answers help leaders reduce overload and decision pressure.', 'Concerns help frame parent and youth reassurance.'])) + section('Short parent input version', '<p>Does your child have a device they can bring? Are you comfortable with a browser-based free account if needed? Is there anything that would help your child feel more supported in the session?</p>')),
        'youth_participant_pack.html': ('Youth Participant Pack', 'Direct, low-pressure participant guidance.', common_youth),
        'leader_support_pack.html': ('Leader Support Pack', 'Leader support role, what to help with, and what to escalate.', common_leader),
        'kb_index.html': ('KB Index', 'Normalized knowledge article overview.', section('Knowledge article index', table(['Title', 'Why this matters', 'Key takeaway'], [(article['title'], article['why'], article['takeaway']) for article in KB_ARTICLES]))),
        'kb_article_template.html': ('KB Article Template', 'Reusable article structure for normalized HTML knowledge pages.', section('Standard KB article structure', bullet(['Title', 'Original source reference', 'Date normalized', 'Tags or category', 'Readable summary', 'Why this matters for the workshop', 'Key takeaway block', 'Related reading links']))),
    }
    return docs


def build_docs() -> None:
    docs = docs_map()
    for filename in REQUIRED_DOCS:
        title, summary, body = docs[filename]
        write(DOCS_ROOT / filename, doc_page(title, summary, body))


def copy_mirror() -> None:
    if GITHUB_ROOT.exists():
        for path in GITHUB_ROOT.iterdir():
            if path.name == '.git':
                continue
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
    else:
        GITHUB_ROOT.mkdir(parents=True, exist_ok=True)
    for path in WEB_ROOT.iterdir():
        target = GITHUB_ROOT / path.name
        if path.is_dir():
            shutil.copytree(path, target, dirs_exist_ok=True)
        else:
            shutil.copy2(path, target)
    (GITHUB_ROOT / '.nojekyll').write_text('', encoding='utf-8')
    log(f"Mirrored web output to {GITHUB_ROOT}")


def main() -> None:
    ensure_dirs()
    log('Browser-first build started')
    build_public_pages()
    build_kb()
    build_docs()
    copy_mirror()
    manifest = {'timestamp': STAMP, 'web_files': sorted(rel(path, WEB_ROOT) for path in WEB_ROOT.rglob('*.html')), 'doc_files': sorted(rel(path) for path in DOCS_ROOT.glob('*.html')), 'kb_articles': [article['slug'] for article in KB_ARTICLES], 'exercise_cards': len(exercise_cards()), 'source_inventory_count': len(source_inventory())}
    write_json(ARTIFACT_DIR / 'build_manifest.json', manifest)
    report = doc_page('Build Delivery System Report', 'Summary of the production-readiness browser-first build pass.', section('Outputs', table(['Type', 'Count'], [('Web HTML pages', str(len(manifest['web_files']))), ('Docs', str(len(manifest['doc_files']))), ('KB articles', str(len(manifest['kb_articles']))), ('Exercise cards', str(manifest['exercise_cards'])), ('Saved source files seen', str(manifest['source_inventory_count']))])) + section('Primary outcome', '<p>The active public system is browser-first and production-ready for learner, family, leader, presenter, backup facilitator, and operator use. Optional VM and advanced tooling remain secondary only.</p>'))
    write(REPORT_DIR / 'build_delivery_system_report.html', report)
    log('Browser-first build completed')


if __name__ == '__main__':
    main()
