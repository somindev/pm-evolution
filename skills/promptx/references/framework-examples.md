# Framework Examples and Interactions

## Overview

This document provides detailed examples of how PromptX responds to various user queries. These examples demonstrate the scoring algorithm in action and show the appropriate response templates for different scenarios.

## Example 1: Clear Single Match

### User Query
"Help me create a prompt for analyzing customer feedback"

### Analysis
- **Domains detected:** business, technical
- **Task types:** prompt_engineering, analysis
- **Keywords:** create, prompt, analyze, customer, feedback
- **Complexity:** medium

### Scoring
Top 5 frameworks:

| Framework | Domain | Task | Keyword | Complexity | Examples | Total |
|-----------|--------|------|---------|------------|----------|-------|
| CIDI | 100 | 100 | 40 | 100 | 10 | 75.0 |
| PEE | 33 | 50 | 20 | 50 | 10 | 35.0 |
| GRADE | 33 | 100 | 40 | 100 | 10 | 60.0 |
| TRACE | 33 | 100 | 20 | 100 | 10 | 54.0 |
| TQA | 33 | 100 | 40 | 50 | 10 | 49.0 |

**Winner:** CIDI (75.0) - Clear winner with > 80 threshold not met, but top score significantly higher than runners-up

### Response
```markdown
## Recommended Framework: CIDI Framework

**Match Score:** 75/100

**Why this framework:** The CIDI Framework (Context, Issue, Decision, Insights) is specifically designed for analytical tasks and technical/business domains. It provides excellent structure for analyzing customer feedback by establishing context, identifying issues, making decisions, and extracting insights.

**Quick Overview:** A comprehensive framework for structured analysis and decision-making in technical and business contexts.

**Framework Components:**
1. **Context**: Establish the background and parameters for the analysis
2. **Issue**: Clearly define the problem or question to be addressed
3. **Decision**: Make informed choices based on the analysis
4. **Insights**: Extract actionable learnings and recommendations

**Best For:**
- Analytical tasks requiring structure
- Business and technical decisions
- Extracting insights from data

**Strengths:**
✅ Comprehensive analytical structure
✅ Excellent for business contexts
✅ Guides from problem to insight

**Considerations:**
⚠️ Requires more setup than simpler frameworks

**Example Application:**

For customer feedback analysis:
- **Context**: "Analyzing Q4 2025 customer feedback from 450 users across web and mobile platforms"
- **Issue**: "Identify top 3 pain points affecting user retention"
- **Decision**: "Prioritize fixes based on impact and feasibility"
- **Insights**: "Users report 40% faster workflow with new interface, but 60% find export functionality confusing"

Would you like me to help you apply this framework to your specific customer feedback analysis?
```

## Example 2: Multiple Good Matches

### User Query
"I need to make a decision about which features to build next"

### Analysis
- **Domains detected:** business, decision
- **Task types:** decision_making
- **Keywords:** decision, features, build, next
- **Complexity:** medium

### Scoring
Top 5 frameworks:

| Framework | Domain | Task | Keyword | Complexity | Examples | Total |
|-----------|--------|------|---------|------------|----------|-------|
| RICE | 100 | 50 | 20 | 100 | 10 | 66.5 |
| Six Thinking Hats | 50 | 50 | 0 | 100 | 10 | 52.5 |
| Pros and Cons | 50 | 50 | 0 | 50 | 10 | 40.0 |

**All scores 60-80:** Present top 3 with comparison

### Response
```markdown
## Top 3 Framework Recommendations

I found multiple frameworks that could work well for your feature prioritization decision.

### 1. RICE Framework - Score: 67/100

**Best for:** Prioritizing features based on quantitative scoring
**Why it fits:** Specifically designed for product decisions, RICE provides a numerical approach to compare features objectively
**Complexity:** Medium
**Components:** Reach, Impact, Confidence, Effort

### 2. Six Thinking Hats - Score: 53/100

**Best for:** Comprehensive decision exploration from multiple perspectives
**Why it fits:** Ensures you consider emotional, creative, and critical aspects of the decision
**Complexity:** Medium
**Components:** Six distinct thinking perspectives (facts, feelings, caution, benefits, creativity, process)

### 3. Pros and Cons Analysis - Score: 40/100

**Best for:** Evaluating multiple options systematically
**Why it fits:** Classic decision-making approach that's versatile and easy to apply
**Complexity:** Simple
**Components:** Listing advantages and disadvantages for each option

## Quick Comparison

| Aspect | RICE | Six Thinking Hats | Pros and Cons |
|--------|------|-------------------|---------------|
| Complexity | Medium | Medium | Simple |
| Flexibility | Medium | High | High |
| Examples | 1 | 1 | 1 |
| Best Domain | Business | Decision | Decision |
| Quantitative | Yes | No | No |

**My Recommendation:** Start with **RICE Framework** because it's specifically designed for feature prioritization and provides quantitative scores that make comparison objective and defensible.

Which framework would you like to explore further?
```

## Example 3: Ambiguous Input

### User Query
"I need a framework"

### Analysis
- **Domains detected:** None
- **Task types:** None
- **Keywords:** framework (too generic)
- **Complexity:** unknown

### Scoring
Top score: 45/100 (no clear match)

**All scores < 60:** Trigger clarification questions

### Response
```markdown
I'd love to help you find the right framework! To recommend the best fit, I need to understand your situation better.

**Quick Questions:**

1. **What are you trying to accomplish?**
   - Create effective AI prompts?
   - Make a business decision?
   - Solve a complex problem?
   - Generate content?
   - Analyze information?

2. **What domain are you working in?**
   - Business/Marketing
   - Education/Learning
   - Creative/Design
   - Technical/Engineering
   - Personal/General

3. **How complex is your task?**
   - Simple (straightforward, single step)
   - Medium (multiple factors to consider)
   - Complex (many variables, deep analysis needed)

Once I know more, I can match you with the perfect framework from our collection of 57 options!
```

## Example 4: Educational Use Case

### User Query
"Create a lesson plan for teaching algebra with increasing complexity"

### Analysis
- **Domains detected:** education
- **Task types:** content_creation, curriculum_design
- **Keywords:** lesson, plan, teaching, algebra, complexity
- **Complexity:** medium

### Scoring
Top 3 frameworks:

| Framework | Domain | Task | Keyword | Complexity | Examples | Total |
|-----------|--------|------|---------|------------|----------|-------|
| Bloom's Taxonomy | 100 | 50 | 20 | 100 | 10 | 67.0 |
| GRADE | 100 | 50 | 20 | 100 | 10 | 67.0 |
| ERA | 100 | 50 | 0 | 100 | 10 | 57.0 |

**Tie:** Bloom's and GRADE both score 67. Use tie-breaking:
- Both have 1 example (tie)
- Both have high flexibility (tie)
- Bloom's has 6 components, GRADE has 5 (fewer wins)
- Wait, fewer components wins → GRADE wins

**Actually:** Let me check the frameworks. Bloom's is better for "increasing complexity" as it explicitly structures cognitive levels.

**Adjustment:** In practice, Bloom's Taxonomy is the perfect match for this query because:
- Explicitly designed for increasing cognitive complexity
- Structures learning objectives progressively
- Perfect for lesson planning

This shows the algorithm needs refinement for domain-specific terms like "increasing complexity" which should map to Bloom's.

### Response
```markdown
## Recommended Framework: Bloom's Taxonomy Prompts

**Match Score:** 67/100

**Why this framework:** Bloom's Taxonomy is perfect for your request because it explicitly structures learning objectives by increasing cognitive complexity - exactly what you need for an algebra lesson plan. It progresses from basic Remember/Understand through higher-order thinking like Analyze, Evaluate, and Create.

**Quick Overview:** A structured approach to fostering higher-order thinking and deep understanding across learning domains.

**Framework Components:**
1. **Remember**: Create prompts that ask for recall of factual information
2. **Understand**: Design questions that probe comprehension of meanings and concepts
3. **Apply**: Formulate tasks that require using information in new situations
4. **Analyze**: Develop prompts that dissect information to understand structure
5. **Evaluate**: Craft questions that demand judgment based on criteria
6. **Create**: Encourage generation of new ideas, products, or perspectives

**Best For:**
- Educational settings and curriculum development
- Progressive learning objectives
- Assessment design

**Strengths:**
✅ Explicitly structures increasing cognitive complexity
✅ Versatile across disciplines and levels
✅ Promotes critical thinking and problem-solving

**Considerations:**
⚠️ May require familiarization with taxonomy levels

**Example Application:**

For an algebra lesson on equations:
- **Remember**: "List the steps to solve a linear equation"
- **Understand**: "Explain why we perform the same operation on both sides"
- **Apply**: "Solve these 5 equations using the balance method"
- **Analyze**: "Compare these two solution methods - when would you use each?"
- **Evaluate**: "Which solution strategy is most efficient for this equation and why?"
- **Create**: "Design your own word problem that requires solving a system of equations"

Would you like me to help you create a complete algebra lesson plan using Bloom's Taxonomy?
```

## Example 5: Creative Brainstorming

### User Query
"Help me brainstorm innovative features for our mobile app"

### Analysis
- **Domains detected:** business, creative
- **Task types:** brainstorming, content_creation
- **Keywords:** brainstorm, innovative, features, mobile, app
- **Complexity:** medium

### Scoring
Top 3 frameworks:

| Framework | Domain | Task | Keyword | Complexity | Examples | Total |
|-----------|--------|------|---------|------------|----------|-------|
| SCAMPER | 75 | 50 | 20 | 100 | 10 | 60.5 |
| How Might We | 50 | 50 | 40 | 50 | 10 | 50.0 |
| Imagine | 50 | 50 | 40 | 50 | 10 | 50.0 |

**SCAMPER wins** with 60.5

### Response
```markdown
## Recommended Framework: SCAMPER Framework

**Match Score:** 61/100

**Why this framework:** SCAMPER is ideal for brainstorming innovative features because it provides a structured approach to creative thinking. Each letter represents a different technique for generating ideas: Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse. This ensures you explore multiple angles for innovation.

**Quick Overview:** A systematic technique for creative thinking and idea generation through seven distinct approaches.

**Framework Components:**
1. **Substitute**: What can be replaced or changed?
2. **Combine**: What can be merged or combined?
3. **Adapt**: What can be adjusted or modified from other contexts?
4. **Modify/Magnify**: What can be altered, enlarged, or enhanced?
5. **Put to other use**: How can it be used differently?
6. **Eliminate**: What can be removed or simplified?
7. **Reverse/Rearrange**: What can be reorganized or flipped?

**Best For:**
- Creative brainstorming and innovation
- Feature ideation and product development
- Problem-solving through creative approaches

**Strengths:**
✅ Systematic approach to creativity
✅ Ensures comprehensive exploration
✅ Easy to apply and understand

**Considerations:**
⚠️ Requires time to explore all seven techniques

**Example Application:**

For mobile app feature brainstorming:
- **Substitute**: "Replace text input with voice commands for hands-free use"
- **Combine**: "Merge social sharing with task management for collaborative productivity"
- **Adapt**: "Adapt gamification from fitness apps to make habit tracking engaging"
- **Modify**: "Enhance notifications with AI-powered personalization"
- **Put to other use**: "Use the app's core algorithm for team scheduling instead of individual tasks"
- **Eliminate**: "Remove onboarding screens - use progressive disclosure instead"
- **Reverse**: "Flip the model - instead of user tracking app, make it a data visualization tool"

Would you like me to help you apply SCAMPER to generate more feature ideas for your app?
```

## Example 6: Complex Technical Analysis

### User Query
"Perform a comprehensive analysis of our system architecture and provide detailed recommendations for scaling to 1M users"

### Analysis
- **Domains detected:** technical
- **Task types:** analysis
- **Keywords:** analysis, system, architecture, scaling, recommendations, comprehensive
- **Complexity:** complex

### Scoring
Top 3 frameworks:

| Framework | Domain | Task | Keyword | Complexity | Examples | Total |
|-----------|--------|------|---------|------------|----------|-------|
| Chain of Thought | 100 | 50 | 20 | 50 | 10 | 52.5 |
| Tree of Thought | 100 | 50 | 0 | 100 | 10 | 55.0 |
| CIDI | 100 | 100 | 40 | 50 | 10 | 75.0 |

**CIDI wins** with 75

### Response
```markdown
## Recommended Framework: CIDI Framework

**Match Score:** 75/100

**Why this framework:** The CIDI Framework excels for complex technical analysis like system architecture reviews. It provides systematic structure for establishing the context (current architecture), identifying issues (scaling bottlenecks), making decisions (prioritizing improvements), and extracting insights (recommendations). Perfect for the comprehensive analysis you need.

**Quick Overview:** A comprehensive framework for structured analysis and decision-making in technical contexts.

**Framework Components:**
1. **Context**: Document current architecture, constraints, and scaling goals
2. **Issue**: Identify bottlenecks, single points of failure, and limitations
3. **Decision**: Prioritize architectural changes and scaling strategies
4. **Insights**: Extract actionable recommendations with implementation guidance

**Best For:**
- Comprehensive technical analysis
- System architecture reviews
- Strategic technical decisions

**Strengths:**
✅ Handles complex, multi-dimensional analysis
✅ Excellent for technical/business contexts
✅ Provides clear path from analysis to action

**Considerations:**
⚠️ Requires thorough information gathering for Context phase

**Example Application:**

For scaling to 1M users:
- **Context**: "Current monolithic architecture on 2 servers, 100K daily users, 95% uptime requirement, PostgreSQL database, Redis cache"
- **Issue**: "Database connection pooling maxed out, no horizontal scaling, caching layer insufficient for read-heavy workload"
- **Decision**: "Prioritize: (1) Database sharding, (2) Microservices migration, (3) CDN implementation, (4) Load balancer upgrade"
- **Insights**: "Implement database read replicas first (quick win), then migrate user service to microservices (3-month project), add CDN for static assets (1-week sprint)"

Would you like me to help you perform a detailed CIDI analysis of your architecture?
```

## Example 7: Content Creation

### User Query
"Write a compelling blog post about the benefits of remote work"

### Analysis
- **Domains detected:** business, creative
- **Task types:** content_creation
- **Keywords:** write, blog, post, benefits, remote, work
- **Complexity:** medium

### Scoring
Top 3 frameworks:

| Framework | Domain | Task | Keyword | Complexity | Examples | Total |
|-----------|--------|------|---------|------------|----------|-------|
| BLOG | 75 | 50 | 40 | 100 | 10 | 68.5 |
| BAB | 50 | 50 | 20 | 100 | 10 | 50.0 |
| RELIC | 50 | 50 | 0 | 100 | 10 | 45.0 |

**BLOG Framework wins** with 68.5

### Response
```markdown
## Recommended Framework: BLOG Framework

**Match Score:** 69/100

**Why this framework:** The BLOG Framework is specifically designed for blog post creation and provides excellent structure for compelling content. It helps organize your thoughts into Background, Lead_out, Options, What's_next, and Goal sections - perfect for writing about remote work benefits.

**Quick Overview:** A structured approach to creating engaging, well-organized blog posts.

**Framework Components:**
1. **Background**: Set the context and hook the reader
2. **Lead_out**: Develop the main narrative and key points
3. **Options**: Present different perspectives or approaches
4. **What's_next**: Provide actionable takeaways
5. **Goal**: Reinforce the main message and call-to-action

**Best For:**
- Blog post and article creation
- Structured storytelling
- Engaging content marketing

**Strengths:**
✅ Designed specifically for blog writing
✅ Ensures compelling narrative flow
✅ Built-in call-to-action structure

**Considerations:**
⚠️ More structured than freeform writing

**Example Application:**

For remote work benefits post:
- **Background**: "In 2024, 40% of employees prefer remote work, but many companies still hesitate. Let's explore why remote work benefits both employees and employers."
- **Lead_out**: "Remote work increases productivity by 13%, reduces overhead costs by $11K per employee, and expands talent pools globally. Companies like GitLab and Zapata have been fully remote for years."
- **Options**: "Different approaches exist: fully remote, hybrid models, remote-first with occasional hubs. Each has unique advantages depending on company culture and industry."
- **What's_next**: "Consider starting with a hybrid pilot program, investing in collaboration tools, and establishing clear remote work policies."
- **Goal**: "Ready to embrace remote work? Start by auditing your current processes and identifying roles that can transition effectively."

Would you like me to help you write the complete blog post using the BLOG Framework?
```

## Edge Cases

### Edge Case 1: User Names Specific Framework

**User Query:** "Tell me about the CRISPE framework"

**Response Strategy:**
- Present CRISPE directly (bypass scoring)
- Still show 2-3 similar alternatives
- Focus on that framework's details

### Edge Case 2: Extremely Long Query

**User Query:** [500+ words describing complex scenario]

**Response Strategy:**
- Extract key themes and keywords
- Focus on main domain and task type
- Score based on extracted essentials
- May ask clarification if themes conflict

### Edge Case 3: Multiple Languages

**User Query:** "Ayúdame a crear un prompt para analizar comentarios"

**Response Strategy:**
- Detect language (Spanish)
- Translate keywords for classification
- Present frameworks in English (available content)
- Offer to assist in user's language if possible

### Edge Case 4: Contradictory Signals

**User Query:** "Simple comprehensive analysis"

**Response Strategy:**
- Detect contradiction (simple vs comprehensive)
- Ask clarification about complexity
- Don't guess - clarify to ensure good match

## Response Time Optimization

### Target: < 3 seconds

**Breakdown:**
- Load index.json: ~0.5s
- Score 57 frameworks: ~0.1s
- Load top 3 framework files: ~1.5s
- Generate response: ~0.5s
- **Total:** ~2.6s

**Optimization Techniques:**
1. Cache index.json in memory
2. Parallel load framework files
3. Pre-compute framework statistics
4. Use efficient data structures (sets for lookups)

## User Feedback Integration

### Collect Feedback
- "Was this recommendation helpful?" (Yes/No)
- "Which framework did you choose?" (Track selection)
- "How would you rate this match?" (1-5 scale)

### Use Feedback to Improve
1. Adjust scoring weights if users consistently skip top recommendations
2. Add new keywords based on successful matches
3. Refine domain/task mappings
4. Identify gaps in framework collection

### A/B Testing
- Test different weight combinations
- Compare response templates
- Measure user satisfaction rates
- Optimize for framework selection accuracy
