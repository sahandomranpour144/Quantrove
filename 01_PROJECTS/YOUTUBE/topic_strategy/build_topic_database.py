#!/usr/bin/env python3
"""
Generate the Quantrove Topic Database Excel Workbook (Quantrove_Topic_Database.xlsx)
using openpyxl with clean Institutional Data Intelligence formatting.
Updated per CEO Decision (2026-09-29):
- Permanent Four-Pillar Content Architecture (AI & ML Real World, AI + Finance + Trading, Finance Simplified, Data Stories)
- Season 1 remains OPEN (~10-15 episodes, minimum 3 longs per pillar)
- Season Boundary Review model for future seasons (no predetermined Season 2)
- Future topics use 'TBD — Season Boundary Review'
"""

import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

def build_database():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)  # Remove default sheet

    # Fonts & Colors
    FONT_TITLE = Font(name='Segoe UI', size=14, bold=True, color='202322')
    FONT_SUBTITLE = Font(name='Segoe UI', size=10, italic=True, color='555555')
    FONT_HEADER = Font(name='Segoe UI', size=10, bold=True, color='FFFFFF')
    FONT_SECTION_HDR = Font(name='Segoe UI', size=11, bold=True, color='202322')
    FONT_REGULAR = Font(name='Segoe UI', size=10, color='202322')
    FONT_BOLD = Font(name='Segoe UI', size=10, bold=True, color='202322')
    FONT_FORMULA = Font(name='Segoe UI', size=10, bold=True, color='233D4C')

    FILL_HEADER = PatternFill(start_color='202322', end_color='202322', fill_type='solid')
    FILL_SECTION = PatternFill(start_color='E6EDF3', end_color='E6EDF3', fill_type='solid')
    FILL_CARD_BG = PatternFill(start_color='F4F6F8', end_color='F4F6F8', fill_type='solid')
    FILL_HIGHLIGHT = PatternFill(start_color='E8F0C6', end_color='E8F0C6', fill_type='solid')

    BORDER_THIN = Border(
        left=Side(style='thin', color='D0D7DE'),
        right=Side(style='thin', color='D0D7DE'),
        top=Side(style='thin', color='D0D7DE'),
        bottom=Side(style='thin', color='D0D7DE')
    )

    # 1. TOPIC_DATABASE
    ws1 = wb.create_sheet(title='TOPIC_DATABASE')
    headers1 = [
        'Topic ID', 'Proposed Title', 'Core Question', 'Season', 'Story Arc / Focus',
        'Pillar', 'Curiosity Score (25%)', 'Season/Narrative Connection (20%)',
        'Data Availability (15%)', 'Visual Potential (15%)', 'Educational Value (15%)',
        'Evergreen Score (10%)', 'Total Score (100)', 'Why This Topic Matters',
        'Primary Data Sources', 'Main Visual Opportunities', 'Related Previous Episodes',
        'Possible Next Episode', 'Status', 'Sahand Notes', 'Claude/Agent Notes',
        'Date Added', 'Date Reviewed', 'CEO Decision'
    ]
    ws1.append(headers1)

    topics_data = [
        ('QT-001', 'Why Stock Market Crashes Happen', 'What really triggers a 20%+ single-day market collapse?',
         'Season 1', 'Money (Genesis)', 'Data Stories', 9, 8, 10, 9, 9, 10,
         '=(G2*25+H2*20+I2*15+J2*15+K2*15+L2*10)/10',
         'Foundational episode establishing margin calls, liquidity drainage, and behavioral cascades across 1929, 2008, 2020.',
         'FRED S&P 500, NYSE margin debt records, SEC market data', 'Historical chart overlays, margin call cascading animations, liquidity drain',
         'None (Series Premiere)', 'long02_50_years_recession_data', 'Published', 'Approved for series launch', 'Exemplary historical data narrative', '2026-08-20', '2026-08-22', 'Approved'),
        ('QT-002', 'What 50 Years of Recession Data Teaches Us', 'Can macroeconomic yield curves and spreads forecast economic winter?',
         'Season 1', 'Markets (Macro Data)', 'Data Stories', 8, 9, 10, 8, 10, 9,
         '=(G3*25+H3*20+I3*15+J3*15+K3*15+L3*10)/10',
         'Explores macroeconomic signal fidelity: 10Y-2Y yield curve inversions, Sahm Rule, and unemployment lags.',
         'FRED 10Y-2Y Treasury spread, BLS unemployment, NBER recession dates', 'Yield curve 3D surface inversion, historical recession timeline bars',
         'long01_why_stock_market_crashes', 'long03_how_algorithms_decide', 'Published', 'Strong macro foundation', 'High retention educational piece', '2026-08-25', '2026-08-28', 'Approved'),
        ('QT-003', 'How Trading Algorithms Actually Decide', 'How do automated execution systems process order books at sub-millisecond speeds?',
         'Season 1', 'Algorithms (Order Routing)', 'AI & ML Real World', 9, 10, 9, 10, 9, 9,
         '=(G4*25+H4*20+I4*15+J4*15+K4*15+L4*10)/10',
         'Decodes market microstructure: limit order books, bid-ask queues, and VWAP/TWAP execution algorithms.',
         'ITCH market data samples, exchange matching engine specs, SEC research', 'Order book depth animations, queue jumping visualizations',
         'long02_50_years_recession_data', 'long04_can_ai_predict_markets', 'Published', 'Breakthrough visualization standard', 'CleanText Manim vector standard established', '2026-09-05', '2026-09-08', 'Approved'),
        ('QT-004', 'Can AI Predict the Stock Market?', 'Why does deep learning thrive in vision and language, but fail against market reflexivity?',
         'Season 1', 'AI (Predictive Models)', 'AI + Finance + Trading', 10, 10, 9, 10, 9, 9,
         '=(G5*25+H5*20+I5*15+J5*15+K5*15+L5*10)/10',
         'Flagship investigation into the limits of AI in non-stationary, reflexive financial environments vs cat recognition.',
         'Quantitative backtests, alpha decay studies, Mandelbrot fat-tail data', 'Reflexivity loop animated diagrams, alpha decay half-life curves',
         'long03_how_algorithms_decide', 'long05_market_making_illusion', 'Published', 'Flagship episode, excellent pacing', 'Script humanizer baseline episode', '2026-09-12', '2026-09-15', 'Approved'),
        ('QT-005', 'The Market Making Illusion', 'Where does market liquidity actually come from, and why does it vanish in a crash?',
         'Season 1', 'Speed (Market Making)', 'Finance Simplified', 9, 10, 9, 9, 9, 8,
         '=(G6*25+H6*20+I6*15+J6*15+K6*15+L6*10)/10',
         'Unveils high-frequency market making: how firms collect half-spreads and pull quotes during volatile dislocations.',
         'Citadel/Virtu 606 reports, FINRA order routing audits, bid-ask spread logs', 'Spread tick visualizer, liquidity withdrawal animation',
         'long04_can_ai_predict_markets', 'TBD (Season 1 expansion)', 'Produced', 'Master rendered; ready for schedule', 'Final chapter of initial 5-part historical arc', '2026-09-18', '2026-09-21', 'Approved'),
        ('QT-006', 'The 8.2-Millisecond Race: Fiber, Microwaves & Co-Location', 'Why did trading firms spend $300M to shave 3 milliseconds between Chicago and NY?',
         'TBD — Season Boundary Review', 'Physical Layer / Latency', 'AI + Finance + Trading', 9, 8, 9, 10, 9, 8,
         '=(G7*25+H7*20+I7*15+J7*15+K7*15+L7*10)/10',
         'Physical geography of finance: microwave relay towers, hollow-core fiber, and server racks at CME Aurora.',
         'Spread Networks FCC filings, microwave line-of-sight coordinates, latency benchmarks', 'Geographic map with microwave hops vs curved fiber optic lines, speed of light comparison',
         'long05_market_making_illusion', 'TBD', 'Evaluating', 'Very high curiosity topic for tech & finance audiences', 'Evaluated for channel compatibility; pending Season Boundary Review', '2026-09-27', '2026-09-29', 'Pending'),
        ('QT-007', 'The Math Behind Jim Simons & Renaissance Medallion', 'What mathematical edge allowed the Medallion Fund to return 66% annualized for 30 years?',
         'TBD — Season Boundary Review', 'Quantitative Models / Medallion', 'AI + Finance + Trading', 10, 8, 8, 9, 9, 9,
         '=(G8*25+H8*20+I8*15+J8*15+K8*15+L8*10)/10',
         'Demystifies statistical arbitrage, hidden Markov models, kernel regression, and 50.75% win rate law of large numbers.',
         'Zuckerman biography data, academic papers on signal combination, SEC Form 13F filings', 'Markov state transition diagrams, law of large numbers cumulative profit curve',
         'None', 'TBD', 'Evaluating', 'Massive viewer appeal, needs rigorous math framing', 'Evaluated for channel compatibility; pending Season Boundary Review', '2026-09-27', '2026-09-29', 'Pending'),
        ('QT-008', 'Dark Pools: The 40% of Stock Trades You Never See', 'Why do sovereign funds and banks trade half of all US equities in secret private venues?',
         'TBD — Season Boundary Review', 'Dark Liquidity / ATS', 'Finance Simplified', 9, 7, 8, 9, 8, 9,
         '=(G9*25+H9*20+I9*15+J9*15+K9*15+L9*10)/10',
         'Examines ATS (Alternative Trading Systems), internalization, payment for order flow, and information leakage.',
         'SEC Form ATS-N filings, FINRA ATS weekly volume data, academic microstructure papers', 'Public exchange book vs private dark pool matching animation',
         'long05_market_making_illusion', 'TBD', 'Backlog', 'Great institutional insight', 'Evaluated for channel compatibility; pending Season Boundary Review', '2026-09-27', '2026-09-29', 'Pending')
    ]

    for row in topics_data:
        ws1.append(row)

    for col_idx in range(1, len(headers1) + 1):
        cell = ws1.cell(row=1, column=col_idx)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    ws1.row_dimensions[1].height = 28

    for row_idx in range(2, len(topics_data) + 2):
        ws1.row_dimensions[row_idx].height = 22
        for col_idx in range(1, len(headers1) + 1):
            c = ws1.cell(row=row_idx, column=col_idx)
            c.border = BORDER_THIN
            c.font = FONT_REGULAR
            if col_idx in [1, 4, 6, 19, 22, 23, 24]:
                c.alignment = Alignment(horizontal='center', vertical='center')
            elif col_idx in range(7, 13):
                c.alignment = Alignment(horizontal='right', vertical='center')
                c.number_format = '0.0'
            elif col_idx == 13:  # Total Score
                c.alignment = Alignment(horizontal='right', vertical='center')
                c.font = FONT_FORMULA
                c.number_format = '0.0'
                c.fill = FILL_HIGHLIGHT

    # 2. IDEA_INBOX
    ws2 = wb.create_sheet(title='IDEA_INBOX')
    headers2 = [
        'Idea ID', 'Raw Idea', 'Why I Find It Interesting', 'Possible Question',
        'Possible Pillar', 'Possible Season', 'Source / Inspiration',
        'Date Added', 'Status', 'Notes'
    ]
    ws2.append(headers2)
    inbox_data = [
        ('INB-001', 'Order Flow Toxicity & VPIN Metric',
         'Shows how algorithms detect informed traders dumping stock before prices move.',
         'Can algorithms mathematically measure when a trade contains toxic inside info?',
         'AI + Finance + Trading', 'TBD — Season Boundary Review', 'Easley, Lopez de Prado paper on VPIN',
         '2026-09-27', 'Raw', 'High mathematical elegance; great Manim formula potential.'),
        ('INB-002', 'Why 90% of Retail Options Expire Worthless',
         'Deconstructs theta decay, volatility smile, and market maker delta hedging.',
         'Are retail traders playing a mathematically rigged game with short-dated options?',
         'Finance Simplified', 'TBD — Season Boundary Review', 'OCC options clearing stats and retail brokerage studies',
         '2026-09-27', 'Raw', 'Strong retail curiosity and education value.'),
        ('INB-003', 'The Flash Crash of 2010: The 36-Minute Trillion Dollar Ghost',
         'A single spoofing trader in London triggered a massive automated liquidity cascade.',
         'How did one spoofing algorithm trigger a trillion-dollar cascade in 36 minutes?',
         'Data Stories', 'TBD — Season Boundary Review', 'CFTC-SEC Joint Report on May 6, 2010 Flash Crash',
         '2026-09-27', 'Under Review', 'Classic documentary case study.')
    ]
    for row in inbox_data:
        ws2.append(row)

    for col_idx in range(1, len(headers2) + 1):
        cell = ws2.cell(row=1, column=col_idx)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    ws2.row_dimensions[1].height = 28

    for row_idx in range(2, len(inbox_data) + 2):
        ws2.row_dimensions[row_idx].height = 22
        for col_idx in range(1, len(headers2) + 1):
            c = ws2.cell(row=row_idx, column=col_idx)
            c.border = BORDER_THIN
            c.font = FONT_REGULAR
            if col_idx in [1, 5, 6, 8, 9]:
                c.alignment = Alignment(horizontal='center', vertical='center')

    # 3. BRAINSTORM
    ws3 = wb.create_sheet(title='BRAINSTORM')
    headers3 = [
        'Brainstorm ID', 'Theme', 'Thought', 'Connection', 'Possible Episode',
        'Possible Short', 'Follow-up Question', 'Notes', 'Date'
    ]
    ws3.append(headers3)
    brainstorm_data = [
        ('BRN-001', 'Market Reflexivity',
         'Soros reflexivity concept applied to LLMs trading on other LLM sentiments.',
         'Connects EP04 AI prediction with future multi-agent market simulations.',
         'When AI Trades Against AI', 'Short on LLM echo chambers in markets',
         'What happens when 50 autonomous trading LLMs share the same base weights?',
         'Explore synthetic market collapse simulations.', '2026-09-27'),
        ('BRN-002', 'Speed of Light in Glass vs Air',
         'Light travels 30% slower in glass fiber (200,000 km/s) than through air microwaves (300,000 km/s).',
         'Physical reason why microwave towers beat fiber between Chicago and NJ.',
         'The 8.2-Millisecond Race', 'Short on fiber vs air latency',
         'Can laser satellite constellations beat ground microwaves for London-Tokyo?',
         'Starlink / Project Kuiper financial low-latency trading.', '2026-09-27')
    ]
    for row in brainstorm_data:
        ws3.append(row)

    for col_idx in range(1, len(headers3) + 1):
        cell = ws3.cell(row=1, column=col_idx)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    ws3.row_dimensions[1].height = 28

    for row_idx in range(2, len(brainstorm_data) + 2):
        ws3.row_dimensions[row_idx].height = 22
        for col_idx in range(1, len(headers3) + 1):
            c = ws3.cell(row=row_idx, column=col_idx)
            c.border = BORDER_THIN
            c.font = FONT_REGULAR
            if col_idx in [1, 9]:
                c.alignment = Alignment(horizontal='center', vertical='center')

    # 4. SEASONS (History & Season Boundary Planning)
    ws4 = wb.create_sheet(title='SEASONS')
    headers4 = [
        'Season Phase / ID', 'Season Title / Working Theme', 'Central Strategic Question',
        'Pillar / Narrative Focus', 'Episode Ref', 'Episode Topic / Strategic Scope',
        'Status', 'Narrative Role & Connection', 'Season Boundary Review Status'
    ]
    ws4.append(headers4)

    seasons_data = [
        ('Season 1 (Active)', 'The Hidden Mechanics of Modern Markets',
         'How did physical capital transform into autonomous algorithms, and who controls modern market liquidity?',
         'Data Stories', 'EP01', 'Why Stock Market Crashes Happen', 'Published',
         'Genesis: Establishes fragility of leveraged capital and panic cascades', 'Current Season Active (~10-15 Ep Target)'),
        ('Season 1 (Active)', 'The Hidden Mechanics of Modern Markets',
         'How did physical capital transform into autonomous algorithms, and who controls modern market liquidity?',
         'Data Stories', 'EP02', 'What 50 Years of Recession Data Teaches Us', 'Published',
         'Macro signals: Yield curve inversions and empirical cycle indicators', 'Current Season Active (~10-15 Ep Target)'),
        ('Season 1 (Active)', 'The Hidden Mechanics of Modern Markets',
         'How did physical capital transform into autonomous algorithms, and who controls modern market liquidity?',
         'AI & ML Real World', 'EP03', 'How Trading Algorithms Actually Decide', 'Published',
         'Microstructure: Electronic order books, matching engines, execution algorithms', 'Current Season Active (~10-15 Ep Target)'),
        ('Season 1 (Active)', 'The Hidden Mechanics of Modern Markets',
         'How did physical capital transform into autonomous algorithms, and who controls modern market liquidity?',
         'AI + Finance + Trading', 'EP04', 'Can AI Predict the Stock Market?', 'Published',
         'Predictive limits: Reflexivity, non-stationarity, and alpha decay half-life', 'Current Season Active (~10-15 Ep Target)'),
        ('Season 1 (Active)', 'The Hidden Mechanics of Modern Markets',
         'How did physical capital transform into autonomous algorithms, and who controls modern market liquidity?',
         'Finance Simplified', 'EP05', 'The Market Making Illusion', 'Produced',
         'Microsecond liquidity: How automated market makers pull quotes during panics', 'Current Season Active (~10-15 Ep Target)'),
        ('Season 1 (Active)', 'The Hidden Mechanics of Modern Markets',
         'How did physical capital transform into autonomous algorithms, and who controls modern market liquidity?',
         'Permanent 4 Pillars', 'EP06–EP15', 'Season 1 Expansion (Min 3 Longs per Pillar)', 'In Planning',
         'Expanding library depth across all 4 pillars before Season 1 closes', 'Minimum 3 longs/pillar required before Season 2'),
        ('Future Seasons', 'TBD — Season Boundary Review',
         'To be formulated at the conclusion of Season 1 based on empirical performance, audience retention, and CEO direction.',
         'Pillar Balance Review', 'TBD', 'Candidate Architectures to be Proposed at Season 1 Boundary', 'Governance Gate',
         'No predetermined Season 2 roadmap; CEO retains sole selection authority', 'Pending CEO-Triggered Season 1 Conclusion')
    ]
    for row in seasons_data:
        ws4.append(row)

    for col_idx in range(1, len(headers4) + 1):
        cell = ws4.cell(row=1, column=col_idx)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    ws4.row_dimensions[1].height = 28

    for row_idx in range(2, len(seasons_data) + 2):
        ws4.row_dimensions[row_idx].height = 24
        for col_idx in range(1, len(headers4) + 1):
            c = ws4.cell(row=row_idx, column=col_idx)
            c.border = BORDER_THIN
            c.font = FONT_REGULAR
            if col_idx in [1, 4, 5, 7]:
                c.alignment = Alignment(horizontal='center', vertical='center')

    # 5. SCORING_GUIDE
    ws5 = wb.create_sheet(title='SCORING_GUIDE')
    guide_rows = [
        ['Quantrove Topic Selection Framework & Scoring Guide', ''],
        ['Version 2.0 — Permanent Four-Pillar & Season Boundary Architecture', ''],
        ['', ''],
        ['1. Scoring Architecture', ''],
        ['Category', 'Weight', 'Description', 'Raw Score Scale (0 to 10)'],
        ['Curiosity / Click Potential', 25, 'Hook strength, counterintuitive premise, thumbnail contrast potential, viewer tension.', '0 = Obvious/Generic, 5 = Moderate interest, 10 = Irresistible paradox'],
        ['Season/Narrative Connection', 20, 'Compatibility with active season, existing channel narrative, and accumulated previous work (TBD if no future season).', '0 = Disconnected, 5 = Loose thematic tie, 10 = Essential narrative/pillar fit'],
        ['Data Availability', 15, 'Access to verified empirical data, FRED records, SEC filings, trade tapes, code repositories.', '0 = Pure speculation, 5 = Secondhand estimates, 10 = Verified tick-level / primary data'],
        ['Visual Potential', 15, 'Opportunities for clean Manim math animations, charts, and cinematic Flow B-roll.', '0 = Talking head/bullet points, 5 = Static charts, 10 = Dynamic 3D Manim / spatial visual'],
        ['Educational Value', 15, 'Real institutional insight delivered to viewer without dumbing down or hype.', '0 = Surface fluff, 5 = Standard textbook summary, 10 = Deep institutional mechanics revealed'],
        ['Evergreen Lifespan', 10, 'Relevance 2 to 5 years from now; enduring mathematical or market principles.', '0 = Ephemeral daily news, 5 = 6-month trend, 10 = Timeless structural truth'],
        ['TOTAL', 100, '', ''],
        ['', ''],
        ['2. Mathematical Scoring Formula', ''],
        ['Formula:', 'Final Score = (Curiosity * 25 + SeasonConnection * 20 + DataAvailability * 15 + VisualPotential * 15 + EducationalValue * 15 + Evergreen * 10) / 10'],
        ['Range:', '0.0 to 100.0'],
        ['', ''],
        ['3. Decision Interpretation Tiers', ''],
        ['Score Tier', 'Classification', 'Recommended Operational Action'],
        ['90.0 – 100.0', 'Exceptional Candidate', 'Priority Fast-Track. Immediate greenlight consideration for scripting and shot listing.'],
        ['80.0 – 89.9', 'Strong Candidate', 'Standard Greenlight Candidate. Proceed to topic research and packaging design.'],
        ['70.0 – 79.9', 'Strategic Review Required', 'Requires refinement. Identify low-scoring dimension (e.g. curiosity or visual) and rework premise.'],
        ['< 70.0', 'Normally Reject / Rework', 'Archive to Idea Inbox or fundamentally reconceptualize core question.'],
        ['', ''],
        ['4. Non-Negotiable Governance Principles', ''],
        ['Principle 1 (Pillars are Permanent):', 'The 4 pillars (AI & ML Real World, AI + Finance + Trading, Finance Simplified, Data Stories) are the permanent channel architecture.'],
        ['Principle 2 (Seasons are Temporary):', 'Seasons are temporary narrative groupings. Future seasons are NEVER predetermined and are designed only at Season Boundary Reviews.'],
        ['Principle 3 (Season 1 Scope):', 'Season 1 remains OPEN (~10-15 episodes target), requiring at least 3 long-form episodes per pillar before Season 2 can be initiated.'],
        ['Principle 4 (CEO Authority):', 'High scores are planning guidance only. Sahand (CEO) maintains 100% final approval over topic selection, season boundaries, and greenlights.']
    ]

    for r in guide_rows:
        ws5.append(r)

    ws5.cell(row=1, column=1).font = FONT_TITLE
    ws5.cell(row=2, column=1).font = FONT_SUBTITLE
    ws5.cell(row=4, column=1).font = FONT_BOLD
    ws5.cell(row=14, column=1).font = FONT_BOLD
    ws5.cell(row=18, column=1).font = FONT_BOLD
    ws5.cell(row=25, column=1).font = FONT_BOLD

    # Style table 1 (rows 5 to 12)
    for col_idx in range(1, 5):
        c = ws5.cell(row=5, column=col_idx)
        c.font = FONT_HEADER
        c.fill = FILL_HEADER
        c.alignment = Alignment(horizontal='center', vertical='center')

    for r_idx in range(6, 13):
        for c_idx in range(1, 5):
            c = ws5.cell(row=r_idx, column=c_idx)
            c.font = FONT_BOLD if r_idx == 12 else FONT_REGULAR
            c.border = BORDER_THIN
            if c_idx == 2:
                c.alignment = Alignment(horizontal='right', vertical='center')

    # Style table 2 (rows 19 to 23)
    for col_idx in range(1, 4):
        c = ws5.cell(row=19, column=col_idx)
        c.font = FONT_HEADER
        c.fill = FILL_HEADER
        c.alignment = Alignment(horizontal='center', vertical='center')

    for r_idx in range(20, 24):
        for c_idx in range(1, 4):
            c = ws5.cell(row=r_idx, column=c_idx)
            c.font = FONT_REGULAR
            c.border = BORDER_THIN

    # 6. DASHBOARD
    ws6 = wb.create_sheet(title='DASHBOARD')
    dash_rows = [
        ['Quantrove Production & Topic Strategy Dashboard', ''],
        ['High-Level Portfolio Metrics & Production Status', ''],
        ['', ''],
        ['Metric', 'Formula / Value', 'Operational Context'],
        ['Total Evaluated Topics', '=COUNTA(TOPIC_DATABASE!A2:A100)', 'Topics fully scored in database'],
        ['Raw Ideas in Inbox', '=COUNTA(IDEA_INBOX!A2:A100)', 'Unprocessed raw ideas awaiting review'],
        ['Average Topic Score', '=AVERAGE(TOPIC_DATABASE!M2:M100)', 'Average score across all evaluated topics'],
        ['Exceptional Candidates (Score >= 90)', '=COUNTIF(TOPIC_DATABASE!M2:M100, ">=90")', 'Top tier potential flagship episodes'],
        ['Strong Candidates (Score >= 80)', '=COUNTIF(TOPIC_DATABASE!M2:M100, ">=80")', 'Greenlight-ready candidates'],
        ['Topics Approved / Planned', '=COUNTIF(TOPIC_DATABASE!S2:S100, "Approved") + COUNTIF(TOPIC_DATABASE!S2:S100, "Evaluating")', 'Active pipeline candidates'],
        ['Topics Awaiting Season Boundary Review', '=COUNTIF(TOPIC_DATABASE!D2:D100, "TBD — Season Boundary Review")', 'High-value topics awaiting next season design'],
        ['Episodes Produced / Mastered', '=COUNTIF(TOPIC_DATABASE!S2:S100, "Produced")', 'Master exports ready for release'],
        ['Episodes Published', '=COUNTIF(TOPIC_DATABASE!S2:S100, "Published")', 'Live on YouTube channel'],
        ['', '', ''],
        ['Permanent Four-Pillar Distribution', 'Count', 'Cadence Rule & Balance Target'],
        ['1. AI & ML Real World', '=COUNTIF(TOPIC_DATABASE!F2:F100, "AI & ML Real World")', '1 pillar/wk, min 3 longs in S1'],
        ['2. AI + Finance + Trading', '=COUNTIF(TOPIC_DATABASE!F2:F100, "AI + Finance + Trading")', '1 pillar/wk, min 3 longs in S1'],
        ['3. Finance Simplified', '=COUNTIF(TOPIC_DATABASE!F2:F100, "Finance Simplified")', '1 pillar/wk, min 3 longs in S1'],
        ['4. Data Stories', '=COUNTIF(TOPIC_DATABASE!F2:F100, "Data Stories")', '1 pillar/wk, min 3 longs in S1']
    ]

    for r in dash_rows:
        ws6.append(r)

    ws6.cell(row=1, column=1).font = FONT_TITLE
    ws6.cell(row=2, column=1).font = FONT_SUBTITLE

    for col_idx in range(1, 4):
        c = ws6.cell(row=4, column=col_idx)
        c.font = FONT_HEADER
        c.fill = FILL_HEADER
        c.alignment = Alignment(horizontal='center', vertical='center')

    for r_idx in range(5, 14):
        ws6.row_dimensions[r_idx].height = 22
        for c_idx in range(1, 4):
            c = ws6.cell(row=r_idx, column=c_idx)
            c.border = BORDER_THIN
            if c_idx == 1:
                c.font = FONT_BOLD
            elif c_idx == 2:
                c.font = FONT_FORMULA
                c.alignment = Alignment(horizontal='right', vertical='center')
                c.fill = FILL_HIGHLIGHT
                if r_idx == 7:  # Average score
                    c.number_format = '0.0'
                else:
                    c.number_format = '0'
            else:
                c.font = FONT_REGULAR

    # Pillar table header
    for col_idx in range(1, 4):
        c = ws6.cell(row=15, column=col_idx)
        c.font = FONT_HEADER
        c.fill = FILL_HEADER
        c.alignment = Alignment(horizontal='center', vertical='center')

    for r_idx in range(16, 20):
        ws6.row_dimensions[r_idx].height = 22
        for c_idx in range(1, 4):
            c = ws6.cell(row=r_idx, column=c_idx)
            c.border = BORDER_THIN
            if c_idx == 1:
                c.font = FONT_BOLD
            elif c_idx == 2:
                c.font = FONT_FORMULA
                c.alignment = Alignment(horizontal='right', vertical='center')
                c.fill = FILL_CARD_BG
                c.number_format = '0'
            else:
                c.font = FONT_REGULAR

    # Auto-adjust column widths across all sheets
    for ws in wb.worksheets:
        for col in ws.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val_str = str(cell.value or '')
                if cell.number_format and val_str.startswith('='):
                    val_str = 'FormulaValue'
                if len(val_str) > max_len:
                    max_len = len(val_str)
            ws.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 48)

    ws1.column_dimensions['A'].width = 12
    ws1.column_dimensions['B'].width = 38
    ws1.column_dimensions['C'].width = 45
    ws1.column_dimensions['D'].width = 28
    ws1.column_dimensions['E'].width = 28
    ws1.column_dimensions['F'].width = 25
    ws1.column_dimensions['M'].width = 16
    ws1.column_dimensions['N'].width = 45

    ws4.column_dimensions['A'].width = 20
    ws4.column_dimensions['B'].width = 38
    ws4.column_dimensions['C'].width = 45
    ws4.column_dimensions['D'].width = 25
    ws4.column_dimensions['E'].width = 15
    ws4.column_dimensions['F'].width = 40
    ws4.column_dimensions['G'].width = 16
    ws4.column_dimensions['H'].width = 45
    ws4.column_dimensions['I'].width = 35

    # Data Validations
    dv_pillar = DataValidation(type='list', formula1='\"AI & ML Real World,AI + Finance + Trading,Finance Simplified,Data Stories\"', allow_blank=True)
    ws1.add_data_validation(dv_pillar)
    dv_pillar.add('F2:F100')

    dv_season = DataValidation(type='list', formula1='\"Season 1,TBD — Season Boundary Review\"', allow_blank=True)
    ws1.add_data_validation(dv_season)
    dv_season.add('D2:D100')

    dv_status = DataValidation(type='list', formula1='\"Backlog,Evaluating,Approved,Scripting,Production,Produced,Published,Rejected\"', allow_blank=True)
    ws1.add_data_validation(dv_status)
    dv_status.add('S2:S100')

    dv_decision = DataValidation(type='list', formula1='\"Approved,Needs Revision,On Hold,Rejected,Pending\"', allow_blank=True)
    ws1.add_data_validation(dv_decision)
    dv_decision.add('X2:X100')

    dv_inbox_pillar = DataValidation(type='list', formula1='\"AI & ML Real World,AI + Finance + Trading,Finance Simplified,Data Stories\"', allow_blank=True)
    ws2.add_data_validation(dv_inbox_pillar)
    dv_inbox_pillar.add('E2:E100')

    dv_inbox_status = DataValidation(type='list', formula1='\"Raw,Under Review,Promoted to Database,Archived\"', allow_blank=True)
    ws2.add_data_validation(dv_inbox_status)
    dv_inbox_status.add('I2:I100')

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Quantrove_Topic_Database.xlsx')
    wb.save(out_path)
    print(f"SUCCESS: Generated {out_path}")

if __name__ == '__main__':
    build_database()
