from collections import deque

# This function partitions the graph based on a zone connection (zoneA-zoneB)
def reachable_without_edge(zoneA, zoneB, adj):
    # Performs BFS from "start" zone
    seen = {zoneA}
    q = deque([zoneA])
    while q:
        u = q.popleft()
        for v in adj[u]:
            # Partitions along the zoneA-zoneB connection
            if (u == zoneA and v == zoneB) or (u == zoneB and v == zoneA):
                continue
            if v not in seen:
                seen.add(v)
                q.append(v)
    return seen