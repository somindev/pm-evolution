# Domain and Task Type Mappings

## Overview

This document defines the keyword mappings used for classifying user queries into domains and task types. These mappings power the PromptX scoring algorithm's domain and task detection.

## Domain Mappings

### Education

**Keywords:**
- education, learning, teaching, teach, learn, educate
- curriculum, lesson, course, class, classroom, academic
- assessment, test, quiz, exam, evaluate, grade
- student, learner, pupil, instructor, teacher, professor
- cognitive, knowledge, understanding, comprehension
- objective, goal, outcome, achievement
- training, tutorial, workshop, seminar

**Indicators:**
- "teach me"
- "create a lesson"
- "assess understanding"
- "learning objectives"
- "educational content"

**Frameworks in this domain:**
- Bloom's Taxonomy (01)
- 3Cs Model (03)
- 4S Method (04)
- ERA Framework (18)
- ELI5 Framework (19)
- GRADE Framework (25)
- Help me Understand (27)

### Business

**Keywords:**
- business, company, enterprise, organization, corporate
- marketing, sales, selling, promotion, advertising
- strategy, strategic, plan, planning, roadmap
- management, manager, lead, leadership, executive
- professional, career, industry, market, competitor
- stakeholder, customer, client, prospect
- revenue, profit, growth, scale, expand
- negotiation, contract, agreement, deal

**Indicators:**
- "business decision"
- "marketing strategy"
- "sales pitch"
- "competitive analysis"
- "business plan"

**Frameworks in this domain:**
- Pros and Cons Analysis (02)
- APE Framework (05)
- BAB Framework (07)
- COAST Framework (15)
- GOPA Framework (24)
- RICE Framework (38)
- Six Thinking Hats (45)

### Creative

**Keywords:**
- creative, creativity, innovate, innovation, innovative
- brainstorm, ideate, ideation, idea, ideas
- design, artistic, art, visual, graphics
- storytelling, story, narrative, plot
- imagination, imagine, envision
- content, writing, write, author, compose
- blog, article, post, copy

**Indicators:**
- "brainstorm ideas"
- "creative thinking"
- "design concept"
- "tell a story"
- "innovative solution"

**Frameworks in this domain:**
- BLOG Framework (08)
- Imagine Framework (29)
- How Might We (HMW) (28)
- SCAMPER (44)
- What If Framework (56)
- RELIC Framework (36)

### Technical

**Keywords:**
- technical, technology, tech
- engineering, engineer, develop, development
- code, coding, program, programming, software
- ai, artificial intelligence, machine learning, ml
- data, database, analytics, analysis
- system, architecture, infrastructure
- algorithm, logic, computational
- debug, troubleshoot, fix, error
- api, integration, deployment

**Indicators:**
- "write code"
- "technical analysis"
- "debug this"
- "system design"
- "data analysis"

**Frameworks in this domain:**
- Chain of Thought (12)
- Tree of Thought (55)
- CIDI Framework (14)
- CRISPE Framework (16)
- RASCEF Framework (35)
- Most prompt engineering frameworks (03-06, 10-11, 15-17, 20, 22, 25, 32-37, 39-43, 47, 49-54)

### Decision

**Keywords:**
- decision, decide, deciding, choice, choose, selecting
- evaluate, evaluation, assess, assessment, judgment
- criteria, weigh, weighing, compare, comparing
- pros and cons, advantage, disadvantage
- rank, ranking, prioritize, priority
- recommend, recommendation, suggest

**Indicators:**
- "make a decision"
- "choose between"
- "evaluate options"
- "rank these"
- "prioritize features"

**Frameworks in this domain:**
- Pros and Cons Analysis (02)
- RICE Framework (38)
- Six Thinking Hats (45)
- Socratic Method (47)

### Problem

**Keywords:**
- problem, solution, solve, solving, resolved
- challenge, obstacle, barrier, issue, difficulty
- troubleshoot, troubleshooting, diagnostic, fix
- address, tackle, overcome, resolve
- answer, solution, workaround

**Indicators:**
- "solve this problem"
- "address the challenge"
- "overcome obstacles"
- "fix the issue"
- "troubleshoot"

**Frameworks in this domain:**
- Chain of Thought (12)
- Tree of Thought (55)
- Challenge-Solution-Benefit (13)
- SCAMPER (44)
- Socratic Method (47)

## Task Type Mappings

### Prompt Engineering

**Keywords:**
- prompt, prompting, prompt engineering
- ai interaction, ai query, ai request
- llm, language model, chatgpt, claude
- ask, query, request, command
- optimize prompt, improve prompt, better prompt
- frame, framework, structure

**Indicators:**
- "optimize my prompt"
- "improve this prompt"
- "structure a prompt for"
- "better way to ask"
- "prompt framework"

**Frameworks:**
- 3Cs Model (03)
- 4S Method (04)
- APE Framework (05)
- Atomic Prompting (06)
- BAB Framework (07)
- CARE Framework (10)
- Chain of Destiny (11)
- Chain of Thought (12)
- CIDI Framework (14)
- COAST Framework (15)
- CRISPE Framework (16)
- Elicitation Framework (17)
- ERA Framework (18)
- Few-shot Prompt (20)
- FOCUS Framework (22)
- Focused Conversation ORID (23)
- GOPA Framework (24)
- GRADE Framework (25)
- Hamburger Model (26)
- Help me Understand (27)
- PAUSE Framework (30)
- PEE Framework (31)
- PROMPT Framework (32)
- RACE Framework (33)
- RAFEC Framework (34)
- RASCEF Framework (35)
- RHODES Framework (37)
- RISE Framework (39)
- RISEN Framework (40)
- RODES Framework (41)
- ROSES Framework (42)
- RTF Framework (43)
- SMART Framework (46)
- SPAR Framework (48)
- SPARK Framework (49)
- SPEAR Framework (50)
- TAG Framework (51)
- TQA Approach (52)
- TRACE Framework (53)
- TRACI Framework (54)
- Zero-shot Prompting (57)

### Decision Making

**Keywords:**
- decision, decide, choice, choose, select
- evaluate, evaluation, assess, assessment
- criteria, weigh, compare, rank
- prioritize, priority, ranking
- recommend, recommend, suggest

**Indicators:**
- "make a decision"
- "choose the best"
- "evaluate and select"
- "prioritize these"
- "rank options"

**Frameworks:**
- Pros and Cons Analysis (02)
- RICE Framework (38)
- Six Thinking Hats (45)
- Socratic Method (47)

### Problem Solving

**Keywords:**
- problem, solution, solve, resolve
- challenge, obstacle, difficulty
- troubleshoot, diagnostic, fix
- address, tackle, overcome
- answer, fix, repair

**Indicators:**
- "solve this problem"
- "find a solution"
- "address the challenge"
- "overcome obstacles"
- "troubleshoot"

**Frameworks:**
- Chain of Thought (12)
- Tree of Thought (55)
- Challenge-Solution-Benefit (13)
- SCAMPER (44)
- Socratic Method (47)

### Content Creation

**Keywords:**
- content, create, generate, write
- article, blog, post, copy
- story, narrative, tale
- compose, author, draft
- produce, output

**Indicators:**
- "write an article"
- "create content"
- "generate a story"
- "compose a post"
- "draft content"

**Frameworks:**
- BLOG Framework (08)
- RELIC Framework (36)
- Hamburger Model (26)
- BAB Framework (07)

### Analysis

**Keywords:**
- analyze, analysis, analytic
- examine, inspect, investigate
- evaluate, assessment, assess
- study, research, explore
- review, audit, check

**Indicators:**
- "analyze this"
- "examine the data"
- "evaluate the options"
- "investigate"
- "review and assess"

**Frameworks:**
- PEE Framework (31)
- CIDI Framework (14)
- GRADE Framework (25)
- TQA Approach (52)
- TRACE Framework (53)

### Brainstorming

**Keywords:**
- brainstorm, ideate, ideation
- idea, ideas, concept, concepts
- innovate, innovation, innovative
- creative, creativity, imagine
- think, thinking, thought
- generate, produce, come up with

**Indicators:**
- "brainstorm ideas"
- "generate concepts"
- "innovative thinking"
- "creative solutions"
- "think outside the box"

**Frameworks:**
- How Might We (HMW) (28)
- Imagine Framework (29)
- SCAMPER (44)
- Six Thinking Hats (45)
- What If Framework (56)

## Complexity Detection Rules

### Simple Complexity

**Characteristics:**
- Query length < 50 words
- Single request or question
- No conjunctions (and, but, however)
- Direct and straightforward
- Single step or action

**Indicators:**
- "analyze this"
- "choose one"
- "write a post"
- "solve this"
- "evaluate"

**Example Queries:**
- "Analyze this text"
- "Choose the best option"
- "Write a blog post"
- "Solve the problem"

### Medium Complexity

**Characteristics:**
- Query length 50-100 words
- 2-3 steps or components
- Some conjunctions
- Moderate detail
- Multiple factors to consider

**Indicators:**
- "analyze and then..."
- "consider these factors..."
- "taking into account..."
- "evaluate both..."

**Example Queries:**
- "Analyze the customer feedback and suggest improvements for our product"
- "Choose the best feature to build next considering impact and effort"
- "Write a blog post that explains the benefits of our new feature"

### Complex Complexity

**Characteristics:**
- Query length > 100 words
- Multi-step process
- Many variables or factors
- Comprehensive, systematic
- Detailed requirements

**Indicators:**
- "comprehensive analysis"
- "systematic approach"
- "considering multiple factors"
- "detailed evaluation"
- "step-by-step"

**Example Queries:**
- "Perform a comprehensive analysis of our customer feedback from the last quarter, considering different customer segments, product categories, and geographic regions, then provide actionable recommendations for product improvements organized by priority and estimated impact"

## Vocabulary Lists

### Common Words (Filtered Out)

**Articles:** a, an, the
**Conjunctions:** and, but, or, nor, for, so, yet
**Prepositions:** in, on, at, to, for, with, by, from, of
**Pronouns:** I, you, he, she, it, we, they, my, your, his, her, its, our, their
**Auxiliary Verbs:** be, am, is, are, was, were, been, being, have, has, had, do, does, did, will, would, could, should, may, might, must, can
**Common Adverbs:** very, just, also, too, more, most, some, such, only, own, same, so, than, too, very

### Framework-Specific Vocabulary

**Stopwords for Framework Detection:**
- framework, method, approach, strategy, technique, model, process, system, way, use, using, through, help, need, want, like

**Prioritized Terms:**
- Domain-specific terms (business, education, technical)
- Task-specific terms (analyze, decide, create, solve)
- Quality indicators (effective, optimal, best, comprehensive)
- Complexity indicators (simple, complex, detailed, systematic)

## Classification Algorithm

```python
def classify_domains(query_text):
    """Classify query into domains."""
    query_lower = query_text.lower()
    domains = []

    for domain, keywords in DOMAIN_KEYWORDS.items():
        score = sum(1 for keyword in keywords if keyword in query_lower)
        if score >= 2:  # Need at least 2 keyword matches
            domains.append(domain)

    # Default to education if no domains match
    if not domains:
        domains.append('education')

    return domains

def classify_task_types(query_text):
    """Classify query into task types."""
    query_lower = query_text.lower()
    task_types = []

    for task_type, keywords in TASK_TYPE_KEYWORDS.items():
        score = sum(1 for keyword in keywords if keyword in query_lower)
        if score >= 1:  # Need at least 1 keyword match
            task_types.append(task_type)

    # Default to prompt_engineering if no task types match
    if not task_types:
        task_types.append('prompt_engineering')

    return task_types

def determine_complexity(query_text):
    """Determine complexity level."""
    word_count = len(query_text.split())

    # Check for complexity indicators
    complex_indicators = ['comprehensive', 'systematic', 'detailed', 'step-by-step', 'multi-step']
    simple_indicators = ['simple', 'quick', 'straightforward', 'basic']

    query_lower = query_text.lower()
    complex_score = sum(1 for indicator in complex_indicators if indicator in query_lower)
    simple_score = sum(1 for indicator in simple_indicators if indicator in query_lower)

    if word_count < 50:
        return 'simple'
    elif word_count > 100 or complex_score >= 1:
        return 'complex'
    else:
        return 'medium'
```

## Validation and Testing

### Test Cases

**Query 1:** "Help me optimize a prompt for analyzing customer feedback"
- Expected Domains: {business, technical}
- Expected Task Types: {prompt_engineering, analysis}
- Expected Complexity: medium

**Query 2:** "Create a lesson plan for teaching algebra"
- Expected Domains: {education}
- Expected Task Types: {content_creation}
- Expected Complexity: medium

**Query 3:** "I need to decide which feature to build next"
- Expected Domains: {business, decision}
- Expected Task Types: {decision_making}
- Expected Complexity: simple

**Query 4:** "Brainstorm innovative solutions for reducing customer churn"
- Expected Domains: {business, creative}
- Expected Task Types: {brainstorming, problem_solving}
- Expected Complexity: medium

**Query 5:** "Perform comprehensive analysis of our technical architecture and provide detailed recommendations"
- Expected Domains: {technical}
- Expected Task Types: {analysis}
- Expected Complexity: complex

## Maintenance

### Updating Mappings

1. **Add new keywords** when users use different terminology
2. **Refine thresholds** based on classification accuracy
3. **Add new domains** if frameworks cover new areas
4. **Adjust task types** if new framework categories emerge

### Accuracy Monitoring

Track classification accuracy:
- Compare predicted domains/task types with user feedback
- Measure precision and recall for each category
- Update mappings if accuracy < 85%

### Version Control

- Current version: 1.0.0
- Last updated: 2026-01-27
- Maintained in: `/Users/lijun/Coding/skill_cook/frameworks/generate_index.py`
