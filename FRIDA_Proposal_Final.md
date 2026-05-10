# FRIDA — First Response Integrated Damage Assessment
## UNDP / InnoCentive Challenge — Build the Future of Crisis Mapping
## Award: US$50,000 | Deadline: June 23, 2026 | Solver: SantiagoDM
## Technology Readiness Level: TRL 4 — Component validation in laboratory environment

---

## 1. THE PROBLEM

In the first 48 hours following a sudden-onset crisis, the organizations responsible for saving lives are operating blind.

Current damage assessment methodologies — however sophisticated — require days or weeks to generate actionable field data. Satellite imagery reveals what collapsed. It cannot reveal who is trapped inside. Formal surveys capture what surveyors can reach. They cannot reach everywhere at once. And the people who know the most — the communities living inside the crisis — have no structured, accessible way to share what they are witnessing in real time.

The result is a dangerous gap between the moment a crisis begins and the moment responders understand where to go, what to bring, and who needs it most. Every hour that gap remains open, lives are lost that could have been saved.

This challenge is not primarily technological. It is human. The people who most need to report damage are the same people experiencing the highest levels of acute stress, limited connectivity, depleted devices, and physical danger. Any solution that ignores this reality will fail — not because the technology does not work, but because the people it was designed for cannot use it in the moment it matters most.

---

## 2. OUR SOLUTION

We present FRIDA — First Response Integrated Damage Assessment.

FRIDA is named after the legendary Mexican rescue dog who saved lives in the 1985 and 2017 earthquakes — arriving where others could not, detecting what others missed, and working tirelessly in the most extreme conditions imaginable. Like her namesake, FRIDA is designed to find the signal inside the chaos.

FRIDA is not an app. It is a behavioral system built around a single insight: in a crisis, technology must descend to the level of the human, not the other way around.

FRIDA is delivered as a Progressive Web App (PWA) — installable on any device directly from the browser, fully functional offline, and accessible without App Store or Google Play dependencies. This architectural choice ensures FRIDA can be deployed and accessed in seconds, even in regions where app stores are unavailable, unreliable, or blocked. Once installed with connectivity, FRIDA operates completely offline — storing reports locally and synchronizing automatically the moment any signal returns.

Most damage reporting tools are designed for normal conditions — stable connectivity, calm users, fully charged devices, and time to think. FRIDA is designed for the opposite: no connectivity, extreme stress, depleted batteries, and zero seconds to think. Every design decision in FRIDA starts with one question: what can a person realistically do in their worst moment?

The answer, we found, is very little — and that is enough.

A single tap. A location. A signal. That is all FRIDA needs to begin building a picture of the crisis. As conditions improve — as users calm down, as connectivity returns, as time passes — FRIDA collects more. Not by demanding more from users, but by making it effortless to give more when they can.

The result is a living map of the crisis, built collectively by the community living inside it, growing more complete and more accurate with every passing minute — starting from minute zero.

---

## 3. HOW FRIDA WORKS

FRIDA operates through ten integrated layers, each designed to function independently and reinforce the others.

**Layer 1 — Minimum Viable Signal**

In the worst connectivity scenario, FRIDA transmits only what is essential: crisis type and GPS coordinates. Twenty characters. One SMS. That single data point, multiplied across dozens of users in the same area, triggers FRIDA's density triangulation — automatically identifying the epicenter of the crisis within minutes of the first report.

As connectivity improves, FRIDA's signal evolves automatically:
- Full internet: complete reports with photos in real time
- Mobile data only: complete reports without photos
- SMS only: compressed coded data — crisis type, coordinates, damage level, timestamp
- No connectivity: full local storage, automatic sync when any signal returns
- No signal at all: a locally generated QR code allows any nearby user with connectivity to upload the report on behalf of the affected person

This architecture ensures FRIDA never fails. It descends gracefully to whatever the moment allows.

**Layer 2 — Cognitive Adaptive Interface**

FRIDA recognizes that not all users experience a crisis the same way. Acute stress affects the brain differently — some freeze, some act, some can give everything, some can only give a single tap. FRIDA is designed for all of them simultaneously.

When density triangulation detects a crisis event, FRIDA activates passively on nearby registered devices — displaying a single button on the lock screen: "Are you in an emergency?" One tap. No searching. No remembering. No app to find.

For users who open FRIDA voluntarily, the same emergency button appears first with double confirmation to filter accidental taps, followed by: "If you are in danger, stop here. This can wait."

For those who can continue, FRIDA collects information in mandatory order — one question per screen, large text, single confirmation button:

1. Nature of the crisis: natural (earthquake, flood, tsunami, hurricane/cyclone, wildfire), technological (explosion, chemical incident), or human-made (conflict, civil unrest)
2. Type of infrastructure: residential, commercial, government, utilities, transport and communication, community, or public spaces
3. Level of damage: minimal/no damage, partially damaged, or completely damaged
4. Photo of the affected infrastructure
5. Whether debris clearing is required on or near the site
6. GPS location or building selection on map footprint

Between each question, FRIDA displays a survival recommendation: "Lower your screen brightness." "Enable airplane mode to save battery." "Do not call unless urgent."

Every partial submission is valid and useful. FRIDA assembles complete pictures from incomplete individual contributions.

**Layer 3 — Dual User Profile System**

FRIDA operates across two user profiles, each calibrated to their real-world credibility and capabilities.

Citizen Profile: community members who report what they witness. Credibility builds gradually through the anonymous reputation system. Their identity is never stored, never traceable, never exposable — even under institutional pressure.

Professional Responder Profile: verified field teams, rescue workers, and UNDP partners with institutional credentials. Professional responders enter FRIDA with maximum credibility weight from first use. Their reports update the official damage map instantly and definitively — no cross-validation required.

Professional responders equipped with satellite connectivity become mobile network hubs. As they move through disconnected zones, FRIDA automatically routes accumulated citizen reports through their connection. They do not only report what they find. They carry the community's voice out with them.

Privacy note: citizens remain fully anonymous at all times. Professional responders verify institutional identity for credibility, but their individual reports can optionally remain anonymous for personal safety in conflict zones.

**Layer 4 — Anonymous Reputation System**

Every citizen device receives a unique encrypted ID — not a name, not a phone number. A random code. This ID accumulates credibility silently.

Confirmed reports increase credibility. False reports trigger asymmetric penalties — losing points costs significantly more than gaining them. The system is self-regulating without human moderation.

High-credibility reports carry greater weight on the official map. Zero-credibility reports are automatically deprioritized — without confrontation, without exposure.

In conflict zones, no authority can identify who reported — because that identity never existed in the system.

**Layer 5 — Temporal Cross-Validation and Duplicate Detection**

Damage levels are not static in a crisis. FRIDA manages this through temporal cross-validation:

- Damage escalation requires confirmation before updating the official map
- Damage de-escalation is rejected automatically — a collapsed building does not repair itself
- When confirmation is unavailable, time becomes the validator: uncontested reports gain full weight after two hours

FRIDA's duplicate detection operates across two dimensions simultaneously:

Temporal duplicates — multiple submissions from the same device about the same location within a short time window — are automatically merged into a single versioned record, preserving the most complete and most recent data.

Spatial duplicates — multiple submissions from different users about the same building within the same time window — are cross-referenced using building footprint data. When two or more reports reference the same structure within minutes of each other, FRIDA treats them as corroborating evidence, increasing the credibility weight of that report automatically.

If a user taps the emergency button multiple times in panic, FRIDA does not create duplicate events. Each additional tap registers as a confirmation signal within the existing event, increasing location credibility. High-activity zones generate higher confidence data — not data pollution.

**Layer 6 — Precise Geolocation and Building Footprints**

GPS coordinates alone are insufficient — a single coordinate can reference a street, a courtyard, or any of twelve apartments in the same building. FRIDA solves this through building footprint overlays sourced from OpenStreetMap and UNDP's existing geospatial databases — both open source and globally available.

When submitting a report, the user sees a zoomed map with the exact outline of every registered structure. They tap the building itself — not an approximate location, not a street address. The building.

When GPS is unavailable, FRIDA offers textual location input: "The school near the central market." "Three blocks from the main church." "The blue building on the corner." FRIDA's AI converts these natural language descriptions into approximate coordinates, flagged as textually-sourced on the map for field team verification.

In communities where formal addresses do not exist — the majority of informal settlements where crisis impact is most severe — textual location is not a fallback. It is the primary method.

Every confirmed building report enriches FRIDA's footprint database — making each crisis more precisely mappable than the last.

**Layer 7 — Citizen-Built GIS Layers**

Once immediate reporting is complete, FRIDA invites calm users to contribute deeper intelligence through a modular post-crisis survey, introduced with: "If you are in a safe place and have a moment, help us understand what happened."

Questions one at a time:
- Are there blocked roads nearby? Where approximately?
- Are any services non-functional? Water / Electricity / Gas
- Is the nearest hospital or health center operational?
- Are there people trapped or injured without attention?
- Are there zones where rescue teams have not arrived?

Each response becomes a live GIS layer on FRIDA's map — blocked roads, failed utilities, unreached zones, non-functional critical infrastructure. Information that satellite imagery cannot capture, built by the people living inside the crisis.

Satellite validation cross-references community reports bidirectionally: satellite detects collapse without reports — FRIDA alerts UNDP. Citizen reports severe damage but satellite detects no change — FRIDA reduces that report's credibility weight automatically.

**Layer 8 — AI-Powered Analysis**

FRIDA's artificial intelligence operates across three functions:

Computer vision classifies building damage from uploaded photos before the user decides — reducing cognitive load under stress. The user sees: "We detected partial damage. Is this correct?" Confirm or correct. If the user abandons the report, the automatic classification is preserved.

Priority ranking algorithm continuously orders affected zones by urgency, crossing: damage density, credibility scores of reporters, time without attention, proximity to critical infrastructure, and satellite data. UNDP coordinators see an ordered list of where to go first — not hundreds of individual reports to interpret.

Automatic multilingual support operates across two operational modes designed for crisis conditions:

In Pre-Crisis Mode, FRIDA pre-downloads all six official UN languages (Arabic, Chinese, English, French, Russian, Spanish) to the device when connectivity is available. The user's preferred language is auto-detected from device settings and can be changed manually with a single tap. This ensures interface translation works completely offline, with zero data consumption during a crisis.

In Active Crisis Mode, no live translation is performed on the user's device. The interface uses pre-downloaded languages exclusively to preserve battery and bandwidth. LibreTranslate operates only on the server side, translating user-submitted text descriptions into all six UN languages for UNDP's dashboard — this happens after data is received, not during user input.

Voice-to-text input is also available offline through pre-downloaded language models, allowing users with limited literacy or those who cannot type under stress to submit voice descriptions, transcribed locally and synced when signal returns.

**Layer 9 — Modular Question Architecture**

FRIDA is not a fixed tool. It is a configurable platform.

Beyond its core damage assessment workflow, FRIDA supports modular question sets activated remotely by UNDP for specific crises, communities, or recovery phases — without requiring any app update.

Examples:
- Livelihood module (weeks after crisis): "Has your primary income source been affected? Have you been able to return to work?"
- Health and sanitation module (post-flood): "Do you have access to clean drinking water? Is your nearest health facility operational?"
- Shelter module (displacement scenarios): "Are you sheltering in your home or elsewhere? How many people share your current shelter?"

Each module follows FRIDA's same progressive interface. Each response feeds directly into GIS layers and dashboard. Each module translates automatically into all six UN languages upon deployment.

FRIDA grows with the crisis — from the first minute of impact to the last mile of recovery.

**Layer 10 — Multi-Event Management**

FRIDA is designed for the reality of simultaneous, overlapping, and prolonged crises.

Every crisis receives a unique Event ID — an independent container with its own map, dashboard, timeline, and data. Reports from an earthquake in Turkey never contaminate data from a flood in Sudan. A building marked as partially damaged in February's earthquake remains a separate record from the same building reported in August's flood.

For prolonged crises — such as armed conflicts lasting months or years — FRIDA creates temporal phases within the same Event ID. Each phase is a separate chapter preserving the complete accumulated history.

For simultaneous crises in the same region, FRIDA maintains full data separation while offering UNDP a unified dashboard with activatable and deactivatable event layers.

Device-level event binding ensures users already assigned to an active Event ID remain bound to it regardless of subsequent actions or geographic movement. Multiple emergency button taps register as confirmation signals — not new events.

UNDP's dashboard displays all active and historical events as independent selectable tabs — each with full data integrity, complete timelines, and exportable records in CSV, GeoJSON, shapefiles, and REST API formats.

---

## 4. DATA SECURITY AND PRIVACY ARCHITECTURE

FRIDA is designed to comply with global humanitarian data protection standards, including UNDP's own data protection guidelines, the GDPR framework, and the principles outlined in the Sphere Standards for humanitarian response.

Three architectural decisions guarantee privacy by design:

**Anonymous by default.** Citizen users never provide names, phone numbers, email addresses, or any personally identifiable information. The encrypted device ID is generated locally and is mathematically impossible to reverse-engineer into a real identity. There is no central registry connecting devices to people.

**Encryption in transit and at rest.** All communications between user devices and FRIDA's servers use TLS 1.3 encryption. Data stored in the database is encrypted at rest using AES-256. Photos are stripped of EXIF metadata before storage, removing camera identifiers and timestamps that could be used to triangulate users.

**Right to disappear.** Users can delete their device-level reputation history at any time. Once deleted, no record of past reports remains associated with that device. In conflict zones, this allows users to "reset" their digital presence if compromised.

**Differential geo-fuzzing.** Even anonymous reports can compromise users if their precise coordinates are exposed — particularly in conflict zones, sparsely populated areas, or small communities where location alone reveals identity. FRIDA addresses this through context-aware coordinate fuzzing: the operational dashboard accessible only to UNDP coordinators displays exact coordinates for response purposes, while any public, partner-shared, or external map view applies adaptive blurring. The blur radius adjusts dynamically based on context — 200 meters in active conflict zones, 50 meters in densely populated disaster zones, and full suppression of isolated single reports until cross-validation occurs through additional reports or a two-hour temporal validation window. A single citizen voice never becomes a single visible target.

FRIDA's hosting architecture supports data residency requirements: when deployed in countries with data sovereignty laws, all data for that crisis remains within national borders. UNDP retains full control over data lifecycle, retention policies, and access permissions.

---

## 5. DATABASE ARCHITECTURE AND SCALABILITY

FRIDA's backend is designed to handle UNDP's stated requirements at every scale level.

**Database engine.** PostgreSQL with the PostGIS extension — open source, battle-tested at global scale, and natively compatible with the geospatial systems UNDP already uses. PostGIS provides native support for building footprints, polygon-based queries, and spatial indexing that allows sub-second response times even with hundreds of thousands of records.

**Schema structure.** Each crisis is stored as an independent Event container with its own partitioned tables. This partitioning allows UNDP to query a single event without performance impact from concurrent crises. Records include: report ID, event ID, encrypted device ID, timestamp, geolocation (lat/lng + building footprint reference), crisis type, infrastructure type, damage classification, photo URI, credibility score, and validation status.

**Scale targets met by architecture.**

| Scale | Reports | Architecture Response |
|---|---|---|
| Local crisis | Up to 50,000 | Single regional server cluster |
| Regional crisis | Up to 250,000 | Auto-scaling cluster with read replicas |
| National crisis | Up to 500,000 | Multi-region distribution, sharded by geography |
| Annual operations | Hundreds of crises | Each event isolated in its own partition |

**Two-queue processing.** FRIDA's backend separates incoming data into two queues: a fast queue for minimum viable signals (coordinates and damage level), and a standard queue for complete reports with photos and descriptions. Under saturation, critical signals are guaranteed to pass through within seconds — a property no traditional architecture provides.

**Export interoperability.** FRIDA exports data in CSV, GeoJSON, shapefiles, and via REST APIs — fully compatible with UNDP's existing geospatial and data management systems, including the RAPIDA methodology.

**Hosting flexibility.** FRIDA can be deployed on UNDP's existing cloud infrastructure, on independent humanitarian cloud providers, or on national government servers — depending on the data residency requirements of each crisis.

---

## 6. ENGAGEMENT MODEL — NON-MONETARY INCENTIVES

FRIDA's engagement model is built entirely on non-monetary incentives, designed to encourage genuine participation while actively discouraging bad actors and repeat submissions.

The foundation is FRIDA's anonymous reputation system — a credibility score that grows with every confirmed report and falls sharply with every false one. High-credibility users see their reports weighted more heavily on the official map, giving them a tangible sense that their contribution matters more.

Three additional engagement mechanisms:

Community impact visibility — users see in real time how many reports from their area have been received and how that data is actively guiding response decisions. The map becomes a mirror: the community sees itself helping itself.

Responder recognition — professional responders and highly active citizen reporters receive verified badges within the system, visible to UNDP coordinators. This creates a pathway from anonymous citizen to trusted community asset — without compromising personal identity.

Crisis memory — after each event closes, FRIDA generates a community contribution summary: how many reports were submitted, how many were validated, and what response decisions they influenced. This closes the loop between reporting and impact — showing every contributor that their signal, however small, was part of something larger.

Between crises, FRIDA operates in Peace Mode — inviting community members to contribute to and verify the OpenStreetMap building footprint database in their neighborhood. The same engagement mechanisms apply: contributions are recognized, impact is visible, and the community map improves continuously. When a crisis hits, FRIDA's map is already accurate because the community built it before the emergency.

None of these incentives require money. All of them require meaning — and meaning, in a crisis, is the most powerful motivator of all.

---

## 7. WHY FRIDA WINS

Most solutions submitted to this Challenge will be built by engineers thinking about technology. FRIDA was built by a systems thinker thinking about people.

That difference is visible in every layer of the solution.

Existing damage reporting tools assume the user is available. FRIDA assumes the user is not. Existing tools assume connectivity. FRIDA assumes there is none. Existing tools ask communities to adapt to technology. FRIDA adapts to communities.

Four specific advantages separate FRIDA from every other submission:

First — FRIDA generates useful data from minute zero. Not from minute thirty, when connectivity is restored. Not from hour six, when field teams arrive. From the moment the first person taps a single button, FRIDA begins building a picture of the crisis. No other system in this Challenge can claim this.

Second — FRIDA's cognitive adaptive interface is the only design in this Challenge built around the neuroscience of acute stress. Under extreme stress, the human brain loses access to complex decision-making. FRIDA does not fight this reality. It designs around it — reducing every interaction to its absolute minimum, and scaling complexity only as the user's cognitive capacity recovers.

Third — FRIDA's anonymous reputation system solves simultaneously the two problems that destroy crowdsourced data quality: false reports and user safety. No monetary incentive. No identifiable data. No exploitable vulnerability. A self-regulating system that gets more accurate over time without human moderation.

Fourth — FRIDA builds GIS intelligence layers that satellite imagery cannot. Satellites see collapsed buildings. They do not see the hospital that lost power, the bridge that looks intact but cannot bear weight, or the neighborhood where rescue teams have not arrived. FRIDA's community-built layers capture what no remote sensing technology can.

Together, these four advantages produce something no other submission will deliver: a complete, accurate, and continuously improving picture of a crisis — built by the community living inside it, starting from the moment it begins.

---

## 8. DEPLOYMENT IN 48 HOURS

Most crisis tools face a deployment paradox: they are most needed in the first hours of a crisis, but require days or weeks to deploy effectively. FRIDA was designed to eliminate this paradox entirely.

FRIDA's deployment strategy operates on three simultaneous tracks:

Track 1 — Pre-Crisis Installation: FRIDA is designed for pre-crisis adoption in high-risk communities. Partnering with local governments, NGOs, schools, and community organizations in disaster-prone regions, FRIDA can be installed and familiarized before any crisis occurs. When a crisis hits, FRIDA is already in the hands of the people who need it. No download required in the chaos. No learning curve under stress.

Track 2 — Passive Activation: The moment density triangulation detects a crisis event, FRIDA activates automatically on nearby registered devices, displaying a single emergency button on the lock screen. The system deploys itself — reaching users who may not have thought to open an app in the first seconds of a crisis.

Track 3 — Open Source Replication: FRIDA is fully open source. Any humanitarian organization, national government, or NGO can deploy FRIDA independently within hours of a crisis, without licensing fees, without technical dependencies, and without waiting for centralized authorization.

48-hour deployment timeline:
- Hour 0-1: Minimum viable signals arrive from pre-installed devices. Density triangulation identifies crisis epicenter. FRIDA activates passively on nearby devices.
- Hour 1-6: Progressive reports build the first complete damage picture. GIS layers begin forming. AI priority ranking identifies zones requiring immediate intervention.
- Hour 6-24: Satellite validation cross-references community reports. Credibility scores stabilize. FRIDA's map reaches operational accuracy.
- Hour 24-48: Full situational awareness achieved. Field teams guided by real-time priority rankings. UNDP's RAPIDA methodology enriched with granular community data unavailable through any other source.

---

## 9. PEOPLE FIRST — THE HUMAN FOUNDATION OF FRIDA

We chose the name FRIDA in honor of the rescue dog who became a global symbol during the 2017 Mexico City earthquake. We chose her not only for her story, but for what she represents: resilience in chaos, tireless search in the most extreme conditions, and hope when everything seems lost. And because a dog — unlike any institution or technology — is a universally impartial figure. She does not judge. She does not discriminate. She only searches, and finds.

FRIDA was born from a simple but uncomfortable question: what does a person actually feel in the first minutes of a disaster?

Not as a statistic. Not as an abstract user. As a human being — afraid, confused, battery at 12%, not knowing if their family is safe, heart racing, fingers trembling over a screen.

From that place, we designed every decision. Every button. Every question. Every silence in the interface.

We understood that extreme stress does not affect everyone equally. That some people freeze and some people act. That some can give a lot and some can only give a single tap. And that a truly human system must work for both — without judging how much each person can give in their worst moment.

This project was also a personal choice. I had the freedom to choose any problem. I chose this one — not because it is the easiest, but because it matters most. Because behind every report FRIDA receives is a real person, in a real moment of vulnerability, who deserves to have had someone think about them before the crisis ever happened.

FRIDA protects their identity. Protects their safety. And in their worst moment, tells them silently that they are not alone.

That is what FRIDA is. Not an app. A human decision.

---

*Submitted by SantiagoDM*
*InnoCentive Challenge: Build the Future of Crisis Mapping*
*UNDP / SeaFreight Labs — June 2026*
