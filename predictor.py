# predictor.py
# 🚀 Predictor Pro – AI-Powered Dice Pattern Engine with Entropy and Seed Analysis

import statistics
import datetime
import json
import os
from collections import Counter

# --- Constants ---
ARCHIVE_PATH = "results_archive.json"

# --- Utils ---
def classify_odd_even(num):
    return "Odd" if num % 2 != 0 else "Even"

def estimate_cycle():
    now = datetime.datetime.now()
    return f"{now.hour}:{now.minute // 10 * 10}"

def save_to_archive(result):
    archive = load_archive()
    archive.append({"time": datetime.datetime.now().isoformat(), "value": result})
    with open(ARCHIVE_PATH, 'w') as f:
        json.dump(archive, f)

def load_archive():
    if os.path.exists(ARCHIVE_PATH):
        try:
            with open(ARCHIVE_PATH, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Archive corrupted. Starting new.")
            return []
    return []

def simulate_entropy(data):
    if len(data) < 10:
        return "Even", 50
    chunks = [data[i:i+5] for i in range(len(data) - 4)]
    odd_runs = sum(1 for chunk in chunks if all(classify_odd_even(x) == "Odd" for x in chunk))
    even_runs = sum(1 for chunk in chunks if all(classify_odd_even(x) == "Even" for x in chunk))
    if odd_runs > even_runs:
        return "Even", 55
    elif even_runs > odd_runs:
        return "Odd", 55
    return classify_odd_even(data[-1]), 50

# --- AI Core ---
class PredictorPro:
    def __init__(self):
        self.memory = []
        self.win_log = []
        self.loss_log = []
        self.prediction_log = []
        self.last_prediction = None
        self.last_confidence = None
        self.entropy_shift_log = []

    def learn(self, result):
        self.memory.append(result)
        if len(self.memory) > 100:
            self.memory.pop(0)
        self.detect_entropy()
        save_to_archive(result)

    def detect_entropy(self):
        if len(self.memory) >= 12:
            current = self.memory[-6:]
            prior = self.memory[-12:-6]
            cur_odd = sum(1 for x in current if classify_odd_even(x) == "Odd")
            pre_odd = sum(1 for x in prior if classify_odd_even(x) == "Odd")
            if abs(cur_odd - pre_odd) >= 5:
                cycle = estimate_cycle()
                self.entropy_shift_log.append((cycle, f"⚠️ Entropy spike: {pre_odd} ➝ {cur_odd}"))

    def predict_next(self):
        data = self.memory[-30:]
        if len(data) < 10:
            return "Even", 50, 10, "Not enough data"

        parity = [classify_odd_even(x) for x in data]
        odd_count = parity.count("Odd")
        even_count = parity.count("Even")
        prediction = "Odd" if odd_count > even_count else "Even"
        confidence = 55 + abs(odd_count - even_count) * 2

        entropy_pred, entropy_conf = simulate_entropy(data)
        if entropy_conf > confidence:
            prediction = entropy_pred
            confidence = entropy_conf

        if len(parity) >= 3 and all(p == parity[-1] for p in parity[-3:]):
            prediction = "Even" if prediction == "Odd" else "Odd"
            confidence -= 5

        filtered = [x for x in data if classify_odd_even(x) == prediction]
        hot_number = Counter(filtered).most_common(1)[0][0] if filtered else 10

        self.last_prediction = prediction
        self.last_confidence = confidence
        self.prediction_log.append((prediction, confidence, hot_number))

        return prediction, min(confidence, 95), hot_number, f"Prediction based on parity trend, entropy and reversal logic."

    def evaluate_result(self, actual_result):
        actual_parity = classify_odd_even(actual_result)
        prediction = self.last_prediction or self.predict_next()[0]
        win = prediction == actual_parity
        if win:
            self.win_log.append(actual_result)
        else:
            self.loss_log.append(actual_result)
        self.learn(actual_result)
        return win

    def get_summary(self):
        total = len(self.win_log) + len(self.loss_log)
        acc = round(len(self.win_log) / total * 100, 2) if total else 0
        return {
            "wins": len(self.win_log),
            "losses": len(self.loss_log),
            "accuracy": acc,
            "entropy_events": self.entropy_shift_log[-3:],
        }

# ✅ Test
if __name__ == "__main__":
    ai = PredictorPro()
    print("🔁 Predictor ready.")
