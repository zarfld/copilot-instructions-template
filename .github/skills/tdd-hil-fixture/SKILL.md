---
name: tdd-hil-fixture
description: >
  Procedural steps for Test-Driven Development using Hardware-in-the-Loop (HIL)
  derived fixtures. Use when implementing features that depend on hardware
  device behavior (MIDI, serial, network protocols, embedded systems).
  Covers: PROBE issue creation, HIL capture, fixture-backed CI test writing,
  and CI hardware exclusion.
triggers:
  - "implement hardware feature"
  - "create PROBE issue"
  - "HIL probe"
  - "hardware fixture"
  - "mock hardware"
  - "capture device response"
  - "write fixture-backed test"
  - "hardware-in-the-loop"
tools: ["read", "search", "edit"]
---

# Skill: TDD with HIL-Derived Fixtures

## Core Rule

> Do not invent mocks from documentation alone. Run a focused HIL probe first, capture the real response, then use that capture as the fixture source for CI tests.

CI must **never** require live hardware, a fixed IP address, a physical device, or physical network state.

## When to use this skill

Use this skill when:
- You need to implement parsing or handling of a hardware device's protocol
- The exact format/values of device responses are unknown or unspecified
- You are about to write a mock but have not verified it against real hardware

## Procedural Steps

### Step 1 — Create issues

1. Confirm a REQ issue exists for the behavior (create `[REQ-F]` if missing).
2. Create a `[PROBE]` issue using `.github/ISSUE_TEMPLATE/13-probe.yml`.
3. Link the PROBE to the REQ: `- Traces to:  #N` in the Traceability section.

### Step 2 — Run the HIL probe

Connect to real hardware. Run the minimal command needed to observe the behavior.

Capture and record in the PROBE issue:
- Device model (exact name + variant)
- Serial number
- Firmware version
- Command / probe name
- Control / key path (channel, address, parameter)
- Raw response (exact bytes, JSON, or text)

### Step 3 — Commit the fixture

```bash
mkdir -p tests/fixtures/hil/<device_slug>/
# Save raw response
echo '<raw_bytes_or_json>' > tests/fixtures/hil/<device_slug>/<command_name>.json
git add tests/fixtures/hil/
git commit -m "feat(hil): add <device> <command> fixture (PROBE #N)"
```

File naming: `tests/fixtures/hil/<device>/<command_or_scenario>.json`

### Step 4 — Write the failing CI test (RED)

```python
# tests/test_<feature>.py
# @verifies #89 TEST-CTRL-STATUS-001
# Fixture source: PROBE #67 — tests/fixtures/hil/yamaha_ql5/channel_status_ch1.json

import json, pathlib

def load_fixture(path: str) -> dict:
    return json.loads((pathlib.Path("tests/fixtures/hil") / path).read_text())

def test_channel_status_response_parses_correctly():
    """
    Verifies: #89 TEST-CTRL-STATUS-001
    """
    fixture = load_fixture("yamaha_ql5/channel_status_ch1.json")
    result = parse_channel_status(fixture["raw_bytes"])
    assert result.channel == fixture["expected"]["channel"]
    assert result.fader_level == fixture["expected"]["fader_level"]
```

Run: test must **fail** before any implementation.

### Step 5 — Implement (GREEN)

Write the smallest code change that makes the test pass.

Add source annotation:
```python
# @implements #123 REQ-F-CTRL-001: Channel status query
def parse_channel_status(raw_bytes: bytes) -> ChannelStatus:
    ...
```

### Step 6 — Verify CI passes without hardware

```bash
# Ensure no hardware calls in test
pytest tests/test_<feature>.py -v
# Must pass without any device connected
```

### Step 7 — Update PROBE issue

Add to the PROBE issue body:
```markdown
- Verified by: #90 (TEST-CTRL-STATUS-001: fixture-backed CI test)
```

Close the PROBE issue once the CI test is green.

## File Naming Rules

| Purpose | Pattern | Default CI |
|---|---|---|
| HIL probe / evidence test | `*.hil.test.*` | ❌ Excluded |
| Fixture-backed CI test | `*.test.*` (no `.hil.`) | ✅ Included |
| Captured fixture data | `tests/fixtures/hil/**` | N/A (data) |

## What HIL evidence proves vs. does NOT prove

**Proves**: The exact command/response on the specific device+firmware tested.

**Does NOT prove**: Behavior on other channels, other firmware versions, load conditions, or other device variants.

**Important**: A fixture-backed CI test does NOT create new HIL evidence by itself.

## Acceptance Criteria

- [ ] PROBE issue created with all metadata fields filled
- [ ] Raw fixture committed to `tests/fixtures/hil/<device>/`
- [ ] CI test references PROBE issue via `# Fixture source: PROBE #N`
- [ ] CI test has `@verifies #N` or `Verifies: #N` annotation
- [ ] Test passes without hardware connected
- [ ] `*.hil.test.*` files are excluded from default CI matrix
- [ ] PROBE issue updated with `- Verified by: #N` and closed

## References

- [.github/ISSUE_TEMPLATE/13-probe.yml](../ISSUE_TEMPLATE/13-probe.yml)
- [.github/instructions/phase-05-implementation.instructions.md](../instructions/phase-05-implementation.instructions.md) — HIL section
- [docs/real-time-systems-guide.md](../../docs/real-time-systems-guide.md)
