import pandas as pd
import numpy as np
import random

def generate_realistic_data(num_rows):
    companies = [
        "Urban Company", "Classplus", "Paytm", "Apna", "Razorpay", "UpGrad", "Delhivery",
        "Airbnb", "Stripe", "Coinbase", "Snapchat", "Zoom", "Robinhood", "DoorDash", "Instacart",
        "Slack", "GitHub", "Square", "Palantir", "Shopify", "Peloton"
    ]
    
    cities = [
        "San Francisco", "New York", "Los Angeles", "Boston", "Austin", "Chicago", "Seattle", 
        "Denver", "Miami", "Dallas", "Gurgaon", "Noida", "Mumbai", "Bengaluru"
    ]
    
    industries = [
        "Tech", "Health", "Finance", "Education", "Retail", "Biotech", "AI", "E-commerce", 
        "Cybersecurity", "Travel", "Apps", "Home Services", "Marketplace", "Service Industry",
        "Financial Services", "FinTech", "Payments", "Software", "Mobile Payments"
    ]
    
    descriptions = [
        "A leading platform in its industry.", "Innovative tech solutions provider.", 
        "Revolutionizing financial services.", "Education platform transforming learning.",
        "Connecting people with services.", "Enhancing healthcare with technology.", 
        "Optimizing logistics and delivery.", "A major player in e-commerce.",
        "Disrupting the financial landscape.", "Empowering businesses with new tech."
    ]
    
    def random_founding_year():
        return random.randint(2010, 2024)
    
    def random_funding_amount():
        return round(random.uniform(500000, 50000000), 2)
    
    def random_employees():
        return random.randint(10, 1000)
    
    data = {
        "Company": [random.choice(companies) for _ in range(num_rows)],
        "City": [random.choice(cities) for _ in range(num_rows)],
        "Starting Year": [random_founding_year() for _ in range(num_rows)],
        "Founders": [f"Founder_{random.randint(1, 100)}" for _ in range(num_rows)],
        "Industries": [random.choice(industries) for _ in range(num_rows)],
        "Description": [random.choice(descriptions) for _ in range(num_rows)],
        "No. of Employees": [random_employees() for _ in range(num_rows)],
        "Funding Amount in USD": [random_funding_amount() for _ in range(num_rows)],
        "Funding Rounds": [random.randint(1, 10) for _ in range(num_rows)],
        "No. of Investors": [random.randint(1, 15) for _ in range(num_rows)]
    }
    
    df = pd.DataFrame(data)
    return df

# Generate 500 new rows of data
additional_data = generate_realistic_data(500)
additional_data.to_csv("expanded_startup_data_realistic.csv", index=False)

print("Realistic dataset generated and saved to 'expanded_startup_data_realistic.csv'.")
