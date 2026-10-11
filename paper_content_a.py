# -*- coding: utf-8 -*-
"""
Research paper content (Part A): front matter, historical foundations,
taxonomy of demands, constitutional framework, challenges.
Rendered by build_paper.py. Inline markup: **bold**, *italic*.
"""

TITLE = "Formulation of New Provinces in Pakistan: Challenges and Prospects"

META_LINES = [
    "Research paper - prepared with the repository's AI Research Agent workflow",
    "Draft for academic review - October 2026",
]

ABSTRACT = (
    "Pakistan's federal map has been redrawn more times than its constitutions, and it is being "
    "redrawn again in the public imagination. Between 2024 and 2026 a succession of events - the "
    "2023 digital census, the Twenty-Sixth Amendment's local-government provisions, a unanimous "
    "Khyber Pakhtunkhwa assembly resolution for a Hazara province (December 2025), and persistent "
    "reporting of a '28th Amendment' package that would split Punjab, Sindh, Khyber Pakhtunkhwa and "
    "Balochistan into smaller units - has put the creation of new provinces back on the national "
    "agenda. This paper examines the formulation of new provinces in Pakistan as a problem of "
    "institutional design. It reconstructs the historical trajectory from the One Unit experiment "
    "(1955-1970) to the post-18th Amendment settlement; catalogues the principal provincial demands "
    "and their social bases; and analyses the constitutional route, which runs through Article 239 "
    "(including the two-thirds consent requirement of the affected provincial assembly) rather than "
    "through executive proclamation. The paper argues that the binding constraints on new provinces "
    "are not legal but political-economic: the arithmetic of supermajorities; the zero-sum character "
    "of National Finance Commission transfers locked by the Article 160(3A) non-regression floor; the "
    "equality-of-provinces doctrine in the Senate; water and resource settlements (the 1991 Indus "
    "accord, gas royalties under Article 158); administrative and judicial capacity; and the risk that "
    "border-making hardens ethnic competition, as comparative evidence from Indonesia, Ethiopia, "
    "Nigeria, Nepal and India suggests. The prospects, however, are real: sub-national re-scaling could "
    "close the 'deprivation divide' documented by the UNDP, shorten the distance between citizens and "
    "the state, and institutionalize conflict accommodation - provided sequencing runs through local "
    "government and divisional devolution first, provided viability and fiscal criteria are written "
    "before the first new province is created, and provided the change is carried by a cross-party "
    "consensus of the kind the 18th Amendment embodied rather than by the bare parliamentary arithmetic "
    "the 26th and 27th Amendments exhibited."
)

KEYWORDS = (
    "federalism; new provinces; provincial autonomy; NFC Award; Article 239; South Punjab; Hazara; "
    "Karachi; Kalat; ethnic conflict; constitutional amendment; Pakistan"
)

BLOCKS_A = [
# ------------------------------------------------------------------ 1
("h1", "1. Introduction"),

("p",
 "Few questions in Pakistani politics are as old as the country itself and as unsettled as the size "
 "and number of its provinces. Pakistan began as a federation of five units (three provinces and two "
 "groups of princely states), collapsed into a single 'One Unit' in West Pakistan in 1955, was "
 "re-regionalized into four provinces in 1970, and has lived under that four-province settlement since "
 "the 1973 Constitution [1][4]. Each of those restructurings was, in its way, a response to the same "
 "problem: a state whose central institutions were too weak to deliver legitimacy but too strong to "
 "share power. The problem has not gone away. The 2023 digital census recorded 241.49 million people in "
 "the four provinces and the Islamabad Capital Territory - Punjab alone accounting for 127.7 million, "
 "more than twice the combined population of Khyber Pakhtunkhwa and Balochistan - and population is the "
 "very criterion by which seats, funds and bureaucratic attention are allocated [2]."),

("p",
 "By the mid-2020s, provincial-statehood demands had become a recurring feature of legislative "
 "business and coalition bargaining. The Pakistan Tehreek-e-Insaf pledged a South Punjab province in its "
 "2018 manifesto, tabled amendment bills in 2019, and circulated a federal cabinet summary in March 2022 "
 "drafting the new province's assembly, high court and Senate representation [39][46]. In October 2024 "
 "the Twenty-Sixth Amendment rewrote Article 140A to require provinces to establish empowered local "
 "governments with elections conducted by the Election Commission of Pakistan (ECP) [33][51]. In "
 "December 2025 the Khyber Pakhtunkhwa assembly unanimously passed a resolution urging the federal "
 "government to initiate the Article 239 process for a Hazara province [41]. And throughout 2025-2026, "
 "with a new National Finance Commission at work and a decennial census on the horizon, newspapers and "
 "politicians have debated a possible '28th Amendment' restructuring package variously reported to divide "
 "Punjab into North, Central, South, Potohar and Bahawalpur units; Sindh into Karachi, Hyderabad, "
 "Mirpurkhas, Sukkur and Larkana; Khyber Pakhtunkhwa into Peshawar, Hazara, Malakand and Dera Ismail "
 "Khan; and Balochistan into Quetta, Makran, Zhob and Kalat, with Karachi and Gwadar in some versions "
 "brought under federal control [40]. As this paper went to draft (October 2026), no such bill had been "
 "tabled, and the federal law minister had publicly characterized the talk as consultations rather than "
 "legislation [40]."),

("p",
 "The gap between talk and legislation is itself the subject of this paper. If creating new provinces is "
 "a plausible answer to Pakistan's governance and regional-inequality problems, why does the process keep "
 "stalling at the threshold of the Constitution? And if it is not, why does the demand recur in every "
 "electoral cycle and in every coalition agreement from Multan to Abbottabad? This paper answers by "
 "treating province creation as a question of **institutional design under fiscal scarcity and ethnic "
 "competition**. Three propositions organize the analysis. *First*, the constitutional route exists and is "
 "not doctrinally blocked - Article 239 supplies a deliberately demanding procedure, whose difficulty is a "
 "feature: any new province must be wanted simultaneously by the federation and by the mother province. "
 "*Second*, the decisive obstacles are political-economic rather than legal: supermajority arithmetic in a "
 "fragmented party system; a fiscal transfer system that is strictly zero-sum; Senate parity that makes "
 "small provinces structural veto-players; unresolved water and resource settlements; and the sheer cost of "
 "duplicating provincial state apparatuses at a moment of IMF-monitored austerity. *Third*, the prospects "
 "are genuine but conditional: the governance and conflict-accommodation gains claimed for new provinces "
 "are better achieved - and only made safe - through a sequenced ladder of devolution (local government "
 "first, divisional autonomy second, provincial statehood only for units that pass pre-committed viability "
 "criteria), under constitutional rules fixed before the particular winners and losers are known."),

("p",
 "The paper proceeds as follows. Section 2 reconstructs the historical logic of Pakistan's provincial "
 "settlements. Section 3 catalogues the contemporary demands and their social bases. Section 4 sets out "
 "the constitutional and legal framework. Section 5 analyses the challenges - political, fiscal, "
 "hydrological, ethnic-administrative and legitimacy-related - drawing on census, budget and NFC data. "
 "Section 5 also presents a comparative assessment: how re-scaling worked, or did not work, in India, "
 "Indonesia, Ethiopia, Nigeria, Nepal and Kenya. Section 6 develops the prospects. Section 7 derives "
 "design principles and policy options, and Section 8 concludes. The analysis is doctrinal and "
 "comparative, relying on primary legal instruments, official statistics and quality secondary "
 "literature; all financial data are in rupees for FY2024-25 (approx. US$1 = Rs278), and events are "
 "described as of mid-October 2026. Because several claims in the current debate rest on reported rather "
 "than tabled proposals, the evidentiary status of each is flagged in place."),

# ------------------------------------------------------------------ 2
("h1", "2. The Provincial Question: Historical Foundations"),

("h2", "2.1 The colonial inheritance and the unitary reflex (1947-1955)"),

("p",
 "Pakistan's founders inherited the Government of India Act 1935 as a working federal template - a "
 "quasi-federal instrument designed, as the Objectives Resolution debates showed, more for control than "
 "for compromise [4]. The 1947 settlement was doubly fragile: the provinces (Punjab, Sindh, "
 "North-West Frontier Province, Balochistan, and East Bengal) carried living memories of provincial "
 "elections and Muslim League governments, while the princely states (Kalat, Bahawalpur, Khairpur, and "
 "others) carried their own sovereignty claims. The traumatic accession of Kalat (March 1948, followed by "
 "the imprisonment of the Khan and a brief armed rising) embedded in Baloch political memory the "
 "association between 'federation' and 'annexation' [7][8]. The Bengali language movement (1948-1952) "
 "likewise fixed the equation of centralization with Urdu-nationalism in the East. When Governor-General "
 "Ghulam Muhammad proclaimed One Unit in October 1955 - amalgamating all of West Pakistan's provinces, "
 "states and tribal agencies into a single unit nominally equal to East Pakistan - the device was "
 "parity-by-aggregation: dissolve the units rather than equalize them [4][6]. Its administrative logic "
 "was noted at the time. The UN adviser Robert Chester's reform report (1964) declared One Unit "
 "unworkably large and proposed re-dividing the country into a dozen or so smaller provinces, among them "
 "**a Hazara province and a South Punjab province** - the first official-adjacent articulation of both "
 "demands that dominate today's debate [5]."),

("h2", "2.2 Re-regionalization, secession, and the 1973 bargain (1958-1973)"),

("p",
 "Ayub's martial law preserved One Unit and its Basic Democracies apparatus; the princely constitutions "
 "were extinguished along the way (Bahawalpur's in 1966). One Unit was dissolved by the Legal Framework "
 "Order of July 1970, reconstituting Punjab, Sindh, NWFP and Balochistan - while, significantly for "
 "today's discussion, the 1970 settlement *promised and never delivered* the political integration or "
 "provincial status of the tribal agencies and the northern areas, leaving grey zones that the 2018 FATA "
 "merger and the Gilgit-Baltistan governance orders are still working out [4][21]. The secession of "
 "East Pakistan in 1971 was, among many other things, a defeat for the unitary state model; the 1973 "
 "Constitution negotiated by Zulfikar Ali Bhutto's government was explicitly a counter-design: four "
 "named provinces in Article 1; a Senate (Article 59) giving every province an *equal* delegation "
 "regardless of population; the Council of Common Interests (Articles 153-154) as the peak "
 "inter-governmental body; a National Finance Commission (Article 160) for revenue sharing; provincial "
 "ownership of minerals and a royalty on natural gas and oil extracted in a province (Article 158); "
 "and, after years of agitation, the recognition that Sindhi, Pashto, Balochi and Punjabi would not be "
 "constitutionally privileged over Urdu but neither suppressed [1][4][6]. The 1973 bargain was genuine "
 "federalism with an iron clause: the center retained emergency powers (Article 112), the civil services, "
 "and - decisive for provincial demands ever since - the planning and development apparatus that "
 "determined where money actually went."),

("h2", "2.3 Centralization's second round: Zia, Musharraf, and devolution-by-decree (1977-2008)"),

("p",
 "Zia's amendments re-centered the federation (the Eighth Amendment's dismissal powers, the 1984 frontier "
 "orders touching FATA and the northern areas) even while Islamization co-opted some symbolic demands [4]. "
 "Pervez Musharraf's Devolution Plan (2000-2001) remains the most instructive precedent for the current "
 "debate: it abolished the divisions as intermediaries, created directly elected district and tehsil "
 "governments with a strong nazim executive, and was celebrated as the most radical decentralization in "
 "Pakistani history. It was also what critics called 'devolution of patronage rather than power': no "
 "meaningful fiscal autonomy, bureaucratic line control retained by deputy commissioners, no provincial "
 "ownership - and it collapsed as quickly as it had been launched, revoked and rewritten by the 2008 "
 "restored civilian order [28][29][22]. The lesson Pakistan has internalized (and, in the 2026 "
 "structuring debate, partly forgotten) is that **a new tier of government created by decree without a "
 "fiscal base reproduces dependency at a new altitude**."),

("h2", "2.4 The autonomy settlement and its extensions (2008-2018)"),

("p",
 "The 18th Amendment (April 2010) rewrote the provincial bargain more ambitiously than the framers of "
 "1973 dared: it abolished the Concurrent List, devolved ~17 ministries (including education and health), "
 "constitutionalized NFC floors (Article 160(3A): no province's share may fall below its previous level), "
 "provincialized water (Article 172), regulated gubernatorial rule (Article 112), created the Constitutional "
 "Appellate Court, and made local-government devolution a constitutional command (Article 140A) [36][1]. "
 "It was accompanied by the landmark Seventh NFC Award (2009), which raised the provincial share of the "
 "divisible pool to 57.5 percent - later with special allocations, roughly 59 percent flowed to provinces - "
 "and tilted the horizontal formula away from pure population to reward poverty, revenue effort and sparsity "
 "[30][47]. Scholars called the package a move from 'the most centralized federation to one of the most "
 "decentralized'; what it also did was *change the currency of provincial conflict*. Once provinces control "
 "school curricula, police, health and a majority of the tax basket, a new province is not merely an "
 "administrative boundary - it is a package of rents and regulatory powers worth fighting over, which is "
 "precisely why the demand re-emerged with renewed political value after 2010 [10][11]. The Twenty-Fifth "
 "Amendment (May 2018) merged FATA into Khyber Pakhtunkhwa - the first successful territorial integration "
 "in decades, pursued through a Supreme Court-mandated committee (the Justice Qazi Faez Isa commission "
 "process and the FATA Reforms Committee chaired by IQ Khan), a five-year Rs1,250 billion federal action "
 "plan for the merged districts, and an extension of the police and courts regime [35][31][21]. Its "
 "instructive features for province-creation were the *phasing* (full integration of the merged districts "
 "was scheduled over 15 years), the *ring-fenced transitional money* (outside provincial NFC arithmetic, "
 "from the federal PSDP), and the *precedent of treating a sub-national territorial question as a national "
 "project requiring consensus in both houses plus the host assembly*."),

("h2", "2.5 The new-province cycle of 2018-2026"),

("p",
 "Against that backdrop the recent cycle is legible. The PTI's 2018 pledge of South Punjab became an "
 "assembly resolution in Punjab, a private member's bill (2019), and in March 2022 a federal cabinet "
 "summary with a drafted amendment bill: South Punjab comprising the Multan, Bahawalpur and Dera Ghazi "
 "Khan divisions; 56 National Assembly seats; a 119-seat provincial assembly; a reduction of the Punjab "
 "assembly from 371 to 252; a Senate enlargement from 96 to 119 (seven seats to South Punjab in staggered "
 "retirement classes); a South Punjab High Court seated at Multan with a bench at Bahawalpur; an "
 "additional ECP member; and a bump for minority reserved seats from four to five [39][46]. The bill died "
 "with the government in April 2022. Its successor, the PML-N-led coalition of 2024, negotiated away the "
 "province question in the Punjab coalition deal with PML-Q by substituting a 'South Punjab package' of "
 "development spending and an additional secretariat at Multan, with a senior minister serving as the "
 "prime minister's coordinator for South Punjab; a Senate standing committee in January 2025 split over "
 "the revived private member's bill, JUI-F members warning that parity in the upper house would be "
 "weakened [38][45]. Meanwhile Hazara politics took an unusual turn: after a decade of street mobilization "
 "(the 2014 March for Hazara rights, four martyrs on 12 April 2014; Baba Haider Zaman's death in 2018) "
 "and two KP assembly resolutions (2014, 2022), the KP assembly - in power shared between parties with "
 "opposing histories on the demand - unanimously resolved in December 2025 that the federal government "
 "should complete the constitutional process for a Hazara province [41]. Sindh's demand set fragmented: "
 "MQM-P traded its support for the 2024 federal and Sindh coalitions for promises of metropolitan status "
 "for Karachi under (then proposed) Article 140-B/140-C provisions, while interior Sindh's Seraiki- and "
 "Sindhi-nationalist formations continued to press for a separate province (Mirpurkhas/Sukkur) with "
 "control of Thar coal royalties [32][51]. In Balochistan, the provincial question is nested inside an "
 "armed insurgency and a missing-persons protest cycle (the Voice for Baloch Missing Persons campaign "
 "into 2024-25), which both sharpens the case for re-scaling and makes it harder to hold anything as calm "
 "as a border referendum; the 'Pashtun Pakhtunkhwa' demand in the sasani (non-Baloch) north-east and the "
 "revived Kalat and Makran proposals each compete with, rather than complement, one another [8][20][43]. "
 "And in August-October 2026 the ECP was publicly pressing Punjab, Sindh, Khyber Pakhtunkhwa and the "
 "capital on local-government delimitation and schedules under Article 140A - with the commission "
 "threatening hearings and the KP assembly amending its own local government thresholds mid-process "
 "[52][53][54]."),

("p",
 "**Table 1** compresses this trajectory. Its central pattern: Pakistan's provincial boundaries have "
 "moved only at moments of *regime reconstruction* - the end of One Unit on the eve of the 1970 election, "
 "the post-1971 constitution, the post-2008 transition, the 2018 FATA merger - and never at a moment of "
 "routine politics. That pattern explains both the recurring talk of a '28th Amendment' as the vehicle for "
 "new provinces, and the consistent failure of every bill so far to survive the ordinary arithmetic it "
 "requires."),

("table", {
  "title": "Table 1. Chronology of Pakistan's provincial question (1947-2026)",
  "head": ["Period", "Development", "Significance for province formulation"],
  "widths": [0.16, 0.52, 0.32],
  "rows": [
   ["1947-55", "Quasi-federal dominion; princely accessions (Kalat 1948, contested); Objectives Resolution 1949", "Centralizing reflex; integration-by-force precedents"],
   ["1955-70", "One Unit; Chester report 1964 proposes smaller provinces incl. Hazara & South Punjab; princely states dissolved (Bahawalpur 1966)", "First systematic province-design debate; ignored"],
   ["1970-73", "LFO 1970 reconstitutes four provinces; 1971 secession; 1973 Constitution: Senate parity, CCI, NFC, royalty clause", "Founding bargain: four units, equal voice, formula money"],
   ["1977-99", "Zia recentralization; Nawaz era's 7th NFC attempt & 12th Amendments", "Autonomy promises used as coalition currency"],
   ["2000-08", "Musharraf Devolution Plan (district govs, elected nazims); reversed post-2008", "Decree-fed decentralization dies when the decree does"],
   ["2009-10", "7th NFC Award (57.5% provincial share); 18th Amendment devolution; Art. 140A local-government duty", "Autonomy 2.0; transfers, courts, police to provinces"],
   ["2013-18", "18th-Amendment implementation litigation; Hazara movement (2014 march; KP resolution); PTI South Punjab pledge", "Sub-provincial demands re-enter mainstream"],
   ["2018", "25th Amendment: FATA merges into KP; Rs1,250 bn 5-yr action plan; phased integration", "Only modern *completed* territorial project; template"],
   ["2019-22", "South Punjab bills & March 2022 cabinet summary (assembly 119; Senate 96->119; high court bench); Rs581 bn package; Multan additional secretariat", "Complete design exists; dies with governments"],
   ["2023", "Digital census (241.49m provinces+ICT; 247.54m national); CCI approval; delimitation on 2023 base", "Map arithmetic becomes auditable; 2027 census next"],
   ["2024", "26th Amendment (Art. 140A: ECP-run LG elections); PML-N-PML-Q Punjab govt with South Punjab 'package'; 27th Amendment talks on NFC parameters", "LG-enforcement moment; package-vs-province trade explicit"],
   ["2025", "Senate panel split on South Punjab (Jan); 27th Amendment passed (Nov: CDF, Const. Court, ouster clause); 11th NFC convened (Aug) & first session (Dec 4) incl. KP 14.62->19.42% demand; KP assembly *unanimous* Hazara resolution (Dec)", "Amendment capacity demonstrated without consensus; small-province anxieties rise"],
   ["2026", "ECP delimitation & directives for LG polls (Mar-Jul-Oct); '28th Amendment' restructuring reports incl. multi-province splits and federalized Karachi/Gwadar; minister 'no indications', consultations 'ongoing' (May)", "Province question re-nationalized, still at rumor stage"],
  ],
  "note": "Compiled from the legislative and reported record; sources as cited in the references."
}),


# ------------------------------------------------------------------ 3
("h1", "3. The Demands: Who Wants What Province, on What Grounds"),

("p",
 "Table 2 catalogues the principal new-province proposals live in Pakistani politics as of 2026, with "
 "their territorial bases, demographic sizes and political vehicles. The demands differ in every "
 "important respect except one: all are argued in the vocabulary of *grievance distance* - the claim that "
 "the parent province's capital is too far, its elites too extractive, and its budget too politically "
 "allocated - and all would, if realized, redraw not only maps but the distribution of Senate votes, NFC "
 "rupees, National Assembly seats, civil-service cadres and, in three cases, canals, gas fields and a "
 "port. That double character - recognition claim *and* resource claim - is what makes each demand "
 "simultaneously attractive and radioactive."),

("table", {
  "title": "Table 2. Principal new-province proposals and their bases (status as of October 2026)",
  "head": ["Proposed unit", "Territorial base", "Approx. population (2023 census)", "Principal grounds and vehicles", "Status"],
  "widths": [0.14, 0.20, 0.14, 0.35, 0.17],
  "rows": [
   ["South Punjab (Saraikistan)", "Multan, Bahawalpur & DG Khan divisions (12 districts; ~83,450 km2)",
    "~42-43 million",
    "Deprivation divide (education, health, MDPI); tail-end canal inequity; Seraiki language recognition since the 1960s; PTI pledge 2018; PML-Q coalition pressure; 2019/2022 amendment bills; Senate bill 2024",
    "Stalled; 'package + additional secretariat' substituted by federal government"],
   ["Hazara", "Hazara division of KP (Abbottabad, Haripur, Mansehra, Battagram, Torghar, Kohistans, Kolai-Palas)",
    "6.19 million",
    "Under-representation post-1970 merger of Malakand into NWFP; earthquake-reconstruction grievance (2005); provincial party of same name; KP assembly resolutions 2014, 2022, and unanimous December 2025 resolution urging Article 239 process",
    "Hostile-free in KP politics; no federal bill"],
   ["Karachi province", "Karachi division",
    "17 million+ (~20-25% of GDP; bulk of federal customs receipts)",
    "MQM ethno-territorial demand since 1989-92; MQM-P's 2024 metropolitan-governance bargain with PML-N; urban governance failure thesis; 2026 reports even mention federation-administered Karachi",
    "No bill; metropolitan option preferred by federation"],
   ["Interior Sindh (Seraikistan / new province)", "Sukkur, Larkana & Mirpurkhas divisions",
    "~18 million (est.)",
    "Tail-end water; Thar coal & Irrigation royalties; Sindhi-nationalist (Jeay Sindh) and Seraiki variants; 'Haq Dastak' assemblies 2024-25",
    "Marginalized; folded into wider Sindh splits in 2026 restructuring reports"],
   ["Pashtun belt of Balochistan ('Pakhtun Pakhtunkhwa')", "Pishin, Zhob, Loralai, Sibi, Musakhel, Duki & Barkhan belts",
    "~4 million (est.)",
    "Pashtun demographic weight in Balochistan (largest minority; now close to plurality in the north-east); ANP & jirga resolutions; counters Kalat nationalism",
    "No process; security situation dominates"],
   ["Kalat & Makran provinces", "Central Baloch divisions; Makran coast (Gwadar, Kech, Panjgur, Washuk)",
    "~5 million combined (est.)",
    "Kalat Khanate sovereignty memory; Makran 'Gwadar without us' grievance; Baloch nationalist and religious-party positions respectively",
    "Subsumed in 2026 restructuring proposals (Quetta/Kalat/Zhob/Makran four-way split)"],
   ["Bahawalpur", "Bahawalpur division (+ adjacent Cholistan belt)",
    "~10 million (est.)",
    "Princely-state institutional memory (merger 1959-66); grievance of patronage diversion to Multan/Lahore; PML-family politics; raised by IPP & others in 2026",
    "Echoed only in 2026 press; no bill"],
   ["Potohar", "Attock, Jhelum, Chakwal, Rawalpindi & Murree belt (definition varies)",
    "~13 million (est.)",
    "Garrison-town under-representation; industrial-zone land acquisition grievances; PML-N intra-Punjab balancing device in 2026 reports",
    "Press-only proposal"],
   ["Gilgit-Baltistan / AJK provincial status", "Existing territories",
    "GB ~1.7 million; AJK ~4.3 million",
    "GB: 2009 & 2018 empowerment orders give provincial-like autonomy without status; AJK assembly & all-party petitions (2023) for NFC inclusion and constitutionally protected rights",
    "Status quo; excluded from NFC and federal lists"],
  ],
  "note": "Populations: 2023 digital census for provinces/divisions where published; '(est.)' values are the author's aggregation of division-level census figures. Vehicles and status compiled from legislative and press record cited in refs [38][39][40][41][46][55][56]."
}),

("h2", "3.1 The southern Punjab case"),

("p",
 "South Punjab is the mature end of the spectrum: its demand has an intellectual literature (the Seraiki "
 "movement of the 1960s-70s, the Saraikistan campaigns of the 1980s), precise territorial arithmetic (the "
 "three divisions; 12 districts), and a fully drafted constitutional amendment twice tested in parliament "
 "[9][39]. Its grievance base is measurable: the UNDP's 2005 human development report mapped a 'deprivation "
 "divide' running through the country's south - a belt spanning southern Punjab, interior Sindh and northern "
 "Balochistan - and district-level multidimensional poverty in the Cholistan belt still runs at two to three "
 "times the national average [11]. Its fiscal grievance is the royalty anomaly: the gas of the Sulaiman "
 "foldbelt (Sui-adjacent fields, Uch, Qadirpur's southern Punjab side) flows through a system that pays "
 "Article 158 royalties to the province in which extraction occurs, an entitlement designed before the "
 "merger of the tribal districts and before any plausible new-province map, and today the single most "
 "explosive line item in any split scenario [1][30]. The federal response since 2022 - ring-fenced development "
 "packages (the Rs581 billion package of March 2022), an additional secretariat in Multan, 33 percent of "
 "Punjab's development budget earmarked for the south, and a coordinator-minister - is the 'package model': "
 "all the fiscal transfers, none of the constitutional sovereignty [39][45][55]. Critics call it "
 "colonial-style 'backward tracts' administration; realists call it the only thing Pakistan's coalition "
 "arithmetic can pass."),

("h2", "3.2 The Hazara case"),

("p",
 "Hazara shows the demand's second form: *the sub-provincial identity that fits an existing administrative "
 "unit like a glove*. Hazara division - 6.19 million people across some 16,000 km2, three districts created "
 "or carved in the 1990s, its own dialect geography (Hindko), its distinct social history of land tenure, "
 "shrines and literacy patterns, and a martyr-narrative sealed on 12 April 2014 when police fire killed "
 "protesters marching for provincial status - has the strongest case as *administrative coherence*: its "
 "boundaries already exist, its bureaucracy already operates at divisional level, and its creation would "
 "dilute no other identity claim except, arguably, the all-Pashtun reading of Khyber Pakhtunkhwa that the "
 "2024 'Pakhtunkhwa' rebranding controversy exposed [41][56]. The December 2025 unanimous KP resolution - "
 "presented by the ruling party's own MPA, invoking Article 239 expressly - marks the first time a mother "
 "provincial assembly has *asked to be diminished* as a body. Whether that consent was principled or "
 "tactical (the ANP-SPPP rivalry; the PTI's hostile silence; the army's suspicion of any border-talk while "
 "the Baloch and TTP insurgencies burn) is the question on which Hazara's fate now depends."),

("h2", "3.3 The Karachi and interior Sindh cases"),

("p",
 "Karachi is the *anti-Hazara*: the most concentrated economic unit in the country (roughly a quarter of "
 "GDP and the lion's share of customs revenue in a division of 17 million+) inside a province whose "
 "political economy is rural, feudal-biradari based, and controlled by the PPP; a city whose Mohajir "
 "working-class electorate has been mobilized for three decades behind, successively, MQM's ethno-territorial "
 "claim, its 2015 'Karachi as a separate administrative unit' formula, the 2024 metropolitan-governance "
 "bargain with PML-N (the federalized city proposal), and its share in the 2026 restructuring chatter "
 "[32][51][40]. The governance case is strong - no metropolitan area anywhere is more under-governed "
 "relative to its tax contribution - but the fiscal corollary cuts the other way for Sindh: a Sindh without "
 "Karachi loses its divisible-pool weight (its 24.55 percent NFC share collapses to under 11 on pro-rata "
 "population), which is precisely why any provincial-assembly consent required under Article 239(4) is "
 "unimaginable while the PPP governs Sindh. Interior Sindh's demands (the Seraiki 'Saraikistan' variant; the "
 "Sindhi-nationalist 'new Sindh' at Sukkur) articulate the same tail-end grievance as South Punjab - "
 "including the 2024-25 'Haq Dastak' (right of access) protests over canal waters and Thar coal royalties, "
 "and the recurring demand that Thar's power royalties flow to Matiarkhel and Tharparkar rather than to "
 "Karachi's provincial treasury - but remain organizationally weak [57]."),

("h2", "3.4 The Balochistan cluster"),

("p",
 "Balochistan contains the sharpest version of the dilemma: provincial demands that are themselves in "
 "conflict. Pashtun inhabitants of the jhalwan (north-eastern sasi belt: Zhob, Loralai, Musakhel, Barkhan, "
 "part of Duki) point to census arithmetic in which Pashtuns may now constitute 30-40 percent of the "
 "province and demand their own unit ('Pakhtun Pakhtunkhwa') to end 'Baloch hegemony' in the provincial "
 "state; Baloch nationalists read any division as the latest chapter of the 1955 and 1973 annexations and "
 "counter-claim Kalat; Makran's Gwadar-area communities demand a province of their own to capture port "
 "rents; and the Hazara minority in Quetta asks only for security guarantees, not territory [8][20]. The "
 "federal state's own practice is revealing: since 2013 it has created three Baloch 'development "
 "packages' and one division-split (Zhob division again), and in 2024-25 announced the long-demanded "
 "Hazara district divisional secretariat - all without touching provincial boundaries, all treated by "
 "Baloch parties as 'divide the province, protect the centre' tactics [58]. No institutional design "
 "question in this paper is more dangerous to answer badly: in an active-insurgency environment, border "
 "redrawing is not a neutral technical act - Toft's canonical finding is that federal boundary-making in "
 "multi-ethnic regions both pacifies and hardens, depending on whether the timing follows or interrupts "
 "violence and whether criteria are fixed before claims crystallize [18]."),

("h2", "3.5 Potohar, Bahawalpur, and the 'Punjab package' logic"),

("p",
 "The 2026 restructuring reports' most consequential feature is not any single new province but the *shape* "
 "of the package: Punjab into 3-5 units, Sindh into 2-5, KP into 4, Balochistan into 4, with Karachi and "
 "Gwadar federalized [40]. This is a 'wholesale re-regionalization' model - closer to One Unit's reversal "
 "logic than to any single movement's demand - and its advocates, including within the governing "
 "coalition, justify it precisely by that: no one *gets* a province as a favor; everyone *gets* smaller "
 "government. The Potohar and Bahawalpur proposals are the ballast in this design (each would neutralize "
 "the charge that Punjab merely concedes the south, each splits the Punjab-PPP/PML-N and MQM/PML-N "
 "voting blocs in ways that answer Senate-parity objections). The counter-charge, led by Punjab-based "
 "parties of every stripe, is that a five-way Punjab is an engine of instability - the 'new provinces "
 "as punishment' narrative that Rana Sanaullah's November 2025 '28th amendment' hint and the subsequent "
 "denials (May 2026: no indications; consultations ongoing) made impossible to retire [40][59]."),

# ------------------------------------------------------------------ 4
("h1", "4. The Constitutional and Legal Framework"),

("h2", "4.1 Article 239 and the consensual architecture"),

("p",
 "Pakistan's Constitution contains no Article 2/3-style provision empowering Parliament to 'form new "
 "States' on petition, as India's does. Province creation is instead *implied* through the general "
 "amendment power plus the territorial clause: Article 1 names the provinces; altering what Article 1 "
 "names is an amendment under Article 239, which requires two-thirds of the total membership of each "
 "house - and, under Article 239(4), **two-thirds of the total membership of the provincial assembly of "
 "any province whose limits are altered**. No referendum is required; the President's assent is formal. "
 "The 2022 South Punjab summary was drafted exactly to this route (with incidental amendments to "
 "Articles 51, 59, 88, 106, 158, 160, 175A, 198 and 218) [39]. Two doctrinal problems are unresolved "
 "and politically charged. First, textualists (including Pakistan Bar Council submissions) argue Article "
 "239(4) addresses *altering limits* of a province, not *substituting new federating units*, and that a "
 "dedicated creation clause should come first; the government line (and the implicit assumption of every "
 "bill since 1967) is that 239 suffices [40]. Second, the 'salient features' doctrine - the Supreme "
 "Court's doctrine since Zafar Ali Shah (2000) [76] that amendments cannot damage the Constitution's "
 "framework items (federalism among them) - casts a shadow both ways: a properly consensual re-scaling "
 "updates federalism without destroying it, while a centralizing package (e.g., federalizing Karachi and "
 "Gwadar without Sindh's and Balochistan's consent) could be reviewed - though after the Twenty-Seventh "
 "Amendment's November 2025 insertion of an ouster clause into Article 239 itself, the justiciability of "
 "even that review is a live, contested question [34][40][49]."),

("h2", "4.2 The dependent provisions: seats, courts, services, resources"),

("p",
 "Every new province is a package amendment, and the 2022 draft bill is the best available inventory of "
 "what that means. **Representation:** NA seats must be redistributed among provinces (Article 51; the "
 "Fifteenth and Twenty-Second Delimitation practice binds apportionment to the last published census, so "
 "any new-province election rests on the 2023 - and announced 2027 - census cycle [2]); Senate "
 "composition (Article 59) must absorb new delegations without breaking the equality doctrine that the "
 "smaller provinces treat as their constitutional *droit de suite*; provincial assembly sizes (Article "
 "106 and the Fourth Schedule) and reserved-seat formulas (Articles 51(3), 59(1)(d), 106(2)) must be "
 "re-derived - in the 2022 bill, Punjab shed 119 NA-eligible provincial seats to 252 and South Punjab "
 "gained a 119-seat house with a staggered first Senate class. **Judiciary:** a new high court means "
 "amending Article 175A's judicial commission membership (the 2022 draft added South Punjab's chief "
 "justice to the commission), the bar council statutes (Article 198), and the Supreme Court's own roster; "
 "**services:** Articles 238-242 govern transfer of officers and all-PAKISTAN cadre strength, and the "
 "Pakistan Administrative Service is already short of senior officers by a quarter - an apportionment of "
 "cadres between Lahore and Multan would be a distributional fight conducted by the federal government, "
 "not by the provinces. **Resources and water:** Article 158 (royalty on oil and gas extracted in a "
 "province) and Article 172 (inter-provincial water) cannot be left silent: a split Punjab must apportion "
 "the Indus system accord of 1991's 'Punjab' column between its successor units - an IRSA-administered "
 "process that Sindh's assembly has already resolved (2025) to treat as *res judicata*: the accord is "
 "between *founding provinces* and no internal boundary may reduce Sindh's share - which converts every "
 "upstream split into a downstream constitutional crisis [32][60]. Article 218A's CCI-approval regime for "
 "programs involving provincial foreign borrowing, and the Council's very composition (Article 153: chief "
 "ministers of each province), must absorb new members. None of this is impossible; all of it means a "
 "new province is legislated as a *constitutional convention*, not a boundary notification."),

("h2", "4.3 Precedents and their lessons"),

("p",
 "Four precedents discipline the imagination. (i) *1970*: Pakistan's most consequential provincial "
 "re-creation was done extra-constitutionally by LFO under martial law - a reminder that in Pakistan, "
 "maps have historically moved only where consent did not; (ii) *2010*: the 18th Amendment's -devolution "
 "was passed by consensus precisely to immunize it against reversal and court challenge, and it survived "
 "[36]; (iii) *2018*: the FATA merger paid for integration in ring-fenced federal money (Rs1,250 billion, "
 "5-year action plan) and phased services over 15 years, proving that Pakistan can execute a sub-national "
 "territorial project when the military, the courts and the host assembly are aligned [31][35]; and (iv) "
 "*2024-25*: the 26th and 27th Amendments showed what happens when a systemically important change is "
 "passed on bare arithmetic over boycott and protest - the settlements are *in force but not accepted*, "
 "which is why the law minister's May 2026 insistence that any 28th 'will proceed only once consensus is "
 "reached, explicitly invoking the 18th's cross-party consensus as the model' is the single most important "
 "official statement in the current debate [33][34][40]. The Constitution supplies a route; the polity has "
 "yet to supply the moment."),

# ------------------------------------------------------------------ 5
("h1", "5. Challenges"),

("h2", "5.1 The supermajority deficit: a consensual instrument in a majoritarian age"),

("p",
 "The arithmetic is fatal so far. Article 239 demands two-thirds of *total membership* - not of those "
 "present - in the National Assembly (336), the Senate (104; 96 for provinces and ICT in the 2022 "
 "baseline), and the concerned provincial assembly (Punjab 371; KP 155; Sindh 168; Balochistan 65). "
 "No party in Pakistan's history has held two-thirds of the Punjab assembly; the PML-N-led coalition of "
 "2024-26, formed with MQM-P and others after a contested election, governs Punjab and the centre without "
 "it; and the largest single party, PTI, treats the new-province agenda with a strategist's coolness - "
 "supporting it in its 2018 manifesto, tabling the 2019/2022 bills, then (in opposition after 2023) "
 "suspecting any Shehbaz Sharif package as either false coin or trap [39][46][61]. JUI-F's Senate objection - "
 "South Punjab would 'weaken the position of other provinces, especially Balochistan, in the upper "
 "house' - is not obstructionism; it is the doctrine working as designed [38]. The lesson is that "
 "province creation in Pakistan is not a policy but a *constitutional moment*, and the 2026 debate's "
 "fate will track national realignments more than it tracks Multan's school statistics."),

("h2", "5.2 The fiscal constitution: zero-sum transfers and the Article 160(3A) lock"),

("p",
 "Table 3 and Figure 1 present the fiscal terrain. Provinces receive roughly Rs7.44 trillion from the "
 "divisible pool (FY2024-25), out of total provincial revenue that is perhaps a sixth own-source at "
 "best; transfers are distributed horizontally on a 7th-NFC formula now 16 years old (Punjab 51.74, "
 "Sindh 24.55, KP 14.62, Balochistan 9.09 percent), and Article 160(3A) forbids making any province "
 "worse off [30][47][48]. A new province therefore cannot be *funded*; it can only be *carved*. On a "
 "pro-rata re-baseline, South Punjab would claim ~42/128 of Punjab's 3.70 trillion - about Rs1.22 "
 "trillion - leaving residual Punjab at Rs2.48 trillion, a 33 percent real cut to Lahore unless the "
 "federation adds money from the center's shrinking 42.5 percent; each additional unit compounds the "
 "problem in a state that has run primary deficits against IMF-programmed floors since 2019. The 2025 "
 "NFC politics make it concrete: Khyber Pakhtunkhwa's finance ministry now demands its share rise from "
 "14.62 to 19.42 percent on account of the merged districts' security costs, Balochistan demands a "
 "formula re-weighting for sparsity (its per-capita transfer of ~Rs44,700 is already the highest), and "
 "the eleventh NFC's December 2025 session opened amid federal signals to *reduce* the pool's provincial "
 "share in exchange for taking back devolved subjects - the so-called 'centralization bargain' floated "
 "with the 27th Amendment and reported for a possible 28th [37][47][62]. The November 2025 Business "
 "Recorder analysis shows the formula's own momentum: applying 2023-census population to the existing "
 "7th-NFC weights would cut Punjab's horizontal share by up to 4 percentage points and lift KP's by ~3 "
 "and Balochistan's by ~2 - meaning **every** re-baseline, with or without new provinces, is a fight at "
 "the razor's edge. A credible new-province design must break the zero-sum explicitly: transitional money "
 "outside the pool (the FATA action-plan model), a per-capita floor for successors of existing provinces "
 "(the 160(3A) direction reversed and generalized), and a sunset so 'transitional' does not become "
 "permanent federal patronage - the disease of the current package model."),

("table", {
  "title": "Table 3. Provincial fiscal snapshot (FY2024-25, rupees; 2023 census)",
  "head": ["Province", "Population", "Area (km2)", "Assembly (general seats)", "NFC transfers (Rs bn)", "Share of pool", "Transfers per capita (Rs)"],
  "widths": [0.15, 0.13, 0.11, 0.17, 0.15, 0.12, 0.17],
  "rows": [
   ["Punjab", "127.69 million", "205,344", "371", "3,695", "51.74%", "~28,900"],
   ["Sindh", "55.70 million", "140,914", "168", "1,856", "24.55%", "~33,300"],
   ["Khyber Pakhtunkhwa", "40.86 million", "~129,000 (incl. merged districts)", "155", "1,221", "14.62% (incl. 1% security premium)", "~29,900"],
   ["Balochistan", "14.89 million", "347,189", "51 (65 general under discussion, 2024-25)", "~666 (residual of 7,438 total)", "9.09%", "~44,700"],
  ],
  "note": "Transfers: FY2024-25 federal budget documents as reported (NFC-award transfers, incl. ~Rs195 bn straight transfers); horizontal shares are 7th NFC Award (2009/2010, as revised). Balochistan figure is residual; per-capita values are approximate. Own-source provincial taxes are an order of magnitude smaller than transfers."
}),

("fig", "figure1.png",
 "Figure 1. Population share (2023 census) versus NFC horizontal share (7th Award, FY2024-25). "
 "Balochistan already receives ~1.5x its population weight; KP, carrying the counter-terrorism premium, "
 "slightly less than it. Every new province re-opens this chart."),

("h2", "5.3 Water, energy and the 'res judicata' problem"),

("p",
 "Pakistan's internal boundaries were historically drawn *across* hydrology, not with it. Punjab's "
 "canal colonies - the engine of its politics - run from headworks in the north-east to tail-enders in "
 "the south-west and into Sindh; the 1991 Indus Apportionment Accord fixes provincial entitlements at "
 "the system's apex (IRSA's operational allocations bind the 'Punjab' and 'Sindh' boxes, not their "
 "future fragments); and Sindh's red line - no reallocation under any internal reorganization, restated "
 "in its assembly's 2025 resolution and in the litigation over the new GLO canal linking Taunsa to the "
 "Left Bank Outfall Drain area - means that any split of Punjab that leaves a 'South Punjab' controlling "
 "tail-end canals and cross-border return flows hands Sindh (and residual Punjab) a veto it will use "
 "[32][60][63]. The energy-royalty architecture is no less locked: Article 158's oil-and-gas royalty "
 "was designed for four provinces, its rate (Rs300 per mmbtu, unchanged since 2011) makes the fight over "
 "the Sui-Mehtar axis in a South Punjab scenario a zero-sum provincial revenue war; Gwadar's levies and "
 "CPEC profit-share flow to the federal government and the GDA, with Balochistan's assembly resolutions "
 "demanding per-container royalties - a demand that any Makran province would inherit as an unresolved "
 "crisis [1][8][64]. The federalization of Karachi or Gwadar floated in 2026 reporting would, "
 "constitutionally, be the *most* aggressive act in the package (expropriating a province's largest tax "
 "and customs base with no textual warrant under 239(4) - Sindh's and Balochistan's assemblies, one "
 "PPP-led and one coalition-dependent, would have to vote themselves poorer before Parliament could "
 "touch their coastlines) [40]."),

("h2", "5.4 Ethnicity, security, and the boundary-hardening risk"),

("p",
 "The comparative and domestic record warns that federal boundary-making in mixed regions is not a "
 "cheap peace. Pakistan's own 1970-71 sequence - re-regionalize, count, delimit, secede - is the dark "
 "baseline [4][18]. Three present-day amplifiers matter. *First*, the demands compete in the same rooms: "
 "Baloch-Pashtun boundary questions in Duki, Musakhel and Loralai run along a real ethnic frontier; "
 "a Karachi province would wall off Pashtun and Sindhi migrants (the city's 'Mohajir majority' is "
 "already plural and shrinking); Seraiki claims to Bahawalpur division and Saraiki claims to Multan's "
 "Seraiki south are mutually exclusive in practice [9][18]. *Second*, two of the claimant regions "
 "(Balochistan, and Khyber Pakhtunkhwa along the Durand fringe) are active conflict theatres - a "
 "TTP/KCP resurgence documented in 2025-26 attacks (Babur camp in KP, May 2025; frontier corps "
 "consequences across the merged districts), and the Baloch insurgency's escalation against both state "
 "and non-Baloch 'settler-colonial' targets in Jhal Mags and Harnai (August 2024) - so that a border "
 "process would run, realistically, under security conditions that India's Punjab and Indonesia's Papua "
 "precedents associate with *securitized* rather than negotiated delimitation [20][65][66]. *Third*, "
 "the federal center's own security institutions have historically treated provincialism as "
 "dis-integration-with-extra-steps; the military command's post-27th-Amendment structural preponderance "
 "(the Chief of Defence Forces construct) makes either outcome - veto or dictated settlement - more "
 "likely than the 2018 FATA-style alignment [34][49]. Toft's generalization applies exactly: where new "
 "boundaries follow identity *cores* with pre-agreed criteria (Hazara, Makran), they can settle claims; "
 "where they slice *frontier* zones between mobilized groups (Karachi's peripheries, Duki belt), they "
 "create focal points for violence - 'borders as votes, and votes as bullets' [18]."),

("h2", "5.5 Administrative capacity: the cost of duplicating the provincial state"),

("p",
 "A province is a fixed-cost machine. The 2022 draft bill's architecture implies, for one new unit: a "
 "119-member assembly (with secretariat), a chief minister's cabinet (21-25 ministers), a governor's "
 "house, a high court (a 20+ judge bench roster and a registry), an advocate-general establishment, a "
 "police department (IG, 4 ranges, specialized wings), a full secretariat of 30+ departments, PDA/ED "
 "offices, and a share of ECP, NAB, FIA and auditor infrastructure; recurring salary and pensions for "
 "perhaps 25,000-40,000 transferred and new officers, and capital costs (a capital precinct - "
 "Multan/Bahawalpur/Dera Gharbi competition for it would itself need a commission). The post-2018 "
 "merged-districts experience is the best available cost estimate: even with the state *adding* capacity "
 "to territory it had administered cheaply through political agents, the Rs1,250 billion 5-year plan has "
 "run years late and was only partially spent, with police lines at ~60 percent sanctioned strength in "
 "the merged KP districts in 2023 [31][21]. Multiplying that build-out across five or nine provinces "
 "in the same PAS cadre pool (Punjab's own LG elections in 2026 were still awaiting ECP delimitation "
 "notices in part for want of officers - a warning sign that matters more than any cost sheet [52]), and "
 "doing so while the 7th NFC's per-capita tilt already flatters sparser units, converts the paper case "
 "for proximity into a delivery-capacity risk. The Indonesia evidence is that sub-national unit creation "
 "under fiscal-transfers logic produced new bureaucratic elites faster than new services; the Nigeria "
 "evidence is that it produced rent-access politics at each new state capital [25][26]."),

("h2", "5.6 Legitimacy and procedural justice: who votes, who counts, who consents"),

("p",
 "Finally, the legitimation problem. Article 239 vests the decision in assemblies - which means in party "
 "high commands, whose intra-party democracy is the weakest institution in the system. There is no "
 "plebiscitary mechanism for territory in Pakistan's Constitution, and the one time the question was put "
 "to something like a popular process (the 2011-12 Gilgit-Baltistan reforms; the local referenda in "
 "Khyber Pakhtunkhwa's agency district mergers) the outcome was engineered by the center. Provinces "
 "created 'from above' in this way carry a democratic deficit that their first legislatures inherit; "
 "provinces denied 'from above' (Seraikistan after 1972; Hazara after 2014) carry the mirror deficit. A "
 "design that takes the vote seriously would couple assembly consent to a *consultative* mechanism "
 "(divisional conventions with reserved seats for women, peasants, workers, minorities, modeled on the "
 "Fourth Schedule's reserved-seat logic and on Canada's Clarity Act clarity-of-question discipline) and "
 "would require, as the 2022 draft implicitly did on minority seats, explicit inclusion floors so that "
 "new provinces do not become ethnic gerrymanders in three-year terms [39][67]. The women's and "
 "minorities' representation stakes are real: a new chamber doubles reserved-seat arithmetic (each "
 "assembly's women's quota is a fixed ratio, so nine provinces would mean 9x17+... - the Senate women's "
 "seats already produced Pakistan's first female deputy chairman), but only if the formula is revised "
 "with the split rather than left to first-past-the-post defaults."),

# ------------------------------------------------------------------ 5B comparative
("h1", "5B. Comparative Assessment: What Redrawing Provinces Has Done Elsewhere"),

("p",
 "Six comparators bracket the design space (Table 4). *India* shows re-scaling by linguistic logic "
 "succeeded as pacification once - the States Reorganisation Act of 1956, following the Fazl Ali "
 "Commission, redrew India's map along language lines *inside* a firm constitutional frame (Parliament's "
 "power under Articles 2-3 requires only 'expression of view' by the affected state, and the payoffs to "
 "new states were bounded by the Finance Commission's formula) - and has since created 24 more states, "
 "most recently Telangana (2014) after a decade-long agitation with a Congress split over it, and with "
 "the 2000 trilogy (Chhattisgarh, Uttarakhand, Jharkhand) bought by the BJP-NDA to end agitation cycles; "
 "the Indian case supports the *conflict-accommodation* hypothesis, but note the enabling conditions: "
 "sequential small moves, court-and-commission dispute settlement (Punjab and Haryana's water tribunal "
 "since 1983), a Finance Commission that re-baselines every five years, and an emergency-fiscal center "
 "that new states share [23][68]. *Indonesia* after 1999 conducted the largest peaceful territorial "
 "proliferation in the developing world - from 27 to 38 provinces and from hundreds to over 400 "
 "districts within a decade, driven by the 'big-bang' autonomy laws (22/25-1999, later 32/33-2004 with "
 "explicit *viability criteria*: minimum area, population, ten-year fiscal capacity, administrative "
 "infrastructure) - and the evidence is genuinely mixed: the new units shortened service distances and "
 "in several cases (North Kalimantan's copper belt; West Papua's fragments) delivered measurable welfare "
 "gains, while elsewhere autonomy ('DOB') became an electoral-currency machine for local elites "
 "financed by the general allocation fund, prompting the 2014 national moratorium on new provinces that "
 "still holds despite the 2022 Papua split (three new provinces created for special-autonomy reasons, "
 "not viability reasons) [25][26][69]. The Papua case is also the cautionary tail: division amid armed "
 "separatism did not resolve the separatist claim, it was read as administrative siege. *Nigeria's* 37 "
 "states - created by decree from 1967 to 1996 - delivered access and deconcentrated oil rent, but the "
 "derivation formula (13 percent of mineral rent to producing states, reduced for onshore oil to 5 "
 "percent zones) re-fights the resource question at every new boundary, and state viability (own "
 "revenue below 15-20 percent of budget across the federation) now mirrors Pakistan's provinces "
 "exactly [24]. *Ethiopia* constitutionalized the opposite logic - nationality-based units with a text "
 "on secession (Article 39) - and the Sidama (2019-20) and South West Ethiopia Peoples' (2021) referenda "
 "show new units *can* be formed constitutionally, while the Tigray war (2020-22) shows regional "
 "re-scaling between hostile governments is a casus belli; the mechanism is not separable from whether "
 "the center is trusted [24][70]. *Nepal's* 2015-2020 settlement is the closest to what a Pakistani "
 "28th Amendment would have to do: seven provinces drawn by a parliamentary constitutional committee "
 "over Madhesi and Tharu objections, then partially re-adopting identity-based names/boundaries after "
 "the 2015-16 agitation killed 44, with a fiscal-transfer schedule (equalization grants via a "
 "Constitution-specified commission) that re-cuts annually; the lesson is *process*: Nepal sequenced "
 "constitution-then-borders-then-finance-then-implementation-law, and the map still runs as an "
 "open quarrel [71]. *Kenya* demonstrates the alternative to redrawing: 47 county governments created "
 "in 2010 from existing districts, with a constitutionally fixed revenue share (15 percent of national "
 "revenue to counties, Article 202) - a service-delivery 'proxy provincehood' that produced Kenya's "
 "post-2013 growth in local health infrastructure and the infamous devolution-corruption split "
 "simultaneously, and - relevant to the 'package model' debate - is now regarded even by its fans as "
 "showing that *money and mandate matter more than altitude* [72]. The synthesis is uncomfortable for "
 "all domestic camps: re-scaling works for conflict accommodation when criteria precede claims "
 "(India 1956, Sidama); it inflates rent politics when transfers fund it unconditionally (Nigeria, "
 "Indonesia's district moratorium); and doing nothing - devolving weakly and packages-forever - "
 "entrenches the deprivation divide Pakistan already has (Kenya's county model, had it come without "
 "the 15 percent floor, would be Pakistan's current South Punjab package)."),

("table", {
  "title": "Table 4. Comparative re-scaling: mechanisms and outcomes",
  "head": ["Country / episode", "Mechanism", "Fiscal design", "Outcome signal"],
  "widths": [0.22, 0.30, 0.24, 0.24],
  "rows": [
   ["India 1956 & later", "Linguistic reorganization via commission + ordinary act (Art. 2-3); sequential small units", "Finance Commission 5-yearly formula; GST Council era; water tribunals for inter-state disputes", "Conflict containment; new states viable when old revenue base split on criteria"],
   ["Indonesia 1999-2014", "Post-authoritarian 'big bang'; 38 provinces, 400+ districts; viability criteria in UU 32/2004; 2014 moratorium", "DAU general allocation fund (transfers pay for new units), special autonomy for Papua/Aceh", "Service distance reduced; elite capture prominent; moratorium = implicit failure admit"],
   ["Nigeria 1967-1996", "State creation by decree 12->36->37; oil-derivation politics", "13% mineral derivation; federation account sharing by formula", "Access improved; unit viability declining; borders re-fight rent each time"],
   ["Ethiopia 1995-2021", "Nationality regions with Art. 39 exit right; referenda (Sidama 2019, SWE 2021)", "Block grants + revenue sharing via House of Federation", "Constitutional creation possible; wartime referenda polarize; secession right untested to stability"],
   ["Nepal 2015-20", "7 provinces by parliamentary committee; identity agitation forced re-draw", "Constitutional equalization grants via NC; provincial fiscal capacity minimal", "Process-first sequencing worked to hold union; map still contested"],
   ["Kenya 2010", "47 counties from existing districts (no new map, new level)", "Art. 202: 15% national revenue to counties, formula by statute", "Proximity dividend real; capture risk real; shows devolution can substitute for re-scaling"],
  ],
  "note": "Sources: Brass [23]; Clapham [24]; Evers & Rammohan [25]; Suberu [27]; Lawoti [71]; Faguet [72]; consolidated in the references."
}),
]
