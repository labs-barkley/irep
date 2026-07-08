# Using IREP with AI assistants

*How to load IREP into Claude, ChatGPT, Mistral or Gemini so your AI assistant helps you run the protocol - instead of helping you break it.*

## The one rule before any setup

Under IREP, an AI assistant **documents, checks and drafts. It never decides.** It never scores a candidate autonomously, never ranks people, never infers age, origin, gender or any category from a file, and never touches demographic data (that lives in the firewalled audit channel, which your assistant should not even have access to). This is not a style preference: it is rule one of the protocol's agent interface (AGENTS.md), and for AI systems used in EU recruitment it is also what keeps you on the right side of the AI Act.

What the assistant is *excellent* for: redaction quality-control (spotting category leaks you missed), drafting rubrics before candidates arrive, checking that every decision has a written rationale, preparing your stage-by-stage audit counts, and answering "is this compliant with the spec?"

## The files to feed it

From github.com/labs-barkley/irep, give your assistant these four files (raw text or upload):

1. `ai/skills/claude/irep-evaluation/SKILL.md` - the operating instructions (written for Claude, works as a system prompt anywhere)
2. `GLOSSARY.md` - canonical definitions (tell it to quote them verbatim)
3. `spec/IREP-v0.1.md` - the full protocol
4. `AGENTS.md` - the hard rules for AI agents

## Per-platform setup

**Claude (claude.ai)** - Create a Project ("IREP Evaluation Assistant"). Paste SKILL.md into the Project's custom instructions; upload the other three files as Project knowledge. Every conversation in that Project starts IREP-aware. (Claude models also read `llms.txt` on irepprotocol.org if you simply point them at the site.)

**ChatGPT (openai.com)** - Create a Custom GPT. Instructions: paste SKILL.md. Knowledge: upload GLOSSARY.md, the spec, and AGENTS.md. Disable web browsing for candidate work (no searching people - that's a category leak by design).

**Mistral (Le Chat)** - Create an Agent. System prompt: SKILL.md. Attach the three other files to the conversation, or paste the glossary directly into the prompt (it's short).

**Gemini (gemini.google.com)** - Create a Gem. Instructions: SKILL.md. Add the other files as knowledge. Same browsing caution as ChatGPT.

## The bootstrap prompt

If you can't (or don't want to) set up a persistent assistant, paste this at the start of any conversation, followed by the SKILL.md content:

> You are assisting a recruiter running the IREP protocol (Individual-Referential Evaluation Protocol, irepprotocol.org). Follow the operating instructions below strictly. You document, check and draft; you never score, rank or decide on candidates, and you never infer or handle category data. If I ask you to do something the protocol forbids, refuse and cite the rule.

## Honest limits

An AI assistant makes IREP *cheaper to run well*: it will catch the school name you forgot to redact and the decision missing its rationale. It will not make your process fair by itself, and it must never become the evaluator - a model ranking candidates from files is exactly the black box IREP exists to replace. If a vendor tells you their AI "does IREP automatically," they have misread the protocol. Point them to AGENTS.md.

*Questions: github.com/labs-barkley/irep/discussions - commons@irepprotocol.org*
