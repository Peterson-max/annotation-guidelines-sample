# Annotation Format

Each annotated video produces five fields:

## 1. Intent
One or two sentences stating the overall goal of the arm's movement — where it starts, what it interacts with, and what the end state looks like. Written from the arm's point of view (first person), matching the phrasing style used in the source task videos.

## 2. Subtasks Summary
A bullet-point, first-person, chronological breakdown of every discrete motion in the task. Each line is one atomic action (e.g. "lift," "move," "lower," "grasp," "release"). Granularity target: 6-10 steps for a single pick-and-place; more for multi-object or multi-stage tasks.

## 3. Final Summary
A short narrative paragraph that reads naturally on its own, without needing the subtask list. Restates the start state, the key action, and the end state in flowing prose rather than a list.

## 4. Outcome
One of: `Success`, `Failure`, `Partial`. Chosen based strictly on what's visible in the video — not assumed intent.

## 5. Outcome Rationale
A justification for the Outcome label, referencing specific, concrete visual evidence (e.g. "the object was grasped without slipping," "the arm did not complete the return motion"). Avoids vague statements like "it looked fine."

## Quality principles I follow
- Object descriptions are precise (color, shape, relative position) so the annotation is unambiguous even without watching the video
- No speculation about intent beyond what the video shows
- Consistent verb tense and first-person voice across all five fields
- Outcome Rationale never just restates the Outcome — it explains it
