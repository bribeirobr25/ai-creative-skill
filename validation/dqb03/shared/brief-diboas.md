# Fixed brief D2 — diBoaS Practice

diBoaS is a **real** pre-launch money app. Its web app **Practice** is live with play money only. This website
presents Practice: a place to rehearse money decisions with practice credits and real market history before any real
money exists. Everything below is the only product truth you may use. Do not add facts, numbers or claims.

## Context, audience and goal

diBoaS helps people separate money by what it is meant to do, understand the path and see the risk before they
decide. Real-money services are **not** live: "diBoaS is NOT currently offering financial services." Practice is the
part people can use today. Audience: a smart adult who was failed by the financial system, including an older,
non-technical reader; the copy must be understood and trusted by that reader.

The visit should: explain what Practice is in plain language; show how a practice cycle works, step by step; let the
visitor try a small local preview of "Your system" (how weekly credits split across goals); send people to Practice;
and offer a local waitlist for the real-money version. Language: **English**.

Voice: plain, calm and specific; a peer, not a teacher. **Never sell, promise or advise.** Upside always travels
with its risk. Write "Practice", never "Sandbox". Do not use: yield, APY, DeFi, stablecoin, blockchain, crypto jargon,
risk-free, guaranteed, safe, passive income, limited-time, "unlock", "seamless", "empower", emoji, em-dashes, urgency
or countdowns, "most popular" or "best" badges, social proof counts, invented figures or balances. Never call
practice credits money, rewards or winnings, and never imply they convert to anything. Never call diBoaS a bank or a
savings account.

## Identity: fixed and open

Fixed: name written exactly **diBoaS**; logo files in `assets/` (`logo-wordmark-onlight.webp`,
`logo-wordmark-ondark.webp`, `logo-mark.avif`). Use them as they are; do not redraw, recolour or distort them.
Brand colour authority: teal is reserved for **action and live data** (`#0f766e` for buttons and accessible teal
text; `#14b8a6` and `#0d9488` brand teal); warmth comes from paper and copper (`#f4f0e8` paper, `#ebe5d8` deeper paper,
`#14110f` editorial ink, `#b67d44` copper, `#875a2b` copper text); deep ink `#0b1f24` for dark sections. No gold, no
purple or blue startup gradients, no pure `#000` or `#fff`.
Brand fonts present in the shared pool: Fraunces (used by the Practice app), Space Grotesk and Inter (used on the
marketing site). Using them is recommended but not required.

Open: layout, grid, scale, composition, rhythm, image treatment and framing via CSS, how you combine the brand
colours, components, micro-interactions and discreet transitions. There is no required reference layout.

## Required content

Hero title: "Practice money decisions before they're real."
Hero text: "Practice gives you 10,000 practice credits, real market history and a calendar that keeps moving. Set goals,
decide where each dollar goes, and see what the market actually did. No real money moves."
Primary action: "Start practicing" (a link to `https://app.diboas.com`, opening in the same tab).
Secondary action: "Join the waitlist for real money".

How a practice cycle works (use these facts; order and presentation free):
1. **Claim:** you receive 10,000 practice credits. "They have no real-world value and never convert to real money."
2. **Goals:** name a goal, give it a target and a time horizon. Strategies appear as a filter, the same unranked list
   for everyone: "You choose. diBoaS never advises."
3. **Your system:** "Decide how each dollar moves toward your goals." You split incoming credits by percentage; what
   you do not assign "Stays in Available". Nothing is pre-filled.
4. **Every week:** 1,000 practice credits arrive on the real calendar, whether or not you are there. You approve or
   decline what your rule would do with them. Credits pause when your balance reaches 20,000.
5. **Life happens:** in your third week, a simulated 1,500 expense shows up. "A practice scenario. The decision is
   real; the money is not." "No rush and no deadline. It waits until you want it."
6. **Time machine:** advance the clock by one month or one year and replay what the market actually did. It can fall:
   "Over this stretch it fell. That happens, and it is what the market actually did."
7. **Month report:** "Every dollar is explained below." History: "Every cent accounted for. Every balance reconciles."
8. **Review before you stop:** leaving a strategy shows its reference cost first, 0.39% with a 0.25 minimum per
   position. "For information only. These reference costs are not charged or deducted in Practice and do not reduce
   the Practice outcome."
Other facts you may state: "Nothing moves until you approve. This is play money." Practice progress is saved in the
browser on this device. Practice uses real market data.

Real money (waitlist section): "Real-money diBoaS is not live. diBoaS opens in each market only when its legal path is
confirmed." Do **not** state any minimum amount, fee cap or rates of return.

FAQ (at least these four, expandable; answers exactly as written):
- "Can practice credits become real money?" — "No. Practice credits have no real-world value and never convert to real
  money."
- "Is this financial advice?" — "No. Practice does not provide financial or investment advice. You choose. diBoaS never
  advises."
- "Can the numbers go down?" — "Yes. The time machine replays what the market actually did, so a stretch can lose
  value. That happens."
- "Is diBoaS a bank?" — "No. diBoaS is not a bank account, not a savings account and not a guarantee. Real-money
  services are not live yet."

Footer (visible, verbatim):
- "Practice is a simulation. No real money moves. Practice does not provide financial or investment advice. Practice
  Credits are simulated practice units with no monetary value; they are not fiat currency or Rewards. They cannot be
  converted into real money, withdrawn, redeemed or transferred."
- "This content is for educational purposes only and does not constitute investment advice, financial advice, or any
  other type of advice. Past performance is not indicative of future results. Any historical data or simulations are
  hypothetical and not guarantees."
- "The value of crypto-assets may fluctuate. You may lose some or all of your money. Crypto-assets are not covered by
  deposit guarantee schemes."
- "diBoaS is NOT currently offering financial services."
- "Preview website. No data is sent."
- Tagline: "Your money deserves an explanation."

## Required experiences and behaviour

1. Homepage with the proposition, the primary and secondary actions, and a view of the practice cycle.
2. A "How Practice works" page or route with the eight steps above.
3. "Your system" preview: a weekly amount of 1,000 practice credits and three example goals named "Emergency
   reserve", "Trip" and "New laptop", each with a percentage input (0–100, whole numbers). Show the credits each goal
   would receive and the amount that "Stays in Available". If the percentages add up to more than 100, show an error
   and no negative or misleading amounts. Label it as a local preview with practice credits.
4. Waitlist: an email field validated locally and a "Join the waitlist" button. An invalid email shows an inline error
   and no confirmation. A valid email shows a local confirmation that says nothing was sent. No account or real
   submission.
5. FAQ with expandable answers, operable by keyboard.
6. Back-and-forth navigation by URL/hash; home, how it works, your system and waitlist reachable on desktop and
   mobile; no decorative controls without a destination.
7. Keyboard, visible focus, accessible labels, alt text and `prefers-reduced-motion`.
8. No external network calls on load: no CDN, analytics, embeds or remote fonts. The only external link is
   `https://app.diboas.com`.

## Required instrumentation (invisible to users)

`data-testid` on functional elements, presentation free:
`nav-home`, `nav-how`, `nav-system`, `nav-waitlist`, `cta-practice` (the "Start practicing" link, at least one),
`how-step` (one per step, eight on the how-it-works view), `system-pct-emergency`, `system-pct-trip`,
`system-pct-laptop` (number inputs), `system-amount-emergency`, `system-amount-trip`, `system-amount-laptop`,
`system-available`, `system-error`, `waitlist-email`, `waitlist-submit`, `waitlist-error`, `waitlist-confirmation`,
`faq-item` (each question toggle).

Reference results: 40 / 30 / 0 gives 400, 300, 0 and 300 staying in Available. 70 / 50 / 0 shows the error.

## Materials

- `assets/`: 22 files and `credits.json`: the three logo files, two Practice app illustrations (watercolour coast,
  light and night) and 17 photo-real images from the brand library. Use without editing pixels; crop and frame with
  CSS without distorting proportions. Using every image is not required. No screenshots of the app exist; do not
  fake app screens with invented balances or numbers. Simple UI illustrations you build in HTML/CSS are allowed only
  if every number shown comes from this brief.
- `fonts/`: shared pool of self-hosted OFL families (`fonts.css`, `FONTS.md`); optional.
