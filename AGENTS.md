# AGENTS.md

## Cursor Cloud specific instructions

This repository (`GPT-Learning-Journey`) is a **documentation-only knowledge base** — an
AI-guided learning/growth curriculum written entirely in Markdown (Chinese-first). At the
time of writing it contains only `*.md` files.

Key implications for agents working here:

- **No application, services, or database.** There is nothing to boot, no ports to bind,
  no backend/frontend. Do not look for a dev server or `docker compose`.
- **No package manager / lockfile / toolchain.** There is no `package.json`,
  `requirements.txt`, `pyproject.toml`, etc. There are **no dependencies to install**, so
  the environment update script is intentionally a no-op.
- **No build / test / lint tooling is configured.** Do not assume `npm test`,
  `npm run build`, or a linter exists. "Testing" in this repo's docs (e.g. `tools/README.md`,
  the "Test Lab" concept) is a *methodology to be authored inside future project write-ups*,
  not an automated test suite.
- **Development = authoring Markdown.** The normal workflow is editing the `.md` files. The
  content is meant to be read on GitHub or any Markdown viewer.
- **Core product concept:** the cross-conversation learning protocol. `learner/CURRENT.md`
  is the persisted "current state" snapshot that a new AI conversation reads first to resume
  the learner's progress (`learner/sessions/` holds history). When editing learner state,
  keep `CURRENT.md` as a snapshot and put historical evidence under `learner/sessions/`.

### Previewing the docs (optional, dev-only)

There is no committed preview tooling. If you want to render the Markdown to a browsable
site during a session, you can use Python (`pip install markdown`) to convert the files and
`python3 -m http.server` to serve them. Render output to a temp directory (e.g. `/tmp`) —
**do not commit generated HTML** into the repo.

### If real code is added later

If/when actual project code is scaffolded (e.g. under `projects/`), update this section and
the environment update script with the real install/build/test/run commands for that stack.
