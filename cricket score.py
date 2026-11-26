import numpy as np

print("="*55)
print("INDIA vs AUSTRALIA- oo series analysis")
print("="*55)

india_scores = np.array([287, 312, 198, 345,267,389,223,301,278, 334])
australia_scores = np.array([256, 298, 210, 320, 290, 310, 275, 305, 299, 315])
match_labels = [f"match {i+1}" for i in range(1, 11)]

print("\n RAW SCORECRD")
print(F"  {'Match':<10}{'India':<8}{'Australia':<12}")
for i in range(len(india_scores)):
    winner = "IN India" if india_scores[i] > australia_scores[i] else "AuAustralia"
    print(f"  {match_labels[i]:<10}{india_scores[i]:>8}{australia_scores[i]:>12}   {winner:>10}")          
print("\nINDIA SCORE ANALYSIS")
print(f"  Average Score    : {np.mean(india_scores):.1f}")
print(f"  Highest Score    : {np.max(india_scores)}  (Match {np.argmax(india_scores)+1})")
print(f"  Lowest Score     : {np.min(india_scores)}  (Match {np.argmin(india_scores)+1})")
print(f"  Std Deviation    : {np.std(india_scores):.1f}  (consistency measure)")
print(f"  Total Runs       : {np.sum(india_scores)}")

india_top3_scores = np.sort(india_scores)[::-1][:3]
india_top3_idx    = np.argsort(india_scores)[::-1][:3]
print(f"  🏆 Top 3 Scores  : {india_top3_scores}")
print(f"  🏆 In Matches    : {[f'Match {i+1}' for i in india_top3_idx]}")

print("\nAUSTRALIA SCORE ANALYSIS")
print(f"  Average Score    : {np.mean(australia_scores):.1f}")
print(f"  Highest Score    : {np.max(australia_scores)}  (Match {np.argmax(australia_scores)+1})")
print(f"  Lowest Score     : {np.min(australia_scores)}  (Match {np.argmin(australia_scores)+1})")
print(f"  Std Deviation    : {np.std(australia_scores):.1f}  (consistency measure)")
print(f"  Total Runs       : {np.sum(australia_scores)}")

australia_top3_scores = np.sort(australia_scores)[::-1][:3]
australia_top3_idx    = np.argsort(australia_scores)[::-1][:3]
print(f"  🏆 Top 3 Scores  : {australia_top3_scores}")
print(f"  🏆 In Matches    : {[f'Match {i+1}' for i in australia_top3_idx]}")

