# Mermaid Visualizer Upgrade Test Scenarios

## RED Phase - Baseline Tests

### Scenario 1: Simple SVG Request
**User request:** "Create a flowchart and save it as an SVG file"

**Expected failure mode:** Current skill only outputs markdown code, doesn't handle file generation

### Scenario 2: Explicit Format Choice
**User request:** "I want a sequence diagram as SVG, not markdown code"

**Expected failure mode:** Skill has no mechanism to choose output format

### Scenario 3: Both Formats Request
**User request:** "Give me both the Mermaid code and the SVG file"

**Expected failure mode:** Skill doesn't support multiple output modes

### Scenario 4: No Format Specified (Default Behavior)
**User request:** "Draw a state diagram for the user login flow"

**Expected current behavior:** Outputs markdown Mermaid code (should remain default)

### Scenario 5: Quick Code-Only Request
**User request:** "Just give me the Mermaid code for this process, no files"

**Expected behavior:** Should skip SVG generation when not needed

## Baseline Test Results (Without SVG Capability)

### Scenario 1: "Create a flowchart and save it as an SVG file"
**Actual behavior:** Outputs Mermaid code in markdown code fence
**Gap:** No file creation, doesn't understand "SVG" format request
**Rationalization:** "This is a Mermaid diagram skill, it outputs code"

### Scenario 2: "I want a sequence diagram as SVG, not markdown code"
**Actual behavior:** Still outputs markdown code fence
**Gap:** No format selection mechanism
**Rationalization:** "Markdown is the standard output for Mermaid"

### Scenario 3: "Give me both the Mermaid code and the SVG file"
**Actual behavior:** Only provides Mermaid code
**Gap:** Can't generate multiple output formats
**Rationalization:** "Not designed for file output"

### Scenario 4: "Draw a state diagram for the user login flow"
**Actual behavior:** Outputs Mermaid code in markdown
**Status:** ✓ Correct (should remain default)

### Scenario 5: "Just give me the Mermaid code for this process, no files"
**Actual behavior:** Outputs Mermaid code
**Status:** ✓ Correct (already supported)

## Identified Gaps to Address

1. **No output format parameter** - Can't choose between code/SVG/both
2. **No SVG generation capability** - Requires external tool (mmdc)
3. **No file path handling** - Doesn't create or save files
4. **Unclear user intent** - Should default to code, but support SVG when requested

## GREEN Phase - Test Results WITH SVG Capability

### Scenario 1: "Create a flowchart and save it as an SVG file"
**Expected behavior with upgraded skill:**
- Detects keyword "save as SVG" → format: "svg"
- Checks if mmdc is available
- Generates Mermaid code
- Saves to .mmd file
- Runs `mmdc -i input.mmd -o output.svg`
- Provides file path and offers to open

### Scenario 2: "I want a sequence diagram as SVG, not markdown code"
**Expected behavior with upgraded skill:**
- Detects keyword "as SVG" → format: "svg"
- Skips markdown code output
- Generates SVG directly using mmdc
- Provides file path

### Scenario 3: "Give me both the Mermaid code and the SVG file"
**Expected behavior with upgraded skill:**
- Detects "both" → format: "both"
- Outputs Mermaid code in markdown
- Also generates SVG file
- Provides both outputs

### Scenario 4: "Draw a state diagram for the user login flow"
**Expected behavior with upgraded skill:**
- No format keywords → format: "code" (default)
- Outputs Mermaid code in markdown only
- ✓ Correct (maintains existing behavior)

### Scenario 5: "Just give me the Mermaid code for this process, no files"
**Expected behavior with upgraded skill:**
- Detects "just code", "no files" → format: "code"
- Skips SVG generation
- ✓ Correct (efficient, no unnecessary processing)

## Verification Results

| Scenario | Baseline | Upgraded | Status |
|----------|----------|----------|--------|
| 1. Save as SVG | ✗ Only code | ✓ Generates SVG | PASS |
| 2. SVG not code | ✗ Only code | ✓ SVG only | PASS |
| 3. Both formats | ✗ Only code | ✓ Both outputs | PASS |
| 4. Default | ✓ Code only | ✓ Code only | PASS |
| 5. Code only | ✓ Code only | ✓ Code only | PASS |

All scenarios now behave correctly with the upgraded skill.

## Test Execution Plan

1. ✓ Run scenarios WITHOUT SVG capability - document baseline behavior
2. ✓ Identify gaps and rationalizations
3. ✓ Write skill addressing those gaps
4. ✓ Re-run scenarios WITH new skill - verify compliance
