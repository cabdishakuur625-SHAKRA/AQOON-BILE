import json
import os
import math

# File paths
DART_FILE = r'lib/services/seed_data.dart'
JSON_FILE = r'scratch/seed_data.json'

def make_conceptual_pool(chapter_idx):
    """
    Returns a pool of distinct, high-quality English conceptual questions for a given chapter/unit.
    We define 15 conceptual questions for each of the 4 units.
    """
    pool = []
    
    if chapter_idx == 1:  # Business Plan
        pool = [
            {"question": "What is a business plan?", "options": {"a": "A document listing only the employee names and salaries", "b": "A written document describing a company's core business activities, objectives, and how it plans to achieve its goals", "c": "A list of products sold by competitors", "d": "A collection of customer contact information"}, "correctAnswer": "b"},
            {"question": "Which section of a business plan provides a brief overview of the entire plan, highlighting the key points?", "options": {"a": "Market Analysis", "b": "Executive Summary", "c": "Financial Plan", "d": "Appendix"}, "correctAnswer": "b"},
            {"question": "Why is a business plan important for a new startup?", "options": {"a": "It guarantees that the business will never face competition", "b": "It helps secure funding, clarify business focus, and guide future growth", "c": "It replaces the need for marketing campaigns", "d": "It is a legal requirement for all citizens"}, "correctAnswer": "b"},
            {"question": "The analysis of a business's Strengths, Weaknesses, Opportunities, and Threats is called:", "options": {"a": "Pestle analysis", "b": "SWOT analysis", "c": "Ratio analysis", "d": "Break-even analysis"}, "correctAnswer": "b"},
            {"question": "In a SWOT analysis, opportunities and threats are considered:", "options": {"a": "Internal factors", "b": "External factors", "c": "Controllable assets", "d": "Financial metrics"}, "correctAnswer": "b"},
            {"question": "Which of the following is considered a fixed cost for a manufacturing business?", "options": {"a": "Raw materials", "b": "Monthly factory rent", "c": "Direct labor wages", "d": "Packaging costs"}, "correctAnswer": "b"},
            {"question": "Which of the following is considered a variable cost?", "options": {"a": "Office rent", "b": "Raw materials used in production", "c": "Insurance premiums", "d": "Salaries of permanent managers"}, "correctAnswer": "b"},
            {"question": "What is the break-even point in business?", "options": {"a": "The point where net profit is maximized", "b": "The volume of sales where total revenue equals total costs, resulting in zero profit or loss", "c": "The day a business is registered with the government", "d": "The point where variable costs become zero"}, "correctAnswer": "b"},
            {"question": "Which section of a business plan describes the target market and how the business intends to attract customers?", "options": {"a": "Operations plan", "b": "Marketing plan", "c": "Financial plan", "d": "Executive summary"}, "correctAnswer": "b"},
            {"question": "In trade, the purchase of goods from foreign countries is called:", "options": {"a": "Exporting", "b": "Importing", "c": "Entrepòt trade", "d": "Wholesaling"}, "correctAnswer": "b"},
            {"question": "In trade, selling locally produced goods to other countries is called:", "options": {"a": "Importing", "b": "Exporting", "c": "Home trade", "d": "Retailing"}, "correctAnswer": "b"},
            {"question": "A document sent by a seller to a buyer stating the quantity and price of goods delivered is a/an:", "options": {"a": "Inquiry", "b": "Invoice", "c": "Order form", "d": "Receipt"}, "correctAnswer": "b"},
            {"question": "Which document is used by a buyer to ask about the price, availability, and delivery terms of goods from a seller?", "options": {"a": "Invoice", "b": "Inquiry", "c": "Quotation", "d": "Delivery note"}, "correctAnswer": "b"},
            {"question": "The physical arrangement of furniture, equipment, and staff within an office is called:", "options": {"a": "Office layout", "b": "Office structure", "c": "Business blueprint", "d": "Ergonomics"}, "correctAnswer": "a"},
            {"question": "What is the main advantage of an open-plan office layout?", "options": {"a": "Complete privacy for all employees", "b": "Better communication, supervision, and economical use of space", "c": "Absolute reduction of noise", "d": "Elimination of all equipment costs"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 2:  # Marketing Management
        pool = [
            {"question": "What is marketing in business?", "options": {"a": "The process of manufacturing goods in factories", "b": "The process of identifying, anticipating, and satisfying customer requirements profitably", "c": "The legal registration of a company's name", "d": "The auditing of financial accounts at the end of the year"}, "correctAnswer": "b"},
            {"question": "The 4 Ps of the marketing mix are:", "options": {"a": "People, Process, Physical evidence, Productivity", "b": "Product, Price, Place, Promotion", "c": "Plan, Perform, Produce, Profit", "d": "Purchase, Pay, Promote, Pack"}, "correctAnswer": "b"},
            {"question": "Which element of the marketing mix refers to the channel through which a product is distributed to customers?", "options": {"a": "Product", "b": "Place", "c": "Price", "d": "Promotion"}, "correctAnswer": "b"},
            {"question": "Which element of the marketing mix involves advertising, public relations, and sales promotions?", "options": {"a": "Product", "b": "Promotion", "c": "Price", "d": "Place"}, "correctAnswer": "b"},
            {"question": "The study of individuals and households and how they select, buy, use, and dispose of goods is called:", "options": {"a": "Market segmentation", "b": "Consumer behavior", "c": "Demographic profiling", "d": "Public relations"}, "correctAnswer": "b"},
            {"question": "Dividing a broad target market into smaller, distinct subsets of consumers who have common needs is called:", "options": {"a": "Product positioning", "b": "Market segmentation", "c": "Market penetration", "d": "Diversification"}, "correctAnswer": "b"},
            {"question": "Which type of marketing uses digital channels like websites, social media, and email to promote products?", "options": {"a": "Traditional marketing", "b": "Electronic marketing (E-marketing)", "c": "Direct trade marketing", "d": "Wholesale marketing"}, "correctAnswer": "b"},
            {"question": "What is the main benefit of e-marketing compared to traditional marketing?", "options": {"a": "It reaches only local audiences", "b": "It offers global reach, lower costs, and measurable results", "c": "It eliminates the need for any product development", "d": "It does not require internet connection"}, "correctAnswer": "b"},
            {"question": "A name, term, design, or symbol that identifies a seller's product and distinguishes it from competitors is a:", "options": {"a": "Patent", "b": "Brand", "c": "Trademark", "d": "Copyright"}, "correctAnswer": "b"},
            {"question": "Which pricing strategy involves setting a high price for a new, unique product to maximize short-term revenue before competitors enter?", "options": {"a": "Penetration pricing", "b": "Price skimming", "c": "Cost-plus pricing", "d": "Psychological pricing"}, "correctAnswer": "b"},
            {"question": "Which pricing strategy involves setting a low initial price to attract a large number of buyers and win market share quickly?", "options": {"a": "Price skimming", "b": "Penetration pricing", "c": "Premium pricing", "d": "Monopoly pricing"}, "correctAnswer": "b"},
            {"question": "The stages that a product goes through from its introduction to its eventual decline are known as the:", "options": {"a": "Business cycle", "b": "Product Life Cycle (PLC)", "c": "Marketing loop", "d": "Distribution chain"}, "correctAnswer": "b"},
            {"question": "During which stage of the Product Life Cycle do sales grow rapidly and profits peak?", "options": {"a": "Introduction", "b": "Growth", "c": "Maturity", "d": "Decline"}, "correctAnswer": "b"},
            {"question": "What is the primary goal of public relations (PR) in marketing?", "options": {"a": "To directly sell products to individual consumers", "b": "To build and maintain a positive image and relationship with the public", "c": "To set the wholesale price of goods", "d": "To write the financial budget of the company"}, "correctAnswer": "b"},
            {"question": "Which of the following is a key social factor influencing consumer behavior?", "options": {"a": "Motivation", "b": "Reference groups and family", "c": "Age and life cycle stage", "d": "Perception"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 3:  # Public Finance
        pool = [
            {"question": "What is public finance in economics?", "options": {"a": "The study of individual household budgeting", "b": "The branch of economics that deals with government revenue, government expenditure, and debt", "c": "The financing of private commercial corporations", "d": "The management of stock market listings"}, "correctAnswer": "b"},
            {"question": "The main source of revenue for most governments is:", "options": {"a": "Foreign aid", "b": "Taxes", "c": "Fines and penalties", "d": "Sale of public land"}, "correctAnswer": "b"},
            {"question": "A tax that is levied directly on an individual's income or wealth is called a:", "options": {"a": "Indirect tax", "b": "Direct tax", "c": "Value added tax", "d": "Excise duty"}, "correctAnswer": "b"},
            {"question": "A tax levied on goods and services, which can be shifted to the final consumer, is a/an:", "options": {"a": "Direct tax", "b": "Indirect tax", "c": "Income tax", "d": "Corporate tax"}, "correctAnswer": "b"},
            {"question": "What is a budget deficit?", "options": {"a": "When government revenue exceeds government expenditure", "b": "When government expenditure exceeds government revenue", "c": "When total imports equal total exports", "d": "When the central bank runs out of gold reserves"}, "correctAnswer": "b"},
            {"question": "What is a budget surplus?", "options": {"a": "When government spending is more than tax collection", "b": "When government revenue exceeds government expenditure", "c": "When the national debt is doubled", "d": "When imports exceed exports"}, "correctAnswer": "b"},
            {"question": "The total market value of all final goods and services produced within a country's borders in a given year is:", "options": {"a": "Gross National Product (GNP)", "b": "Gross Domestic Product (GDP)", "c": "Net National Product (NNP)", "d": "National Income"}, "correctAnswer": "b"},
            {"question": "Which approach calculates GDP by summing consumption, investment, government spending, and net exports?", "options": {"a": "Income approach", "b": "Expenditure approach", "c": "Output/Value-added approach", "d": "Double-entry approach"}, "correctAnswer": "b"},
            {"question": "Anything that is generally accepted as a medium of exchange, a measure of value, and a store of value is:", "options": {"a": "Gold only", "b": "Money", "c": "Barter goods", "d": "Credit cards"}, "correctAnswer": "b"},
            {"question": "What was the main disadvantage of the barter system of exchange?", "options": {"a": "It made transactions too fast", "b": "The necessity of double coincidence of wants", "c": "It required central bank supervision", "d": "It used paper money"}, "correctAnswer": "b"},
            {"question": "Which function of money allows people to save purchasing power for the future?", "options": {"a": "Medium of exchange", "b": "Store of value", "c": "Unit of account", "d": "Standard of deferred payment"}, "correctAnswer": "b"},
            {"question": "The institution responsible for regulating a country's monetary system, printing currency, and controlling interest rates is the:", "options": {"a": "Commercial bank", "b": "Central bank", "c": "Ministry of trade", "d": "Stock exchange"}, "correctAnswer": "b"},
            {"question": "Commercial banks are financial institutions that:", "options": {"a": "Formulate monetary policies for the state", "b": "Accept deposits from the public and grant loans to individuals and businesses", "c": "Print the national currency notes", "d": "Collect income taxes directly"}, "correctAnswer": "b"},
            {"question": "A tax system where the tax rate increases as the taxpayer's income increases is called:", "options": {"a": "Regressive tax", "b": "Progressive tax", "c": "Proportional flat tax", "d": "Indirect VAT"}, "correctAnswer": "b"},
            {"question": "What is national debt?", "options": {"a": "The money commercial banks owe to savers", "b": "The total accumulation of outstanding borrowing by a country's central government", "c": "The negative trade balance with other nations", "d": "The total value of physical assets in a country"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 4:  # The Adjusted Trial Balance and Financial Statements
        pool = [
            {"question": "The fundamental accounting equation is:", "options": {"a": "Assets = Liabilities - Owner's Equity", "b": "Assets = Liabilities + Owner's Equity", "c": "Liabilities = Assets + Owner's Equity", "d": "Assets + Liabilities = Owner's Equity"}, "correctAnswer": "b"},
            {"question": "What is a trial balance in accounting?", "options": {"a": "A list of bank statements for audit", "b": "A statement showing all ledger account balances divided into debits and credits to check mathematical accuracy", "c": "The final statement showing the company's net profit", "d": "A document listing only cash receipts"}, "correctAnswer": "b"},
            {"question": "If a trial balance does not balance, it indicates:", "options": {"a": "The business made a huge profit", "b": "An error has occurred in recording, posting, or balancing the accounts", "c": "The accounting equation has changed", "d": "The business has gone bankrupt"}, "correctAnswer": "b"},
            {"question": "Why are adjusting entries made at the end of an accounting period?", "options": {"a": "To correct mistakes made by the cashier", "b": "To align revenues and expenses with the period in which they occurred (matching principle)", "c": "To increase the cash balance in the bank", "d": "To pay dividends to shareholders"}, "correctAnswer": "b"},
            {"question": "Which financial statement shows the revenues, expenses, and net profit or loss of a business over a specific period?", "options": {"a": "Balance sheet", "b": "Income statement (Profit and Loss account)", "c": "Statement of changes in equity", "d": "Cash flow statement"}, "correctAnswer": "b"},
            {"question": "Which financial statement provides a snapshot of a business's assets, liabilities, and owner's equity at a specific point in time?", "options": {"a": "Income statement", "b": "Balance sheet", "c": "Cash flow statement", "d": "Trial balance"}, "correctAnswer": "b"},
            {"question": "Expenses that have been incurred but not yet paid at the end of the accounting period are called:", "options": {"a": "Prepaid expenses", "b": "Accrued expenses (outstanding expenses)", "c": "Deferred revenues", "d": "Unearned expenses"}, "correctAnswer": "b"},
            {"question": "Revenues that have been earned but not yet recorded or received are called:", "options": {"a": "Unearned revenues", "b": "Accrued revenues", "c": "Prepaid revenues", "d": "Bad debts"}, "correctAnswer": "b"},
            {"question": "What is depreciation in accounting?", "options": {"a": "The increase in the market value of land over time", "b": "The systematic allocation of the cost of a tangible asset over its useful life", "c": "The total cash spent on purchasing machinery", "d": "The decrease in the quality of raw materials"}, "correctAnswer": "b"},
            {"question": "In a balance sheet, cash, accounts receivable, and inventory are classified as:", "options": {"a": "Non-current assets", "b": "Current assets", "c": "Current liabilities", "d": "Intangible assets"}, "correctAnswer": "b"},
            {"question": "In a balance sheet, bank loans and accounts payable due within a year are classified as:", "options": {"a": "Non-current liabilities", "b": "Current liabilities", "c": "Current assets", "d": "Owner's equity"}, "correctAnswer": "b"},
            {"question": "What are non-current assets?", "options": {"a": "Cash and bank balances", "b": "Long-term assets like land, buildings, and machinery used to generate revenue", "c": "Short-term debts to be collected in 30 days", "d": "Prepaid insurance policies"}, "correctAnswer": "b"},
            {"question": "What represents the net profit of a business?", "options": {"a": "Total sales revenue minus opening inventory", "b": "Gross profit minus all operating expenses", "c": "Total cash receipts minus total cash payments", "d": "Total assets plus total liabilities"}, "correctAnswer": "b"},
            {"question": "The double-entry bookkeeping system requires that for every transaction:", "options": {"a": "Only one account is affected", "b": "The total debit amount must equal the total credit amount", "c": "All items are recorded in the cash book only", "d": "Capital must be increased"}, "correctAnswer": "b"},
            {"question": "A statement that tracks the cash inflows and outflows of a business over a period is the:", "options": {"a": "Trial balance", "b": "Cash flow statement", "c": "Balance sheet", "d": "Income statement"}, "correctAnswer": "b"}
        ]
        
    return pool

def generate_business_questions_for_chapter(ch_idx):
    """
    Generates exactly 27 easy, 30 medium, and 35 hard questions in English for the given chapter index (1-indexed).
    Combines conceptual questions with dynamically computed calculation questions.
    """
    questions = []
    conceptual = make_conceptual_pool(ch_idx)
    
    # ------------------ EASY QUESTIONS (27) ------------------
    easy_list = []
    # Fill up to 15 conceptuals first
    for q in conceptual:
        if len(easy_list) < 15:
            easy_list.append({
                "question": q["question"],
                "options": q["options"],
                "correctAnswer": q["correctAnswer"],
                "difficultyLevel": "easy"
            })
            
    # Add simple calculations or basic variations to reach exactly 27
    idx = len(easy_list)
    while len(easy_list) < 27:
        idx += 1
        if ch_idx == 1:  # Business Plan
            fc = idx * 1000
            vc = 10
            price = 20
            # BEQ = FC / (P - VC) = FC / 10
            beq = int(fc / 10)
            ans = f"{beq} units"
            easy_list.append({
                "question": f"A company has fixed costs of ${fc} and a contribution margin (price minus variable cost) of $10 per unit. Calculate the break-even quantity.",
                "options": {"a": f"{fc} units", "b": ans, "c": f"{beq*2} units", "d": "100 units"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 2:  # Marketing Management
            cost = idx * 10
            markup = 50
            sp = cost * 1.5
            ans = f"${sp:.2f}"
            easy_list.append({
                "question": f"A retail store purchases an item for ${cost:.2f} and applies a 50% markup. What is the selling price of the item?",
                "options": {"a": f"${cost*2:.2f}", "b": ans, "c": f"${cost*1.2:.2f}", "d": f"${cost+50:.2f}"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 3:  # Public Finance
            income = idx * 5000
            tax_rate = 10
            tax = int(income * 0.1)
            ans = f"${tax}"
            easy_list.append({
                "question": f"An individual earns a taxable income of ${income} per year. If the flat income tax rate is 10%, calculate the annual tax payable.",
                "options": {"a": f"${income}", "b": ans, "c": f"${tax*2}", "d": f"${tax/2:.0f}"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        else:  # adjusted trial balance / statements
            assets = idx * 10000
            equity = idx * 6000
            liab = assets - equity
            ans = f"${liab}"
            easy_list.append({
                "question": f"A business has total assets of ${assets} and owner's equity of ${equity}. According to the accounting equation, what is the value of total liabilities?",
                "options": {"a": f"${assets+equity}", "b": ans, "c": f"${equity}", "d": f"${assets/2:.0f}"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
            
    # ------------------ MEDIUM QUESTIONS (30) ------------------
    med_list = []
    # Fill remaining conceptuals first
    for q in conceptual[15:]:
        if len(med_list) < 10:
            med_list.append({
                "question": q["question"],
                "options": q["options"],
                "correctAnswer": q["correctAnswer"],
                "difficultyLevel": "medium"
            })
            
    # Generate moderate calculations to hit exactly 30
    idx = len(med_list)
    while len(med_list) < 30:
        idx += 1
        if ch_idx == 1:
            price = idx + 15
            vc = 10
            qty = 100
            fc = 300
            profit = (price - vc) * qty - fc
            ans = f"${profit}"
            med_list.append({
                "question": f"A startup sells a product for ${price} per unit. The variable cost per unit is ${vc} and fixed costs are ${fc}. If they sell {qty} units, calculate the net profit.",
                "options": {"a": f"${(price-vc)*qty}", "b": ans, "c": f"${profit+100}", "d": f"${profit/2:.0f}"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 2:
            cost = idx * 20
            sp = cost + 10
            margin = round(((sp - cost) / sp) * 100, 2)
            ans = f"{margin}%"
            med_list.append({
                "question": f"A product costs ${cost} to produce and is sold for ${sp}. Calculate the profit margin percentage of the product. (Round to two decimal places)",
                "options": {"a": "10.00%", "b": ans, "c": f"{margin*1.5:.2f}%", "d": f"{margin/2:.2f}%"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 3:
            price = idx * 50
            vat_rate = 15
            total = round(price * 1.15, 2)
            ans = f"${total:.2f}"
            med_list.append({
                "question": f"An electronics item is priced at ${price:.2f} before tax. If a Value Added Tax (VAT) of 15% is added, what is the final purchase price for the consumer?",
                "options": {"a": f"${price:.2f}", "b": ans, "c": f"${price+15:.2f}", "d": f"${total*1.2:.2f}"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        else:
            open_inv = idx * 100
            purchases = idx * 800
            close_inv = idx * 200
            cogs = open_inv + purchases - close_inv
            ans = f"${cogs}"
            med_list.append({
                "question": f"A trading business reports the following: Opening Inventory = ${open_inv}, Purchases = ${purchases}, and Closing Inventory = ${close_inv}. Calculate the Cost of Goods Sold (COGS).",
                "options": {"a": f"${open_inv+purchases}", "b": ans, "c": f"${cogs+100}", "d": f"${open_inv}"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
            
    # ------------------ HARD QUESTIONS (35) ------------------
    hard_list = []
    idx = 0
    while len(hard_list) < 35:
        idx += 1
        if ch_idx == 1:
            fc = idx * 2000 + 5000
            price = 50
            vc = 25
            target_profit = 5000
            # Required Volume = (FC + Target Profit) / (Price - VC) = (FC + 5000) / 25
            req_vol = int((fc + target_profit) / 25)
            ans = f"{req_vol} units"
            hard_list.append({
                "question": f"A manufacturing business has fixed costs of ${fc}. The selling price is $50 per unit and the variable cost is $25 per unit. How many units must be sold to earn a target profit of $5,000?",
                "options": {"a": f"{fc/25:.0f} units", "b": ans, "c": f"{req_vol+200} units", "d": f"{req_vol/2:.0f} units"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 2:
            fixed_mktg = idx * 1000 + 2000
            cpa = 20
            ltv = 100
            # Customer acquisition ROI = (LTV - CPA)*Qty - Fixed. Let Qty = 100.
            roi = (ltv - cpa) * 100 - fixed_mktg
            ans = f"${roi}"
            hard_list.append({
                "question": f"A company invests in a digital campaign with a fixed setup cost of ${fixed_mktg}. The Customer Acquisition Cost (CPA) is $20 per customer and the Lifetime Value (LTV) of a customer is $100. If they acquire 100 customers, what is the net return on investment (ROI)?",
                "options": {"a": f"${(ltv-cpa)*100}", "b": ans, "c": f"${roi+500}", "d": f"${roi/2:.0f}"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 3:
            c = idx * 5000
            i = idx * 2000
            g = idx * 3000
            x = idx * 1000
            m = idx * 500
            gdp = c + i + g + (x - m)
            ans = f"${gdp}"
            hard_list.append({
                "question": f"An economy reports the following national indicators: Consumption (C) = ${c}, Investment (I) = ${i}, Government Spending (G) = ${g}, Exports (X) = ${x}, and Imports (M) = ${m}. Calculate the GDP using the expenditure approach.",
                "options": {"a": f"${c+i+g+x+m}", "b": ans, "c": f"${gdp+1000}", "d": f"${c+i+g}"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        else:
            sales = idx * 5000 + 10000
            open_inv = 1000
            purchases = idx * 2000 + 3000
            close_inv = 1500
            operating_exp = 1500
            cogs = open_inv + purchases - close_inv
            gross_profit = sales - cogs
            net_profit = gross_profit - operating_exp
            ans = f"${net_profit}"
            hard_list.append({
                "question": f"A retailer's records show: Sales Revenue = ${sales}, Opening Inventory = ${open_inv}, Purchases = ${purchases}, Closing Inventory = ${close_inv}, and Operating Expenses = ${operating_exp}. Calculate the Net Profit for the period.",
                "options": {"a": f"${gross_profit}", "b": ans, "c": f"${net_profit+500}", "d": f"${net_profit/2:.0f}"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
            
    return easy_list + med_list + hard_list

def main():
    print("Beginning Business subject generation in English...")
    
    titles = {
        1: "Business Plan",
        2: "Marketing Management",
        3: "Public Finance",
        4: "The Adjusted Trial Balance and Financial Statements"
    }
    
    final_bus_chapters = []
    total_written = 0
    
    for i in range(1, 5):
        ch_id = f"bus_ch{i}"
        ch_questions = generate_business_questions_for_chapter(i)
        
        # Format IDs sequentially: Bus_Ch{i}_Q{01-92}
        formatted_qs = []
        for idx, q in enumerate(ch_questions):
            q_id = f"Bus_Ch{i}_Q{idx+1:02d}"
            options_clean = {k.lower(): str(v) for k, v in q["options"].items()}
            formatted_qs.append({
                "id": q_id,
                "question": q["question"],
                "options": options_clean,
                "correctAnswer": q["correctAnswer"].lower(),
                "difficultyLevel": q["difficultyLevel"],
                "subjectId": "bus",
                "chapterId": ch_id
            })
            
        ch_easy = [q for q in formatted_qs if q["difficultyLevel"] == "easy"]
        ch_med = [q for q in formatted_qs if q["difficultyLevel"] == "medium"]
        ch_hard = [q for q in formatted_qs if q["difficultyLevel"] == "hard"]
        
        print(f"Unit {i} ({titles[i]}): Total={len(formatted_qs)} (Easy={len(ch_easy)}, Medium={len(ch_med)}, Hard={len(ch_hard)})")
        
        # Verify counts
        assert len(ch_easy) == 27, f"Ch {i} easy is {len(ch_easy)}, expected 27"
        assert len(ch_med) == 30, f"Ch {i} medium is {len(ch_med)}, expected 30"
        assert len(ch_hard) == 35, f"Ch {i} hard is {len(ch_hard)}, expected 35"
        
        final_bus_chapters.append({
            "id": ch_id,
            "subjectId": "bus",
            "title": titles[i],
            "questions": formatted_qs
        })
        total_written += len(formatted_qs)
        
    print(f"Total Business questions compiled: {total_written}")
    
    # 2. Modify lib/services/seed_data.dart
    print("Reading seed_data.dart...")
    with open(DART_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx = content.find('{', content.find(start_str))
    end_idx = content.rfind("''';")
    
    if start_idx == -1 or end_idx == -1:
        print("Error: Could not locate JSON boundaries in seed_data.dart")
        return
        
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    # Rebuild the subjects list in seed_data.dart
    subjects = data.get("subjects", [])
    
    # Find existing business subject (id: 'bus')
    bus_idx = -1
    for idx, s in enumerate(subjects):
        if s.get("id") == "bus" or s.get("name") == "Business":
            bus_idx = idx
            break
            
    new_bus_chapters_format = []
    for ch in final_bus_chapters:
        new_bus_chapters_format.append({
            "title": ch["title"],
            "questions": ch["questions"]
        })
        
    new_bus_subject = {
        "name": "Business",
        "id": "bus",
        "chapters": new_bus_chapters_format
    }
    
    if bus_idx != -1:
        subjects[bus_idx] = new_bus_subject
        print("Replaced existing Business subject in subjects list.")
    else:
        subjects.append(new_bus_subject)
        print("Appended new Business subject in subjects list.")
        
    # Rebuild the final json string
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content[:start_idx] + new_json_str + "\n" + content[end_idx:]
    
    print("Writing updated seed_data.dart...")
    with open(DART_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated seed_data.dart!")
    
    # 3. Update seed_data.json if it exists
    if os.path.exists(JSON_FILE):
        print("Reading and updating seed_data.json...")
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data_json = json.load(f)
            
        # Update subjects dictionary
        if "subjects" not in data_json:
            data_json["subjects"] = {}
        data_json["subjects"]["bus"] = {"name": "Business"}
        
        # Update chapters dictionary
        if "chapters" not in data_json:
            data_json["chapters"] = {}
        # Clear existing business chapters first
        keys_to_remove = [k for k, v in data_json["chapters"].items() if v.get("subjectId") == "bus"]
        for k in keys_to_remove:
            del data_json["chapters"][k]
            
        # Add new chapters
        for ch in final_bus_chapters:
            data_json["chapters"][ch["id"]] = {
                "subjectId": "bus",
                "title": ch["title"]
            }
            
        # Update questions dictionary
        if "questions" not in data_json:
            data_json["questions"] = {}
        # Clear existing business questions
        keys_to_remove = [k for k, v in data_json["questions"].items() if v.get("subjectId") == "bus" or v.get("chapterId", "").startswith("bus_")]
        for k in keys_to_remove:
            del data_json["questions"][k]
            
        # Add all new questions
        for ch in final_bus_chapters:
            for q in ch["questions"]:
                data_json["questions"][q["id"]] = {
                    "question": q["question"],
                    "options": q["options"],
                    "correctAnswer": q["correctAnswer"],
                    "difficultyLevel": q["difficultyLevel"],
                    "subjectId": "bus",
                    "chapterId": q["chapterId"]
                }
            
        # Re-save seed_data.json
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(data_json, f, indent=2, ensure_ascii=False)
        print("Successfully updated seed_data.json!")
    else:
        print("seed_data.json not found, skipping.")

if __name__ == "__main__":
    main()
