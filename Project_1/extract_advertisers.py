import json
import csv
import random

# Load the JSON file
with open('advertisers_using_your_activity_or_information.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract all advertiser names from both lists
all_names = set()
for lv in data['label_values']:
    if 'vec' in lv:
        for item in lv['vec']:
            name = item.get('value', '').strip()
            all_names.add(name)

# Filter out non-ASCII / garbled names and empty strings
def is_clean(name):
    if not name:
        return False
    try:
        name.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

clean_names = [n for n in all_names if is_clean(n)]
clean_names.sort()

# Randomly sample 300
random.seed(42)
sample = random.sample(clean_names, min(300, len(clean_names)))
sample.sort()

# Category mapping - keyword-based first pass
def categorize(name):
    n = name.lower()

    # Finance
    if any(k in n for k in ['bank', 'capital', 'credit', 'loan', 'finance', 'invest', 'wealth',
                              'financial', 'insurance', 'mortgage', 'tax', 'fund', 'brokerage',
                              'trading', 'payroll', 'accounting', 'alliant', 'fidelity', 'vanguard',
                              'schwab', 'chase', 'wells fargo', 'citibank', 'amex', 'american express',
                              'mastercard', 'visa', 'cash', 'money', 'nerd wallet', 'nerdwallet',
                              'sofi', 'robinhood', 'coinbase', 'crypto', 'bitcoin', 'acorns', 'mint']):
        return 'Finance'

    # Tech
    if any(k in n for k in ['software', 'tech', 'app', 'digital', 'cloud', 'cyber', 'ai ', ' ai',
                              'saas', 'data', 'code', 'dev', 'gaming', 'game', 'studio', 'labs',
                              'grammarly', 'adobe', 'microsoft', 'google', 'apple', 'amazon',
                              'nvidia', 'intel', 'amd', 'hp', 'dell', 'lenovo', 'asus', 'samsung',
                              'spotify', 'netflix', 'discord', 'slack', 'zoom', 'notion',
                              'shopify', 'squarespace', 'wix', 'webflow', 'figma', 'canva',
                              'migaku', 'omen', 'razer', 'logitech', 'corsair']):
        return 'Tech'

    # Fitness
    if any(k in n for k in ['fitness', 'gym', 'workout', 'training', 'sport', 'running', 'run',
                              'yoga', 'pilates', 'crossfit', 'nutrition', 'protein', 'supplement',
                              'athletic', 'athletics', 'performance', 'muscle', 'weight',
                              'altra', 'vivobarefoot', 'hoka', 'brooks', 'asics', 'under armour',
                              'nike', 'adidas', 'reebok', 'lululemon', 'gymshark', 'peloton',
                              'whoop', 'garmin', 'strava', 'nasm', 'ace certified']):
        return 'Fitness'

    # Fashion
    if any(k in n for k in ['fashion', 'apparel', 'clothing', 'wear', 'style', 'boutique',
                              'shoes', 'shoe', 'boots', 'sneaker', 'denim', 'jeans', 'shirt',
                              'dress', 'suit', 'jacket', 'luxury', 'brand', 'collection',
                              'h&m', 'hm', 'zara', 'gap', 'uniqlo', 'j.crew', 'nordstrom',
                              'bloomingdale', 'macy', 'forever 21', 'shein', 'asos', 'farfetch',
                              'browns shoes', 'boot barn', 'brooklyn industries', 'burton snowboards']):
        return 'Fashion'

    # Food
    if any(k in n for k in ['food', 'restaurant', 'cafe', 'coffee', 'tea', 'kitchen', 'cook',
                              'eat', 'meal', 'diet', 'snack', 'drink', 'beverage', 'bakery',
                              'burger', 'pizza', 'sushi', 'grill', 'bbq', 'bar ', ' bar',
                              'wine', 'beer', 'spirits', 'whiskey', 'vodka', 'rum',
                              'starbucks', 'chipotle', 'mcdonalds', "mcdonald's", 'subway',
                              'doordash', 'grubhub', 'ubereats', 'instacart', 'whole foods',
                              'trader joe', 'hello fresh', 'hellofresh', 'factor', 'freshly']):
        return 'Food'

    # Travel
    if any(k in n for k in ['travel', 'hotel', 'resort', 'airline', 'flight', 'vacation',
                              'trip', 'tour', 'cruise', 'booking', 'airbnb', 'hostel',
                              'luggage', 'baggage', 'passport', 'adventure', 'explore',
                              'samsonite', 'tumi', 'away', 'expedia', 'kayak', 'trivago',
                              'marriott', 'hilton', 'hyatt', 'airbnb', 'delta', 'united',
                              'southwest', 'alaska airlines']):
        return 'Travel'

    # Education
    if any(k in n for k in ['university', 'college', 'school', 'education', 'learn', 'course',
                              'academy', 'institute', 'tutoring', 'degree', 'mba', 'online class',
                              'coursera', 'udemy', 'skillshare', 'masterclass', 'duolingo',
                              'khan', 'edx', 'bootcamp', 'coding school', 'study']):
        return 'Education'

    # Health / Wellness
    if any(k in n for k in ['health', 'wellness', 'medical', 'clinic', 'dental', 'pharmacy',
                              'vitamin', 'skincare', 'skin care', 'beauty', 'hair', 'spa',
                              'therapy', 'mental', 'sleep', 'meditation', 'cbd',
                              'hims', 'hers', 'ro health', 'noom', 'calm', 'headspace',
                              'cetaphil', 'neutrogena', 'cerave', 'ordinary', 'glossier']):
        return 'Health'

    # Automotive
    if any(k in n for k in ['auto', 'car', 'vehicle', 'motor', 'truck', 'suv', 'drive',
                              'dealer', 'dealership', 'toyota', 'honda', 'ford', 'chevy',
                              'chevrolet', 'bmw', 'mercedes', 'audi', 'tesla', 'hyundai',
                              'kia', 'subaru', 'mazda', 'volkswagen', 'porsche', 'lexus']):
        return 'Automotive'

    return 'Other'

# Build rows
rows = []
for i, name in enumerate(sample, 1):
    category = categorize(name)
    rows.append({'#': i, 'Advertiser Name': name, 'Category': category, 'Relevancy': ''})

# Write to CSV
with open('advertisers_300.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['#', 'Advertiser Name', 'Category', 'Relevancy'])
    writer.writeheader()
    writer.writerows(rows)

# Print summary
from collections import Counter
cats = Counter(r['Category'] for r in rows)
print("Done! Written to advertisers_300.csv")
print(f"Total rows: {len(rows)}")
print("\nCategory breakdown:")
for cat, count in sorted(cats.items(), key=lambda x: -x[1]):
    print(f"  {cat}: {count}")
