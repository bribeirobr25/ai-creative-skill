# Scenario 3 · Photoshoot → storyboard → image generation

**Type:** conceptual compatibility check. Fictional backpack product series. There is no photoshoot role yet; it is assumed only for this check.

**Question:** who makes the storyboard, and where does generation start?

| # | Step | Owner | Knowledge | Delegation | Records | Authority |
|---|---|---|---|---|---|---|
| 1 | User supplies product photos and asks for a five-image series | photoshoot | Photoshoot pack | — | assets `USER_PROVIDED` with rights; product entity with its approved version | — |
| 2 | Clean, cropped references, one product each, no third-party marks | photoshoot | Pack: clean references (photoshoot study) | — | derived assets with `parent_assets` | — |
| 3 | Shot list and text storyboard | photoshoot | — | None: planning is the owner's work | deliverable `proposed`; closing check | — |
| 4 | Optional cheap sketch storyboard proposed as scope v1 (5 low-cost frames) | photoshoot | — | — | `execution_scope` v1 `proposed` with quote | — |
| 5 | User approves scope v1 | — | — | — | `execution_scope` approval | User |
| 6 | Production generates the sketches | production | — | `permission` | package, assets | Scope v1 |
| 7 | User approves the storyboard; photoshoot proposes scope v2 for final images | photoshoot | — | — | `direction` approval; scope v2 `proposed` | User |
| 8 | Production generates finals; the small label is composited from the real photo, not generated | production | Production pack: label composite | `permission` | package; assets linked to product version | Scope v2 |
| 9 | Independent review of identity, label and rights | reviewer | — | `independent_review` | review C per image (each item of the batch) | — |

The answer to "who makes the storyboard?": the photoshoot owner plans it; Production generates any image, sketches included, because generating needs the `spend` level. A text storyboard needs no delegation.

## Gaps found

| Gap | Class | Note |
|---|---|---|
| Shot taxonomy and series background rules | Domain extension | Photoshoot pack (gaps listed in the photoshoot study) |
| Product content as a deliverable type | Domain extension | The study's `PRODUCT_CONTENT` gap belongs to the area, not the core |
| Deterministic compositing as a Production route | Accepted limitation | Production's routes are decided when Production is designed |

No blocking gap.
