"""One fixture vocabulary module shadowing the named Research Evidence owner.

Candidate-only snapshot. Production must resolve these enum values from the
versioned canonical method / Execution Contracts, never establish a second owner.
"""
SOURCE_OUTCOMES = frozenset({
    "OK", "NO_RESULTS", "PARTIAL", "RATE_LIMITED", "AUTH_FAILED",
    "PAYMENT_REQUIRED", "UNREACHABLE", "TIMEOUT", "SCHEMA_DRIFT",
    "SKIPPED_UNCONFIGURED", "ERROR",
})
RESEARCH_STATUSES = frozenset({"COMPLETE", "PARTIAL", "INSUFFICIENT_EVIDENCE", "BLOCKED"})
DATE_CONFIDENCE = frozenset({"HIGH", "MED", "LOW", "UNKNOWN"})
RELEVANCE = frozenset({"DIRECT", "SUPPORTING", "CONTEXTUAL", "TANGENTIAL"})
EVIDENCE_STRENGTH = frozenset({"STRONG", "MODERATE", "WEAK", "INDETERMINATE"})
GEO_MEANINGS = frozenset({
    "AD_DELIVERY_GEO", "CREATOR_REGISTERED_GEO", "AUDIENCE_GEO",
    "SEARCH_RESULT_LOCALE", "SELLER_GEO", "SHIPPING_DESTINATION",
})
TIME_MEANINGS = frozenset({
    "PUBLISHED_DURING_WINDOW", "ACTIVE_DURING_WINDOW",
    "ENGAGEMENT_GAINED_DURING_WINDOW", "OBSERVED_AS_OF",
})
RESEARCH_REQUIRED = frozenset({
    "research_execution_id", "research_intent", "primary_entity",
    "market", "language", "range_from", "range_to", "generated_at",
    "query_plan", "source_outcomes", "coverage", "evidence_clusters",
    "counterevidence", "freshness_verdicts", "status", "unknowns", "reuse_notes",
})
