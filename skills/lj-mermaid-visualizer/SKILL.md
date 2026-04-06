---
name: lj-mermaid-visualizer
description: Transform text content into professional Mermaid diagrams for presentations and documentation. Use when users ask to visualize concepts, create flowcharts, or make diagrams from text. Supports process flows, system architectures, comparisons, mindmaps, and more with built-in syntax error prevention.
---

# Mermaid Visualizer

## Overview

Convert text content into clean, professional Mermaid diagrams optimized for presentations and documentation. Automatically handles common syntax pitfalls (list syntax conflicts, subgraph naming, spacing issues) to ensure diagrams render correctly in Obsidian, GitHub, and other Mermaid-compatible platforms.

## Quick Start

When creating a Mermaid diagram:

1. **Analyze the content** - Identify key concepts, relationships, and flow
2. **Choose diagram type** - Select the most appropriate visualization (see Diagram Types below)
3. **Select configuration** - Determine layout, detail level, and styling
4. **Choose output format** - Code (default), SVG, or both
5. **Generate diagram** - Create syntactically correct Mermaid code
6. **Output** - Wrap in markdown code fence and/or generate SVG file

**Default assumptions:**
- Vertical layout (TB) unless horizontal requested
- Medium detail level (balanced between simplicity and information)
- Professional color scheme with semantic colors
- Obsidian/GitHub compatible syntax
- **Output: Mermaid code only** (unless SVG explicitly requested)

## Diagram Types

### 1. Process Flow (graph TB/LR)
**Best for:** Workflows, decision trees, sequential processes, AI agent architectures

**Use when:** Content describes steps, stages, or a sequence of actions

**Key features:**
- Swimlanes via subgraph for grouping related steps
- Arrow labels for transitions
- Feedback loops and branches
- Color-coded stages

**Configuration options:**
- `layout`: "vertical" (TB), "horizontal" (LR)
- `detail`: "simple" (core steps only), "standard" (with descriptions), "detailed" (with annotations)
- `style`: "minimal", "professional", "colorful"

### 2. Circular Flow (graph TD with circular layout)
**Best for:** Cyclic processes, continuous improvement loops, agent feedback systems

**Use when:** Content emphasizes iteration, feedback, or circular relationships

**Key features:**
- Central hub with radiating elements
- Curved feedback arrows
- Clear cycle indicators

### 3. Comparison Diagram (graph TB with parallel paths)
**Best for:** Before/after comparisons, A vs B analysis, traditional vs modern systems

**Use when:** Content contrasts two or more approaches or systems

**Key features:**
- Side-by-side layout
- Central comparison node
- Clear differentiation via color/style

### 4. Mindmap
**Best for:** Hierarchical concepts, knowledge organization, topic breakdowns

**Use when:** Content is hierarchical with clear parent-child relationships

**Key features:**
- Radial tree structure
- Multiple levels of nesting
- Clean visual hierarchy

### 5. Sequence Diagram
**Best for:** Interactions between components, API calls, message flows

**Use when:** Content involves communication between actors/systems over time

**Key features:**
- Timeline-based layout
- Clear actor separation
- Activation boxes for processes

### 6. State Diagram
**Best for:** System states, status transitions, lifecycle stages

**Use when:** Content describes states and transitions between them

**Key features:**
- Clear state nodes
- Labeled transitions
- Start and end states

## Critical Syntax Rules

**Always follow these rules to prevent parsing errors:**

### Rule 1: Avoid List Syntax Conflicts
```
❌ WRONG: [1. Perception]       → Triggers "Unsupported markdown: list"
✅ RIGHT: [1.Perception]         → Remove space after period
✅ RIGHT: [① Perception]         → Use circled numbers (①②③④⑤⑥⑦⑧⑨⑩)
✅ RIGHT: [(1) Perception]       → Use parentheses
✅ RIGHT: [Step 1: Perception]   → Use "Step" prefix
```

### Rule 2: Subgraph Naming
```
❌ WRONG: subgraph AI Agent Core  → Space in name without quotes
✅ RIGHT: subgraph agent["AI Agent Core"]  → Use ID with display name
✅ RIGHT: subgraph agent          → Use simple ID only
```

### Rule 3: Node References
```
❌ WRONG: Title --> AI Agent Core  → Reference display name directly
✅ RIGHT: Title --> agent          → Reference subgraph ID
```

### Rule 4: Special Characters in Node Text
```
✅ Use quotes for text with spaces: ["Text with spaces"]
✅ Escape or avoid: quotation marks → use 『』instead
✅ Escape or avoid: parentheses → use 「」instead
✅ Line breaks in circle nodes only: ((Text<br/>Break))
```

### Rule 5: Arrow Types
- `-->` solid arrow
- `-.->` dashed arrow (for supporting systems, optional paths)
- `==>` thick arrow (for emphasis)
- `~~~` invisible link (for layout only)

For complete syntax reference and edge cases, see [references/syntax-rules.md](references/syntax-rules.md)

## Configuration Options

All diagrams accept these parameters:

**Layout:**
- `direction`: "vertical" (TB), "horizontal" (LR), "right-to-left" (RL), "bottom-to-top" (BT)
- `aspect`: "portrait" (default), "landscape" (wide), "square"

**Detail Level:**
- `simple`: Core elements only, minimal labels
- `standard`: Balanced detail with key descriptions (default)
- `detailed`: Full annotations, explanations, and metadata
- `presentation`: Optimized for slides (larger text, fewer details)

**Style:**
- `minimal`: Monochrome, clean lines
- `professional`: Semantic colors, clear hierarchy (default)
- `colorful`: Vibrant colors, high contrast
- `academic`: Formal styling for papers/documentation

**Additional Options:**
- `show_legend`: true/false - Include color/symbol legend
- `numbered`: true/false - Add sequence numbers to steps
- `title`: string - Add diagram title

**Output Format:**
- `format`: "code" (default), "svg", "both"
- `filename`: string - Output filename for SVG (without extension)
- `filepath`: string - Full output path for SVG (optional, defaults to current directory)

## Output Format Handling

**Default behavior (code):**
```mermaid
graph TD
    A[Start] --> B[End]
```
Outputs Mermaid code in markdown code fence - compatible with Obsidian, GitHub, etc.

**SVG format:**
When user explicitly requests SVG ("save as SVG", "export as SVG file", "create SVG"):
1. Save Mermaid code to temporary .mmd file
2. Use `mmdc` (mermaid-cli) to convert to SVG
3. Provide file path and preview option

**Both formats:**
When user requests both ("give me code and SVG", "save SVG and show code"):
1. Output Mermaid code in markdown
2. Generate SVG file
3. Provide both outputs

**Detecting user intent:**
- "as SVG", "save as SVG", "export SVG", "SVG file" → `format: "svg"`
- "both", "code and SVG", "save and show" → `format: "both"`
- No format mentioned → `format: "code"` (default)

**SVG Generation:**
```bash
# Check if mmdc is available
mmdc --version

# Generate SVG
mmdc -i input.mmd -o output.svg
```

If mmdc is not installed, offer to install it:
```bash
npm install -g @mermaid-js/mermaid-cli
# Or use domestic mirror for faster installation
npm install -g @mermaid-js/mermaid-cli --registry=https://registry.npmmirror.com
```

**Fallback when mmdc unavailable:**
- Generate HTML file with embedded Mermaid renderer
- User can open in browser and manually export SVG
- Provide instructions for manual export

**Edge cases to handle:**
1. **No filename specified**: Auto-generate based on diagram type (e.g., "flowchart_20250403.svg")
2. **File already exists**: Ask user before overwriting, or add timestamp suffix
3. **mmdc installation fails**: Suggest alternative methods (Puppeteer, online converters)
4. **Complex diagrams**: May need to adjust SVG size or scale
5. **Ambiguous requests**: Default to "code" format when unclear

## Example Usage Patterns

**Pattern 1: Basic request**
```
User: "Visualize the software development lifecycle"
Response: [Analyze → Choose graph TB → Generate with standard detail]
```

**Pattern 2: With configuration**
```
User: "Create a horizontal flowchart of our sales process with lots of detail"
Response: [Analyze → Choose graph LR → Generate with detailed level]
```

**Pattern 3: Comparison**
```
User: "Compare traditional AI vs AI agents"
Response: [Analyze → Choose comparison layout → Generate with contrasting styles]
```

## Workflow

1. **Understand the content**
   - Identify main concepts, entities, and relationships
   - Determine hierarchy or sequence
   - Note any comparisons or contrasts

2. **Select diagram type**
   - Match content structure to diagram type
   - Consider user's presentation context
   - Default to process flow if ambiguous

3. **Choose configuration**
   - Apply user-specified options
   - Use sensible defaults for unspecified options
   - Optimize for readability

4. **Determine output format**
   - Check user request for format keywords (SVG, file, save, export)
   - Default to "code" if no format specified
   - Set format parameter: "code", "svg", or "both"

5. **Generate Mermaid code**
   - Follow all syntax rules strictly
   - Use semantic naming (descriptive IDs)
   - Apply consistent styling
   - Test for common errors:
     * No "number. space" patterns in node text
     * All subgraphs use ID["display name"] format
     * All node references use IDs not display names

6. **Output based on format**
   - **code**: Wrap in ```mermaid code fence, add explanation
   - **svg**: Save .mmd file, run mmdc, provide SVG path
   - **both**: Provide code in markdown AND generate SVG file

7. **Follow-up**
   - Mention rendering compatibility (Obsidian, GitHub, etc.)
   - Offer to adjust or create variations
   - For SVG: offer to open in browser or default viewer

## Color Scheme Defaults

Standard professional palette:
- Green (#d3f9d8/#2f9e44): Input, perception, start states
- Red (#ffe3e3/#c92a2a): Planning, decision points
- Purple (#e5dbff/#5f3dc4): Processing, reasoning
- Orange (#ffe8cc/#d9480f): Actions, tool usage
- Cyan (#c5f6fa/#0c8599): Output, execution, results
- Yellow (#fff4e6/#e67700): Storage, memory, data
- Pink (#f3d9fa/#862e9c): Learning, optimization
- Blue (#e7f5ff/#1971c2): Metadata, definitions, titles
- Gray (#f8f9fa/#868e96): Neutral elements, traditional systems

## Common Patterns

### Swimlane Pattern (Grouping)
```mermaid
graph TB
    subgraph core["Core Process"]
        A --> B --> C
    end
    subgraph support["Supporting Systems"]
        D
        E
    end
    core -.-> support
```

### Feedback Loop Pattern
```mermaid
graph TB
    A[Start] --> B[Process]
    B --> C[End]
    C -.->|Feedback| A
```

### Hub and Spoke Pattern
```mermaid
graph TB
    Central[Hub]
    A[Spoke 1] --> Central
    B[Spoke 2] --> Central
    C[Spoke 3] --> Central
```

## Quality Checklist

Before outputting, verify:
- [ ] No "number. space" patterns in any node text
- [ ] All subgraphs use proper ID syntax
- [ ] All arrows use correct syntax (-->, -.->)
- [ ] Colors applied consistently
- [ ] Layout direction specified
- [ ] Style declarations present
- [ ] No ambiguous node references
- [ ] Compatible with Obsidian/GitHub renderers
- [ ] Output format matches user request (code/SVG/both)
- [ ] SVG file path provided when format is "svg" or "both"

## Common Mistakes

### Mermaid Syntax
- **List syntax conflict**: Using "1. Step" instead of "1.Step" or "① Step"
- **Subgraph naming**: Forgetting quotes on display names
- **Node references**: Referencing display names instead of IDs

### Output Format
- **Assuming SVG when user wants code**: Check request carefully
- **Generating SVG unnecessarily**: If user just wants code, skip mmdc
- **Missing mmdc check**: Always verify tool availability before using
- **Overwriting existing files**: Check if file exists before saving

### SVG Generation
- **Not checking mmdc availability**: Leads to confusing errors
- **Wrong file paths**: Always use absolute paths or verify current directory
- **Not opening/showing result**: User can't find the generated file

## Output Format Examples

**User: "Create a flowchart"**
→ Output: Mermaid code in markdown (format: code)

**User: "Draw a sequence diagram as SVG"**
→ Output: Generate SVG file using mmdc (format: svg)

**User: "Show me the code and save as SVG"**
→ Output: Mermaid code + SVG file (format: both)

**User: "Just the code, no files"**
→ Output: Mermaid code only, skip SVG (format: code)

## References

For detailed syntax rules and troubleshooting, see:
- [references/syntax-rules.md](references/syntax-rules.md) - Complete syntax reference and error prevention
