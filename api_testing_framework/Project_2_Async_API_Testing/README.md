# Project 2: Async API Testing with httpx

## Overview

Welcome to **Project 2: Async API Testing with httpx**! This project teaches you how to write high-performance asynchronous API tests using httpx's AsyncClient and pytest-asyncio. By the end, you'll be able to run tests in parallel, achieving 10-50x faster execution!

---

## What You'll Build

A high-performance async API test suite that:
- ✅ Uses httpx.AsyncClient for parallel execution
- ✅ Runs multiple tests concurrently
- ✅ Integrates pytest-asyncio seamlessly
- ✅ Achieves 10-50x speed improvements
- ✅ Handles async errors gracefully
- ✅ Mixes sync and async tests when needed
- ✅ Follows async best practices

---

## Prerequisites

Before starting Project 2, you should have completed:
- ✅ **Project 1**: REST API Testing Foundations
- ✅ Understanding of sync httpx
- ✅ Basic pytest knowledge
- ✅ HTTP methods and status codes

**New to async Python?** No worries! We'll teach you everything you need.

---

## Tools & Technologies

- **Python 3.10+**: With native async/await support
- **pytest >=8.0**: Testing framework
- **pytest-asyncio >=0.21**: Async test support for pytest
- **httpx[http2] >=0.27**: AsyncClient for parallel requests
- **asyncio**: Python's built-in async library

---

## Project Structure

```
Project_2_Async_API_Testing/
├── README.md                                    # This file
├── 2.1_Introduction_to_Async_Testing.md
├── 2.2_Sync_vs_Async_Explained.md
├── 2.3_When_to_Use_Async_Tests.md
├── 2.4_Installing_pytest_asyncio.md
├── 2.5_Your_First_Async_Test.md
├── 2.6_httpx_AsyncClient_Basics.md
├── 2.7_Async_Context_Managers.md
├── 2.8_Async_Fixtures_in_pytest.md
├── 2.9_Testing_Multiple_Endpoints_Concurrently.md
├── 2.10_Gathering_Async_Results.md
├── 2.11_Error_Handling_in_Async_Tests.md
├── 2.12_Async_Timeouts_and_Retries.md
├── 2.13_Connection_Pooling_with_httpx.md
├── 2.14_HTTP2_Support_in_httpx.md
├── 2.15_Performance_Benefits_of_Async.md
├── 2.16_Mixing_Sync_and_Async_Tests.md
└── 2.17_Best_Practices_for_Async_Testing.md
```

---

## Learning Path

### Phase 1: Async Fundamentals (Lessons 2.1-2.5)
Learn what async is, why it matters, and write your first async test.

### Phase 2: AsyncClient Mastery (Lessons 2.6-2.9)
Master httpx.AsyncClient, context managers, fixtures, and concurrent testing.

### Phase 3: Advanced Patterns (Lessons 2.10-2.14)
Gathering results, error handling, timeouts, connection pooling, and HTTP/2.

### Phase 4: Production Ready (Lessons 2.15-2.17)
Performance optimization, mixing sync/async, and best practices.

---

## Key Concepts You'll Master

✅ **async/await syntax**: Modern Python async patterns  
✅ **AsyncClient**: httpx async client for parallel requests  
✅ **pytest-asyncio**: Async test support in pytest  
✅ **asyncio.gather()**: Run multiple coroutines concurrently  
✅ **Async fixtures**: Shared async setup/teardown  
✅ **Context managers**: Proper async resource management  
✅ **Error handling**: Try/except in async code  
✅ **Performance**: Measure and optimize speed  
✅ **HTTP/2**: Leverage modern protocol features  
✅ **Best practices**: Production-ready async testing  

---

## Performance Comparison

### Sync Testing (Project 1)
```python
# Test 50 endpoints synchronously
# Each takes ~1 second
# Total time: ~50 seconds
```

### Async Testing (Project 2)
```python
# Test 50 endpoints concurrently
# All run in parallel
# Total time: ~2-5 seconds (10-25x faster!)
```

**When you'll see the biggest gains**:
- Testing multiple independent endpoints
- Large test suites (100+ tests)
- APIs with network latency
- Smoke tests across services

---

## What Makes This Different

### From Project 1:
- **Parallel execution**: Multiple requests at once
- **AsyncClient**: New async-aware client
- **async/await**: Modern async syntax
- **pytest-asyncio**: Async test support
- **10-50x faster**: Dramatic speed improvements

### Why Async?
- Tests run concurrently, not sequentially
- Better resource utilization
- Faster CI/CD pipelines
- More tests in less time
- Production-grade performance

---

## Real-World Use Cases

**Perfect for**:
- Smoke tests across multiple services
- Testing many similar endpoints (GET /users/1-100)
- Load testing with concurrent requests
- Integration tests with multiple API calls
- Performance testing

**Not ideal for**:
- Sequential operations (create → read → update → delete)
- Tests with dependencies
- Simple, single-endpoint tests
- When order matters

---

## Installation

Before starting, install the required packages:

```bash
# Activate your virtual environment
source venv/bin/activate

# Install async dependencies
pip install pytest-asyncio httpx[http2]
```

**requirements.txt**:
```
pytest>=8.0.0
pytest-asyncio>=0.21.0
httpx[http2]>=0.27.0
```

---

## Quick Start

After completing lessons, you'll write tests like this:

```python
import pytest
import httpx

@pytest.mark.asyncio
async def test_multiple_users_async():
    """Test fetching multiple users concurrently."""
    async with httpx.AsyncClient() as client:
        # Fetch 10 users in parallel!
        tasks = [
            client.get(f"https://api.example.com/users/{i}")
            for i in range(1, 11)
        ]
        responses = await asyncio.gather(*tasks)
        
        # All responses in ~1 second instead of ~10!
        assert all(r.status_code == 200 for r in responses)
```

---

## Success Criteria

You'll know you've mastered Project 2 when you can:

1. Explain the difference between sync and async
2. Write async tests with pytest-asyncio
3. Use httpx.AsyncClient effectively
4. Run multiple requests concurrently
5. Handle async errors properly
6. Create async fixtures
7. Mix sync and async tests appropriately
8. Measure and optimize async performance
9. Apply async best practices

---

## Estimated Time

- **Per Lesson**: 30-60 minutes
- **Total Project**: 1-2 weeks
- **Prerequisites**: Project 1 completed

---

## Tips for Success

💡 **Start simple**: Master basic async before complex patterns  
💡 **Run examples**: Execute every code sample yourself  
💡 **Measure performance**: Time sync vs async to see gains  
💡 **Debug carefully**: Async errors can be tricky at first  
💡 **Practice concurrency**: Write tests that run in parallel  
💡 **Use type hints**: Helps catch async/sync mismatches  

---

## Getting Started

Start with **Lesson 2.1: Introduction to Async Testing**

Ready to make your tests blazing fast? Let's go! 🚀

---

## Need Help?

Each lesson includes:
- Clear concept explanations
- Complete code examples
- Common mistakes and solutions
- Performance comparisons
- Best practices

If you get stuck, review the "Common Stumbling Blocks" section in each lesson!

---

**Let's build high-performance async tests together!** ⚡
