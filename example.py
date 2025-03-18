# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#!/usr/bin/env python3
"""Example usage of the Chronicle Security Operations MCP server.

This example demonstrates how to use the secops-mcp server to perform
security operations tasks using Chronicle.
"""

import asyncio
import os
from datetime import datetime, timedelta, timezone
import json

# Example configuration - defaults to environment variables if available
PROJECT_ID = os.environ.get("CHRONICLE_PROJECT_ID", "your-google-cloud-project-id")
CUSTOMER_ID = os.environ.get("CHRONICLE_CUSTOMER_ID", "your-chronicle-customer-id")
REGION = os.environ.get("CHRONICLE_REGION", "us")

# Chronicle security examples
async def security_examples():
    """Run examples of Chronicle security API calls."""
    print("\n=== Chronicle Security API Examples ===\n")
    
    # Example 1: Search for network connection events using defaults
    print("Example 1: Search for network connection events (using environment defaults)")
    events_result = await search_security_events(
        query='metadata.event_type = "NETWORK_CONNECTION"',
        hours_back=24,
        max_events=5
    )
    
    # Handling the JSON response
    total_events = events_result.get('total_events', 0)
    event_list = events_result.get('events', [])
    
    print(f"Found {total_events} events, showing details for {len(event_list)} events:")
    
    # Process the events
    for i, event_wrapper in enumerate(event_list, 1):
        # Extract the actual event data from the wrapper
        event = event_wrapper.get('event', {})
        
        # Extract metadata
        metadata = event.get('metadata', {})
        event_time = metadata.get('eventTimestamp', 'Unknown')
        event_type = metadata.get('eventType', 'Unknown')
        
        print(f"\nEvent {i}:")
        print(f"  Time: {event_time}")
        print(f"  Type: {event_type}")
        
        # Extract principal data (source)
        principal = event.get('principal', {})
        if 'ip' in principal:
            print(f"  Source IP: {', '.join(principal.get('ip', ['Unknown']))}")
        if 'port' in principal:
            print(f"  Source Port: {principal.get('port', 'Unknown')}")
        
        # Extract target data (destination)
        target = event.get('target', {})
        if 'ip' in target:
            print(f"  Target IP: {', '.join(target.get('ip', ['Unknown']))}")
        if 'port' in target:
            print(f"  Target Port: {target.get('port', 'Unknown')}")
        
        # Extract network info
        network = event.get('network', {})
        if 'ipProtocol' in network:
            print(f"  Protocol: {network.get('ipProtocol', 'Unknown')}")
        if 'application_protocol' in network:
            print(f"  Application: {network.get('application_protocol', 'Unknown')}")
    
    # Example 2: Get security alerts with explicit parameters
    print("\nExample 2: Get security alerts (with explicit parameters)")
    alerts = await get_security_alerts(
        project_id=PROJECT_ID,
        customer_id=CUSTOMER_ID,
        region=REGION,
        hours_back=24,
        max_alerts=5
    )
    print(alerts)
    
    # Example 3: Look up an entity (example IP address)
    print("\nExample 3: Look up an entity (using environment defaults)")
    entity_info = await lookup_entity(
        entity_value="8.8.8.8"  # Example IP address (Google DNS)
    )
    print(entity_info)
    
    # Example 4: List security rules
    print("\nExample 4: List security rules (using environment defaults)")
    rules = await list_security_rules()
    print(rules)
    
    # Example 5: Get IoC matches
    print("\nExample 5: Get IoC matches (using environment defaults)")
    iocs = await get_ioc_matches(
        hours_back=24,
        max_matches=5
    )
    print(iocs)

async def main():
    """Run security examples."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Security Operations MCP examples')
    parser.add_argument('--verbose', action='store_true', help='Show more detailed output')
    args = parser.parse_args()
    
    await security_examples()

# Import the functions after defining the example functions to avoid circular imports
from secops_mcp import (
    search_security_events,
    get_security_alerts,
    lookup_entity,
    list_security_rules,
    get_ioc_matches
)

if __name__ == "__main__":
    asyncio.run(main()) 