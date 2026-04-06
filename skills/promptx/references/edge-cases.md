# Edge Cases, Red Flags & Troubleshooting

## Red Flags

These thoughts mean STOP — you're rationalizing:

| Thought | Reality |
|---------|---------|
| "This is just a simple prompt question" | Users asking about prompts likely need framework guidance. Check PromptX. |
| "I can recommend a framework quickly" | Framework selection requires systematic analysis. Use the scoring algorithm. |
| "Any framework will work" | Poor framework matches reduce effectiveness. Score properly. |
| "User didn't explicitly ask for a framework" | Implicit need for structure is common. Analyze the task type. |
| "I'll just give them a popular one" | Popularity ≠ relevance. Match to their specific use case. |
| "The query is too short to score" | Short queries still have domains and keywords. Score what you have. |
| "They need examples, not frameworks" | Examples are part of frameworks. Present both together. |

## Quality Checklist

Before presenting a framework recommendation:

- [ ] Extracted user's domain, task type, complexity, and keywords
- [ ] Scored all 57 frameworks using the algorithm
- [ ] Verified top score makes sense for the query
- [ ] Checked for ties and applied tie-breaking rules
- [ ] Loaded framework details from data/index.json
- [ ] Read actual framework file for examples if score > 60
- [ ] Prepared response matching the appropriate template
- [ ] Included rationale for the recommendation
- [ ] Offered to help apply the framework

## Troubleshooting

| Problem | Solution |
|---------|----------|
| All frameworks score < 60 | Ask clarification questions to gather more context |
| Multiple frameworks tie at top score | Apply tie-breaking rules (examples > flexibility > simplicity > ID) |
| User asks for specific framework by name | Present that framework directly, but also show similar alternatives |
| Query is too long/complex | Focus on key themes, extract main domain/task, score accordingly |

## Critical Success Factors

1. **Accurate Domain Classification**: Correctly identifying the user's domain is crucial (30% of score)
2. **Task Type Matching**: Understanding what the user wants to accomplish (25% of score)
3. **Keyword Relevance**: Extracting meaningful keywords from the query (20% of score)
4. **Appropriate Complexity**: Matching framework complexity to task complexity (15% of score)
5. **Practical Examples**: Frameworks with examples get higher scores (10% bonus)
