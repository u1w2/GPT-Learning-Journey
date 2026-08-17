#!/usr/bin/env python3
"""Check GPT-Learning-Journey repository structure and CURRENT.md sections."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DIRS = [
    "ai/protocols",
    "curriculum/01-engineering",
    "curriculum/02-system-design",
    "curriculum/03-software-architecture",
    "curriculum/04-distributed-systems",
    "curriculum/05-cloud-native",
    "curriculum/06-security",
    "curriculum/07-sre",
    "curriculum/08-business-architecture",
    "curriculum/09-ai-engineering",
    "curriculum/10-ai-architecture",
    "experience/patterns",
    "experience/trade-offs",
    "experience/failures",
    "experience/decisions",
    "experience/experience-cards",
    "interview",
    "learner/sessions",
    "projects/_template",
    "templates",
    "tools",
]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "ai/README.md",
    "ai/coach.md",
    "ai/reviewer.md",
    "ai/interviewer.md",
    "ai/red-team.md",
    "ai/protocols/chatgpt-cursor.md",
    "ai/protocols/cursor-startup.md",
    "ai/protocols/no-direct-answers.md",
    "ai/protocols/constraint-increment.md",
    "ai/protocols/git-evidence.md",
    "ai/protocols/capability-edge.md",
    "ai/protocols/reinforce.md",
    "learner/CURRENT.md",
    "learner/progress.md",
    "learner/capability.md",
    "learner/weak-points.md",
    "learner/mistakes.md",
    "learner/defects.md",
    "learner/profile.md",
    "templates/adr.md",
    "templates/experience-card.md",
    "templates/experiment.md",
    "curriculum/02-system-design/README.md",
]

CURRENT_SECTIONS = [
    "Current Stage",
    "Current Phase",
    "Current Task",
    "Current Project",
    "Status",
    "Current Goal",
    "Completed",
    "In Progress",
    "Current Capability",
    "Weak Points",
    "Unresolved Problems",
    "Latest Learning Result",
    "Next Single Task",
    "Evidence",
    "Last Updated",
]


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED_DIRS:
        path = ROOT / rel
        if not path.is_dir():
            errors.append(f"missing directory: {rel}")

    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"missing file: {rel}")

    current = ROOT / "learner" / "CURRENT.md"
    if current.is_file():
        text = current.read_text(encoding="utf-8")
        for section in CURRENT_SECTIONS:
            heading = f"## {section}"
            if heading not in text:
                errors.append(f"CURRENT.md missing section: {section}")
        if "API Question 1" not in text and "第一阶段" not in text:
            errors.append("CURRENT.md does not record the current API Design question")
        if "L3" not in (ROOT / "learner" / "capability.md").read_text(encoding="utf-8"):
            errors.append("capability.md does not define L3+ evidence rule")

    capability = ROOT / "learner" / "capability.md"
    if capability.is_file():
        text = capability.read_text(encoding="utf-8")
        for level in ["L0", "L1", "L2", "L3", "L4", "L5", "L6"]:
            if level not in text:
                errors.append(f"capability.md missing level: {level}")

    if errors:
        print("FAIL: repository structure check")
        for item in errors:
            print(f"- {item}")
        return 1

    print("PASS: repository structure check")
    print(f"checked dirs: {len(REQUIRED_DIRS)}")
    print(f"checked files: {len(REQUIRED_FILES)}")
    print(f"checked CURRENT sections: {len(CURRENT_SECTIONS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
