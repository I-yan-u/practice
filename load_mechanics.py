import time
import httpx
import asyncio
import random
import json
from faker import Faker

fake = Faker()
Faker.seed(0)  # Ensure reproducibility if run multiple times
url = "http://127.0.0.1:8000/api/mechanics/register"
latitude_range = (6.2607, 6.7020)  # (min_lat, max_lat)
longitude_range = (2.6731, 4.3556)  # (min_lon, max_lon)

async def generate_data(url):
    # Helper function to generate random phone numbers
    def generate_phone():
        return f"+234{random.randint(1000000000, 9999999999)}"

    # Initialize list to hold 100 generated entries
    data = []

    # Generate 100 entries
    for _ in range(200):
        entry = {
            "username": fake.user_name(),
            "email": fake.email(),
            "password": fake.password(length=12),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "address": f"{fake.street_address()}, Lagos, Nigeria",
            "phone": generate_phone(),
            "country": "Nigeria",
            "state": "Lagos",
            "location": [round(random.uniform(*latitude_range), 5), 
            round(random.uniform(*longitude_range), 5)]
        }

        async with httpx.AsyncClient() as client:
            try:
                # Use `json=entry` to ensure the data is sent as JSON
                response = await client.post(url, json=entry)
                response.raise_for_status()  # Check for HTTP errors
                data.append(response.json())
            except httpx.HTTPStatusError as e:
                print(f"Error posting data: {e}")
        
        # Use asyncio sleep for non-blocking wait
        await asyncio.sleep(0.5)

    # Write to JSON file
    with open("generated_data.json", "w") as f:
        json.dump(data, f, indent=4)

    print("200 entries generated and saved to 'generated_data.json'")

if __name__ == "__main__":
    asyncio.run(generate_data(url))
