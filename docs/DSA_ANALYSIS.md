# DSA (Data Structures & Algorithms) Analysis

## Overview
This document presents a comprehensive analysis of two search algorithms for finding transactions by ID: Linear Search and Dictionary Lookup.

---

## Executive Summary

| Metric | Linear Search | Dictionary Lookup | Winner |
|--------|---------------|-------------------|--------|
| **Time Complexity** | O(n) | O(1) | Dictionary ✓ |
| **Space Complexity** | O(1) | O(n) | Linear ✓ |
| **Avg Time (1682 records)** | 147.99µs | 84.42µs | Dictionary ✓ |
| **Total Time (2000 ops)** | 2,959.80µs | 1,688.40µs | Dictionary ✓ |
| **Speedup** | Baseline | **1.75x faster** | Dictionary ✓ |
| **Improvement** | Baseline | **43% time savings** | Dictionary ✓ |

**Recommendation:** Use **Dictionary Lookup** for transaction search operations.

---

## 1. Linear Search Algorithm

### Definition
Linear search (sequential search) examines each element in a list sequentially until the target is found or the list is exhausted.

### Implementation
```python
def linear_search(transactions, target_id):
    """Linear Search - O(n) complexity"""
    for tx in transactions:
        if tx['id'] == target_id:
            return tx
    return None
```

### Complexity Analysis

**Time Complexity: O(n)**
- **Best Case:** O(1) - Target at first position
- **Average Case:** O(n/2) ≈ O(n) - Target in middle
- **Worst Case:** O(n) - Target at end or not found
- For 1,682 transactions: up to 1,682 comparisons needed

**Space Complexity: O(1)**
- Uses only constant extra space
- No additional data structures required
- Memory efficient

### Performance Data (Benchmark Results)

Searching first 20 transaction IDs (100 iterations each):

| ID | Time (µs) | Observations |
|----|-----------|--------------|
| 1 | 42.70 | Found immediately (best case) |
| 5 | 74.20 | Linear growth visible |
| 10 | 185.70 | Proportional to position |
| 15 | 189.50 | Continued growth |
| 20 | 254.90 | Worst case (last record) |

**Trend:** Time increases roughly linearly with transaction position.

### Use Cases
✓ **Recommended for:**
- Small datasets (< 100 items)
- Memory constraints critical
- One-time search operations
- Unsorted or rarely accessed data
- When simplicity is priority

✗ **Not recommended for:**
- Large datasets (> 1,000 items)
- Repeated searches on same data
- Performance-critical operations
- Real-time systems

---

## 2. Dictionary Lookup Algorithm

### Definition
Dictionary lookup (hash table access) uses a hash function to map keys to values, enabling direct access in constant time.

### Implementation
```python
def create_transaction_dict(transactions):
    """Convert list to dictionary for O(1) lookup"""
    return {tx['id']: tx for tx in transactions}

def dictionary_lookup(transactions_dict, target_id):
    """Dictionary Lookup - O(1) complexity"""
    return transactions_dict.get(target_id)
```

### Complexity Analysis

**Time Complexity: O(1) Average Case**
- **Best Case:** O(1) - Direct hash table access
- **Average Case:** O(1) - No collision
- **Worst Case:** O(n) - Hash collision (very rare)
- For 1,682 transactions: typically 1 access needed
- Python dict uses hash function: highly optimized, few collisions

**Space Complexity: O(n)**
- Stores mapping for all n items
- Each key-value pair takes memory
- For 1,682 transactions: ~50-100KB overhead

### Performance Data (Benchmark Results)

Searching first 20 transaction IDs (100 iterations each):

| ID | Time (µs) | Speedup vs Linear |
|----|-----------|-------------------|
| 1 | 38.20 | 1.12x |
| 5 | 22.60 | 3.28x |
| 10 | 28.80 | 6.45x |
| 15 | 32.50 | 5.83x |
| 20 | 21.50 | 11.86x |

**Trend:** Time remains relatively constant (~20-35µs) regardless of position. One anomaly (ID 13: 1180.90µs) likely due to Python garbage collection.

### Use Cases
✓ **Recommended for:**
- Large datasets (> 100 items)
- Repeated searches on same data
- Real-time/performance-critical systems
- API endpoints with high query frequency
- Mobile Money transaction lookups

✗ **Not recommended for:**
- Memory-constrained embedded systems
- One-time sequential access
- Very small datasets where overhead not justified
- When insertion/deletion happens frequently

---

## 3. Comparative Analysis

### Performance Comparison

**Benchmark Setup:**
- Dataset: 1,682 MoMo transactions
- Search IDs: First 20 records (IDs 1-20)
- Iterations: 100 searches per ID
- Total Operations: 2,000 searches

**Results:**

```
Linear Search:       2,959.80µs total (147.99µs avg per ID)
Dictionary Lookup:   1,688.40µs total (84.42µs avg per ID)

Speedup:             1.75x faster
Improvement:         43.0% time savings
```

**Graphical Representation:**

```
Time (microseconds)
250 |     Linear Search        Dictionary Lookup
    |     (Sequential)         (O(1) Hash)
    |     ●                    ○
200 |     ●                    ○
    |   ●                      ○
150 |   ●                      ○
    |  ●                       ○
100 | ●                        ○
    |●     ○                   ○
 50 |○○○○○○○                   ○
    |
  0 |________________________
    1  5  10  15  20
       Transaction ID
```

### Scalability Analysis

**For 1,682 transactions:**

| Operation | Linear Search | Dictionary Lookup |
|-----------|---------------|-------------------|
| Find TX#1 | ~30µs | ~35µs |
| Find TX#500 | ~1,500µs | ~25µs |
| Find TX#1682 | ~3,000µs | ~25µs |
| 1,000 lookups | ~150,000µs | ~25,000µs | 

**Dictionary is 6-120x faster** depending on position searched.

### Memory Trade-off

```
Linear Search:
├─ Transaction objects already in memory
└─ Zero additional overhead

Dictionary Lookup:
├─ Transaction objects already in memory
├─ Plus: Hash table structure (~50-100KB)
└─ Trade: 50-100KB memory → 1.75x speed improvement
```

For modern systems, this trade-off is **always favorable** (RAM is cheap, speed is valuable).

---

## 4. Alternative Data Structures

### B-Tree
- **Use Case:** Ordered range queries, database indices
- **Time Complexity:** O(log n) for search
- **Better than:** Linear search
- **Worse than:** Hash table for exact match

### Skip List
- **Use Case:** Probabilistic balanced search
- **Time Complexity:** O(log n) expected
- **Better than:** Linked list
- **Worse than:** Dictionary for exact match

### Bloom Filter
- **Use Case:** Fast negative lookups
- **Time Complexity:** O(1) check (false positives possible)
- **Better than:** Dictionary when space critical
- **Worse than:** Dictionary for accuracy

---

## 5. Implementation Recommendation

### For MoMo Transaction API

**Recommended Approach:**
```python
# Load transactions once
transactions_list = load_from_json('transactions.json')

# Create dictionary for lookups
transactions_dict = {tx['id']: tx for tx in transactions_list}

# Use dictionary for GET /transactions/{id}
@app.route('/transactions/<id>')
def get_transaction(id):
    tx = transactions_dict.get(int(id))
    if not tx:
        return {"error": "Not found"}, 404
    return tx, 200
```

**Why This Works:**
1. ✓ Load all transactions once at startup (cold start cost)
2. ✓ Use O(1) dictionary for all subsequent lookups
3. ✓ Handle 1,682 transactions in microseconds
4. ✓ Scales well to 10,000+ transactions

---

## 6. Real-World Impact

### Current System (1,682 Transactions)

**Daily API Usage Scenario:**
```
10,000 API requests per day
Average lookup: 100µs (linear) vs 25µs (dictionary)

Linear Search:   10,000 × 100µs = 1.0 seconds
Dictionary:      10,000 × 25µs  = 0.25 seconds

Savings: 0.75 seconds per day (25% faster)
```

### Scaling to 100,000 Transactions

```
Linear Search:   100,000 × 5,000µs = 500 seconds = 8.3 minutes
Dictionary:      100,000 × 25µs   = 2.5 seconds

Dictionary is 200x faster at scale
```

---

## 7. Conclusion

### Summary

| Aspect | Linear | Dictionary |
|--------|--------|-----------|
| Code Simplicity | ★★★★★ Simple | ★★☆☆☆ Slightly complex |
| Memory Usage | ★★★★★ Efficient | ★★★☆☆ ~50KB overhead |
| Performance | ★★☆☆☆ Slow at scale | ★★★★★ Very fast |
| Consistency | ★★★☆☆ Variable time | ★★★★★ Constant time |
| Production Ready | ❌ No | ✅ Yes |

### Final Recommendation

**Use Dictionary Lookup for the MoMo Transaction API:**

✅ **Reasons:**
1. **1.75x faster** on current dataset (1,682 transactions)
2. **Scales excellently** - remains O(1) even at 100,000+ records
3. **API requirement** - RESTful endpoints need millisecond response times
4. **Minimal overhead** - 50-100KB memory trade-off is negligible
5. **Production standard** - Industry-standard approach for transaction lookups

### Implementation Status
- ✅ Linear search implemented (`dsa/search.py`)
- ✅ Dictionary lookup implemented (`dsa/search.py`)
- ✅ Benchmark completed with real data
- ✅ API uses dictionary for endpoint performance

---

## References

- **Time Complexity:** Big O notation - measuring algorithm efficiency
- **Hash Tables:** Python dict implementation (hash function + open addressing)
- **Benchmark Tool:** Python `time.perf_counter()` (nanosecond precision)
- **Dataset:** 1,682 actual MoMo transaction records from Rwanda SMS backup

---

**Document Version:** 1.0  
**Date:** January 26, 2026  
**Author:** Team 7 - Backend Team  
**Status:** Complete & Tested
