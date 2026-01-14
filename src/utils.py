"""
Utility functions for the AI Actions Demos project.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional


def format_timestamp(timestamp: str) -> str:
    """
    Format an ISO timestamp to a human-readable format.
    
    Args:
        timestamp: ISO format timestamp string
    
    Returns:
        Formatted date string (YYYY-MM-DD)
    """
    dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
    return dt.strftime('%Y-%m-%d')


def parse_issue_json(json_str: str) -> List[Dict]:
    """
    Parse JSON string containing GitHub issues.
    
    Args:
        json_str: JSON string with issue data
    
    Returns:
        List of issue dictionaries
    """
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return []


def filter_by_label(issues: List[Dict], label: str) -> List[Dict]:
    """
    Filter issues by a specific label.
    
    Args:
        issues: List of issue dictionaries
        label: Label name to filter by
    
    Returns:
        Filtered list of issues containing the label
    """
    return [
        issue for issue in issues
        if any(lbl['name'] == label for lbl in issue.get('labels', []))
    ]


def calculate_staleness(updated_at: str, threshold_days: int = 30) -> bool:
    """
    Determine if an issue is stale based on last update time.
    
    Args:
        updated_at: ISO timestamp of last update
        threshold_days: Number of days to consider stale (default: 30)
    
    Returns:
        True if issue is stale, False otherwise
    """
    last_update = datetime.fromisoformat(updated_at.replace('Z', '+00:00'))
    days_old = (datetime.now(last_update.tzinfo) - last_update).days
    return days_old > threshold_days


class IssueAnalyzer:
    """Analyze GitHub issues for insights."""
    
    def __init__(self, issues: List[Dict]):
        """
        Initialize with a list of issues.
        
        Args:
            issues: List of issue dictionaries from GitHub API
        """
        self.issues = issues
    
    def count_by_label(self) -> Dict[str, int]:
        """
        Count issues grouped by label.
        
        Returns:
            Dictionary mapping label names to counts
        """
        label_counts = {}
        for issue in self.issues:
            for label in issue.get('labels', []):
                label_name = label['name']
                label_counts[label_name] = label_counts.get(label_name, 0) + 1
        return label_counts
    
    def get_stale_issues(self, threshold_days: int = 30) -> List[Dict]:
        """
        Get list of stale issues.
        
        Args:
            threshold_days: Days since update to consider stale
        
        Returns:
            List of stale issue dictionaries
        """
        return [
            issue for issue in self.issues
            if calculate_staleness(issue['updatedAt'], threshold_days)
        ]
    
    def get_summary(self) -> Dict:
        """
        Generate summary statistics about issues.
        
        Returns:
            Dictionary with summary statistics
        """
        return {
            'total_issues': len(self.issues),
            'stale_count': len(self.get_stale_issues()),
            'label_distribution': self.count_by_label(),
            'average_comments': sum(i.get('comments', 0) for i in self.issues) / len(self.issues) if self.issues else 0
        }
