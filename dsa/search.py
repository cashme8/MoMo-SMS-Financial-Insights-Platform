"""
DSA Integration: Linear Search vs Dictionary Lookup Performance Comparison

This module compares two approaches to finding transactions by ID:
1. Linear Search - O(n) time complexity, iterate through list
2. Dictionary Lookup - O(1) time complexity, hash table access
"""

import json
import time
import os


def load_transactions(json_file):
    """Load transactions from JSON file"""
    try:
        with open(json_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"✗ File not found: {json_file}")
        return []
    except json.JSONDecodeError:
        print(f"✗ Invalid JSON: {json_file}")
        return []


def linear_search(transactions, target_id):
    """
    Linear Search - O(n) complexity
    Iterate through list sequentially until target is found
    """
    for tx in transactions:
        if tx['id'] == target_id:
            return tx
    return None


def dictionary_lookup(transactions_dict, target_id):
    """
    Dictionary Lookup - O(1) complexity
    Direct hash table access using transaction ID as key
    """
    return transactions_dict.get(target_id)


def create_transaction_dict(transactions):
    """Convert list to dictionary for O(1) lookup"""
    return {tx['id']: tx for tx in transactions}


def benchmark_search(transactions, test_ids, num_iterations=100):
    """
    Benchmark both search methods
    """
    print("\n" + "="*80)
    print("DSA INTEGRATION: SEARCH ALGORITHM COMPARISON")
    print("="*80)
    
    # Create dictionary for O(1) lookup
    tx_dict = create_transaction_dict(transactions)
    
    print(f"\n📊 Test Setup:")
    print(f"   Total Transactions: {len(transactions)}")
    print(f"   Test IDs: {test_ids}")
    print(f"   Iterations per ID: {num_iterations}")
    print(f"   Total Searches: {len(test_ids) * num_iterations}")
    
    # ========== LINEAR SEARCH BENCHMARK ==========
    print(f"\n{'─'*80}")
    print("🔍 METHOD 1: LINEAR SEARCH (O(n) - Sequential Scan)")
    print(f"{'─'*80}")
    
    linear_results = {}
    linear_total_time = 0
    
    for target_id in test_ids:
        start_time = time.perf_counter()
        
        for _ in range(num_iterations):
            result = linear_search(transactions, target_id)
        
        elapsed = time.perf_counter() - start_time
        linear_total_time += elapsed
        linear_results[target_id] = elapsed
        
        status = "✓ FOUND" if result else "✗ NOT FOUND"
        print(f"   ID {target_id}: {elapsed*1000000:.2f}µs ({status})")
    
    avg_linear = linear_total_time / len(test_ids)
    print(f"\n   Average: {avg_linear*1000000:.2f}µs per search")
    print(f"   Total:   {linear_total_time*1000000:.2f}µs")
    
    # ========== DICTIONARY LOOKUP BENCHMARK ==========
    print(f"\n{'─'*80}")
    print("⚡ METHOD 2: DICTIONARY LOOKUP (O(1) - Hash Table Access)")
    print(f"{'─'*80}")
    
    dict_results = {}
    dict_total_time = 0
    
    for target_id in test_ids:
        start_time = time.perf_counter()
        
        for _ in range(num_iterations):
            result = dictionary_lookup(tx_dict, target_id)
        
        elapsed = time.perf_counter() - start_time
        dict_total_time += elapsed
        dict_results[target_id] = elapsed
        
        status = "✓ FOUND" if result else "✗ NOT FOUND"
        print(f"   ID {target_id}: {elapsed*1000000:.2f}µs ({status})")
    
    avg_dict = dict_total_time / len(test_ids)
    print(f"\n   Average: {avg_dict*1000000:.2f}µs per search")
    print(f"   Total:   {dict_total_time*1000000:.2f}µs")
    
    # ========== COMPARISON & ANALYSIS ==========
    print(f"\n{'─'*80}")
    print("📈 PERFORMANCE COMPARISON")
    print(f"{'─'*80}")
    
    speedup = linear_total_time / dict_total_time if dict_total_time > 0 else 0
    improvement = ((linear_total_time - dict_total_time) / linear_total_time) * 100
    
    print(f"\n   Linear Search Total:   {linear_total_time*1000000:.2f}µs")
    print(f"   Dictionary Lookup Total: {dict_total_time*1000000:.2f}µs")
    print(f"\n   Speedup Factor: {speedup:.2f}x faster")
    print(f"   Improvement:   {improvement:.1f}%")
    
    # ========== COMPLEXITY ANALYSIS ==========
    print(f"\n{'─'*80}")
    print("🔬 COMPLEXITY ANALYSIS")
    print(f"{'─'*80}")
    
    print(f"\n   Linear Search:")
    print(f"      Time Complexity:  O(n) - proportional to list size")
    print(f"      Space Complexity: O(1) - no extra space")
    print(f"      Approach: Sequential iteration until match found")
    
    print(f"\n   Dictionary Lookup:")
    print(f"      Time Complexity:  O(1) - constant time (average case)")
    print(f"      Space Complexity: O(n) - stores hash table")
    print(f"      Approach: Direct hash table access using key")
    
    # ========== PRACTICAL ANALYSIS ==========
    print(f"\n{'─'*80}")
    print("💡 PRACTICAL ANALYSIS")
    print(f"{'─'*80}")
    
    print(f"\n   When to use Linear Search:")
    print(f"      • Small datasets (< 100 items)")
    print(f"      • Memory is critical")
    print(f"      • Single lookup required")
    print(f"      • Unsorted data that won't be reused")
    
    print(f"\n   When to use Dictionary Lookup:")
    print(f"      • Large datasets (> 100 items)")
    print(f"      • Performance critical")
    print(f"      • Multiple lookups on same data")
    print(f"      • Need consistent O(1) performance")
    
    print(f"\n   Recommendation for {len(transactions)} Transactions:")
    if len(transactions) > 100:
        print(f"      ✓ USE DICTIONARY LOOKUP")
        print(f"        {speedup:.1f}x faster, acceptable memory trade-off")
    else:
        print(f"      ✓ EITHER METHOD")
        print(f"        Small dataset, both perform similarly")
    
    # ========== SUMMARY TABLE ==========
    print(f"\n{'─'*80}")
    print("📋 SUMMARY TABLE")
    print(f"{'─'*80}\n")
    
    print(f"{'ID':<8} | {'Linear (µs)':<15} | {'Dict (µs)':<15} | {'Speedup':<10}")
    print(f"{'-'*60}")
    
    for target_id in test_ids:
        lin_time = linear_results[target_id] * 1000000
        dict_time = dict_results[target_id] * 1000000
        speedup_val = lin_time / dict_time if dict_time > 0 else 0
        print(f"{target_id:<8} | {lin_time:<15.2f} | {dict_time:<15.2f} | {speedup_val:<10.2f}x")
    
    print(f"\n{'='*80}\n")
    
    return {
        'linear_total': linear_total_time,
        'dict_total': dict_total_time,
        'speedup': speedup,
        'improvement': improvement,
        'linear_results': linear_results,
        'dict_results': dict_results
    }


if __name__ == '__main__':
    # Determine file path relative to script location
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_file = os.path.join(script_dir, 'data', 'transactions.json')
    
    # Load transactions
    print("\n📂 Loading transactions...")
    transactions = load_transactions(json_file)
    
    if not transactions:
        print("✗ No transactions loaded. Exiting.")
        exit(1)
    
    print(f"✓ Loaded {len(transactions)} transactions")
    
    # Select test IDs (first 20 transactions or less if fewer available)
    num_test_ids = min(20, len(transactions))
    test_ids = [transactions[i]['id'] for i in range(num_test_ids)]
    
    # Run benchmark
    results = benchmark_search(transactions, test_ids, num_iterations=100)
    
    print("\n✓ Benchmark complete!")
