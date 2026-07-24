# Robot Task Video Annotation — VLA Training Data

A sample project demonstrating my annotation workflow for robot arm manipulation videos, used to generate structured training/evaluation data for Vision-Language-Action (VLA) models.

## Overview

This repo documents and enforces the annotation format I use to convert raw robot arm task videos into structured data: an **Intent**, a **Subtask breakdown**, a **Final Summary**, and a labeled **Outcome** with supporting **Rationale**. A JSON Schema defines the format precisely, and a validation script checks example annotations against it — mirroring the QA step I run on real annotation batches before submission.

## Repo structure

```
annotation-guidelines-sample/
├── README.md
├── requirements.txt
├── docs/
│   └── annotation-format.md      ← the 5-field schema, explained
├── schema/
│   └── annotation.schema.json    ← machine-readable JSON Schema
├── examples/
│   ├── sample-001.json           ← worked example: successful task
│   └── sample-002.json           ← worked example: failed task
└── scripts/
    └── validate.py                ← validates examples/ against the schema
```

## Try it

```bash
pip install -r requirements.txt
python scripts/validate.py
```

Expected output:
```
✓ sample-001.json — valid
✓ sample-002.json — valid

All 2 example annotation(s) passed validation.
```

## Why this format

- **Intent** captures the task-level goal a model should learn to associate with the visual sequence
- **Subtasks Summary** gives fine-grained, ordered motion steps — useful for models that need to reason about intermediate states, not just start/end
- **Final Summary** provides a natural-language recap, useful for models trained on narrative-style captions
- **Outcome + Rationale** creates labeled success/failure data with justification, useful for evaluation and reward-model training, not just imitation

Two examples are included on purpose — a `Success` case and a `Failure` case — since real annotation datasets need both, and rationale-writing for a failure case is a different (and often harder) skill than for a clean success.

## My process

1. Watch the full video once without annotating, to understand the complete task
2. Note the objects, their positions, and lighting/scene conditions
3. Draft the Intent based on start and end state
4. Break the middle of the video into discrete subtasks (typically 6-10 steps for a single pick-and-place)
5. Write the Final Summary as a standalone narrative (should make sense without reading the subtasks)
6. Assign Outcome and justify it with specific visual evidence, not just "it worked"
7. Validate the structured output against the schema before submission

## Context

Done as part of annotation work for AI training data platforms (e.g. Mercor, Encord), focused on Vision-Language-Action model datasets. Object descriptions in the public examples are generalized to avoid publishing exact task content that may be covered under a contractor agreement.
