# Court V2 Decisions Log

This is the authoritative list of Court V2 product decisions Matthew Keslin has locked. Every Court bot (BA, Dev, Tester, Doc) reads it before speccing, building or testing. Add each new decision with its date. When a decision changes, update the entry and note what it replaces.

> Draft 1 (2026-10-15), compiled by Court BA Bot from saved notes. Older decisions from September 2026 may be incomplete. Matthew, please flag anything missing or wrong.

## Standing process rules
- Dev commits locally only after a BA PASS. Dev never pushes unless Matthew asks.
- Dev runs unit tests only, with no local runs unless asked. Matthew restarts the API and Vite himself.
- Database writes (migrations, seeds, backfills) need Matthew's OK, given in Dev's chat.
- Follow AGENTS.md, `.cursor/rules` and the tls-* control rules. Every confirmation uses the Thin Line confirm dialog, never the browser's confirm.
- Follow Texas law. TMCEC comes first for forms and rules (2025–2026 Bench Book and charts).
- With standing permission (2026-10-11), Dev builds anything Matthew OKs without asking him again.
- Status updates are in plain English, and scores are PASS, HOLD or blocked. Don't use "Soft" terms (2026-09-30).
- Court Doc Bot may commit and push changes to the internal docs (2026-10-15).

## Global principles
- **Outcomes, not state machines (2026-09-24).** The violator picks an outcome, the software composes the packet steps, and the case is submitted for approval. Clerks and violators never walk the old state machine.
- **Derive everything from current state (2026-10-14).** For every outcome, the steps, forms and documents are derived from the case's current state, and only what's needed to reach the target state is included. For example, the plea form is included only when no plea has been entered yet. Matthew shouldn't be asked per-outcome variations of this.
- **No standalone guilty or no contest plea (2026-10-13).** Every outcome is something else (DSC, Deferred, payment plan, and so on), and a plea may be a step inside it. Not Guilty stays: the violator signs and the case goes to Pre-Trial.
- **Not guilty online is allowed (2026-10-06).** Portal not-guilty pleas go to Pre-Trial, since there's no statutory counter-only rule under Art. 45A.151.
- **Signatures come from the violator (2026-10-05).** Through the portal, the tablet, or printed paper. Never a clerk typing a name at the counter.
- **Signature verification depends on the route (2026-10-13).** The tablet verifies the signature itself. On paper, the clerk marks the document signed (clerk name and time saved), and the judge verifies it at approval.
- **The judge signs every judgment and dismissal (2026-09-23, Art. 27.14(c)).** No auto-close or auto-stamp. Pay-in-full and compliance dismissals also need a judge signature.
- **In-person and online eligibility differ (2026-09-24).** In-person has fewer limits than the portal.
- **Switching outcomes (2026-09-24).** Cancel the unapproved packet, then start a new outcome. Switching after approval is deferred.
- **One open request per case (2026-10-15).**

## NEW citations and intake
- **NEW state (2026-10-06).** The portal shows no resolution flows ("still processing; check back later"). Outcomes and tablet pairing aren't available while NEW.
- **Clerk actions while NEW (2026-10-06).** Intake (offense, appearance date, fees and fee mapping, DOB), Proceed to Pre-Plea, Transfer to another court, Void citation, and Enter follow-up date.
- **DOB is required for NEW to Pre-Plea (2026-10-06).** The API blocks without it, the clerk has a DOB control, and it prefills from the master person when the citation's DOB is blank.
- **Speed and posted limit are required for NEW to Pre-Plea on speeding offenses (2026-10-10).** A health check flags missing values.
- **The clerk can't edit speed (2026-10-15).** It's static text. If either value is missing, a read-only note says the citation must be corrected before the case can proceed. A missing speed shouldn't happen, and Matthew fixes it in the database if it does.
- **Complaint (2026-10-15).** View Complaint opens the in-app PDF previewer instead of downloading the file.
- **Intake cards (2026-10-14).** Titles are in Title Case. Key values show as static text when collapsed: OCA type code, appearance date, DOB, speed and limit, and fee balance. A value that isn't stored but can be mapped, like the OCA type code, shows the mapped value instead of "not set".
- **Follow-up date (2026-10-14).** It can be cleared with an X inside the card (with a confirm) or by saving the dialog blank.

## In-person workspace (clerk screen)
- **Layout (2026-10-07).** Outcomes (violator options) on the left, Clerk actions in the middle, Tablet on the right. On narrow screens the actions collapse into a top menu.
- **Middle column (2026-10-15).** "Case requests and orders" lives here. It holds the dismissal requests, parent nonattendance, ability to pay, fine waiver, commitment discharge and DSC more-time panels, each gated by case state and claim. The deprecated utility drawer no longer shows them.
- **Person edits (2026-10-14).** Edits happen in the person detail drawer, not through an Edit button in the In-Person drawer. Saving refreshes the In-Person drawer.
- **Stacking order (2026-10-14).** To fix layering, lower the component's own z-index (the In-Person drawer). Don't raise the shared values. The person drawer must open on top.
- **Legal basis card (2026-10-14).** It sits under Pair tablet, with statute links.
- **Draft outcome alert (2026-10-14).** It offers "Go back to outcome" next to Cancel.
- **Clerk Dismiss case removed (2026-10-19).** The clerk's direct Dismiss case action was removed. Dismissals go through the request flows. (BA call, Matthew informed; built locally, not pushed.)

## Paper path
- **Flow (2026-10-06).** The clerk starts the outcome as Paper, prints the filled packet, the violator hand-signs, the clerk marks it signed and submits it for the judge as Paper, and the judge approves, rejects or returns it with the same case effects. The paper is the record.
- **No scanner assumed (2026-10-15).** Uploads are never required on paper. Photocopied evidence goes with the signed motion in a physical folder the judge reviews.
- **Payment (2026-10-15).** The clerk enters the payment method and payment on their screen and can print a receipt.
- **Packet printing (2026-10-14).** Every document in the packet is listed, based on the case's current state, with a Print button for each plus "Print all (one PDF)".
- **First rollout (2026-10-15).** Testing and rollout start with in-person paper flows. The portal and tablet come later.
- **Paper plea copy (2026-10-19).** On paper, the clerk copies the plea (guilty or no contest, no default) from the hand-signed form for payment plan, community service, DSC and Deferred. The hand-signed mark records the jury waiver. (BA call, Matthew informed; built locally, not pushed.)
- **Paper proof is a clerk check (2026-10-19).** Paper proof is a clerk check, never an upload. It covers the prosecutor's signed motion (CCP 32.02), the school's proof (45A.403), DSC proof of insurance, and soon the youth diversion prosecutor objection. The server records who and when, a judge return clears the check, and the queue card shows the verified line. On a resubmit after a return, an upload already on file counts for DSC but not for school proof. (BA call, Matthew informed; built locally, not pushed.)
- **Paper DSC military status (2026-10-19).** On paper DSC the clerk copies the military status from the signed form, with no default. License state comes from the person record. (BA call, Matthew informed; built locally, not pushed.)
- **Tablet-started, paper-finished (2026-10-19).** A request started on the tablet and finished on paper is checked by the paper rules (printed plus hand-signed), not the tablet answers. (BA call, Matthew informed; built locally, not pushed.)

## Tablet path
- **Controls (2026-10-14).** All tablet controls follow the tls-* rules.
- **Steps shown (2026-10-14).** The tablet shows a step list of the packet steps. A cancelled outcome clears from the tablet.
- **Document preview (2026-10-14).** Before signing, the violator previews the templated documents filled from case data (not their draft answers) and must check "I have reviewed these documents".
- **Who does what (2026-10-15).** The clerk enters dates, confirms eligibility and verifies proof. The violator uploads proof (required on the tablet), e-signs, and picks a payment method. For cash or check they hand it to the clerk. For a card they enter it on the tablet, the same way as the payment portal. The clerk can print a receipt.

## Queues and permissions
- **Three queues (2026-10-14).** Clerk Queue, Prosecutor Queue and Judge Queue, named for who works them. They replace "Violator portal queue" and "Judge packet queue". Each item is in exactly one queue at a time and moves as the case moves.
- **Who works each queue (2026-10-14).** Clerk Queue: anyone with Modify, judges included. Judge Queue: Adjudicate (judges) only. Prosecutor Queue: Prosecute only. The CA role must not have normal court violation Modify. Judges hold both Modify and Adjudicate.
- **What goes where (2026-10-14).** The Judge Queue holds all V2 judge packets from any source, with source badges and filter chips (Portal, Tablet, Paper, Clerk). Needs Info items go to the Clerk Queue.
- **Look (2026-10-15).** All three queues use the standard iterator-and-card pattern with matching cards, plain labels (no codes), and a refresh icon. Empty queues use the standard "No Records" card. Case review opens in a dialog.
- **Documents (2026-10-14).** Queues show the judge the packet documents and all available case information.
- **Agency (2026-10-14).** Queues use the selected agency. There's no agency ID field.
- **Permission labels (2026-10-14).** "View court queues", "Work Clerk Queue", "Work Judge Queue (rule on packets)", "Work Prosecutor Queue".
- **Court V2 switch (2026-10-16).** The agency setting formerly labelled for the online portal is the single on-switch for all of Court V2 (portal, in-person workspace, paper, queues, dashboard card, V2 case panels). Label: 'Turn on Court V2 for this agency'.
- **One-way switch (2026-10-19).** Courts only ever move onto Court V2; it's never turned off once enabled, so there's no handling for turning it off (for example, open portal sessions aren't cut off).
- **Warrant and issuance pages (2026-10-19).** FTA/CPF/LPC warrant pages and officer IssuancePc stay available to every agency. Portal acknowledgment (PortalAckStaff) is gated by the V2 switch.
- **Batch paper approve (2026-10-19).** The judge can batch-approve paper packets with the paper check. One unconfirmed paper packet refuses the whole batch, dismissal types are refused per packet, the server requires notes, and verify plus approve run as one transaction. (BA call, Matthew informed; built locally, not pushed.)

## Compliance dismissal
- **Scope (2026-09-25).** Only rule packs on the 2025 TMCEC Compliance Dismissals Chart are offered. FMFR and display-DL are included. The judge signs every compliance dismissal, whether the chart says "shall" or "may".
- **Steps for both channels (2026-10-15).** Preliminary eligibility, then proof and dates, then confirm eligibility, then the violator signs the motion, then the fee is collected, then the packet is submitted to the Judge Queue.
- **Documents (2026-10-15).** A defendant's Motion to Dismiss for Compliance plus an Order (a TMCEC form if one exists). No plea form.
- **Fee timing (2026-10-15).** The fee is collected at the counter while the violator is present, before the judge rules, assuming approval, because some judges sit once a month.
- **Fee amount (2026-10-15).** It follows the TMCEC chart. Fixed fees can't be edited. Where the chart says "up to" an amount, the fee defaults to the maximum and the clerk can lower it within the range, which is logged.
- **Submit checks (2026-10-15).** Deadline met, signed, fee recorded, plus proof verified (paper) or at least one proof file (tablet).
- **Judge approval (2026-10-15).** Approve generates the signed order and dismisses the case.
- **Needs Info and denial (2026-10-15).** Needs Info returns the packet to the Clerk Queue. The clerk contacts the violator, updates it and resubmits, and the fee stays paid. A denial goes to the Clerk Queue as a follow-up so the violator can choose another outcome. There's no automatic refund: a denied or cancelled packet with a posted fee is flagged in the Clerk Queue for the court administrator to resolve (2026-10-16).
- **Fee booking (2026-10-16).** When the fee is posted, the case's fine lines are zeroed, the CD fee is added as its own line, and the payment credits it, all in one transaction.
- **Fees (2026-10-15).** Every fee on the 2025 TMCEC chart is a 'not to exceed' amount, so none are fixed.
- **Order (2026-10-15).** A one-page Motion to Dismiss for Compliance and Order. The judge draws a signature (the same dialog as other dismissals), and compliance dismissals are excluded from batch approve.
- **Deadline (2026-10-15).** 'Expired at today's date' is only a warning. Submit is blocked only when the remedy date is after the deadline.
- **Registration (502.407(b)).** Dismissal is discretionary. The violator must remedy it and pay the delinquent registration fee. The deadline is 20 working days after the offense or before the first appearance, whichever is later. The fee is optional, up to $20.
- **Refund copy (2026-10-19).** The screen says "refunded", never "refunded by check". When pay in full is cancelled or rejected after payment posted, the payment is reversed as a refund. A compliance dismissal with a posted fee is not refunded automatically; it's flagged on the Clerk Queue. (BA call, Matthew informed; built locally, not pushed.)

## Dismissals (prosecutor and judge)
- **Prosecutor role (2026-10-13).** Dismissals need a prosecutor role and a prosecutor queue.
- **Prosecutor motions need a judge order (2026-10-13, CCP 32.02).** A prosecutor motion to dismiss gets a judge-signed order. Clerical Error, Other and similar dismissals are also judge-signed. Proof-based dismissals stay in the compliance dismissal flow.
- **Single clerk entry point (2026-10-15).** The clerk uses "Request dismissal" in the middle column and chooses one of:
  - a prosecutor motion, which goes to the Prosecutor Queue, where the prosecutor approves and signs it (sending it to the Judge Queue) or declines with a note;
  - a motion the prosecutor already signed on paper, which goes straight to the Judge Queue;
  - a judge-ordered dismissal (judicial discretion, clerical error, other, or parent nonattendance under 45A.403), which goes to the Judge Queue.
- **Self-initiated (2026-10-15).** A prosecutor can file their own motion, which goes straight to the judge. A judge can sign their own order. The judge signs through a signature pad plus a confirm, and the signed order PDF is generated. Prosecutors can never sign orders.
- **Declined requests (2026-10-15).** A prosecutor decline on a clerk request shows up as a Clerk Queue follow-up.

## Outcomes
- **DSC (2026-10-10).** Hard deny at 95+ mph or 25+ over the limit (CCP 45A.352(a)(5)). School bus (TC 545.066) is a DSC hard deny. Deferred is discretionary for both. Drivers under 25 choosing Deferred are forced into DSC.
- **Deferred (2026-10-06).** When Available, it's like DSC: the plea is folded into the packet.
- **DSC and Deferred eligibility (2026-09-25).** Live eligibility is used at Available and at Submit, not just the case stage.
- **Community service and payment plan (2026-09-25).** They can be requested without a Hardship packet, and approving one is the ability-to-pay finding. Payment plan approval signs the judgment and then activates the schedule.
- **Community service with no judgment on file (2026-10-19).** Community service from pre-plea or post-plea with no judgment on file: approval stamps a guilty judgment and doesn't check the ability-to-pay answers, per the 9/25 decision. (BA call, Matthew informed; built locally, not pushed.)
- **Hardship (2026-09-24).** It's its own outcome using the full TMCEC Indigent Application, and financial disclosure fields are required at submit.
- **Pay in full (2026-10-05).** It's blocked online and by mail for FV and other deny-list offenses, so the violator must appear. Counter paths stay open.
- **Pay in full and pleas (2026-10-19).** Pay in full keeps any plea already on the case, and the judge doesn't have to answer the ability-to-pay questions before approving it. (BA call, Matthew informed; built locally, not pushed.)
- **Teen court (2026-10-12).** Hours are optional for the clerk to enter.
- **Youth Diversion (2026-10-06 to 10-11).** Ages 10 to 16, non-traffic, fine-only, counter or paper only (blocked online). Records are confidential, visible to court staff only, with anonymous counts. Only a judge enters hearing orders, with a drawn signature.
- **Juvenile Combined (2026-09-25).** A clerk and tablet outcome, blocked online.

## Online portal
- **NEW cases (2026-10-06).** No resolution flows.
- **FTA and CPF show cause (2026-09-23).** Read and acknowledge receipt only, with no upload.
- **Portal payments.** Use Stripe.

## Test data
- **Complaints seeded (2026-10-14).** Four cases have complaints and can leave NEW: DEMO-NEWMP-01-01, DEMO-NEWMP-02-01, DEMO-NEWUM-03-01 and MC-SPD-08-01. DEMO-NEWMP-03-01 is the deny fixture with no complaint.

## Parked for later
- Applying a denied compliance dismissal's fee to a new balance, instead of refunding it.
- Copying speed fields onto the violation record so the court can edit them.
- The agency-header check fix for seven non-court controllers. It's shared platform code, and court isn't exposed today.
- The work-queue drawer's forced z-index of 2410.
- The complaint flow for clerk-entered citations from the regular citation module.
- Youth diversion and child record expunction at 18 (CCP 45.313(c), 45A.463/464).
- An unsuccessful youth diversion auto-transferring or auto-referring the case.
- The parent relationship field on youth diversion.
- Child community service and tutoring election, and the foster-care community-service-only rule (45A.253(b)-(d)).
- Deferred-disposition community service location rules (45A.255).
- Phone and video appearance tracking, juvenile-now-adult handling, and public receipt page access.
- Tier-2 DSC denies, and alcohol-minor with 2+ priors.
- E2E helper updates for tls-* controls, and converting the remaining old upload controls.
