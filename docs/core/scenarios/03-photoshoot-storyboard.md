# Scenario 3 · Photoshoot → storyboard → image generation

**Type:** conceptual compatibility check. Fictional ceramic mug with a small printed mark. There is no photoshoot role yet; it is assumed only for this check.

**Question:** who makes the storyboard, and where does generation start?

| # | Step | Owner | Knowledge | Delegation | Records | Authority |
|---|---|---|---|---|---|---|
| 1 | User supplies product photos and asks for a five-image series | photoshoot | Photoshoot pack | — | assets `USER_PROVIDED` with rights; product entity, approved version | — |
| 2 | Clean, cropped references, one product per reference | photoshoot | Pack: clean references | — | derived assets with `parent_assets` and dependencies | — |
| 3 | Shot list and text storyboard | photoshoot | — | None: planning is the owner's work | storyboard v1 `proposed`; closing check | — |
| 4 | Optional cheap sketch storyboard: scope v1 drafted (5 low-cost frames) and quoted | photoshoot | — | — | scope v1 with quote; approval requested | — |
| 5 | User approves scope v1 | — | — | — | `execution_scope` approval | User |
| 6 | Production generates the sketches | production | — | `permission` | package, assets | Scope v1 |
| 7 | User approves the storyboard; photoshoot drafts scope v2 for final images | photoshoot | — | — | `direction` approval; scope v2 quoted, approval requested | User |
| 8 | Production generates finals; the small printed mark is composited from the real photo, not generated | production | Production pack: mark composite | `permission` | package; assets depending on the product version | Scope v2 |
| 9 | Independent review of identity, mark and rights, image by image | reviewer | — | `independent_review` | review C per image (each item of the batch) | — |

The answer to "who makes the storyboard?": the photoshoot owner plans it; Production generates any image, sketches included, because generating needs the `spend` level. A text storyboard needs no delegation.

## Gaps found

| Gap | Class | Note |
|---|---|---|
| Shot taxonomy and series background rules | Domain extension | Photoshoot pack |
| Product content as a deliverable type | Domain extension | Belongs to the area, not the core |
| Deterministic compositing as a Production route | Accepted limitation | Production's routes are decided when Production is designed |
