---
user-invocable: false
description: Review comment templates for different contributor types and actions
---

# Message Templates

Select template based on contributor type (from Step 1).

**Bot templates**: Professional/technical tone, no emojis

## Template Matrix

| Action | External | Internal | Bot |
|--------|----------|----------|-----|
| **Approve** | "Thank you! [≤1 sentence praise if warranted]. Welcome! 🎉" | "LGTM! [feedback/suggestions]" | **Dependabot**: "Security patch approved [testing notes]" (security), "High-risk update reviewed. Checklist: [items]" (high), "Update reviewed for quarterly batch" (med/low)<br>**Other**: "Automated changes approved." |
| **Approve and merge** | "Thank you! [≤1 sentence praise]. Auto-merge enabled. 🎉" | "LGTM! Auto-merge enabled." | **Dependabot**: "Security patch approved. Auto-merge enabled." (security), "High-risk update tested. Auto-merge enabled." (high), "Update approved. Auto-merge enabled." (med/low)<br>**Other**: "Automated changes approved. Auto-merge enabled." |
| **Make changes and approve** | "Applied minor style/formatting fixes. Thank you! 🙏" | "Applied style/formatting fixes. LGTM!" | N/A (excluded for bots) |
| **Request changes** | Opening: "Thank you!"<br>Acknowledge positives (≤1 sentence)<br>Issues with line numbers<br>Suggestion blocks<br>Close: "Mention @claude if you need help" | Professional opening<br>Issues with line numbers<br>Suggestion blocks<br>Clear action items | Technical issue description<br>Line numbers<br>What needs changing<br>No suggestion blocks<br>Close: "This automated PR may need closing and regeneration after fixing source configuration." |
| **Close PR** | "Thank you for contributing!"<br>Clear, kind closing reason<br>Acknowledge valuable aspects<br>Suggest alternatives<br>"We appreciate your interest in Pulumi!" | Clear closing reason | **Dependabot quarterly**: "Closing to batch with other low/medium-risk updates in quarterly review. See [Dependency Management](https://github.com/pulumi/docs/blob/master/BUILD-AND-DEPLOY.md#dependency-management)."<br>**Dependabot other**: "Closing this update. [Technical reason: conflicts, superseded, etc.]"<br>**Other bots**: "Closing. [Technical reason]" |

## Tone Guidelines

### External Contributors

- Warm and welcoming tone
- Express gratitude explicitly
- Use emojis appropriately (🎉, 🙏, etc.)
- Acknowledge learning curve and effort
- Offer continued support
- Build community connection

**Example (Approve)**:
```
Thank you for your first contribution to Pulumi! This documentation improvement is excellent. Welcome! 🎉
```

### Internal Contributors

- Professional and efficient tone
- Brief acknowledgments
- Focus on technical feedback
- "LGTM" acceptable shorthand
- No excessive praise
- Direct and clear

**Example (Approve)**:
```
LGTM! Nice improvements to the error handling section. Consider adding a link to the troubleshooting guide in line 42.
```

### Bot PRs (All Types)

- Technical and factual tone
- No emojis
- State what was checked/tested
- Mention risk level for Dependabot
- Note any special handling required
- Reference documentation for context

**Example (Dependabot HIGH)**:
```
High-risk update reviewed. Testing checklist completed:
- ✅ make serve-all passed
- ✅ Search functionality verified
- ✅ No console errors
- ✅ PR deployment loads correctly
- ✅ Lambda@Edge functions operating normally
```

## Dependabot Variations

### Security Patches (HIGH Priority)

**Approve**:
```
Security patch approved. Testing completed:
- ✅ make serve-all passed
- ✅ PR deployment verified
- ✅ No Lambda@Edge errors

Critical security update merged despite high-risk classification.
```

**Approve and merge**:
```
Security patch approved. Auto-merge enabled. Testing completed:
- ✅ make serve-all passed
- ✅ PR deployment verified
```

### High Risk (Non-Security)

**Approve**:
```
High-risk update reviewed. Testing checklist completed:
- ✅ make serve-all passed
- ✅ Search functionality verified
- ✅ No console errors
- ✅ PR deployment loads correctly

Safe to merge after additional checks pass.
```

**Approve and merge**:
```
High-risk update tested. Auto-merge enabled. Checklist:
- ✅ make serve-all passed
- ✅ PR deployment verified
- ✅ Lambda@Edge functions operating normally
```

### Medium/Low Risk

**Approve**:
```
Update reviewed for quarterly batch. Basic checks passed:
- ✅ make lint passed
```

**Approve and merge**:
```
Update approved. Auto-merge enabled. Lint checks passed.
```

### Quarterly Review

**Close with quarterly note**:
```
Closing to batch with other low/medium-risk updates in quarterly review. We'll merge accumulated quarterly updates together after comprehensive testing. This reduces testing overhead while keeping dependencies current.

See [Dependency Management](https://github.com/pulumi/docs/blob/master/BUILD-AND-DEPLOY.md#dependency-management) for details.
```

## Implementation Notes

- Always use confirmed/edited content from preview step
- Base template selection on contributor type detected in Step 1
- For Dependabot: Check risk tier and labels to select appropriate variation
- Include specific testing results when approving HIGH risk updates
- Keep bot messages factual and concise
- Adjust tone but maintain professionalism across all contributor types
