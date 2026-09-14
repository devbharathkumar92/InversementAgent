"""Authoritative requirement registry.

Each entry maps a numbered SRS requirement identifier (e.g. ``1.3.2``) to
its title. The identifiers and titles below were extracted from the frozen
topic files in ``srs/topics/``. They are change-controlled data: they must
only be modified through the controlled change workflow (Topic 1 / Topic 27).
"""

from __future__ import annotations

from typing import Final

# Authoritative requirement IDs for the implemented SRS topics.
REQ_REGISTRY: Final[dict[str, dict[str, str]]] = {
    "1": {
        "1.0": "Reference and Validation Basis",
        "1.1": "Document Identity",
        "1.2": "Document Metadata",
        "1.3": "Versioning Structure",
        "1.3.1": "Version Numbering Rules",
        "1.3.2": "Version Increment Rules",
        "1.4": "Version Status",
        "1.5": "Change Control",
        "1.5.1": "Change Request",
        "1.5.2": "Change Impact Assessment",
        "1.5.3": "Change Approval",
        "1.6": "Approval and Governance",
        "1.6.1": "Approval Authority",
        "1.6.2": "Approval State",
        "1.7": "Version History",
        "1.8": "Document Integrity",
        "1.9": "Document Storage and Access",
        "1.10": "Document Review Cycle",
        "1.11": "Baseline Locking",
        "1.11.1": "Baseline Creation",
        "1.11.2": "Baseline Lock",
        "1.11.3": "Baseline Modification",
        "1.12": "Auditability",
    },
    "2": {
        "2.1": "Goal Statement",
        "2.2": "Mission Statement",
        "2.3": "Primary Objective",
        "2.3.1": "Primary Objective Definition",
        "2.3.2": "Secondary Objectives",
        "2.4": "Expected System Outcome",
        "2.5": "Goal Scope",
        "2.6": "Goal Constraints",
        "2.7": "Non-Negotiable Goal Conditions",
        "2.7.1": "Mandatory Conditions",
        "2.7.2": "Goal Violation Conditions",
        "2.8": "Goal Immutability",
        "2.8.1": "Immutable Goal Elements",
        "2.8.2": "Controlled Modification Exception",
        "2.9": "Goal Evaluation Criteria",
        "2.10": "Goal Success Metrics",
        "2.10.1": "Quantitative Success Metrics",
        "2.10.2": "Qualitative Success Metrics",
        "2.11": "Goal Alignment",
        "2.12": "Goal Conflict Resolution",
        "2.12.1": "Conflict Detection",
        "2.12.2": "Conflict Resolution Priority",
        "2.13": "Goal Deviation Detection",
        "2.14": "Goal Validation and Review",
        "2.15": "Goal Baseline and Approval",
    },
    "3": {
        "3.1": "Proof of Value Definition",
        "3.2": "PoV Objectives",
        "3.3": "PoV Success Definition",
        "3.3.1": "Functional Success",
        "3.3.2": "Technical Success",
        "3.3.3": "Outcome Success",
        "3.4": "PoV Scope",
        "3.5": "PoV Success Conditions",
        "3.5.1": "Minimum Success Thresholds",
        "3.5.2": "Release Blocking Conditions",
        "3.6": "Evaluation Criteria",
        "3.7": "Performance Metrics",
        "3.7.1": "Performance Metrics Definition",
        "3.7.2": "Performance Metric Thresholds",
        "3.7.3": "Reliability Metrics",
        "3.8": "Functional Validation",
        "3.9": "Technical Validation",
        "3.10": "System Reliability Validation",
        "3.11": "Agent Behaviour Validation",
        "3.12": "Output Quality Validation",
        "3.13": "Risk and Safety Validation",
        "3.14": "Real-World Scenario Validation",
        "3.15": "PoV Test Environment",
        "3.15.1": "Simulation Environment",
        "3.15.2": "Paper-Trading Environment",
        "3.16": "PoV Data",
        "3.17": "Acceptance Criteria",
        "3.17.1": "Functional Acceptance",
        "3.17.2": "Safety Acceptance",
        "3.18": "Failure Criteria",
        "3.18.1": "Critical Failure",
        "3.18.2": "Non-Critical Failure",
        "3.19": "Evidence and Documentation",
        "3.20": "PoV Review and Approval",
        "3.21": "PoV Completion Criteria",
        "3.21.1": "Completion Validation",
        "3.21.2": "Expansion Approval",
        "3.22": "PoV Baseline and Version Control",
        "3.23": "PoV Re-Evaluation Criteria",
        "3.24": "PoV Limitations and Constraints",
    },
    "4": {
        "4.1": "System Scope Definition",
        "4.2": "In-Scope Capabilities",
        "4.2.1": "Included Capabilities",
        "4.2.2": "Capability Limits",
        "4.3": "Out-of-Scope Capabilities",
        "4.3.1": "Explicitly Excluded Functions",
        "4.4": "Functional Boundaries",
        "4.5": "Technical Boundaries",
        "4.6": "Data Boundaries",
        "4.7": "Market and Geographic Boundaries",
        "4.7.1": "Geographic Scope",
        "4.7.2": "Market Scope",
        "4.7.3": "Currency Scope",
        "4.8": "Operational Boundaries",
        "4.9": "User Interaction Boundaries",
        "4.10": "Agent Authority Boundaries",
        "4.10.1": "Allowed Agent Authority",
        "4.10.2": "Prohibited Agent Authority",
        "4.11": "Sub-Agent Scope Boundaries",
        "4.12": "Input Boundaries",
        "4.13": "Output Boundaries",
        "4.14": "Decision-Making Boundaries",
        "4.15": "Execution and Action Boundaries",
        "4.15.1": "Simulation Actions",
        "4.15.2": "Live-Action Restrictions",
        "4.16": "Risk and Safety Boundaries",
        "4.17": "External System and API Boundaries",
        "4.18": "Resource and Infrastructure Boundaries",
        "4.19": "Scope Violation Detection",
        "4.20": "Boundary Enforcement",
        "4.21": "Scope Expansion Restriction",
        "4.21.1": "Expansion Trigger",
        "4.21.2": "Expansion Approval",
        "4.22": "Scope Change Control",
        "4.23": "Scope Validation and Review",
        "4.24": "Scope Freeze and Baseline",
        "4.25": "Scope Exceptions and Escalation",
        "4.25.1": "Exception Detection",
        "4.25.2": "Escalation Rules",
    },
    "5": {
        "5.1": "Core System Principles",
        "5.2": "Non-Negotiable Rules",
        "5.3": "Goal Immutability Principle",
        "5.3.1": "Immutable Goal Elements",
        "5.3.2": "Goal Change Prohibition",
        "5.4": "Specification Completeness Principle",
        "5.5": "Agent Determinism Principle",
        "5.6": "No-Assumption Principle",
        "5.7": "No Unauthorized Change Principle",
        "5.8": "Human Approval",
        "5.8.1": "Approval-Required Actions",
        "5.8.2": "Non-Approval Actions",
        "5.9": "Scope Compliance Principle",
        "5.10": "Safety First Principle",
        "5.11": "Risk Control Principles",
        "5.12": "Data Integrity Principles",
        "5.13": "Decision Integrity Principles",
        "5.14": "Transparency and Explainability Rules",
        "5.15": "Auditability Requirements",
        "5.16": "Traceability Requirements",
        "5.17": "Error Handling Principles",
        "5.18": "Failure and Recovery Rules",
        "5.19": "Blocked-State and Escalation Rules",
        "5.20": "Security and Access Principles",
        "5.21": "Agent-to-Agent Communication Rules",
        "5.22": "Sub-Agent Behaviour Constraints",
        "5.23": "Parallel Execution Rules",
        "5.24": "Conflict Resolution Rules",
        "5.25": "Self-Evaluation Rules",
        "5.26": "Self-Improvement Restrictions",
        "5.26.1": "Allowed Improvements",
        "5.26.2": "Prohibited Self-Modifications",
        "5.27": "Change Proposal and Approval Rules",
        "5.27.1": "Change Proposal",
        "5.27.2": "Impact Assessment",
        "5.27.3": "Approval Gate",
        "5.27.4": "Validation Before Adoption",
        "5.28": "System Consistency Rules",
        "5.29": "Rule Violation Detection",
        "5.30": "Rule Enforcement Mechanism",
        "5.31": "Exception Handling Rules",
        "5.31.1": "Exception Definition",
        "5.31.2": "Exception Handling",
        "5.32": "Principle Validation and Review",
        "5.33": "Baseline Lock and Controlled Modification",
        "5.33.1": "Baseline Creation",
        "5.33.2": "Baseline Protection",
        "5.34": "Governance of Principles",
    },
}

# Authorized lifecycle statuses for controlled documents (Topic 1.4/1.6).
REQ_AUTHORIZED_STATUSES: Final[frozenset[str]] = frozenset(
    {
        "DRAFT",
        "IN_REVIEW",
        "APPROVED",
        "BASELINED",
        "SUPERSEDED",
        "REJECTED",
        "ARCHIVED",
    }
)


def get_requirement_title(topic: str, requirement_id: str) -> str:
    """Return the title for a numbered requirement ID.

    Args:
        topic: Topic number as a string (e.g. ``"1"``).
        requirement_id: Numbered requirement ID (e.g. ``"1.3.2"``).

    Returns:
        The registered title for the requirement.

    Raises:
        KeyError: If the topic or requirement ID is not registered.
    """
    if topic not in REQ_REGISTRY:
        raise KeyError(f"Topic {topic} is not registered in the requirements registry")
    if requirement_id not in REQ_REGISTRY[topic]:
        raise KeyError(f"Requirement {requirement_id} is not registered in topic {topic}")
    return REQ_REGISTRY[topic][requirement_id]
