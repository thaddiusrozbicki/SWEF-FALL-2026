# Homework 4 submission

Keep this short. Do not paste your API key.

## What POST /ask does (2–3 sentences)

POST /ask takes a prompt sent from Insomnia and forwards it to OpenAI's Chat Completions API, using the API key loaded from `.env`. It returns the model's response as `{ "reply": "..." }`. If the prompt is missing it returns a 400, and if OpenAI rejects the request (like no credits or a bad key) it passes OpenAI's error message back.

## Confirm

- [ ] Insomnia got `{ reply: ... }`
- [x] I ran `git status` — `.env` and `node_modules` were **not** staged

Note: The route is written and set up, but I wasn't able to get a working OpenAI API key without paying, so I couldn't get a reply back.
