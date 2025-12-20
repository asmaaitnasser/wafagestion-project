"""
Script de test pour vérifier les prédictions ML
"""
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent / "backend" / "src"))

from api.wrapper import MLPredictor

# Test
print("Testing MLPredictor.get_top_predictions()...")
result = MLPredictor.get_top_predictions(n_top=10)

print(f"\nResult shape: {result.shape if not result.empty else 'EMPTY'}")
print(f"Result:\n{result}")

if result.empty:
    print("\n❌ ERROR: DataFrame is empty!")
else:
    print(f"\n✅ SUCCESS: Got {len(result)} predictions")
    print(f"Tickers: {result['Ticker'].tolist()}")
