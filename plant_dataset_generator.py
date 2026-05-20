from faker import Faker
import random
import json

fake = Faker()

PLANTS = [
    "Tomato",
    "Potato",
    "Rice",
    "Corn"
]

DISEASES = [
    "Leaf Blight",
    "Rust",
    "Fungal Spot",
    "Powdery Mildew"
]

def generate_plant_record():

    return {
        "plant_name": random.choice(PLANTS),
        "disease_name": random.choice(DISEASES),
        "symptoms": fake.sentence(nb_words=10)
    }

if __name__ == "__main__":

    for _ in range(5):
        print(
            json.dumps(
                generate_plant_record()
            )
        )
