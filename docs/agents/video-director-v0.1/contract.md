# Video Director v0.1 · Input and output contract

**Status:** proposal. The contract is meant to be reused by later specialists (photographer, script writer, researcher), so only the media-specific blocks are video-only.

## Rules for using it

- **Only one field is needed:** an idea or a brief. Everything else may be given, assumed or not needed. The Director fills what it can and lists every assumption the user should confirm.
- **Fields are information, not a questionnaire.** The Director asks only for what is missing and matters to the deliverable requested.
- **An authority overrides the Director's preference.** Every authority names its source.

## Input

```yaml
request:
  idea_or_brief:          # free text; may be vague ("I want to launch my product")
  deliverable_level:      # concept | creative_direction | storyboard | production_plan | finished_video
                          # finished_video needs Production and the user's approval of an execution scope
  user_profile:
    experience:           # beginner | intermediate | professional (stated or inferred, then confirmed)
    preferences_ref:      # taste or past feedback, if any (private half)

objective:                # why the video exists; kept separate from the type
  goal:                   # launch | sell | educate | entertain | build brand | other
  audience:
  desired_effect:         # what the viewer should feel, know or do
  call_to_action:
  success_signal:         # how the user will judge it (approval, views, sign-ups...)

video_type:               # what the video is: launch teaser, feature showcase, software demo,
                          # UGC-style ad, explainer, tutorial, talking head, episode...
medium:                   # how it is built: cinematic/photoreal generation | motion graphics |
                          # 2D | 3D | avatar | live footage | illustrated/parallax | hybrid
techniques: []            # optional: kinetic typography, morphing, parallax, stop-motion look...

specifications:
  duration_s:
  aspect_ratios: []       # 16:9, 4:3, 1:1, 3:4, 9:16...
  resolution:             # 480p, 720p, 1080p, 4K...
  frame_rate:
  languages: []
  platforms: []
  audio:                  # voice-over, dialogue, music, sound effects
  captions:

authorities:              # what must be respected, each with its source
  brand:                  # identity, voice, palette, logo rules
  products: []            # product truth: shape, colour, labels, real interface
  characters: []          # approved character sheets, voices
  story_bible:            # long-form only; owned by the Story Lead
  claims: []              # approved facts; anything else stays UNKNOWN
  rights: []              # licences and consents for every asset, face and voice
  budget:                 # limit and who approves an execution scope

references:               # one entry per asset
  - id:
    kind:                 # product | character | environment | interface | style | motion | audio
    source:
    rights:
    version:
    notes:

constraints:
  must_preserve: []
  must_avoid: []
  deadline:
```

## Output

The Director returns only the parts the deliverable level needs.

```yaml
direction_package:
  summary:
    objective:
    approach:             # the chosen direction in two or three sentences
    why:
    alternatives_considered: []   # when distinct concepts were useful or requested
  assumptions: []         # [{field, value, confirm: true}]
  planning_depth:
    level:                # light | standard | deep
    reasons: []
  dimension_policy:       # what is fixed and what is free
    - dimension:          # product, face, palette, camera, lighting, pacing...
      latitude:           # preserve | bounded variation | open exploration
      authority:          # the source that fixes it, or "user instruction", or "open"
  reference_review:
    - ref:
      role:
      status:             # sufficient | missing | inconsistent | unsuitable
      action:             # what to supply or change, and why
  creative_direction:     # written for another professional to execute
    concept:
    message:
    tone:
    pacing:
    camera_language:
    light_and_atmosphere:
    emotional_beats: []
    sound_direction:
    preserve: []
    avoid: []
  look:                   # moodboard / style frames
    references: []
    style_frames: []
    palette:
    materials:
    framing:
  storyboard:             # depth follows planning_depth
    - shot:
      purpose:            # what changes or what the viewer gains
      action:
      camera:
      duration_s:
      transition:
      references: []
      continuity_in_out:
      on_screen_text:     # none | rendered precisely in the graphics or edit layer
  repurposing:            # optional
    planned:
    reusable_assets: []
  proposed_execution_scope:   # a PROPOSAL, never authority; nothing runs on it
    scope_id:
    version:                  # any change makes a new version, which needs a new approval
    status: proposed          # proposed | approved | superseded (only the user's recorded approval changes it)
    approval_ref: null        # set only by the user's recorded approval
    permitted_operations: []  # e.g. generate key frames, animate approved frames, edit, add sound
    deliverables: []          # what is produced, with formats
    preserve: []              # what must stay fixed (product, identity, approved text)
    vary: []                  # what may vary, and within what range
    quantities:               # items per deliverable
    attempts_per_item:
    tool_classes: []          # kinds of route (reference-based generation, code-based motion graphics, avatar...), never a single provider
    spend_limit:              # amount and currency
    valid_until:
    shot_briefs: []
    cost_estimate:
    risks: []
  quality_focus:          # which of artistic / technical / commercial matter most here, and why
  open_questions: []
```

## Approval points the contract produces

- **Standard and deep levels:** the user approves the creative direction before pre-production goes further.
- **Every level:** the Director only *proposes* an execution scope. It becomes authority when the user approves that exact version, and the approval is recorded in `approval_ref`. Nothing outside the approved scope is covered, however much budget remains. A changed scope is a new version that needs a new approval (ADR-0006 D6; the frozen Execution Contracts' batch template binds an approval to what is preserved and varied, counts, attempts, route class and spend envelope). No runtime implementation is part of v0.1.
